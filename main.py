from functions import *

#PARAMETERS
samplingRate = 44100
duration = 5.0
#rootFrequency = 261.63 #default DO3

#INITIALIZATION
pygame.init()
pygame.mixer.init(samplingRate, -16, 2)

choice = int(input("1. Inserire la frequenza\n2. Inserire il nome della nota\n-->"))

match choice:
    case 1:
        rootFrequency = float(input("Inserisci il valore in hz della frequenza di base: "))
    case 2:
        noteName = input("Inserisci il nome della nota\nC\tC#\tD\tEb\tE\tF\tF#\tG\tG#\tA\tBb\tB\n-->")
        octave = int(input("Inserisci l'ottava (Da 0 a 8): "))
        rootFrequency = get_noteFrequency(noteName, octave)
    case _:
        rootFrequency = float(input("Inserisci il valore in hz della frequenza di base: "))

"""
1. Major
2. Minor
3. Diminished
4. Sus2
5. Sus4
6. Augmented
None => Major
"""

chordType = input("Inserisci il tipo di accordo (da 1 a 6 oppure vuto)\n-->")

if chordType != None:
    chordType = int(chordType)

playNoteByHarmonics(rootFrequency, duration, samplingRate)
playChordByHarmonicsRatio(rootFrequency, duration, samplingRate, chordType)
playChordSingleNotes(rootFrequency, duration, samplingRate, chordType)
plt.show()

pygame.quit()
