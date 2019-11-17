import wave
import sys
ip = wave.open(sys.argv[1], "r")

op = wave.open(sys.argv[2], "w")
op.setparams(ip.getparams())

for i in range(ip.getnframes()):
	iframes = ip.readframes(1)
	amp = int(iframes.encode("hex"),16)
if amp > 32767:
	amp = 65535 - int(iframes.encode("hex"),16)#-ve
	print amp
else:
	amp = int(iframes.encode("hex"),16)#+ve
	print amp
if amp < 2000:
#make it zero
	final_frame = "x00x00"
else:
#Keep the frame
	final_frame = iframe
op.writeframes(final_frame)
op.close()
ip.close()
