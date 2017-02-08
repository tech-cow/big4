#!/usr/bin/python
#coding:utf-8

#对代码的解释视频：https://www.useloom.com/share/c4817960ecc911e689c9c95ad27ead9a

#写个简单的英雄联盟的Champion Class
class Champion():
    gold = 500  #class variable

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp



#main
annie = Champion('Annie', '300', '300')
print annie.gold

urgot = Champion('Urgot', '30','0')
print urgot.gold
