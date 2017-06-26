# Copyright (c) 2017 Martin Mujica <martin.mujica@imt-atlantique.net>
#                    Florencia Costa Episcoco <florencia.costaepiscopo@imt-atlantique.net>
#                    Fatima-Ezzahra Elaamraoui <fe.elaamraoui@imt-atlantique.net>
#                    Bowen Xue <bowen.xue@imt-atlantique.net>
#                    Lotfi Moubakir <lotfi.moubakir@imt-atlantique.net>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter
from tkinter.filedialog import *
#from PIL import Image

from PIL.Image import * 
import sys
from Prise import Prise 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage
from Reglages import *
#Initialisation des variables globales
x      = 0
y      = 0
red  = []
green   = []
blue   = []
index  = 0
arrayX = []
arrayY = []
colors=[[0,0,0]]
global prises
global prises2
prises = []
prises2 = []
count_clicks=0
flag = False
button = [] #this will be the list of buttons placed in the centers of the prises
finalWidth = 0
finalHeight = 0

def resizeImage(img):
	"Modifies the dimensions of the inserted image so it fits in the screen"
	global finalWidth
	global finalHeight
	width, height = img.size
	img=img.transpose(FLIP_LEFT_RIGHT) # Images from Kinect are reflected, if not using kinect, or image not reflected, this line should not be there
	if (width>screen_width-250 or height>screen_height-150):
		difx= (screen_width -250)/width
		dify= (screen_height-150)/height
		if difx<dify:
			factor=difx
		else:
			factor=dify 
		img = img.resize((round(width*factor), round(height*factor)), ANTIALIAS)
	finalWidth, finalHeight = img.size # for putting the values of center in relative way
	return img


def creationPrise(img):
	"Creation of the different objects that will be the holds (prises) and give the some characteristics"	
	global prises
	global prises2
	global colors
	im = open('outputimag.png')
	InsideFlag=False  # for the colour assigment
	
	byn = ndimage.gaussian_filter(img.convert("L"), 0.9) # image improvement filter
	byn2 = img.convert("L") # black and white image
	s = [[0, 1, 0], [1,1,1], [0,1,0]] # connectivity condition
	label_im, nb_labels = ndimage.label(byn,s) #introduction of the labels to the image's matrix
	lbl = ndimage.label(label_im)[0]
	centers=ndimage.measurements.center_of_mass(label_im, lbl,range(nb_labels + 1))
	windows=ndimage.find_objects(label_im) #making windows wherer there is a prise
	for i in range(nb_labels): 
		counter=0
		insideFlag=False # prise has not colour assigned
		prises.append(Prise(i))
		prises[i].centre=(round(centers[i+1][1]),round(centers[i+1][0])) # centers had (y,x), so we put it inverted, center[0] doesn't exist
		insideFlag=False # prise has not colour assigned
		for k in range(windows[i][0].start,windows[i][0].stop):  # going throw the array using the slices of windows
			for j in range(windows[i][1].start,windows[i][1].stop):
				if label_im[k,j]==i+1:  #first slice is 0 but label 0 is background
					counter+=1
					(R,G,B)=img.getpixel((j,k))
					if (R,G,B)!=(0,0,0) and insideFlag==False: # if not black colour and the prise has no colour yet
						prises[i].couleur=[R,G,B] # we put the RGB colour in the prise
						insideFlag=True # to show the prise already has it colour
		prises[i].surface=counter

	j=0
	for i in range(len(prises)): #to remove small objects and rename the prises, also put colour Id based on the colours
		if prises[i].surface>100:
			prises2.append(prises[i])
			prises2[j].priseId=j
			for l in range(1,len(colors)): # it goes through a list of colours , index=0 belongs to color black (0,0,0)
				if prises2[j].couleur == colors[l]: #and compares all of them to the colour in the prise
					prises2[j].couleurId = l #if it's the same it put de index as Id
			if prises2[j].couleurId==0: # if the colour doesn't match any of the colours in the list (other prises colours)
				prises2[j].couleurId = len(colors) # it puts asi id the index of the next colour 
				colors.append(prises2[j].couleur) # and it puts the colour in the array of colours
			j+=1


def pointer(event):
	"detects the values of x and y when a click is made"
	global x
	global y
	global index
	global arrayX
	global arrayY
	global count_clicks
	global flag
	count_clicks+=1
	if flag==False: #        check if it is entering here to add prises or to recognise colours
		chaine.configure(text = "couleurs sélectionnées  =  "+str(count_clicks))
	arrayX.append(event.x)
	arrayY.append(event.y)
	index+= 1	
  
def pushed(X,Y,newpath):
	" Save the treated image once the button OK is pushed"
	global red
	global green
	global blue
	global flag
	im = open(newpath)
	for i in range (0, len(X)):
		  
		(R,G,B)  =  im.getpixel((X[i],Y[i]))
		red.append(R)
		green.append(G)
		blue.append(B)   
		"give the colors of the pixel where the user made click (x,y)"
	imgMatrix = selectionColors(red,green,blue,25,newpath)
	instructions.delete(	1.0,END)
	instructions.insert(END,"-Appuyer sur Réglages pour afficher toutes les prises détectées")
	p  =  fromarray(imgMatrix) #Cree une image de la matrice retournee par la fonction 'selectionColors'
	p.save('image_traitee.png')
	creationPrise(p)
	chaine.destroy()
	flag=True # put in true so recognition phase is over
 
def selectionColors(R,V,B,intervalle,newpath):
	"Definition of the color rangs of the selected pixel, leaves in the image only what belongs to those rangs"
	im = open(newpath)
	img = np.array(im)       # matrix of the selected image
	s1,s2  =  img.shape[:2]  # dimensions of the image  
	pixelInRange=False

	for i in range(0,s1): #go through the lines of the matrix
		for j in range(0,s2): #go through the columns of the matrix
			pixelInRange=False
			for k in range(0, len(R)):
				seuilR1 = R[k]-intervalle
				seuilR2 = R[k]+intervalle
				seuilV1 = V[k]-intervalle
				seuilV2 = V[k]+intervalle
				seuilB1 = B[k]-intervalle
				seuilB2 = B[k]+intervalle

				if img[i,j][0] in range(seuilR1,seuilR2) and img[i,j][1] in range(seuilV1,seuilV2) and img[i,j][2] in range(seuilB1,seuilB2):
							pixelInRange=True
							img[i,j][0] = R[k]
							img[i,j][1] = V[k]
							img[i,j][2] = B[k]
							break  # Save colors of the pixel
											
			if pixelInRange==False:
				img[i,j][0] = 0
				img[i,j][1] = 0
				img[i,j][2] = 0
	return img

def buttonCentres():
	"place a button in the center of the objects Prises"
	global button
	B_ajouterPrise=Button(fenetre, text  = 'Ajouter prise', command  =  lambda : addPrise())
	B_ajouterPrise.pack(side = LEFT, padx = 5, pady = 5)
	for i in range(len(prises2)):
		button=[0]*len(prises2)
		print(button)
		centrex=prises2[i].centre[0]
		centrey=prises2[i].centre[1]
		button[i]=Button(fenetre,  command  =  lambda f=fenetre, ii=i, p=prises2[i], b=button, c=colors: Reglages(f,ii,p,b,c))
		button[i].pack(padx = 1, pady = 1)
		button[i].place(x=centrex,y=centrey, width=10, height=10)
		instructions.delete(1.0,END)
		instructions.insert(END,"-Appuyer sur le boutton de chaque prise pour la categoriser ou la supprimer\n-Faire un clic sur la prise qui n'a pas été détectée\n-Appuyer sur le bouton Ajouter prise")

def imprime():

	for i in range(len(prises2)):
		print(prises2[i].ordre)
		print(priseUpdated.type_prise)

def addPrise():
	"Allows to create a new object of the class prise when this is indicated by the user"
	global arrayX
	global arrayY
	global colors
	#Creation of the new prise
	newPrise=Prise(len(prises2))
	#we pur as center of the prise the values of x and y given by the click made
	centrex=arrayX[len(arrayX)-1]
	centrey=arrayY[len(arrayY)-1]
	newPrise.centre=(centrex,centrey)
	# we get the color of the prise from the pixel where the click was made
	im = open('image_traitee.png')
	(R,G,B)  =  im.getpixel((arrayX[len(arrayX)-1],arrayY[len(arrayY)-1]))
	newPrise.couleur=[R,G,B] 
	for l in range(1,len(colors)): # it goes through a list of colours , index=0 belongs to color black (0,0,0)
		if newPrise.couleur == colors[l]: #and compares all of them to the colour in the prise
			newPrise.couleurId = l #if it's the same it put de index as Id
	prises2.append(newPrise)			
	i=len(prises2)-1
	button.append(0)                                                                                                       # add one more valur to the list Bottoms
	button[len(button)-1]=Button(fenetre,  command  =  lambda f=fenetre, ii=i, p=prises2[i], b=button,c=colors: Reglages(f,ii,p,b,c)) # add bottom to the list of bottoms
	button[len(button)-1].pack(padx = 1, pady = 1)                                                                         # and place it in the right place
	button[len(button)-1].place(x=centrex,y=centrey, width=10, height=10)


"Main program with the interface"
#Creation d'une fenetre 
fenetre =  Tk()
fenetre.title('Braille pour grimpeur')
v = IntVar()
v.set(1) 
screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()

#opening the image
filepath = askopenfilename(title = "Ouvrir une image",filetypes = [('png files','.png'),('all files','.*')])
photoBase = open(filepath)
photoBase = resizeImage(photoBase)
photoBase.save('outputimag.png')
photo = PhotoImage(file='outputimag.png')
canvas = Canvas(fenetre, width = screen_width-250, height = screen_height-150)
canvas.pack(anchor=W,expand =1,fill= BOTH)
canvas.create_image(0, 0, anchor = NW, image = photo)
fenetre.geometry("%dx%d+0+0" % (screen_width, screen_height*0.9))

canvas.focus_set()
canvas.bind("<Button-1>", pointer) #write the number of colors when a click is made
canvas.pack()
chaine = Label(fenetre)
B_OK= Button(fenetre, text  = 'OK', command  =  lambda : pushed(arrayX,arrayY, 'outputimag.png'))
B_OK.pack(side = LEFT, padx = 5, pady = 5)
B_reglages= Button(fenetre, text= 'Réglages',  command  =  lambda : buttonCentres())
B_reglages.pack(side = LEFT, padx = 5, pady = 5)
instructions=Text(fenetre,height=10,width=30,wrap=WORD)
instructions.insert(END,"-Faire un clic sur une prise de la/les couleurs de votre choix\n-Pousser le boutton OK\n-Attendre")
instructions.place(x=photo.width()+5,rely=0.005)
#Execution de la fenetre generale
chaine.pack(side=LEFT)

fenetre.mainloop()

