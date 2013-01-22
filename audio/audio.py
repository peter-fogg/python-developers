#!/usr/bin/env python3
import os
import wave

# All sorts of cross-platform support.
WINDOWS = False
LINUX = False
OSX = False
try:
    import winsound
    WINDOWS = True
except ImportError:
    try:
        import ossaudiodev
        LINUX = True
    except ImportError:
        OSX = True

def write_file(sound, filename='audio.wav'):
    """
    Takes an array of floats in the range [0, 1] and writes it to a
    .wav file.
    """
    w = wave.open(filename, 'w')
    framerate = 44100
    # (number of channels, samplewidth in bytes, framerate, number of frames, compression type, compression name)
    w.setparams((1, 2, framerate, len(sound), 'NONE', 'noncompressed'))
    signal = b''
    for s in sound:
        signal += wave.struct.pack('h', int(1000*s))
    w.writeframes(signal)

def play(filename='audio.wav'):
    if WINDOWS:
        winsound.PlaySound(sound, winsound.SND_FILENAME)
    elif LINUX:
        dev = ossaudiodev.open('w')
        print('foo')
    elif OSX:
        os.system('afplay %s' % filename)

if __name__ == '__main__':
    import math
    sound = [math.sin(2*math.pi*440*i/44100) for i in range(44100)]
    write_file(sound)
    play()
