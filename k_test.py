# -*- encoding=utf8 -*-
__author__ = "user"

from airtest.core.api import *
import numpy as np
#import time  
from datetime import datetime, date,time,timedelta

auto_setup(__file__)
def meirilingqu():
    if exists(Template(r"tpl1702138643195.png", record_pos=(-0.443, -0.227), resolution=(1280, 720))):
        touch(Template(r"tpl1702138643195.png", record_pos=(-0.443, -0.227), resolution=(1280, 720)))
        sleep(2.0)
        touch(Template(r"tpl1702138674341.png", record_pos=(-0.28, 0.225), resolution=(1280, 720)))
        sleep(2.0)
    if exists(Template(r"tpl1702142254765.png", record_pos=(0.005, -0.016), resolution=(1280, 720))):
        touch(Template(r"tpl1702142098125.png", record_pos=(-0.001, 0.102), resolution=(1280, 720)))
    sleep(2.0)
    for i in range(10):
        if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
            touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
            sleep(1.0)
        else:
            for m in range(3):
                posx=["1230","35"]
                touch(posx)
                sleep(1.0)
            break
    sleep(1.0)
    touch(Template(r"tpl1702138770008.png", record_pos=(0.445, -0.205), resolution=(1280, 720)))
    sleep(1.0)
    touch(Template(r"tpl1702138788810.png", record_pos=(0.166, -0.249), resolution=(1280, 720)))
    sleep(1.0)
    # 暂时填充一下
    pos1=["1120","210"]
    touch(pos1)
    sleep(1.0)
    touch(Template(r"tpl1702138815889.png", record_pos=(-0.009, -0.247), resolution=(1280, 720)))
    sleep(1.0)
    # 暂时填充一下
    pos1=["1037","369"]
    touch(pos1)
    sleep(1.0)
    for i in range(10):
        if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
            touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
            sleep(1.0)
        else:
            for m in range(3):
                posx=["1230","35"]
                touch(posx)
                sleep(1.0)
            break
    sleep(1.0)
    if (exists(Template(r"tpl1702139013750.png", record_pos=(-0.112, -0.137), resolution=(1280, 720)))):
        touch(Template(r"tpl1702139159259.png", record_pos=(-0.116, -0.132), resolution=(1280, 720)))

    sleep(1.0)
    touch(Template(r"tpl1702138929291.png", record_pos=(-0.402, 0.122), resolution=(1280, 720)))
    sleep(1.0)
    swipe(Template(r"tpl1702139237284.png", record_pos=(-0.135, 0.164), resolution=(1280, 720)), vector=[0.0095, -0.1341])
    sleep(5.0)
    pos=exists(Template(r"tpl1702139309555.png", record_pos=(-0.127, -0.048), resolution=(1280, 720)))
    pos1=["0","0"];
    pos1[0]=str(int(pos[0])+675)
    pos1[1]=pos[1]
    touch(pos1)
    sleep(1.0)
    if exists(Template(r"tpl1702140616411.png", record_pos=(-0.002, -0.035), resolution=(1280, 720))):
        touch(Template(r"tpl1702140793092.png", record_pos=(0.205, -0.083), resolution=(1280, 720)))
    sleep(1.0)
    pos1=["648","528"]
    touch(pos1)
    sleep(1.0)
    pos1=["963","93"]
    touch(pos1)
    sleep(1.0)
    touch(Template(r"tpl1702140859902.png", record_pos=(-0.394, 0.078), resolution=(1280, 720)))
    sleep(1.0)
    pos1=["1140","565"]
    touch(pos1)
    sleep(1.0)
    touch(Template(r"tpl1702140935177.png", record_pos=(0.208, -0.083), resolution=(1280, 720)))
    sleep(1.0)
    pos1=["648","528"]
    touch(pos1)
    sleep(1.0)
    pos1=["963","93"]
    touch(pos1)
    sleep(1.0)
    touch(Template(r"tpl1702141060221.png", record_pos=(-0.393, -0.009), resolution=(1280, 720)))
    sleep(1.0)
    swipe(Template(r"tpl1702141077328.png", record_pos=(-0.223, 0.164), resolution=(1280, 720)), vector=[0.0432, -0.7689])
    sleep(5.0)
    if exists(Template(r"tpl1702142349949.png", record_pos=(-0.222, 0.167), resolution=(1280, 720))):
        pos1=["1150","567"]
        touch(pos1)
        sleep(1.0)
        pos1=["648","528"]
        touch(pos1)
        sleep(1.0)
        pos1=["963","93"]
        touch(pos1)
    sleep(1.0)
    for i in range(10):
        if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
            touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
            sleep(1.0)
        else:
            for m in range(3):
                posx=["1230","35"]
                touch(posx)
                sleep(1.0)
            break
    sleep(1.0)
    if exists(Template(r"tpl1702186744052.png", record_pos=(-0.345, -0.07), resolution=(1280, 720))):
        touch(Template(r"tpl1702186755317.png", record_pos=(-0.341, -0.061), resolution=(1280, 720)))
        sleep(1.0)
    pos1=["1112","143"];
    touch(pos1)
    sleep(1.0)
    for i in range(10):
        if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
            touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
            sleep(1.0)
        else:
            for m in range(3):
                posx=["1230","35"]
                touch(posx)
                sleep(1.0)
            break
    sleep(1.0)
    if exists(Template(r"tpl1702186846083.png", record_pos=(-0.455, 0.12), resolution=(1280, 720))):
        touch(Template(r"tpl1702186865421.png", record_pos=(-0.452, 0.13), resolution=(1280, 720)))
        sleep(1.0)
    if  wait(Template(r"tpl1702186891899.png", record_pos=(-0.097, 0.025), resolution=(1280, 720))):
        touch(Template(r"tpl1702186901720.png", record_pos=(-0.096, 0.023), resolution=(1280, 720)))
    sleep(2.0)
    if  exists(Template(r"tpl1702186923226.png", record_pos=(-0.179, -0.248), resolution=(1280, 720))):
        touch(Template(r"tpl1702186935394.png", record_pos=(-0.178, -0.247), resolution=(1280, 720)))
        sleep(2.0)
        posabs=["230","645"]
        touch(posabs)
        if exists(Template(r"tpl1702187001694.png", record_pos=(0.311, -0.252), resolution=(1280, 720))):
            touch(Template(r"tpl1702187012810.png", record_pos=(0.307, -0.253), resolution=(1280, 720)))
            sleep(2.0)
        if  exists(Template(r"tpl1702187041416.png", record_pos=(0.002, 0.209), resolution=(1280, 720))):
            touch(Template(r"tpl1702187058473.png", record_pos=(-0.001, 0.21), resolution=(1280, 720)))
        for i in range(10):
            if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                sleep(1.0)
            else:
                for m in range(3):
                    posx=["1230","35"]
                    touch(posx)
                    sleep(1.0)
                break
    if exists(Template(r"tpl1702187230090.png", record_pos=(-0.444, -0.228), resolution=(1280, 720))):
        posabs=["1260","493"]
        touch(posabs)
        sleep(1.0)
        posabs=["320","659"]
        touch(posabs)
        sleep(2.0)
        posabs=["935","650"]
        touch(posabs)
        sleep(1.0)
        for i in range(10):
            if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                sleep(1.0)
            else:
                for m in range(3):
                    posx=["1230","35"]
                    touch(posx)
                    sleep(1.0)
                break
    if exists(Template(r"tpl1702187230090.png", record_pos=(-0.444, -0.228), resolution=(1280, 720))):
        swipe(Template(r"tpl1702188429951.png", record_pos=(0.213, 0.234), resolution=(1280, 720)), vector=[-0.6355, -0.0045])
        sleep(3.0)
        if exists(Template(r"tpl1702188485106.png", record_pos=(-0.33, 0.008), resolution=(1280, 720))):
            touch(Template(r"tpl1702188515562.png", record_pos=(-0.326, 0.011), resolution=(1280, 720)))
            sleep(2.0)
            posabs=["841","459"]
            touch(posabs)
            sleep(2.0)
            if exists(Template(r"tpl1702188627865.png", record_pos=(-0.126, 0.003), resolution=(1280, 720))):
                touch(Template(r"tpl1702188678170.png", record_pos=(-0.122, -0.045), resolution=(1280, 720)))
                sleep(1.0)
                if exists(Template(r"tpl1702188720112.png", record_pos=(0.152, 0.229), resolution=(1280, 720))):
                    touch(Template(r"tpl1702188732749.png", record_pos=(0.149, 0.227), resolution=(1280, 720)))
                    sleep(1.0)
            for i in range(10):
                if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                    touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                    sleep(1.0)
                else:
                    for m in range(3):
                        posx=["1230","35"]
                        touch(posx)
                        sleep(1.0)
                    break
            if exists(Template(r"tpl1702188920312.png", record_pos=(-0.395, 0.205), resolution=(1280, 720))):
                touch(Template(r"tpl1702188933670.png", record_pos=(-0.398, 0.201), resolution=(1280, 720)))
                sleep(1.0)
            for i in range(10):
                if exists(Template(r"tpl1702188968936.png", record_pos=(0.002, 0.155), resolution=(1280, 720))):
                    touch(Template(r"tpl1702188980944.png", record_pos=(0.002, 0.14), resolution=(1280, 720)))
                    sleep(1.0)
                else:
                    break
            if exists(Template(r"tpl1702189098199.png", record_pos=(-0.173, -0.245), resolution=(1280, 720))):
                touch(Template(r"tpl1702189108544.png", record_pos=(-0.167, -0.247), resolution=(1280, 720)))
                sleep(1.0)
            if exists(Template(r"tpl1702189136436.png", record_pos=(0.122, -0.248), resolution=(1280, 720))):
                touch(Template(r"tpl1702189149902.png", record_pos=(0.12, -0.248), resolution=(1280, 720)))
                sleep(1.0)
            for i in range(3):
                if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                    touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                    sleep(1.0)
                else:
                    for m in range(3):
                        posx=["1230","35"]
                        touch(posx)
                        sleep(1.0)
                    break
            if exists(Template(r"tpl1702188862224.png", record_pos=(-0.405, -0.175), resolution=(1280, 720))):
                touch(Template(r"tpl1702188874613.png", record_pos=(-0.405, -0.176), resolution=(1280, 720)))
                sleep(1.0)
#meirilingqu()
        
#每日福利的代码
def meirifuli():
    if exists(Template(r"tpl1702230060943.png", record_pos=(-0.441, -0.228), resolution=(1280, 720))):
        posabs=["723","96"]
        touch(posabs)
        sleep(1.0)
        if exists(Template(r"tpl1702141562763.png", record_pos=(-0.192, 0.062), resolution=(1280, 720))):
            touch(Template(r"tpl1702141577822.png", record_pos=(-0.187, 0.06), resolution=(1280, 720)))
        sleep(1.0)
        posabs=["1066","433"]
        touch(posabs)
        sleep(1.0)
        for i in range(10):
            if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                sleep(1.0)
            else:
                for m in range(3):
                    posx=["1230","35"]
                    touch(posx)
                    sleep(1.0)
                break

def youjian():
    posabs=["188","677"]
    touch(posabs)
    sleep(1.0)
    if exists(Template(r"tpl1702141836462.png", record_pos=(0.219, 0.173), resolution=(1280, 720))):
        touch(Template(r"tpl1702141851483.png", record_pos=(0.219, 0.173), resolution=(1280, 720)))
    sleep(1.0)
    if exists(Template(r"tpl1702141886214.png", record_pos=(-0.002, -0.001), resolution=(1280, 720))):
        touch(Template(r"tpl1702141902499.png", record_pos=(-0.104, 0.087), resolution=(1280, 720)))
    if wait(Template(r"tpl1702141941375.png", record_pos=(0.005, -0.002), resolution=(1280, 720)),timeout=120.0):
        if exists(Template(r"tpl1702141969470.png", record_pos=(0.264, -0.113), resolution=(1280, 720))):
            touch(Template(r"tpl1702141969470.png", record_pos=(0.264, -0.113), resolution=(1280, 720)))
            sleep(1.0)
        for i in range(10):
            if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                sleep(1.0)
            else:
                for m in range(3):
                    posx=["1230","35"]
                    touch(posx)
                    sleep(1.0)
                break

def shilian2zhuye():
    if exists(Template(r"tpl1702186271115.png", record_pos=(0.286, 0.082), resolution=(1280, 720))):
        for i in range(2):
            touch(Template(r"tpl1702186341270.png", record_pos=(0.28, 0.081), resolution=(1280, 720)))
            sleep(1.0)
        for i in range(10):
            if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                sleep(1.0)
            else:
                for m in range(3):
                    posx=["1230","35"]
                    touch(posx)
                    sleep(1.0)
                break
    sleep(1.0)
#shilian2zhuye()

def zhuye2lunch():
    if  exists(Template(r"tpl1702186513446.png", record_pos=(0.449, 0.234), resolution=(1280, 720))):
        touch(Template(r"tpl1702186526336.png", record_pos=(0.443, 0.234), resolution=(1280, 720)))
        sleep(1.0)
        touch(Template(r"tpl1702186544865.png", record_pos=(0.445, 0.086), resolution=(1280, 720)))
        sleep(1.0)
    if exists(Template(r"tpl1702186581641.png", record_pos=(-0.001, 0.101), resolution=(1280, 720))):
        touch(Template(r"tpl1702186595718.png", record_pos=(0.001, 0.107), resolution=(1280, 720)))
    sleep(1.0)
#zhuye2lunch()

def lunch():
    if exists(Template(r"tpl1702186639646.png", record_pos=(-0.002, 0.221), resolution=(1280, 720))):
        touch(Template(r"tpl1702186652433.png", record_pos=(-0.002, 0.221), resolution=(1280, 720)))
    sleep(10.0)
    for i in range(3):
        if exists(Template(r"tpl1702186689773.png", record_pos=(0.253, -0.18), resolution=(1280, 720))):
            touch(Template(r"tpl1702186701525.png", record_pos=(0.259, -0.18), resolution=(1280, 720)))
            sleep(1.0)
        else:
            break
#lunch()
def shenmota():
    if exists(Template(r"tpl1702189264921.png", record_pos=(-0.447, -0.223), resolution=(1280, 720))):
        posabs=["731","195"]
        touch(posabs)
        sleep(1.0)
    if exists(Template(r"tpl1702189323016.png", record_pos=(0.326, 0.17), resolution=(1280, 720))):
        touch(Template(r"tpl1702189359684.png", record_pos=(0.327, 0.171), resolution=(1280, 720)))
        sleep(1.0)
        touch(Template(r"tpl1702189374234.png", record_pos=(-0.005, 0.237), resolution=(1280, 720)))
        sleep(1.0)
    for m in range(200):
        posabs=["1100","120"];
        touch(posabs)
        sleep(1.0)
        if exists(Template(r"tpl1702228015458.png", record_pos=(-0.013, -0.019), resolution=(1280, 720))):
            touch(Template(r"tpl1702189758609.png", record_pos=(0.001, 0.104), resolution=(1280, 720)))
            break
        posabs=["991","473"];
        touch(posabs)
        sleep(1.0)
    if exists(Template(r"tpl1702189800824.png", record_pos=(-0.173, -0.245), resolution=(1280, 720))):
        touch(Template(r"tpl1702189811183.png", record_pos=(-0.18, -0.246), resolution=(1280, 720)))
        sleep(1.0)
        for i in range(30):
            if exists(Template(r"tpl1702189868675.png", record_pos=(-0.339, 0.23), resolution=(1280, 720))):
                touch(Template(r"tpl1702189876795.png", record_pos=(-0.343, 0.23), resolution=(1280, 720)))
                sleep(1.0)
    for i in range(5):
        if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
            touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
            sleep(1.0)
        else:
            for m in range(3):
                posx=["1230","35"]
                touch(posx)
                sleep(1.0)
            break    
    else:
        posabs=["731","195"]
        touch(posabs)
        sleep(1.0)
#shenmota()
huodong_flag=0
def huodong():
    if exists(Template(r"tpl1702190644444.png", record_pos=(-0.445, -0.222), resolution=(1280, 720))):
        posabs=["622","94"]
        touch(posabs)
        sleep(1.0)
        for m in range(3):
            pos3=[262,348]
            pos4=[262,278]
            swipe(pos3, pos4)
            sleep(2.0)
            if exists(Template(r"tpl1702190966950.png", record_pos=(-0.313, 0.127), resolution=(1280, 720))):
                huodong_flag=1
            if exists(Template(r"tpl1702191000388.png", record_pos=(-0.315, 0.209), resolution=(1280, 720))):
                huodong_flag=2
        for i in range(10):
            if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                sleep(1.0)
            else:
                for m in range(3):
                    posx=["1230","35"]
                    touch(posx)
                    sleep(1.0)
                break
    for m in range(5):
        if exists(Template(r"tpl1702190644444.png", record_pos=(-0.445, -0.222), resolution=(1280, 720))):
            posabs=["622","94"]
            touch(posabs)
            sleep(1.0)
            for i in range(3):
                pos3=[934,548]
                pos4=[934,478]
                swipe(pos3, pos4)
                sleep(2.0)
                if exists(Template(r"tpl1702191240916.png", record_pos=(0.353, 0.191), resolution=(1280, 720))):
                    touch(Template(r"tpl1702191248113.png", record_pos=(0.355, 0.195), resolution=(1280, 720)))
                    sleep(1.0)
                    break
            for i in range(10):
                if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                    touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                    sleep(1.0)
                else:
                    for m in range(3):
                        posx=["1230","35"]
                        touch(posx)
                        sleep(1.0)
                    break  
    #print(huodong_flag)
    return huodong_flag

def zhuchengrenwu(huodong_flag):
    #huodong_flag=2
    if exists(Template(r"tpl1702191556679.png", record_pos=(-0.44, -0.22), resolution=(1280, 720))):
        if exists(Template(r"tpl1702191584261.png", record_pos=(0.259, 0.023), resolution=(1280, 720))):
            touch(Template(r"tpl1702192413849.png", record_pos=(0.259, 0.026), resolution=(1280, 720)))
            sleep(1.0)
            touch(Template(r"tpl1702192433499.png", record_pos=(0.072, 0.097), resolution=(1280, 720)))
            sleep(1.0)
        if huodong_flag==1:
            huodong_flag=0
            for i in range(30):
                if exists(Template(r"tpl1702192806294.png", record_pos=(0.087, 0.237), resolution=(1280, 720))):
                    huodong_flag=0
                    break
                pos1=["1076","661"]
                touch(pos1)
                sleep(1.0)
                if exists(Template(r"tpl1702192604997.png", record_pos=(0.002, -0.121), resolution=(1280, 720))):
                    touch(Template(r"tpl1702192614518.png", record_pos=(-0.106, 0.087), resolution=(1280, 720)))
                    sleep(1.0)
                if exists(Template(r"tpl1702192692149.png", record_pos=(0.088, 0.237), resolution=(1280, 720))):
                    pos1=["1076","661"]
                    touch(pos1)
                    break
        else:
            for i in range(10):
                if exists(Template(r"tpl1702192806294.png", record_pos=(0.087, 0.237), resolution=(1280, 720))):
                    #huodong_flag=0
                    break
                pos1=["1076","661"]
                touch(pos1)
                sleep(1.0)
                if exists(Template(r"tpl1702192604997.png", record_pos=(0.002, -0.121), resolution=(1280, 720))):
                    touch(Template(r"tpl1702192614518.png", record_pos=(-0.106, 0.087), resolution=(1280, 720)))
                    sleep(1.0)
        if exists(Template(r"tpl1702193031166.png", record_pos=(-0.001, -0.245), resolution=(1280, 720))):
            touch(Template(r"tpl1702193038408.png", record_pos=(-0.005, -0.248), resolution=(1280, 720)))
            sleep(1.0)
            for i in range(35):
                if exists(Template(r"tpl1702193105828.png", record_pos=(-0.001, 0.252), resolution=(1280, 720))):
                    touch(Template(r"tpl1702193117353.png", record_pos=(-0.001, 0.255), resolution=(1280, 720)))
                    sleep(1.0)
        for i in range(10):
            if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                sleep(1.0)
            else:
                for m in range(3):
                    posx=["1230","35"]
                    touch(posx)
                    sleep(1.0)
                break
    if huodong_flag==2:
        huodong_flag=0
        if exists(Template(r"tpl1702224531882.png", record_pos=(0.438, -0.21), resolution=(1280, 720))):
            touch(Template(r"tpl1702224542562.png", record_pos=(0.436, -0.205), resolution=(1280, 720)))
            sleep(1.0)
        if  exists(Template(r"tpl1702224573848.png", record_pos=(-0.176, -0.248), resolution=(1280, 720))):
            touch(Template(r"tpl1702224599971.png", record_pos=(-0.173, -0.248), resolution=(1280, 720)))
            sleep(1.0)
        if  exists(Template(r"tpl1702224632478.png", record_pos=(-0.329, -0.026), resolution=(1280, 720))):
            posabs=["1044","363"]
            touch(posabs)
            sleep(1.0)
            if exists(Template(r"tpl1702224732071.png", record_pos=(0.205, -0.081), resolution=(1280, 720))):
                touch(Template(r"tpl1702224742719.png", record_pos=(0.207, -0.08), resolution=(1280, 720)))
                sleep(1.0)
            posabs=["628","514"]
            touch(posabs)
            sleep(1.0)
            posabs=["960","82"]
            touch(posabs)
            sleep(1.0)
        for i in range(5):
            if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
                touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
                sleep(1.0)
            else:
                for m in range(3):
                    posx=["1230","35"]
                    touch(posx)
                    sleep(1.0)
                break
    huodong_flag=0
    return huodong_flag

def yingxiongmen():
    break_sign=0
    def chuangjianzhandou(break_sign):
        if exists(Template(r"tpl1702193912877.png", record_pos=(0.119, 0.233), resolution=(1280, 720))):
            touch(Template(r"tpl1702193595218.png", record_pos=(0.12, 0.235), resolution=(1280, 720)))
            sleep(1.0)
            pos1=["1099","382"]
            touch(pos1)
            sleep(1.0)
            pos2=["483","483"]
            touch(pos2)
            sleep(1.0)
            pos1=["1099","548"]
            touch(pos1)
            sleep(1.0)
            pos2=["483","483"]
            touch(pos2)
            sleep(1.0)
            touch(Template(r"tpl1702193744114.png", record_pos=(0.248, 0.236), resolution=(1280, 720)))
            sleep(2.0)
            if exists(Template(r"tpl1702276893241.png", record_pos=(0.005, -0.01), resolution=(1280, 720))):
                posx=["613","501"];
                touch(posx)
                sleep(1.0)
                posx=["1210","30"]
                touch(posx)
                sleep(1.0)
                break_sign=1
            else:
                sleep(1.0)
                pos1=["571","486"]
                touch(pos1)
                sleep(10.0)
                for m in range(5):
                    pos1=["1170","680"]
                    touch(pos1)
                    sleep(1.0)
                pos1=["479","608"]
                touch(pos1)
                sleep(1.0)
        return break_sign
    def baoku():
        pos1=["1130","221"]
        touch(pos1)
        sleep(1.0)
        pos1=["1130","355"]
        touch(pos1)
        sleep(1.0)
        if exists(Template(r"tpl1702283366634.png", record_pos=(0.262, -0.044), resolution=(1280, 720))):
            swipe(Template(r"tpl1702283378689.png", record_pos=(0.261, -0.042), resolution=(1280, 720)), vector=[-0.0035, -0.0896])
            sleep(3.0)
        if exists(Template(r"tpl1702283423545.png", record_pos=(0.263, -0.136), resolution=(1280, 720))):
            pos2=exists(Template(r"tpl1702283423545.png", record_pos=(0.263, -0.136), resolution=(1280, 720)))
            pos1=["0","0"]
            pos1[0]=str(int(pos2[0])+160)
            pos1[1]=str(int(pos2[1])+30)
            touch(pos1)
            sleep(1.0)

    if exists(Template(r"tpl1702187230090.png", record_pos=(-0.444, -0.228), resolution=(1280, 720))):
        swipe(Template(r"tpl1702188429951.png", record_pos=(0.213, 0.234), resolution=(1280, 720)), vector=[-0.6355, -0.0045])
        sleep(3.0)
        if exists(Template(r"tpl1702193266436.png", record_pos=(0.257, 0.205), resolution=(1280, 720))):
            touch(Template(r"tpl1702193274911.png", record_pos=(0.26, 0.202), resolution=(1280, 720)))
            sleep(1.0)
        if exists(Template(r"tpl1702277226664.png", record_pos=(-0.344, -0.248), resolution=(1280, 720))):
            if exists(Template(r"tpl1702193384264.png", record_pos=(-0.079, 0.09), resolution=(1280, 720))):
                swipe(Template(r"tpl1702193384264.png", record_pos=(-0.079, 0.09), resolution=(1280, 720)), vector=[-0.3338, 0.0464])
                sleep(1.0)
            if exists(Template(r"tpl1702193433253.png", record_pos=(-0.016, 0.049), resolution=(1280, 720))):
                swipe(Template(r"tpl1702193433253.png", record_pos=(-0.016, 0.049), resolution=(1280, 720)), vector=[-0.3338, 0.0464])
                sleep(1.0)
            if exists(Template(r"tpl1702193484433.png", record_pos=(-0.002, 0.073), resolution=(1280, 720))):
                swipe(Template(r"tpl1702193484433.png", record_pos=(-0.002, 0.073), resolution=(1280, 720)), vector=[-0.3338, 0.0464])
                sleep(1.0)
            if exists(Template(r"tpl1702193550324.png", record_pos=(-0.004, 0.072), resolution=(1280, 720))):
                touch(Template(r"tpl1702193562716.png", record_pos=(-0.048, 0.003), resolution=(1280, 720)))
                sleep(3.0)
                if exists(Template(r"tpl1702284267380.png", record_pos=(-0.248, -0.122), resolution=(1280, 720))):
                    touch(Template(r"tpl1702284267380.png", record_pos=(-0.248, -0.122), resolution=(1280, 720)))
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                if exists(Template(r"tpl1702277262009.png", record_pos=(-0.245, -0.013), resolution=(1280, 720))):
                    touch(Template(r"tpl1702277262009.png", record_pos=(-0.245, -0.013), resolution=(1280, 720)))
                    sleep(1.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                if exists(Template(r"tpl1702277366506.png", record_pos=(-0.245, 0.098), resolution=(1280, 720))):
                    touch(Template(r"tpl1702277366506.png", record_pos=(-0.245, 0.098), resolution=(1280, 720)))
                    sleep(1.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                posl=["290","659"]
                touch(posl)
                sleep(1.0)
                posl=["640","580"]
                touch(posl)
                sleep(1.0)
                posx=["1127","127"]
                touch(posx)
                sleep(1.0)
                if exists(Template(r"tpl1702277366506.png", record_pos=(-0.245, 0.098), resolution=(1280, 720))):
                    swipe(Template(r"tpl1702277598065.png", record_pos=(-0.249, 0.099), resolution=(1280, 720)), vector=[0.0173, -0.5377])
                    sleep(3.0)
                if exists(Template(r"tpl1702277697433.png", record_pos=(-0.245, -0.05), resolution=(1280, 720))):
                    touch(Template(r"tpl1702277697433.png", record_pos=(-0.245, -0.05), resolution=(1280, 720)))
                    sleep(1.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                if exists(Template(r"tpl1702277366506.png", record_pos=(-0.245, 0.098), resolution=(1280, 720))):
                    swipe(Template(r"tpl1702277598065.png", record_pos=(-0.249, 0.099), resolution=(1280, 720)), vector=[0.0173, -0.5377])
                    sleep(3.0)
                if exists(Template(r"tpl1702277794547.png", record_pos=(-0.246, 0.048), resolution=(1280, 720))):
                    touch(Template(r"tpl1702277794547.png", record_pos=(-0.246, 0.048), resolution=(1280, 720)))
                    sleep(1.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                if exists(Template(r"tpl1702277366506.png", record_pos=(-0.245, 0.098), resolution=(1280, 720))):
                    swipe(Template(r"tpl1702277598065.png", record_pos=(-0.249, 0.099), resolution=(1280, 720)), vector=[0.0173, -0.5377])
                    sleep(3.0)
                if exists(Template(r"tpl1702277863634.png", record_pos=(-0.246, 0.124), resolution=(1280, 720))):
                    touch(Template(r"tpl1702277863634.png", record_pos=(-0.246, 0.124), resolution=(1280, 720)))
                    sleep(1.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                posl=["290","659"]
                touch(posl)
                sleep(1.0)
                posl=["640","580"]
                touch(posl)
                sleep(1.0)
                posx=["1127","127"]
                touch(posx)
                sleep(1.0)
                baoku()
                sleep(1.0)
                posx=["1230","30"]
                touch(posx)
                sleep(1.0)
                posc=["764","136"]
                touch(posc)
                sleep(1.0)#chongzhi
                posc=["482","482"]
                touch(posc)
                sleep(1.0)#chongzhi
            if exists(Template(r"tpl1702193550324.png", record_pos=(-0.004, 0.072), resolution=(1280, 720))):
                touch(Template(r"tpl1702193562716.png", record_pos=(-0.048, 0.003), resolution=(1280, 720)))
                sleep(3.0)
                if exists(Template(r"tpl1702284267380.png", record_pos=(-0.248, -0.122), resolution=(1280, 720))):
                    touch(Template(r"tpl1702284267380.png", record_pos=(-0.248, -0.122), resolution=(1280, 720)))
                    sleep(2.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                if exists(Template(r"tpl1702277262009.png", record_pos=(-0.245, -0.013), resolution=(1280, 720))):
                    touch(Template(r"tpl1702277262009.png", record_pos=(-0.245, -0.013), resolution=(1280, 720)))
                    sleep(1.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                if exists(Template(r"tpl1702277366506.png", record_pos=(-0.245, 0.098), resolution=(1280, 720))):
                    touch(Template(r"tpl1702277366506.png", record_pos=(-0.245, 0.098), resolution=(1280, 720)))
                    sleep(1.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                posl=["290","659"]
                touch(posl)
                sleep(1.0)
                posl=["640","580"]
                touch(posl)
                sleep(1.0)
                posx=["1127","127"]
                touch(posx)
                sleep(1.0)
                if exists(Template(r"tpl1702277366506.png", record_pos=(-0.245, 0.098), resolution=(1280, 720))):
                    swipe(Template(r"tpl1702277598065.png", record_pos=(-0.249, 0.099), resolution=(1280, 720)), vector=[0.0173, -0.5377])
                    sleep(3.0)
                if exists(Template(r"tpl1702277697433.png", record_pos=(-0.245, -0.05), resolution=(1280, 720))):
                    touch(Template(r"tpl1702277697433.png", record_pos=(-0.245, -0.05), resolution=(1280, 720)))
                    sleep(1.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                if exists(Template(r"tpl1702277366506.png", record_pos=(-0.245, 0.098), resolution=(1280, 720))):
                    swipe(Template(r"tpl1702277598065.png", record_pos=(-0.249, 0.099), resolution=(1280, 720)), vector=[0.0173, -0.5377])
                    sleep(3.0)
                if exists(Template(r"tpl1702277794547.png", record_pos=(-0.246, 0.048), resolution=(1280, 720))):
                    touch(Template(r"tpl1702277794547.png", record_pos=(-0.246, 0.048), resolution=(1280, 720)))
                    sleep(1.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                if exists(Template(r"tpl1702277366506.png", record_pos=(-0.245, 0.098), resolution=(1280, 720))):
                    swipe(Template(r"tpl1702277598065.png", record_pos=(-0.249, 0.099), resolution=(1280, 720)), vector=[0.0173, -0.5377])
                    sleep(3.0)
                if exists(Template(r"tpl1702277863634.png", record_pos=(-0.246, 0.124), resolution=(1280, 720))):
                    touch(Template(r"tpl1702277863634.png", record_pos=(-0.246, 0.124), resolution=(1280, 720)))
                    sleep(1.0)
                    break_sign=0
                    for m in range(4):
                        break_sign=chuangjianzhandou(break_sign)
                        sleep(1.0)
                        if break_sign==1:
                            break
                posl=["290","659"]
                touch(posl)
                sleep(1.0)
                posl=["640","580"]
                touch(posl)
                sleep(1.0)
                posx=["1127","127"]
                touch(posx)
                sleep(1.0)
                baoku()
                sleep(1.0)
                posx=["1230","30"]
                touch(posx)
                sleep(1.0)
    for i in range(3):
        if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
            touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
            sleep(1.0)
        else:
            for m in range(3):
                posx=["1230","35"]
                touch(posx)
                sleep(1.0)
            break 
#yingxiongmen()                            
                            
def huodongshilian():
    if exists(Template(r"tpl1702194051922.png", record_pos=(-0.445, -0.223), resolution=(1280, 720))):
        posabs=["620","189"]
        touch(posabs)
        sleep(1.0)
    if exists(Template(r"tpl1702194116441.png", record_pos=(-0.344, -0.249), resolution=(1280, 720))):
        touch(Template(r"tpl1702194127926.png", record_pos=(-0.345, -0.245), resolution=(1280, 720)))
        sleep(2.0)
        pos1=["636","378"]
        touch(pos1)
        sleep(1.0)
        if exists(Template(r"tpl1702194186578.png", record_pos=(0.211, 0.173), resolution=(1280, 720))):
            touch(Template(r"tpl1702194195716.png", record_pos=(0.211, 0.175), resolution=(1280, 720)))
            sleep(2.0)
        if exists(Template(r"tpl1702194221621.png", record_pos=(0.322, -0.249), resolution=(1280, 720))):
            touch(Template(r"tpl1702194233316.png", record_pos=(0.319, -0.25), resolution=(1280, 720)))
            sleep(1.0)
#             if exists(Template(r"tpl1702207763239.png", record_pos=(-0.416, -0.099), resolution=(1280, 720))):
#                 touch(Template(r"tpl1702194309969.png",threshold=0.9, record_pos=(-0.42, -0.096), resolution=(1280, 720)))
#                 sleep(1.0)
#             if exists(Template(r"tpl1702194259213.png", record_pos=(-0.351, 0.222), resolution=(1280, 720))):
#                 touch(Template(r"tpl1702194268085.png", record_pos=(-0.353, 0.221), resolution=(1280, 720)))
#                 sleep(1.0)
#                 if exists(Template(r"tpl1702207763239.png", record_pos=(-0.416, -0.099), resolution=(1280, 720))):
#                     touch(Template(r"tpl1702194309969.png", record_pos=(-0.42, -0.096), resolution=(1280, 720)))
#                     sleep(1.0)
            if exists(Template(r"tpl1702194339490.png", record_pos=(0.254, 0.205), resolution=(1280, 720))):
                touch(Template(r"tpl1702194379957.png", record_pos=(0.252, 0.202), resolution=(1280, 720)))
                sleep(1.0)
#huodongshilian()
def xuezhuan():
    if exists(Template(r"tpl1702194051922.png", record_pos=(-0.445, -0.223), resolution=(1280, 720))):
        posabs=["620","189"]
        touch(posabs)
        sleep(1.0)
    if exists(Template(r"tpl1702194116441.png", record_pos=(-0.344, -0.249), resolution=(1280, 720))):
        touch(Template(r"tpl1702194127926.png", record_pos=(-0.345, -0.245), resolution=(1280, 720)))
        sleep(2.0)
        pos1=["636","668"]
        touch(pos1)
        sleep(1.0)
        if exists(Template(r"tpl1702194186578.png", record_pos=(0.211, 0.173), resolution=(1280, 720))):
            touch(Template(r"tpl1702194195716.png", record_pos=(0.211, 0.175), resolution=(1280, 720)))
            sleep(2.0)
        if exists(Template(r"tpl1702194221621.png", record_pos=(0.322, -0.249), resolution=(1280, 720))):
            touch(Template(r"tpl1702194233316.png", record_pos=(0.319, -0.25), resolution=(1280, 720)))
            sleep(1.0)
#             for i in range(5):
#                 if exists(Template(r"tpl1702194511153.png", threshold=0.9,record_pos=(-0.414, -0.101), resolution=(1280, 720))):
#                     touch(Template(r"tpl1702194520900.png", threshold=0.9,record_pos=(-0.416, -0.098), resolution=(1280, 720)))
#                     sleep(1.0)
#                 if exists(Template(r"tpl1702207686129.png", record_pos=(-0.415, -0.098), resolution=(1280, 720))):
#                     break
#             if exists(Template(r"tpl1702194259213.png", record_pos=(-0.351, 0.222), resolution=(1280, 720))):
#                 touch(Template(r"tpl1702194268085.png", record_pos=(-0.353, 0.221), resolution=(1280, 720)))
#                 sleep(1.0)
#                 for i in range(5):
#                     if exists(Template(r"tpl1702194511153.png", threshold=0.9,record_pos=(-0.414, -0.101), resolution=(1280, 720))):
#                         touch(Template(r"tpl1702194520900.png", threshold=0.9,record_pos=(-0.416, -0.098), resolution=(1280, 720)))
#                         sleep(1.0)
#                     if exists(Template(r"tpl1702207686129.png", record_pos=(-0.415, -0.098), resolution=(1280, 720))):
#                         break
            if exists(Template(r"tpl1702194339490.png", record_pos=(0.254, 0.205), resolution=(1280, 720))):
                touch(Template(r"tpl1702194379957.png", record_pos=(0.252, 0.202), resolution=(1280, 720)))
                sleep(1.0)                

def shilianjiangli():
    if exists(Template(r"tpl1702194051922.png", record_pos=(-0.445, -0.223), resolution=(1280, 720))):
        posabs=["620","189"]
        touch(posabs)
        sleep(1.0)
        if exists(Template(r"tpl1702199757244.png", record_pos=(-0.002, -0.251), resolution=(1280, 720))):
            touch(Template(r"tpl1702199766823.png", record_pos=(-0.004, -0.246), resolution=(1280, 720)))
            sleep(2.0)
            for m in range(100):
                if exists(Template(r"tpl1702307104206.png", record_pos=(-0.302, 0.239), resolution=(1280, 720))):
                    touch(Template(r"tpl1702307104206.png", record_pos=(-0.302, 0.239), resolution=(1280, 720)))
                    sleep(1.0)
                else:
                    break
    for i in range(3):
        if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
            touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
            sleep(1.0)
        else:
            for m in range(3):
                posx=["1230","35"]
                touch(posx)
                sleep(1.0)
            break 

def wakuang():
    def putongkuang():
        pos1=["437","269"]
        touch(pos1)
        sleep(1.0)
        pos2=["1070","269"]
        touch(pos2)
        sleep(1.0)
        pos1=["200","627"]
        touch(pos1)
        sleep(10.0)
        pos1=["1130","697"]
        touch(pos1)
        sleep(1.0)
        if exists(Template(r"tpl1702201615169.png", record_pos=(-0.134, 0.184), resolution=(1280, 720))):
            touch(Template(r"tpl1702201624384.png", record_pos=(-0.133, 0.184), resolution=(1280, 720)))
            sleep(2.0)
        pos1=["200","627"]
        touch(pos1)
        sleep(2.0)
        if exists(Template(r"tpl1702201663197.png", record_pos=(-0.079, -0.061), resolution=(1280, 720))):
            touch(Template(r"tpl1702201674579.png", record_pos=(-0.08, -0.064), resolution=(1280, 720)))
            sleep(2.0)
        if exists(Template(r"tpl1702201694227.png", record_pos=(0.398, 0.237), resolution=(1280, 720))):
            touch(Template(r"tpl1702201704189.png", record_pos=(0.398, 0.238), resolution=(1280, 720)))
            sleep(3.0)
        pos2=["833","621"]
        touch(pos2)
        sleep(10.0)
        pos1=["1130","697"]
        touch(pos1)
        sleep(2.0)
        if exists(Template(r"tpl1702201615169.png", record_pos=(-0.134, 0.184), resolution=(1280, 720))):
            touch(Template(r"tpl1702201624384.png", record_pos=(-0.133, 0.184), resolution=(1280, 720)))
            sleep(2.0)
        pos2=["833","621"]
        touch(pos2)
        sleep(2.0)
        if exists(Template(r"tpl1702201663197.png", record_pos=(-0.079, -0.061), resolution=(1280, 720))):
            touch(Template(r"tpl1702201674579.png", record_pos=(-0.08, -0.064), resolution=(1280, 720)))
            sleep(2.0)
        if exists(Template(r"tpl1702201694227.png", record_pos=(0.398, 0.237), resolution=(1280, 720))):
            touch(Template(r"tpl1702201704189.png", record_pos=(0.398, 0.238), resolution=(1280, 720)))
            sleep(2.0)
        if exists(Template(r"tpl1702201801293.png", record_pos=(0.459, -0.253), resolution=(1280, 720))):
            touch(Template(r"tpl1702201842091.png", record_pos=(0.455, -0.252), resolution=(1280, 720)))
            sleep(1.0)

    def jingying():
        for i in range(3):
            pos1=["1155","330"]
            touch(pos1)
            sleep(1.0)
        for i in range(3):
            pos1=["320","425"]
            touch(pos1)
            sleep(1.0)
        pos1=["609","555"]
        touch(pos1)
        sleep(3.0)
        pos1=["1130","697"]
        touch(pos1)
        sleep(1.0)
        if exists(Template(r"tpl1702201615169.png", record_pos=(-0.134, 0.184), resolution=(1280, 720))):
            touch(Template(r"tpl1702201624384.png", record_pos=(-0.133, 0.184), resolution=(1280, 720)))
            sleep(2.0)
        for i in range(3):
            pos1=["1155","528"]
            touch(pos1)
            sleep(1.0)
        for i in range(3):
            pos1=["320","425"]
            touch(pos1)
            sleep(1.0)
        pos1=["609","555"]
        touch(pos1)
        sleep(3.0)
        pos1=["1130","697"]
        touch(pos1)
        sleep(2.0)
        if exists(Template(r"tpl1702201615169.png", record_pos=(-0.134, 0.184), resolution=(1280, 720))):
            touch(Template(r"tpl1702201624384.png", record_pos=(-0.133, 0.184), resolution=(1280, 720)))
            sleep(2.0)
        pos1=["1107","330"]
        touch(pos1)
        sleep(1.0)
        if exists(Template(r"tpl1702201663197.png", record_pos=(-0.079, -0.061), resolution=(1280, 720))):
            touch(Template(r"tpl1702201674579.png", record_pos=(-0.08, -0.064), resolution=(1280, 720)))
            sleep(2.0)
        if exists(Template(r"tpl1702201694227.png", record_pos=(0.398, 0.237), resolution=(1280, 720))):
            touch(Template(r"tpl1702201704189.png", record_pos=(0.398, 0.238), resolution=(1280, 720)))
            sleep(2.0)
        pos1=["1107","524"]
        touch(pos1)
        sleep(2.0)
        if exists(Template(r"tpl1702201663197.png", record_pos=(-0.079, -0.061), resolution=(1280, 720))):
            touch(Template(r"tpl1702201674579.png", record_pos=(-0.08, -0.064), resolution=(1280, 720)))
            sleep(2.0)
        if exists(Template(r"tpl1702201694227.png", record_pos=(0.398, 0.237), resolution=(1280, 720))):
            touch(Template(r"tpl1702201704189.png", record_pos=(0.398, 0.238), resolution=(1280, 720)))
            sleep(2.0)
        if exists(Template(r"tpl1702203018805.png", record_pos=(0.46, -0.248), resolution=(1280, 720))):
            touch(Template(r"tpl1702203018805.png", record_pos=(0.46, -0.248), resolution=(1280, 720)))
            sleep(1.0)

    print("zx!")
    if exists(Template(r"tpl1702201218982.png", record_pos=(-0.133, 0.185), resolution=(1280, 720))):
        touch(Template(r"tpl1702201240625.png", record_pos=(-0.134, 0.199), resolution=(1280, 720)))
        sleep(1.0)
    if exists(Template(r"tpl1702203602672.png", record_pos=(0.333, -0.111), resolution=(1280, 720))):
        for i in range(5):
            if exists(Template(r"tpl1702201285059.png", record_pos=(-0.398, 0.202), resolution=(1280, 720))):
                touch(Template(r"tpl1702201295272.png", record_pos=(-0.395, 0.204), resolution=(1280, 720)))
                sleep(1.0)
            if exists(Template(r"tpl1702225982681.png", record_pos=(-0.096, -0.151), resolution=(1280, 720))):
                break   
    if exists(Template(r"tpl1702201336719.png", record_pos=(-0.101, -0.156), resolution=(1280, 720))):
        touch(Template(r"tpl1702201348019.png", record_pos=(-0.105, -0.152), resolution=(1280, 720)))
        sleep(1.0)
    if exists(Template(r"tpl1702232638747.png", record_pos=(-0.341, -0.252), resolution=(1280, 720))):
        touch(Template(r"tpl1702232668661.png", record_pos=(-0.336, -0.248), resolution=(1280, 720)))
        sleep(1.0)
    if exists(Template(r"tpl1702201390519.png", record_pos=(-0.339, 0.025), resolution=(1280, 720))):
        touch(Template(r"tpl1702201400332.png", record_pos=(-0.34, 0.034), resolution=(1280, 720)))
        sleep(1.0)
        putongkuang()
    if exists(Template(r"tpl1702201933702.png", record_pos=(-0.028, 0.01), resolution=(1280, 720))):
        touch(Template(r"tpl1702201950406.png", record_pos=(-0.023, 0.027), resolution=(1280, 720)))
        sleep(1.0)
        putongkuang()
    if exists(Template(r"tpl1702201999422.png", record_pos=(0.316, 0.019), resolution=(1280, 720))):
        touch(Template(r"tpl1702202008567.png", record_pos=(0.312, 0.013), resolution=(1280, 720)))
        sleep(1.0)
        putongkuang()
    if exists(Template(r"tpl1702202029981.png", record_pos=(-0.171, -0.248), resolution=(1280, 720))):
        touch(Template(r"tpl1702202037856.png", record_pos=(-0.175, -0.249), resolution=(1280, 720)))
        if exists(Template(r"tpl1702201390519.png", record_pos=(-0.339, 0.025), resolution=(1280, 720))):
            touch(Template(r"tpl1702201400332.png", record_pos=(-0.34, 0.034), resolution=(1280, 720)))
            sleep(1.0)
            if exists(Template(r"tpl1702202084103.png", record_pos=(-0.353, 0.087), resolution=(1280, 720))):
                touch(Template(r"tpl1702202091647.png", record_pos=(-0.349, 0.086), resolution=(1280, 720)))
                sleep(1.0)
                pos1=["1155","404"]
                touch(pos1)
                sleep(1.0)
                pos1=["1155","587"]
                touch(pos1)
                sleep(1.0)
                jingying()
                sleep(1.0)
        if exists(Template(r"tpl1702203283746.png", record_pos=(-0.025, 0.02), resolution=(1280, 720))):
            touch(Template(r"tpl1702203295920.png", record_pos=(-0.024, 0.023), resolution=(1280, 720)))
            sleep(1.0)
            if exists(Template(r"tpl1702203319631.png", record_pos=(-0.326, 0.084), resolution=(1280, 720))):
                touch(Template(r"tpl1702203329749.png", record_pos=(-0.336, 0.086), resolution=(1280, 720)))
                sleep(1.0)
                pos1=["1155","404"]
                touch(pos1)
                sleep(1.0)
                pos1=["1155","587"]
                touch(pos1)
                sleep(1.0)
                jingying()
                sleep(1.0)
        if exists(Template(r"tpl1702203392896.png", record_pos=(0.31, 0.02), resolution=(1280, 720))):
            touch(Template(r"tpl1702203403885.png", record_pos=(0.293, 0.027), resolution=(1280, 720)))
            sleep(1.0)
            if exists(Template(r"tpl1702203422553.png", record_pos=(-0.35, 0.086), resolution=(1280, 720))):
                touch(Template(r"tpl1702203438908.png", record_pos=(-0.345, 0.086), resolution=(1280, 720)))
                sleep(1.0)
                pos1=["1155","404"]
                touch(pos1)
                sleep(1.0)
                pos1=["1155","587"]
                touch(pos1)
                sleep(1.0)
                jingying()
                sleep(1.0)
    for i in range(3):
        if exists(Template(r"tpl1702187103866.png", record_pos=(0.46, -0.25), resolution=(1280, 720))):
            touch(Template(r"tpl1702187113110.png", record_pos=(0.46, -0.25), resolution=(1280, 720)))
            sleep(1.0)
        else:
            for m in range(3):
                posx=["1230","35"]
                touch(posx)
                sleep(1.0)
            break
        if exists(Template(r"tpl1702188862224.png", record_pos=(-0.405, -0.175), resolution=(1280, 720))):
            touch(Template(r"tpl1702188874613.png", record_pos=(-0.405, -0.176), resolution=(1280, 720)))
            sleep(1.0) 
#wakuang()            
            
def chonglian():
    def lunch():
        if exists(Template(r"tpl1702186639646.png", record_pos=(-0.002, 0.221), resolution=(1280, 720))):
            touch(Template(r"tpl1702186652433.png", record_pos=(-0.002, 0.221), resolution=(1280, 720)))
        sleep(10.0)
        for i in range(3):
            if exists(Template(r"tpl1702186689773.png", record_pos=(0.253, -0.18), resolution=(1280, 720))):
                touch(Template(r"tpl1702186701525.png", record_pos=(0.259, -0.18), resolution=(1280, 720)))
                sleep(1.0)
            else:
                break
    for i in range(100):
        if exists(Template(r"tpl1702191691268.png", record_pos=(-0.003, 0.222), resolution=(1280, 720))):
            lunch()
        else:
            break
            
def xuezuanshift():
    if exists(Template(r"tpl1702208964907.png", record_pos=(0.281, 0.08), resolution=(1280, 720))):
        touch(Template(r"tpl1702208974662.png", record_pos=(0.284, 0.082), resolution=(1280, 720)))
        sleep(1.0)
    if exists(Template(r"tpl1702208997696.png", record_pos=(0.318, -0.252), resolution=(1280, 720))):
        touch(Template(r"tpl1702209007279.png", record_pos=(0.324, -0.248), resolution=(1280, 720)))
        sleep(1.0)
    if exists(Template(r"tpl1702209032112.png", record_pos=(-0.417, -0.099), resolution=(1280, 720))):
        touch(Template(r"tpl1702209045378.png", record_pos=(-0.416, -0.099), resolution=(1280, 720)))
        sleep(1.0)
    else:
        touch(Template(r"tpl1702209064800.png", record_pos=(-0.358, 0.226), resolution=(1280, 720)))
        sleep(1.0)
        touch(Template(r"tpl1702209045378.png", record_pos=(-0.416, -0.099), resolution=(1280, 720)))
        sleep(1.0)
    if exists(Template(r"tpl1702209238284.png", record_pos=(0.253, 0.199), resolution=(1280, 720))):
        touch(Template(r"tpl1702209248000.png", record_pos=(0.255, 0.202), resolution=(1280, 720)))
        sleep(1.0)
def xuezuanoff():
    if exists(Template(r"tpl1702208964907.png", record_pos=(0.281, 0.08), resolution=(1280, 720))):
        touch(Template(r"tpl1702208974662.png", record_pos=(0.284, 0.082), resolution=(1280, 720)))
        sleep(1.0)
    if exists(Template(r"tpl1702208997696.png", record_pos=(0.318, -0.252), resolution=(1280, 720))):
        touch(Template(r"tpl1702209007279.png", record_pos=(0.324, -0.248), resolution=(1280, 720)))
        sleep(1.0)
    if exists(Template(r"tpl1702209306626.png", record_pos=(-0.417, -0.098), resolution=(1280, 720))):
        touch(Template(r"tpl1702209306626.png", record_pos=(-0.417, -0.098), resolution=(1280, 720)))
        sleep(1.0)
    else:
        touch(Template(r"tpl1702209064800.png", record_pos=(-0.358, 0.226), resolution=(1280, 720)))
        sleep(1.0)
        touch(Template(r"tpl1702209306626.png", record_pos=(-0.417, -0.098), resolution=(1280, 720)))
        sleep(1.0)
    if exists(Template(r"tpl1702209238284.png", record_pos=(0.253, 0.199), resolution=(1280, 720))):
        touch(Template(r"tpl1702209248000.png", record_pos=(0.255, 0.202), resolution=(1280, 720)))
        sleep(1.0)

            
current_date = date.today()  
#print("当前日期：", current_date)
current_time = datetime.now().time()  
current_datetime = datetime.now() 
weekday = current_datetime.weekday()  
weekday_tmp=weekday
print("星期几：",weekday+1)
# 获取当前时间  
print("当前时间：", current_time)
start_time1 = time(hour=8, minute=30, second=0)  
end_time1 = time(hour=8, minute=32, second=0)
start_time0 = time(hour=7, minute=59, second=58)  
end_time0 = time(hour=8, minute=1, second=30)
start_time2 = time(hour=16, minute=0, second=30)  
end_time2 = time(hour=23, minute=55, second=0)
start_time3 = time(hour=22, minute=0, second=30)  
end_time3 = time(hour=23, minute=55, second=0)
start_time4 = time(hour=1, minute=0, second=30)  
end_time4 = time(hour=1, minute=2, second=0)
start_time5 = time(hour=0, minute=0, second=30)  
end_time5 = time(hour=0, minute=2, second=0)
start_time6 = time(hour=2, minute=29, second=30)  
end_time6 = time(hour=2, minute=30, second=30)
start_time7 = time(hour=10, minute=0, second=30)  
end_time7 = time(hour=10, minute=1, second=30)
start_time8 = time(hour=12, minute=0, second=30)  
end_time8 = time(hour=12, minute=1, second=30)
start_time9 = time(hour=22, minute=30, second=30)  
end_time9 = time(hour=22, minute=31, second=30)
start_time10 = time(hour=23, minute=30, second=30)  
end_time10 = time(hour=23, minute=31, second=30)
start_time11 = time(hour=20, minute=40, second=30)  
end_time11 = time(hour=20, minute=42, second=0)
start_time12 = time(hour=21, minute=40, second=30)  
end_time12 = time(hour=21, minute=42, second=0)
rest_time = time(hour=9, minute=30, second=30)
rest_time1 = time(hour=9, minute=32, second=30)
rest_end = time(hour=21, minute=30, second=30)
rest_end1 = time(hour=21, minute=32, second=30)
# dm_time = time(hour=13, minute=0, second=30)
# dm_time1 = time(hour=13, minute=2, second=30)

zx_flag1=0
zx_flag0=0
zx_flag2=0
zx_flag3=0
zx_flag4=0
while 1:
    current_date = date.today()  
    current_time = datetime.now().time()  
    current_datetime = datetime.now() 
    weekday = current_datetime.weekday()
    if weekday!=weekday_tmp:
        print(weekday_tmp)
#         zx_flag1=0
#         zx_flag0=0
        zx_flag2=0
        zx_flag3=0
#         zx_flag4=0
    weekday_tmp=weekday
    #sleep(2.0)
    #for i in range(2):
    sleep(1.0)
        #if zx_flag1==0:
    if start_time1 <= current_datetime.time() <= end_time1:
        #try:
        shilian2zhuye()
        sleep(1.0)
        meirifuli()
        sleep(1.0)
        meirilingqu()
        sleep(1.0)
        youjian()
        sleep(1.0)
        huodong_flag=huodong()
        sleep(1.0)
        huodong_flag=zhuchengrenwu(huodong_flag)
        sleep(1.0)
        shilianjiangli()
        sleep(1.0)
        huodongshilian()
        sleep(60.0)
        #zx_flag1=1
#                 except:
#                     chonglian()
    #for i in range(2):
    sleep(20.0)
    #if zx_flag0==0:
    if start_time0 <= current_datetime.time() <= end_time0:
        #try:
        shilian2zhuye()
        sleep(1.0)
        zhuye2lunch()
        sleep(1.0)
        lunch()
        sleep(1.0)
        shenmota()
        sleep(1.0)
        meirifuli()
        sleep(1.0)
        huodongshilian()
        sleep(90.0)
            #zx_flag0=1
#                 except:
#                     chonglian()
    sleep(1.0)
    if zx_flag2==0:
        if weekday==6 or weekday==5 or weekday==0:
            if start_time2 <= current_datetime.time() <= end_time2:
                shilian2zhuye()
                sleep(1.0)
                xuezhuan()
                sleep(1.0)
                zx_flag2=1
    sleep(1.0)
    if weekday==4:
        if zx_flag3==0:
            if start_time3 <= current_datetime.time() <= end_time3:
                shilian2zhuye()
                sleep(1.0)
                xuezhuan()
                sleep(1.0)
                zx_flag3=1
    sleep(1.0)
    if weekday==3:
        #if zx_flag4==0:
        if start_time4 <= current_datetime.time() <= end_time4:
            shilian2zhuye()
            sleep(1.0)
            shenmota()
            sleep(1.0)
            huodongshilian()
            sleep(90.0)
            #zx_flag4=1
    if weekday==4 or weekday==5 or weekday==6:
        if start_time9 <= current_datetime.time() <= end_time9:
            xuezuanshift()
            sleep(60.0)
        if start_time10 <= current_datetime.time() <= end_time10:
            xuezuanoff()
            sleep(60.0)
    if weekday==0:
        if start_time11 <= current_datetime.time() <= end_time11:
            xuezuanshift()
            sleep(90.0)
        if start_time12 <= current_datetime.time() <= end_time12:
            xuezuanoff()
            sleep(90.0)
    if start_time6 <= current_datetime.time() <= end_time6:
        shilian2zhuye()
        sleep(2.0)
        meirifuli()
        sleep(1.0)
        wakuang()
        sleep(60.0)
        huodongshilian()
        sleep(1.0)
    if  start_time7 <= current_datetime.time() <= end_time7:
        shilian2zhuye()
        sleep(2.0)
        meirifuli()
#         sleep(1.0)
#         huodongshilian()
        sleep(90.0)
    if  start_time8 <= current_datetime.time() <= end_time8:
        shilian2zhuye()
        sleep(2.0)
        meirifuli()
        sleep(1.0)
        yingxiongmen()
#         huodongshilian()
        sleep(90.0)
#     if  dm_time <= current_datetime.time() <= dm_time1:
#         shilian2zhuye()
#         sleep(2.0)
#         yingxiongmen()
#         sleep(60.0)
    if weekday==1 or weekday==2 or weekday==3 or weekday==4:
        if rest_time <= current_datetime.time() <= rest_time1:
            shilian2zhuye()
            sleep(120.0)
        if rest_end <= current_datetime.time() <= rest_end1:
            shilian2zhuye()
            sleep(1.0)
            xuezhuan()
            sleep(120.0)
    if exists(Template(r"tpl1702199267930.png", record_pos=(0.316, 0.143), resolution=(1280, 720))):
        chonglian()
        sleep(1.0)
        huodongshilian()
        zx_flag2=0
        zx_flag3=0
        sleep(1.0)
    if exists(Template(r"tpl1702199546943.png", record_pos=(-0.311, -0.266), resolution=(1280, 720)))or(start_time5 <= current_datetime.time() <= end_time5):
        if exists(Template(r"tpl1702200895735.png", record_pos=(0.283, 0.081), resolution=(1280, 720))):
            shilian2zhuye()
            sleep(1.0)
        if ((weekday==1 or weekday==2 or weekday==3 or weekday==4)and (rest_time<= current_datetime.time()<=rest_end)):
            sleep(1.0)
        else:
            if exists(Template(r"tpl1702294962571.png", record_pos=(0.002, -0.178), resolution=(1280, 720))):
                posx=["969","130"]
                touch(posx)
                sleep(2.0)
            huodongshilian()
        #sleep(1.0)
#     print(zx_flag1)
#     print(zx_flag0)
#     print(zx_flag2)
#     print(zx_flag3)
#     print(zx_flag4)
