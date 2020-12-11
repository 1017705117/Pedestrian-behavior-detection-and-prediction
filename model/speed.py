import math
#location1和location2分别为检测目标的前一个位置和后一个位置的坐标，具体为[x, y, w, h] ti分别为前一个位置所记录的时间和后一个位置记录的时间
def Speed(location1, location2,ti1,ti2):
    #算出变化的像素距离
    dis = math.sqrt(math.pow(location2[0] - location1[0], 2) + math.pow(location2[1] - location1[1], 2))
    #距离除以时间获得粗略的速度
    speed = dis/(ti2-ti1)
    return speed

