#! /usr/bin/env python3
######################################################################
# tuner.py - a minimal command-line guitar/ukulele tuner in Python.
######################################################################
# Author:  Matt Zucker
# Date:    July 2016
# License: [Creative Commons Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/us/)
######################################################################

import numpy as np
import pyaudio

######################################################################
# 请自由发挥这些数值的作用。可能想改变NOTE_MIN和NOTE_MAX，特别是对于吉他/贝斯。可能想保持FRAME_SIZE和FRAMES_PER_FFT为2的幂。

NOTE_MIN = 60        # C4
NOTE_MAX = 69        # A4
FSAMP = 22050        # 采样率，单位：Hz
FRAME_SIZE = 2048    # 每一帧有多少个样本
FRAMES_PER_FFT = 16  # FFT在多少帧中取平均值

######################################################################
# 从上面的常数衍生出来的数量。请注意，随着SAMPLES_PER_FFT的增加，频率的步长会减少（所以分辨率会提高）；但是，处理新的声音会产生更大的延迟。

SAMPLES_PER_FFT = FRAME_SIZE * FRAMES_PER_FFT
FREQ_STEP = float(FSAMP) / SAMPLES_PER_FFT

######################################################################
# 用于打印音符

NOTE_NAMES = 'C C# D D# E F F# G G# A A# B'.split()

######################################################################
# 这三个很有用的函数基于此网页：
# https://newt.phys.unsw.edu.au/jw/notes.html


def freq_to_number(f):
    return 69 + 12 * np.log2(f / 440.0)


def number_to_freq(n):
    return 440 * 2.0 ** ((n - 69) / 12.0)


def note_name(n):
    return NOTE_NAMES[n % 12] + str(n / 12 - 1)

######################################################################
# 获取我们关心的音符在FFT中的最小/最大索引。参考 numpy.rfftfreq() 文档


def note_to_fftbin(n):
    return number_to_freq(n)/FREQ_STEP


imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN-1))))
imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX+1))))

# 分配空间来运行FFT（快速傅里叶变换）。
buf = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)
num_frames = 0

# 初始化音频
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=FSAMP,
                    input=True,
                    frames_per_buffer=FRAME_SIZE)
stream.start_stream()

# 创建Hanning窗功能
window = 0.5 * (1 - np.cos(np.linspace(0, 2*np.pi, SAMPLES_PER_FFT, False)))

# 打印初始文本
print(f'sampling at {FSAMP} Hz with max resolution of {FREQ_STEP} Hz')

# 只要我们获得数据：
while stream.is_active():

    # 缓冲区下移，新数据进入
    buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
    buf[-FRAME_SIZE:] = np.frombuffer(stream.read(FRAME_SIZE), np.int16)

    # 在窗口化的缓冲区上运行FFT
    fft = np.fft.rfft(buf * window)

    # 获取范围内最大响应的频率
    freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP

    # 获取银丰数值和最近的音符
    n = freq_to_number(freq)
    n0 = int(round(n))

    # 一旦我们有一个完整的缓冲区，控制台输出
    num_frames += 1

    if num_frames >= FRAMES_PER_FFT:
        print(f'freq: {freq:7.2f} Hz     note: {note_name(n0):>3s} {n - n0:+.2f}')
