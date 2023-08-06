#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import simpleaudio as sa


# 获取每个样本的持续时间，T为音符持续秒数，即周期
sample_rate = 44100
# T = 1  # BPM: 60
T = 0.25  # BPM: 120
t = np.linspace(0, T, int(T * sample_rate), False)

# 计算音符频率
freq_list = [440*2**(i / 12) for i in range(13)]
# 生成正弦波音符
notes = [np.sin(i*t*2*np.pi) for i in freq_list]

# 连环音符
audio = np.hstack(notes)
# 归一化为16位范围
audio *= (2 ** 15 - 1) / np.max(np.abs(audio))
# 转换为16位数据
audio = audio.astype(np.int16)

# 开始回放
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# 退出前等待回放结束
play_obj.wait_done()
