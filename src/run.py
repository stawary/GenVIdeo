# coding=utf-8
# -*- coding: utf-8 -*-
from DataBase import DataBase
from CutWorld import CutWorld
from TextToAudio import TextToAudio
from Audio_Process import Audio_Process
from Gen_Video import Gen_Video

'''

'''

class run():
    def __init__(self):
        pass
    def get_word(self):
        '''
        从数据库获取一条未生成视频的语料
        :return: text
        '''
        text = DataBase().get_word()
        return text
    def run(self):
        uuid,text = self.get_word()
        num = CutWorld().CutWorld(text,uuid)
        audio = TextToAudio().TextToAudio(text)
        #audio地址修改为本地音频的绝对路径
        beat_info = Audio_Process().Audio_Process(audio,num)
        Gen_Video().Gen_Video(beat_info,audio,uuid)

if __name__ == '__main__':
    run().run()
