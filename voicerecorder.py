# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from datetime import datetime
  
# Sampling frequency
freq = 44100
  
# Recording duration
duration = 60

# Get time to add to audio file
now = datetime.now()
now_string = now.strftime("%H_%M_%S")
print(now)
print(type(now))
print(now_string)
print(type(now_string))

# Start recorder with the given values 
# of duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
print("Recording Started...")
# Record audio for the given number of seconds
sd.wait()
  
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write(f"recording0_{now_string}.wav", freq, recording)
  
# Convert the NumPy array to audio file
wv.write(f"recording_{now_string}.wav", recording, freq, sampwidth=2)

print("Recording ended...")