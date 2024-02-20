from functions import *

#PARAMETERS
samplingRate = 44100
duration = 5.0
#rootFrequency = 261.63 #default DO3

#INITIALIZATION
pygame.init()
pygame.mixer.init(samplingRate, -16, 2)

rootFrequency = float(input("Inserisci il valore in hz della frequenza di base: "))

playNoteByHarmonics(rootFrequency, duration, samplingRate)
playMajorChordByHarmonicsRatio(rootFrequency, duration, samplingRate)
playMajorChordSingleNotes(rootFrequency, duration, samplingRate)
plt.show()

pygame.quit()
