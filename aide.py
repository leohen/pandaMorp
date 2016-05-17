# This Python file uses the following encoding: utf-8
"""
Morpion en 3 dimensions avec une IA utilisant l'algorithme Minimax implémenté
Copyright (C) 2015  Guillaume Augustoni, Leo Henriot, Raphael Chevalier et Enzo cabezas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, LPoint3
from random import randrange
from copy import *
from itertools import chain
from IA import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib
from direct.gui.DirectGui import DirectFrame





MARRON = (0.5,0.25,0,1)
BLACK = (0, 0, 0, 1)

def position(i):
    return LPoint3(-3+3*(i%3),-3+3*(i//3),0)


class MyApp(ShowBase):

    def testVictoire(self, Liste):
        if Liste[0][0] + Liste [0][1] + Liste [0][2] == 30:
            self.son.LancerMusiquevictoire()
            return 1
        elif Liste[0][0] + Liste [0][1] + Liste [0][2] == 3:
            self.son.LancerMusiquevictoire()
            return -1
        elif Liste[1][0] + Liste [1][1] + Liste [1][2] == 30:
            self.son.LancerMusiquevictoire()
            return 1
        elif Liste[1][0] + Liste [1][1] + Liste [1][2] == 3:
            self.son.LancerMusiquevictoire()
            return -1
        elif Liste[2][0] + Liste [2][1] + Liste [2][2] == 30:
            self.son.LancerMusiquevictoire()
            return 1
        elif Liste[2][0] + Liste [2][1] + Liste [2][2] == 3:
            self.son.LancerMusiquevictoire()
            return -1
        elif Liste[0][0] + Liste [1][0] + Liste [2][0] == 30:
            self.son.LancerMusiquevictoire()
            return 1
        elif Liste[0][0] + Liste [1][0] + Liste [2][0] == 3:
            self.son.LancerMusiquevictoire()
            return -1
        elif Liste[0][1] + Liste [1][1] + Liste [2][1] == 30:
            self.son.LancerMusiquevictoire()
            return 1
        elif Liste[0][1] + Liste [1][1] + Liste [2][1] == 3:
            self.son.LancerMusiquevictoire()
            return -1
        elif Liste[0][2] + Liste [1][2] + Liste [2][2] == 30:
            self.son.LancerMusiquevictoire()
            return 1
        elif Liste[0][2] + Liste [1][2] + Liste [2][2] == 3:
            self.son.LancerMusiquevictoire()
            return -1
        elif Liste[0][0] + Liste [1][1] + Liste [2][2] == 30:
            self.son.LancerMusiquevictoire()
            return 1
        elif Liste[0][0] + Liste [1][1] + Liste [2][2] == 3:
            self.son.LancerMusiquevictoire()
            return -1
        elif Liste[0][2] + Liste [1][1] + Liste [2][0] == 30:
            self.son.LancerMusiquevictoire()
            return 1
        elif Liste[0][2] + Liste [1][1] + Liste [2][0] == 3:
            self.son.LancerMusiquevictoire()
            return -1
        else:
            return 0
        print("Si ce texte s'affiche sur la console il y a un probleme avec le test de victoire")
    def __init__(self):
        ShowBase.__init__(self)
        self.camera.setPosHpr(0, -12, 8, 0, -35, 0)
        self.disableMouse()
        self.tableau = [[0 for i in range(3)]for i in range(3)]
        self.tours = [None for i in range(9)]
        self.environ = [None for i in range(9)]
        self.tourBlanc = True
        self.son = AudioManager(self.loader)
        self.IA = IA(self.testVictoire, self.mouvementPossible)
        self.chargersfx()
        self.Chargerboutons()
        self.menu()
        self.accept('1',lambda : self.ajouterCercle(0))
        self.accept('2',lambda : self.ajouterCercle(1))
        self.accept('3',lambda : self.ajouterCercle(2))
        self.accept('4',lambda : self.ajouterCercle(3))
        self.accept('5',lambda : self.ajouterCercle(4))
        self.accept('6',lambda : self.ajouterCercle(5))
        self.accept('7',lambda : self.ajouterCercle(6))
        self.accept('8',lambda : self.ajouterCercle(7))
        self.accept('9',lambda : self.ajouterCercle(8))
        self.accept('r',self.reset)
        self.accept('t',self.test)
        self.accept('d',self.dechargerGraphismes)
        self.accept('c',self.chargerGraphismes)
        self.accept('f',self.son.disableaudio)

    def Chargerboutons(self):
        self.b4= DirectButton(text =("Settings"),scale=0.2,text_scale=(0.6,0.6), pos = (-0.95,0,0.80),command=self.dechargerjeupouroptions)
        self.b3= DirectButton(text = ("Reset", "click!", "Reset", "disabled"), scale=.18, pos = (0.95,0,0.80), command = self.reset,clickSound=self.resetsound)    #def Volume(self):
        self.b = DirectButton(text = ("Jouer", "Jouer", "Jouer", "disabled"),text_scale=(0.1,0.2),pos=(0,0,0.5),command=(self.dechargermenupourmenu2),clickSound=(self.buttonson),rolloverSound=(self.rollsound))
        
        self.b2 = DirectButton(text = ("Settings","Settings","Settings"),text_scale=(0.1,0.2),pos=(0,0,0),command=self.dechargermenupouroptions)
        self.b5 = DirectButton(text= ("IA Facile"), text_scale=(0.1,0.2),pos=(0,0,0.75),command=self.dechargermenu2pourgraph)
        self.b6 = DirectButton(text= ("IA Intermediaire"), text_scale=(0.1,0.2),pos=(0,0,0),command=self.dechargermenu2pourgraph)
        self.b7 = DirectButton(text= ("IA Difficile"), text_scale=(0.1,0.2),pos=(0,0,-0.75),command=self.dechargermenu2pourgraph)
        self.b.hide()
        self.b5.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.b6.hide()
        self.b7.hide()
    def chargerGraphismes(self):
        for i in range(9):#création des 9 tours
            self.tours[i] = self.loader.loadModel("bois")
            self.tours[i].reparentTo(self.render)
            self.tours[i].setScale(0.25, 0.25, 0.25) #Echelle
            self.tours[i].setColor(MARRON)
            self.tours[i].setPos(position(i))
            self.son.Musiquegame.play()
            self.son.Musiquemenu.stop()
            self.b3.show()
            self.b4.show()

    def dechargerGraphismes(self):
        """Efface tous les tours présente et les pions"""
        for tour in self.tours:
            if tour is not None:
                tour.detachNode()
        self.reset()
        self.b3.hide()
        self.b4.hide()

    def reset(self):
        for i in range(9):
            if self.environ[i] is not None:
                self.environ[i].detachNode()
            self.tableau[i//3][i%3] = 0
        self.tourBlanc = True
        self.son.Musiquegame.play()
        self.son.Musiquewin.stop()

    def mouvementPossible(self, table):
        temp = []
        for i in range(9):
            if table[i//3][i%3] == 0:
                temp.append(i)
        return temp


    def ajouterCercle(self, i):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[i // 3][i %3] == 0:
                self.environ[i] = self.loader.loadModel("torus")
                self.environ[i].reparentTo(self.render)
                self.environ[i].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.tableau[i//3][i%3] = 1
                    self.environ[i].setColor(BLACK)
                else:
                    self.tableau[i//3][i%3] = 10
                self.environ[i].setPos(position(i))
                self.tourBlanc = not self.tourBlanc
            self.testVictoire(self.tableau)

    def test(self):
        if 0 in chain.from_iterable(self.tableau):
            self.ajouterCercle(self.IA.meilleurMouvement(self.tableau, self.tourBlanc))
            self.son.Musiquegame.play()
            self.son.Musiquewin.stop()


    def menu(self):
        self.b.show()
        self.b2.show()
        self.son.LancerMusiquemenu()
        self.son.Musiquegame.stop()
        self.son.Musiquewin.stop()

    def dechargermenupourmenu2(self):
        self.b.hide()
        self.b2.hide()
        self.menu2()

    def dechargermenupouroptions(self):
        self.b.hide()
        self.b2.hide()
        self.Option()
        self.son.Musiquemenu.stop()

    def dechargermenu2pourgraph(self):
    	self.b5.hide()
    	self.b6.hide()
    	self.b7.hide()
    	self.chargerGraphismes()
    	self.son.Musiquemenu.stop()

    def dechargerjeupouroptions(self):
        self.dechargerGraphismes()
        self.Option()
        self.son.Musiquegame.stop()

    def dechargeroptionspourjeu(self):
        self.dechargeroptions()
        self.chargerGraphismes()

    def dechargeroptionspourmenu(self):
        self.dechargeroptions()
        self.menu()

    def dechargeroptions(self):
        self.slider.hide()
        self.labelvolume.hide()
        self.retourjeu.hide()
        self.retourmenu.hide()
        self.disablesfx.hide()

    def showValue(self):
    	print (self.slider['value'])
    	self.son.Actualiserson(self.slider['value'])
    def chargersfx(self):
		self.buttonson=self.loader.loadSfx("playbutton.mp3")
		self.rollsound=self.loader.loadSfx("rollbutton.mp3")
		self.resetsound=self.loader.loadSfx("resetbutton.mp3")

    def disablefx(self,status):
		if status == True:
			self.buttonson.setVolume(0) 
			self.rollsound.setVolume(0)
			self.resetsound.setVolume(0)
		else :
			self.buttonson.setVolume(1) 
			self.rollsound.setVolume(1)
			self.resetsound.setVolume(1)

    def Option(self):
        self.slider = DirectSlider(range=(0,1), value=0.5, pageSize=0.5,scale=0.4,pos=(0.65,0,0.75),command=(self.showValue)) #PB 1 FAIRE SORTIR VALEUR DANS OPTION
        self.labelvolume = DirectLabel(text=("Volume"),scale=0.5,pos=(-0.65,0,0.75),text_scale=(0.4,0.6))
        self.retourjeu= DirectButton(text=("Resume"),scale=0.5,pos=(-0.65,0,-0.90),text_scale=(0.4,0.6),command= (self.dechargeroptionspourjeu))
        self.retourmenu= DirectButton(text=("Menu"),scale=0.5,pos=(0.65,0,-0.90),text_scale=(0.4,0.6),command=(self.dechargeroptionspourmenu))
        self.disablesfx=DirectCheckButton(text=("Disable Sound Effects"),text_scale=(0.4,0.6),scale=0.3,pos=(0,0,0.15),command=self.disablefx)

    def menu2(self):
    	self.b5.show()
    	self.b6.show()
    	self.b7.show()

	
class AudioManager():
	def __init__(self, loader):
		self.loader = loader
		self.Musiquewin = self.loader.loadMusic("Epic_sax_guy_10_hours.wav")
		self.Musiquegame = self.loader.loadMusic("Elevator_Music.wav")
		self.Musiquegame.setLoop(True)
		print("éxécuté")
		self.Musiquemenu = self.loader.loadMusic("Lugias Song.wav")
		self.volumeSon = 1
		self.Musiquemenu.setLoop(True)
		self.Musiquemenu.play()

	def Arretermusiques(self):
		self.Musiquewin.stop()
		self.Musiquegame.stop()
		self.buttonson.stop()
		self.rollsound.stop()
		self.resetsound.stop()

	def LancerMusiquevictoire(self):
		if self.Musiquewin.status() != self.Musiquewin.PLAYING:
			self.Musiquewin.play()
			self.Musiquegame.stop()
    
	def LancerMusiquemenu(self):
		if self.Musiquemenu != self.Musiquemenu.PLAYING:
			self.Musiquemenu.play()


	def disableaudio(self):
		self.disableAllAudio()


	def Actualiserson(self,Volume):
		self.Musiquegame.setVolume(Volume)
		self.Musiquewin.setVolume(Volume)
		self.Musiquemenu.setVolume(Volume)





























app = MyApp()
app.run()
