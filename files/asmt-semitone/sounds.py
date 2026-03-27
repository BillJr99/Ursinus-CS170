# https://stackoverflow.com/questions/974071/python-library-for-playing-fixed-frequency-sound

"""Play a fixed frequency sound."""
from __future__ import division
import math
from scipy import signal
from pyaudio import PyAudio # sudo apt-get install python{,3}-pyaudio

try:
    from itertools import izip
except ImportError: # Python 3
    izip = zip
    xrange = range

def sine_tone(frequency, duration, volume=1, sample_rate=22050):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)
                    
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))

    if duration >= 1:
        sample_size = sample_rate
    else:
        sample_size = int(sample_rate * duration)

    for buf in izip(*[samples]*sample_size): # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()

def square_tone(frequency, duration, volume=1, sample_rate=22050):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)

    s = lambda t: volume * signal.square(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))

    if duration >= 1:
        sample_size = sample_rate
    else:
        sample_size = int(sample_rate * duration)

    for buf in izip(*[samples]*sample_size): # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()    

def dtmf_tone(frequency1, frequency2, duration, volume=1, sample_rate=22050):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate 

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)
                    
    s1 = lambda t: volume * math.sin(2 * math.pi * frequency1 * t / sample_rate)
    s2 = lambda t: volume * math.sin(2 * math.pi * frequency2 * t / sample_rate)
    samples = (int(s1(t) * 0x3f + 0x40) + int(s2(t) * 0x3f + 0x40) for t in xrange(n_samples)) # scale to 0-255

    if duration >= 1:
        sample_size = sample_rate
    else:
        sample_size = int(sample_rate * duration)

    for buf in izip(*[samples]*sample_size): # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()

def sine_chord(frequencies, duration, volume=1, sample_rate=22050):
    if len(frequencies) >= 6:
        frequencies = frequencies[:6]

    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate 

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)

    s = []
    k = len(frequencies)
    for i in range(k):                
        f = frequencies[i]
        sf = lambda t: volume * math.sin((2 * math.pi * f * t / sample_rate))
        s.append(sf)

    z = lambda t: sum([int(x(t) * (2**(8-k)-1) + 2**(8-k)) for x in s])
    samples = (z(t) for t in xrange(n_samples)) # scale to 0-255

    if duration >= 1:
        sample_size = sample_rate
    else:
        sample_size = int(sample_rate * duration)

    for buf in izip(*[samples]*sample_size): # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()    