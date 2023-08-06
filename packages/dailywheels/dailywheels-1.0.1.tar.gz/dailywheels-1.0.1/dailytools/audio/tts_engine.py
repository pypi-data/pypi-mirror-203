# -*- coding: utf-8 -*
import os
import json
import requests
import traceback

from aip import AipSpeech

from .audio_db import AudioData

from .headers import * 
from dailytools.__exceptions import *


class TTSEngine:
    audioDB = AudioData()

    def __init__(self, path:str, config=DIRPATH + "/config/config.json"):
        
        try:
            config = json.load(open(config, "r"))  # load the config file
        except FileNotFoundError as e:
            raise ConfigNotFoundError(e.__str__())
        except Exception as e:
            raise e
        
        if "tts_offline" in config:
            OfflineConfig = config["tts_offline"]
            self.__ip = OfflineConfig["ip"]
            self.__port = OfflineConfig["port"]

        if "tts_online" in config:
            OnlineConfig = config["tts_online"]
            self.__APP_ID = OnlineConfig["APP_ID"]
            self.__API_KEY = OnlineConfig["API_KEY"]
            self.__SECRET_KEY = OnlineConfig["SECRET_KEY"]
            self.allow_online = True
        
        os.makedirs(path, exist_ok=True)
        self.__class__.audioDB.connect(os.path.join(path, "audio_content.db"))

    
    def __synthesize_audio_online(self, name, audio_format="mp3", **kwargs):
        """
        Synthesize the audio from text by Baidu (audio_format == mp3)
        """
        spd = kwargs.get('spd', 5)
        pit = kwargs.get('pit', 5)
        per = kwargs.get('per', 0)
        vol = kwargs.get('vol', 5)

        audio = self.__server.synthesis(name, 'zh', 1, {'spd': spd, 'pit': pit, 'vol': vol, 'per': per})

        if not isinstance(audio, dict):
            self.__class__.audioDB.insert_data(name, audio=audio, audio_format=audio_format)
        else:
            raise OnlineTTSError(str(audio))
        return {"code": 200, "msg": "TTS Success", "fmt": audio_format, "data": audio}


    def __synthesize_audio_offline(self, msg: str, audio_format="wav"):
        """
        Synthesize the audio by TTS on server
        """
        url = "http://{0}:{1}/api/tts?voice={2}&text={3}"
        try:
            resp = requests.get(url.format(self.__ip, self.__port, "zh", msg))
            result = {"code": 200, "msg": "TTS Success"}
        except Exception as e:
            raise OfflineTTSError(traceback.format_exc())
        try:
            self.__class__.audioDB.insert_data(msg, audio=resp.content, audio_format=audio_format)
            result["fmt"] = audio_format
            result["data"] = resp.content
        except Exception as e:
            raise DBInsertError(e.__str__())
        return result

    # update the answer audio dict
    def sync_audio(self,
                   msg: str,
                   ifonline: bool,
                   **kwargs) -> filePathStr:
    
        if "__server" not in self.__dict__ and self.allow_online is True:  # 避免多次启动server
            self.__server = AipSpeech(self.__APP_ID, self.__API_KEY, self.__SECRET_KEY)
        
        elif self.allow_online is False:
            raise OnlineTTSError("Server Init Failed: Token Not Found !")
        
        if ifonline:
            spd = kwargs.get("spd")
            if spd:
                resp = self.__synthesize_audio_online(msg, per=5118, spd=spd)
            else:
                resp = self.__synthesize_audio_online(msg, per=5118)
        else:
            resp = self.__synthesize_audio_offline(msg=msg)
            
        return resp


if __name__ == '__main__':
    tts = TTSEngine("/home/pi/")
    sync_audio = tts.sync_audio
    result = sync_audio("我在。", ifonline=True)
    result = sync_audio("正在处理，请稍后。", ifonline=True)
