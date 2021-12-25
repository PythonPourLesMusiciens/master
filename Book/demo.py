# Créé par Olivier, le 18/12/2021 en Python 3.7


import pygame.midi
import time
import random


class Accord:

    def __init__(self, fondamental):

        self.fondamental = fondamental
        self.notes = []

    def AfficheToi(self):
        print(self.notes)

    def DonneMoiNotes(self):
        return self.notes

class AccordMajeur(Accord):

    def __init__(self, fondamental):

        self.fondamental = fondamental
        self.notes = [self.fondamental+4, self.fondamental+7, self.fondamental-12]

class AccordMineur(Accord):

    def __init__(self, fondamental):

        self.fondamental = fondamental
        self.notes = [self.fondamental+3, self.fondamental+7, self.fondamental-12]

class AccordSeptieme(Accord):

    def __init__(self, fondamental):

        self.fondamental = fondamental
        self.notes = [self.fondamental+3, self.fondamental+10, self.fondamental-12]


#
# Une Gamme est une suite de note
# premiere note, premier degree
# deuxieme note, deuxieme degree
# etc...
#

class Gamme:

    def __init__(self):

        self.maGamme = []

    def NoteDeDegree(self,degree):

        return self.maGamme[degree]

    def Degree(self):

        return len(self.maGamme)

    def AfficheToi(self):

        print(self.maGamme)

    def joue(self, piano):

        for n in self.maGamme:

            piano.joueUneNote(n,1)

class GammeMajor(Gamme):

    def __init__(self, i):

        self.maGamme = [i,i+2,i+4,i+5,i+7,i+9,i+11,i+12]

class GammeMineur(Gamme):

    def __init__(self,i):

        self.maGamme = [i, i+2, i+3, i+5, i+7, i+8, i+10, i+12]


class GammeChromatique(Gamme):
    def __init__(self,i):

        self.maGamme = [i,i+1,i+2,i+3,i+4,i+5,i+6,i+7,i+8,i+9,i+10,i+11,i+12,]


class Piano:


    def __init__(self):
        pygame.midi.init()
        pygame.midi.get_default_output_id()
        pygame.midi.get_device_info(0)
        self.player = pygame.midi.Output(0)
        self.player.set_instrument(0)
        self.notes =["c","c#","d","d#","e","f","f#","g","g#","a","a#","b"]
        self.midi = [60,61,62,63,64,65,66,67,68,69,70,71,72]


    def DuNomVersMidi(self,nom):
        self.maPartition = []
        for i in nom:
            calcul = ord(i[0])-ord('a')+60
            if(calcul == -5):
                calcul = 0
            print('lettre' ,i ,'valeur',ord(i),'midi',calcul)
            self.maPartition.append(calcul)
        return self.maPartition

    def joue(self, nom):

        partition = self.DuNomVersMidi(nom)
        for note in partition:
            print('joue;',note)
            self.player.note_on(note,100)
            time.sleep(0.35)
            self.player.note_off(40,27)

    def joueAccord(self,accord):

        notes = accord.DonneMoiNotes()
        for n in notes:
            self.player.note_on(n,100)
        time.sleep(0.35)
        self.player.note_off(40,27)

    def joueUneNote(self, note,duration):
        self.player.note_on(note, 100)
        time.sleep(duration)
        self.player.note_off(40, 27)

maPremiereGammeMajor = GammeMajor(60)

monPiano = Piano()
maPremiereGammeMajor.joue(monPiano)
maPremiereGammeMineur = GammeMineur(60)
maPremiereGammeMineur.joue(monPiano)

maPremiereGammeChromatique = GammeChromatique(60)
maPremiereGammeChromatique.joue(monPiano)
