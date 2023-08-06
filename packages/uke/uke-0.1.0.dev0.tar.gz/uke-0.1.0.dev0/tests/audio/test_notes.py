#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#simpleaudio
import numpy as np
import simpleaudio as sa

# 计算音符频率
A1_freq = 440  # 纯一度A¹
Ash1_freq = A1_freq * 2 ** (1 / 12)  # 增一度A#¹/小二度Bb¹
B1_freq = A1_freq * 2 ** (2 / 12)  # 大二度B¹
C_freq = A1_freq * 2 ** (3 / 12)  # 小三度C
Csh_freq = A1_freq * 2 ** (4 / 12)  # 大三度C#
D_freq = A1_freq * 2 ** (5 / 12)  # 纯四度D
Dsh_freq = A1_freq * 2 ** (6 / 12)  # 增四度D#/减五度Eb
E_freq = A1_freq * 2 ** (7 / 12)  # 纯五度E
F_freq = A1_freq * 2 ** (8 / 12)  # 小六度F
Fsh_freq = A1_freq * 2 ** (9 / 12)  # 大六度F#
G_freq = A1_freq * 2 ** (10 / 12)  # 小七度G
Gsh_freq = A1_freq * 2 ** (11 / 12)  # 大七度G#
A_freq = A1_freq * 2  # 纯八度A

# 获取每个样本的持续时间，T为音符持续秒数，即周期
sample_rate = 44100
T = 1
# T = 0.25
t = np.linspace(0, T, int(T * sample_rate), False)

# 生成正弦波音符
A1_note = np.sin(A1_freq * t * 2 * np.pi)
Ash1_note = np.sin(Ash1_freq * t * 2 * np.pi)
B1_note = np.sin(B1_freq * t * 2 * np.pi)
C_note = np.sin(C_freq * t * 2 * np.pi)
Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
D_note = np.sin(D_freq * t * 2 * np.pi)
Dsh_note = np.sin(Dsh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)
F_note = np.sin(F_freq * t * 2 * np.pi)
Fsh_note = np.sin(Fsh_freq * t * 2 * np.pi)
G_note = np.sin(G_freq * t * 2 * np.pi)
A_note = np.sin(A_freq * t * 2 * np.pi)

# 连环音符
audio = np.hstack((
    A1_note, Ash1_note, B1_note,
    C_note, Csh_note, D_note,
    Dsh_note, E_note, F_note,
    Fsh_note, G_note, A_note,
))
# 归一化为16位范围
audio *= (2 ** 15 - 1) / np.max(np.abs(audio))
# 转换为16位数据
audio = audio.astype(np.int16)

# 开始回放
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# 退出前等待回放结束
play_obj.wait_done()
