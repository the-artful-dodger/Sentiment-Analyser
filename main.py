# -*- coding: utf-8 -*-

import requests
from analyser import Analyser
from src.parser import *
from emotions import Emotion
import numpy as np
import matplotlib.pyplot as plt

page = requests.get('http://www.huffingtonpost.com/byron-williams/bitter-frustrated-welcome_b_96884.html')

p = Parser()
parser = CommentParser()
parser.init_parser()
parser.feed(page.text)

analyser = Analyser()

emo1 = Emotion()

wt_angry, wt_sad, wt_happy = analyser.analyse_emotion(parser.data_list)

data_list = analyser.remove_punctuation(parser.data_list)
for word in data_list:
    if word in emo1.angry:
        wt_angry += 1
    if word in emo1.sad:
        wt_sad += 1
    if word in emo1.happy:
        wt_happy += 1

print wt_happy, wt_sad, wt_angry


##############
N = 3
pol1Means = (wt_happy, wt_sad, wt_angry)
pol1Std = (0, 0, 0)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(ind, pol1Means, width, color='r', yerr=pol1Std)
#
# pol2Means = (5, 24, 10)
# pol2Std = (0, 0, 0)
# rects2 = ax.bar(ind + width, pol2Means, width, color='y', yerr=pol2Std)

# add some text for labels, title and axes ticks
ax.set_xticks(ind + width)
ax.set_xticklabels(('Happy', 'Sad', 'Angry'))

ax.legend((rects1[0], rects2[0]), ('Pol1', 'Pol2'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
