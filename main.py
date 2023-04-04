import numpy as np
from pydub import AudioSegment
from scipy.fft import fft


def analyze_frequency(audio_segment):
    # Get the raw audio data and the frame rate
    audio_data = np.frombuffer(audio_segment.get_array_of_samples(), dtype=np.int16)
    frame_rate = audio_segment.frame_rate

    # Perform FFT on the audio data
    freq_data = np.abs(fft(audio_data))

    # Find the frequency with the highest amplitude
    dominant_freq = np.argmax(freq_data)

    # Convert the index to frequency
    freq = dominant_freq * frame_rate / len(audio_data)

    # Determine if the frequency is high or low
    if freq > 550:
        return "1"
    else:
        return "0"


def process_audio_file(file_path):
    # Read the audio file
    audio = AudioSegment.from_file(file_path)

    # Determine the duration in seconds
    duration = int(audio.duration_seconds)

    # Initialize an empty list for the frequency readings
    frequency_readings = []

    # Analyze the frequency at each second of the audio
    for i in range(duration):
        segment = audio[i * 1000 : (i + 1) * 1000]
        freq_status = analyze_frequency(segment)
        frequency_readings.append(freq_status)

    return frequency_readings


if __name__ == "__main__":
    file_path = "realworld.wav"
    results = process_audio_file(file_path)
    print(results)
