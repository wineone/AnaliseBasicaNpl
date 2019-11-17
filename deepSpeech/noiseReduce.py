import noisereduce as nr
import librosa
from scipy.io import wavfile

data, rate =  librosa.load("saida1.wav")

nois = data[:]

data = nr.reduce_noise(data,nois)

librosa.output.write_wav("saida1noisereduce.wav",data,rate)
