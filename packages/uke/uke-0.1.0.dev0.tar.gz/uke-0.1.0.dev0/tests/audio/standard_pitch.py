#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plt

frequency = 440  # 标准音高440Hz
fs = 44100  # 采样率
secends = 3  # 音符持续3秒

t = np.linspace(0, secends, secends * fs)

note = np.sin(frequency * t * 2 * np.pi)  # 440Hz正弦波
plt.plot(note)
plt.show()

audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)

play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj.wait_done()
