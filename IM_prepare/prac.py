import random
from tkinter import *

name_list = [
    '예지인',
    '민경현',
    '이예슬',
    '유창재',
    '진익근',
    '허주혁',
    '임혜진',
    '서동훈',
    '김성용',
    '송준우',
]

line = [
    '망나니',
    '황족',
    '백정',
    '왕자',
    '도구'
]

idx = 0

random.shuffle(name_list)

for i in range(len(name_list)):
    widget = Label(None, text=f'{name_list[i]} 는 {line[idx]} 입니다.')
    widget.pack()
    if i % 2 == 1:
       idx += 1

widget.mainloop()