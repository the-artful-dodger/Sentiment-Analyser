# -*- coding: utf-8 -*-

import requests
from analyser import Analyser
from src.parser import *
import random
from emotions import Emotion
import time
import numpy as np
import matplotlib.pyplot as plt


#page = requests.get('http://www.sandeepweb.com/narendra-modi-rocks-capitol-hill-burnol-inc-burns-rajdeep-sardesai-nidhi-razdan-karan-thapar-subramanian-swamy-capitol-hill-us-congress-obama-indian-media-stolen-indian-artifacts/')
i = 0
#p = Parser()
#parser = CommentParser()
#parser.init_parser()
#parser.feed(page.text)
# http://www.sandeepweb.com/narendra-modi-rocks-capitol-hill-burnol-inc-burns-rajdeep-sardesai-nidhi-razdan-karan-thapar-subramanian-swamy-capitol-hill-us-congress-obama-indian-media-stolen-indian-artifacts/
#analyser = Analyser()

emo1 = Emotion()
wt_angry = 0
wt_sad = 0
wt_happy = 0

#wt_angry, wt_sad, wt_happy = analyser.analyse_emotion(parser.data_list)
j = 0
k = 0
#data_list = analyser.remove_punctuation(parser.data_list)

while i<15:
    i += 1
    k = 0
    while k< 600:
        k += 1
        tmp = random.choice(random.choice([Emotion.angry, Emotion.sad, Emotion.happy]))
        if tmp in Emotion.sad:
            wt_sad += random.randrange(1, 5, 1)
        if tmp in Emotion.angry:
            wt_angry += random.randrange(1, 5, 1)
        if tmp in Emotion.happy:
            wt_happy += random.randrange(1, 5, 1)

        print tmp
        time.sleep(0.1)

print wt_happy, wt_sad, wt_angry

##############
N = 3
pol1Means = (wt_happy, wt_sad, wt_angry)
pol1Std = (0, 0, 0)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, pol1Means, width, color='r', yerr=pol1Std)
ax.set_xticks(ind + width - 0.2)
ax.set_xticklabels(('Happy', 'Sad', 'Angry'))
plt.show()