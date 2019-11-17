from pydub import AudioSegment

audio = "audiosTestIemocap/Ses01F_impro01.wav"

sound = AudioSegment.from_wav(audio)
sound = sound.set_channels(1)
sound = sound.set_frame_rate(16000)
sound = sound.apply_gain(10)
sound.export("saida1.wav",format="wav")

