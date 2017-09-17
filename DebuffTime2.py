
# coding=utf-8

import os
import sys
import string 
import argparse
import random

#================================================================================ 
# 攻速是A下/秒，有%B的概率造成C秒眩晕。新的眩晕会覆盖原来的效果。求眩晕覆盖率。
#================================================================================    
def debuff_time(apm, prob1, prob2, time1, time2):
    _apm = float(apm)
    _prob1 = float(prob1)/100
    _time1 = float(time1) * 1000
    _prob2 = float(prob2)/100
    _time2 = float(time2) * 1000

    #private

    #time:ms
    _atkTime = 1000 / _apm
    _totalTime = 10000*1000
    _totalBuffTime = 0
    _buffTime = 0
    _timer = 0

    # statics
    for i in range(_totalTime):
        _timer += 1
        if _timer >= _atkTime:
            _timer = 0
            if random.random() <= _prob1:
                _buffTime = _time1

            if random.random() <= _prob2:
                _buffTime = _time2
        
        _buffTime -= 1

        if _buffTime > 0:
            _totalBuffTime += 1

    # result
    result = float(_totalBuffTime)/_totalTime

    # print
    print(" apm: " + str(apm) + "\n prob1: " + str(prob1) + "%, buff1 duration: " + str(time1)  + "s\n prob2: " + str(prob2) + "%, buff2 duration: " + str(time2)  + "s\n")
    print("coverage rate: " + str(result) + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apm", help="apm")
    parser.add_argument("-b1", "--probability1", help="probability")
    parser.add_argument("-b2", "--probability2", help="probability")
    parser.add_argument("-c1", "--time1", help="buff duration")
    parser.add_argument("-c2", "--time2", help="buff duration")

    args = parser.parse_args()
    debuff_time(args.apm,args.probability1, args.probability2, args.time1, args.time2)
