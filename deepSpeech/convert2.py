import librosa

y,sr = librosa.load("audiosTestIemocap/Ses01F_impro01.wav",mono=False)
y_mono = librosa.to_mono(y)
y_mono = librosa.resample(y_mono,16000,sr)
print(sr)
librosa.output.write_wav('convert2.wav',y_mono,sr)
