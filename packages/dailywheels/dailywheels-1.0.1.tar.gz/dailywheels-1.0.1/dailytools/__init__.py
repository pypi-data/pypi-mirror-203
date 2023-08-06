from dailytools.logger import Logger
from .encrypt.__sm4 import SM4
from .audio.tts_engine import TTSEngine
from .audio.utils import play_audio, get_audio_duration, stop_play
from .utils import get_host_ip
from .audio.audio_db import AudioData
from dailytools.__exceptions import *

__version__ = "0.3.1"

print("Good Luck!")
print("Best Wishes for Ur Journey from **Daily Tools** ^_^ ! (init on Feb 2023)")
if __version__ == "0.3.0":
    print("")