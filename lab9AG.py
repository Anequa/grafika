from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps, ImageShow
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

im = Image.open('brain.png')

szary = im.convert("L")
print(szary.mode)
statystyki(szary)

hist = szary.histogram()
plt.title("histogram - leg ")
plt.bar(range(256), hist[:256], color='r', alpha=0.5)

plt.show()

# extrema  [(0, 204)]
# count  [246024]
# mean  [71.68539248203427]
# median  [68]
# stddev  [66.80954765052061]

def histogram_norm(szary):
    h,w= szary.size
    hist = szary.histogram()
    for i in range(len(hist)):
        hist[i]=hist[i]/(w*h)
    plt.title("histogram - leg ")
    plt.plot(range(256), hist[:256], color='r', alpha=0.5)
    plt.show()
    return hist

# histogram_norm(szary)

def histogram_cumul(szary):
    temp=[]
    hist = histogram_norm(szary)
    h,w= szary.size
    for i in range(len(hist)):
        temp.append(sum(hist[:i+1]))
    plt.title("histogram - cumul ")
    plt.plot(range(256), temp[:256], color='r', alpha=0.5)
    plt.show()
histogram_cumul(szary)