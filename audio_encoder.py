import numpy as np
from scipy.io.wavfile import write


def generate_audio(data, filename="output.wav"):
    # Constants
    sample_rate = 44100  # Sample rate in Hz
    duration = 1  # Duration of each tone in seconds

    # Generate tones
    audio_data = np.array([], dtype=np.float32)

    for bit in data:
        freq = 300 if bit == 0 else 800
        t = np.linspace(0, duration, duration * sample_rate, False)
        tone = np.sin(freq * 2 * np.pi * t)
        audio_data = np.concatenate((audio_data, tone))

    # Normalize the audio
    audio_data = (audio_data * (2 ** 15 - 1) / np.max(np.abs(audio_data))).astype(np.int16)

    # Save the audio to a WAV file
    write(filename, sample_rate, audio_data)


data = [0, 1, 0, 1, 1, 0]
generate_audio(data)
