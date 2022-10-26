from math import *
from datetime import datetime

import numpy
from PIL import Image

import save
from constants import ACTIVITIES, COLOR_BG, MAX_X, MAX_Y, RESIZE_TO, RADIUS
from constants import h, m, s

data = numpy.zeros((MAX_X, MAX_Y, 3), dtype=numpy.uint8)
data[:][:] = COLOR_BG
x_prev = 0
days = 0

for x in save.activities_log:
    activity, x = x
    x = (datetime.strptime(x, "%H:%M:%S") - datetime.strptime("00:00:00", "%H:%M:%S")).total_seconds() + 1
    x /= h

    if x < x_prev: days += 1
    x_prev = x

    y = round(cos(pi * x / 12)*(RADIUS + days//7) - MAX_Y//2)
    x = round(sin(pi * x / 12)*(RADIUS + days//7) + MAX_X//2)
    data[x][y] = ACTIVITIES[activity]

print(days/7, 'weeks')

image = Image.fromarray(data)
image = image.transpose(Image.Transpose.ROTATE_90)
image = image.resize((RESIZE_TO[0], RESIZE_TO[1]), resample=Image.Resampling.BOX)
image.save('image.png')
image.show()