import pygame
import numpy as np
import matplotlib.pyplot as plt


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


def generateMajorChord(rootFrequency, duration, samplingRate):
    frequencies = [rootFrequency, rootFrequency / (4 / 5), rootFrequency / (2 / 3)]

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


def playMajorChordByHarmonicsRatio(rootFrequency, duration, samplingRate):
    majorChord = generateMajorChord(rootFrequency, duration, samplingRate)
    majorChord = np.column_stack((majorChord, majorChord))
    majorChord = np.ascontiguousarray(majorChord)
    majorChordSound = pygame.sndarray.make_sound(majorChord)
    majorChordSound.play()
    pygame.time.wait(int(duration * 1000))


def playMajorChordSingleNotes(rootFrequency, duration, samplingRate):
    for i in range(3):
        if i == 0:
            noteFrequency = rootFrequency
        elif i == 1:
            noteFrequency = rootFrequency / (4 / 5)
        else:
            noteFrequency = rootFrequency * (3 / 2)

        noteAudioData = generateSingleNote(noteFrequency, duration, samplingRate)
        noteAudioData = np.column_stack((noteAudioData, noteAudioData))
        noteAudioData = np.ascontiguousarray(noteAudioData)
        noteSound = pygame.sndarray.make_sound(noteAudioData)
        noteSound.play()
        pygame.time.wait(int(duration * 1000))
