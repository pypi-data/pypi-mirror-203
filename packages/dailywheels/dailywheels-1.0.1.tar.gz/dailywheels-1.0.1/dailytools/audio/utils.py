# -*- coding: utf-8 -*
import os
import platform
from subprocess import Popen

import wave
import eyed3
import contextlib
from time import sleep
# import AudioSegment

from dailytools.__exceptions import *

def stop_play():
    os.system("kill -9 $(ps -ef | grep 'mpg\|play' | grep -v grep | awk '{print $2}')")


def play_audio(filename: str, ifterminate:bool=True):
    """
    Args:
        filename: Audio filename
    """
    if ifterminate:
        stop_play()
    if platform.system() == 'Darwin':
        Popen(['afplay', filename])
    else:
        if filename.endswith(".mp3"):
            Popen(['mpg123', '-q', filename])
        elif filename.endswith(".wav"):
            Popen(["play", "-q", filename])

def get_duration_wav(file_path:str):
    """
    获取wav音频文件时长
    :param file_path:
    :return:
    """
    with contextlib.closing(wave.open(file_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration


def get_duration_mp3(file_path:str):
    mp3Info = eyed3.load(file_path)
    return mp3Info.info.time_secs

def get_audio_duration(file_path:str):
    fmt = file_path[-3:]
    if file_path[-3:] not in ["mp3", "wav"]:
        raise FormatNotSupport("Expect wav, mp3 audio format. Received: {} not support".format(fmt))
    
    return eval("get_duration_{}('{}')".format(fmt, file_path))


# def mp3towav(src, dst):
#     sound = AudioSegment.from_mp3(src)
#     sound.export(dst, format="wav")
