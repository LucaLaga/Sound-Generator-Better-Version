import pygame
import numpy as np
import matplotlib.pyplot as plt


def get_noteFrequency(name, octave):
    note = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
    frequencies = [[16.35, 17.32, 18.35, 19.45, 20.6, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87],
                   [32.7, 34.65, 36.71, 38.89, 41.2, 43.65, 46.25, 49, 51.91, 55, 58.27, 61.74],
                   [65.41, 69.3, 73.42, 77.78, 82.41, 87.31, 92.5, 98, 103.8, 110, 116.5, 123.5],
                   [130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185, 196, 207.7, 220, 233.1, 246.9],
                   [261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370, 392, 415, 440, 466.2, 493.9],
                   [523.3, 554.4, 587.3, 622.3, 659.3, 698.5, 740, 784, 830.6, 880, 932.3, 987.8],
                   [1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976],
                   [2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951],
                   [4186, 4435, 4699, 4978,5274, 5588, 5920, 6272, 6645, 7040, 7459, 7902]]
    
    return frequencies[octave][note.index(name)]

def generateHarmonicsSounds(rootFrequency, duration, samplingRate):
    frequencies = []
    for i in range(1, 17):
        frequencies.append(rootFrequency * i)
    print(f"Frequenze dei primi 16 armonici partendo dalla frequenza fondamentale {rootFrequency} Hz:")
    n = 0
    for frequency in frequencies:
        n += 1
        print(f"Armonico {n}: frequenza {frequency}")

    t = np.linspace(0, duration, int(samplingRate * duration), endpoint=False)
    audioData = np.zeros(len(t))

    for freq in frequencies:
        audioData += np.sin(2 * np.pi * freq * t)

    maxValue = np.max(np.abs(audioData))
    if maxValue > 0:
        audioData /= maxValue

    envelope = np.linspace(0, 1, int(0.05 * samplingRate))
    audioData[:len(envelope)] *= envelope
    audioData[-len(envelope):] *= envelope[::-1]

    audioData = (audioData * 32767).astype(np.int16)
    plt.subplot(3, 1, 1)
    plt.plot(audioData[:1024])
    #plt.plot(t[:1024], audioData[:1024])
    plt.title('Harmonic Sound')

    return audioData

def generate_chordFreqs(rootFreq, chordType=1):
    match chordType:
        case 1:
            return np.array([rootFreq, (5 / 4) * rootFreq, (3 / 2) * rootFreq])
        case 2:
            return np.array([rootFreq, (6 / 5) * rootFreq, (3 / 2) * rootFreq])
        case 3:
            return np.array([rootFreq, (6 /5) * rootFreq, (45 / 32) * rootFreq])
        case 4:
            return np.array([rootFreq, (9 / 8) * rootFreq, (3 / 2) * rootFreq])
        case 5:
            return np.array([rootFreq, (4 / 3) * rootFreq, (3 / 2) * rootFreq])
        case 6:
            return np.array([rootFreq, (5 / 4) * rootFreq, (8 / 5) * rootFreq])
        case _:
            return np.array([rootFreq, (5 / 4) * rootFreq, (3 / 2) * rootFreq])

def generateChord(rootFrequency, duration, samplingRate, chordType=1):
    frequencies = generate_chordFreqs(rootFrequency, chordType)

    t = np.linspace(0, duration, int(samplingRate * duration), endpoint=False)
    audioData = np.zeros(len(t))

    for freq in frequencies:
        audioData += np.sin(2 * np.pi * freq * t)

    maxValue = np.max(np.abs(audioData))
    if maxValue > 0:
        audioData /= maxValue

    envelope = np.linspace(0, 1, int(0.05 * samplingRate))
    audioData[:len(envelope)] *= envelope
    audioData[-len(envelope):] *= envelope[::-1]

    audioData = (audioData * 32767).astype(np.int16)
    plt.subplot(3, 1, 2)
    plt.plot(audioData[:1024])
    plt.title('Major Chord Sound')


    return audioData


def generateSingleNote(rootFrequency, duration, samplingRate):
    t = np.linspace(0, duration, int(samplingRate * duration), endpoint=False)
    audioData = np.sin(2 * np.pi * rootFrequency * t)

    max_value = np.max(np.abs(audioData))
    if max_value > 0:
        audioData /= max_value

    envelope = np.linspace(0, 1, int(0.05 * samplingRate))
    audioData[:len(envelope)] *= envelope
    audioData[-len(envelope):] *= envelope[::-1]

    audioData = (audioData * 32767).astype(np.int16)
    plt.subplot(3, 1, 3)
    plt.plot(audioData[:1024])
    plt.title('Major Chord Pure Sounds')

    return audioData


def playNoteByHarmonics(rootFrequency, duration, samplingRate):
    harmonics = generateHarmonicsSounds(rootFrequency, duration, samplingRate)
    # Raddoppia l'array per avere sia il canale sinistro che destro
    harmonics = np.column_stack((harmonics, harmonics))
    harmonics = np.ascontiguousarray(harmonics)
    soundByHarmonics = pygame.sndarray.make_sound(harmonics)
    soundByHarmonics.play()
    pygame.time.wait(int(10 * 1000))


def playChordByHarmonicsRatio(rootFrequency, duration, samplingRate, chordType=1):
    chord = generateChord(rootFrequency, duration, samplingRate, chordType)
    chord = np.column_stack((chord, chord))
    chord = np.ascontiguousarray(chord)
    chordSound = pygame.sndarray.make_sound(chord)
    chordSound.play()
    pygame.time.wait(int(duration * 1000))


def playChordSingleNotes(rootFrequency, duration, samplingRate, chordType=1):
    freqs = generate_chordFreqs(rootFrequency, chordType)
    for noteFrequency in freqs:
        noteAudioData = generateSingleNote(noteFrequency, duration, samplingRate)
        noteAudioData = np.column_stack((noteAudioData, noteAudioData))
        noteAudioData = np.ascontiguousarray(noteAudioData)
        noteSound = pygame.sndarray.make_sound(noteAudioData)
        noteSound.play()
        pygame.time.wait(int(duration * 1000))
