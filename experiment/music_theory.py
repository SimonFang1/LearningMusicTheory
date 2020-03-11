import numpy as np
import struct
import pyaudio

def sound(input_array, fs, volome=0.8):
    A = 32767 * volome
    input_array = np.array(input_array)
    toInt = np.int16(np.around(A * input_array/ np.max(input_array)))
    bin_dat = struct.pack('{}h'.format(len(toInt)), *toInt)
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()
    # open stream (2), 2 is size in bytes of int16
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=fs,
                    output=True)
    # play stream (3), blocking call
    stream.write(bin_dat)
    # stop stream (4)
    stream.stop_stream()
    stream.close()
    # close PyAudio (5)
    p.terminate()


def sound_binary(input_array, fs):
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()
    # open stream (2), 2 is size in bytes of int16
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=fs,
                    output=True)
    # play stream (3), blocking call
    stream.write(input_array)
    # stop stream (4)
    stream.stop_stream()
    stream.close()
    # close PyAudio (5)
    p.terminate()

def fft(signal, fs = 44100, f_up = 8000):
    t_size = len(signal)
    if f_up <= 0:
        fft_size = t_size
    else:
        fft_size = np.int(f_up * t_size / fs)  
    freqs = np.linspace(0, f_up, fft_size)
    yf = np.abs(np.fft.fft(signal)) / fft_size
    yf = yf[:fft_size]
    return yf, freqs


def fft4plot(signal, fs = 44100, f_up = 8000):
    yfp, freqs = fft(signal, fs, f_up)
    yfp = 20*np.log10(np.clip(yfp, 1e-10, 1e100))
    return yfp, freqs
