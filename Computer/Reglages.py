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

from tkinter import *
from tkinter import font
from Prise import *

global priseUpdated
priseUpdated=Prise(0)
def Reglages(fenetre,index,prise,bouton,couleurs):
	priseUpdated=Prise(0)
	root =Toplevel(fenetre)
	root.geometry("1000x500")
	root.resizable(width=TRUE, height=TRUE)
	v1 = IntVar()
	v2 = IntVar()
	v3 = IntVar()
	v4 = IntVar()
	v5 = BooleanVar()
	v6 = BooleanVar()
	v7 = IntVar()
	v8 = IntVar()
	v9 = StringVar()	

	# initializing the choice, i.e. Python
	if prise.parametrise==False: #if the prise has already been categorised we put the options chosen in the menu, if not, default 
		v1.set(0)  
		v2.set(0)
		v3.set(0)
		v4.set(0)
		v5.set(False)
		v6.set(False)
		v7.set(0)
		v8.set(prise.couleurId)
		v9.set(0)
		v9.set('')
	else:
		v1.set(prise.type_prise)
		v2.set(prise.difficulte)
		v3.set(prise.apprehension)
		v4.set(prise.proximite)
		v5.set(prise.prise_Depart)
		v6.set(prise.prise_Fin)
		v7.set(prise.ordre)
		v8.set(prise.couleurId)
		v9.set(prise.main)		
		v9.set(prise.tag_Id)

	type_Prise = [("Aucune information",0),
	    ("Prise main gauche",1),
	    ("Prise main droite",2),
	    ("Prise pied gauche",3),
	    ("Prise pied droit",4),
	    ]

	difficulte = [("Aucune information",0),
	    ("Abominable",1),
	    ("Dure",2),
	    ("Facile",3),
	    ("Très facile",4),
	    ]

	apprehension= [("Aucune information",0),
	    ("Arquée",1),
	    ("Pince",2),
	    ("Plate",3),
	    ("Bacs",4),
	    ]

	proximite = [("Aucune information",0),
	    ("Très loin",1),
	    ("Loin",2),
	    ("Proche",3),
	    ("Très proche",4),
	    ]
  

	def getValueofSpin(s):
		v7.set(Spinbox.get(s))
		

	def saveChoice():

		root.withdraw()
	  
	  	#Set type de prise
		prise.set_TypePrise(v1.get())

		#Set difficulté de prise
		prise.set_Difficulte(v2.get())

		#Set apprehension de la prise
		prise.set_Apprehension(v3.get())

		#Set proximité de la prise
		prise.set_Proximite(v4.get())

		#Indiquer prise départ
		prise.isPriseDepart(v5.get())

		#Indiquer prise fin
		prise.isPriseFin(v6.get())

		#Indiquer couleur
		prise.set_Couleur(couleurs[v8.get()])

		#Indiquer couleurId
		prise.set_CouleurId(v8.get())

		#Set ordre prise
		prise.set_Ordre(v7.get())

		#Set prise tag
		prise.set_TagId(v9.get())

		prise.isParametrise(True)
		priseUpdated=prise
		return priseUpdated

	def deletePrise(bouton):
		bouton[index].destroy()
		prise.isSuprimer(True)
		root.withdraw()


	Helvfont = font.Font(family="Helvetica", size=10, weight="bold")
	title=Label(root, 
	      text="""CARACTERISATION DE LA PRISE""",
	      justify = LEFT,
	      font=Helvfont,
	      padx = 20)
	title.grid(row=1,column=1)

	l=Label(root, 
	      text="""Type de prise:""",
	      justify = LEFT)
	l.place(x = 20, y = 30)
	i=0
	for txt, val in type_Prise:
		r=Radiobutton(root, 
			        text=txt,
			        indicatoron=0,
			        width = 20,
			        padx = 20, 
			        variable=v1, 
			        value=val)
		r.place(x = 20, y =80 + i*30, width=120, height=25)
		i+=1

	l=Label(root, 
	  text="""Difficulté:""",
	  justify = LEFT)
	l.place(x = 220, y = 30)
	i=0
	for txt, val in difficulte:
		r=Radiobutton(root, 
			        text=txt,
			        indicatoron=0,
			        width = 20,
			        padx = 20, 
			        variable=v2, 
			        value=val)
		r.place(x = 220, y =80 + i*30, width=120, height=25)
		i+=1


	l=Label(root, 
	  text="""Apprehension:""",
	  justify = LEFT)
	l.place(x = 420, y = 30)
	i=0
	for txt, val in apprehension:
		r=Radiobutton(root, 
			        text=txt,
			        indicatoron=0,
			        width = 20,
			        padx = 20, 
			        variable=v3, 
			        value=val)
		r.place(x = 420, y =80 + i*30, width=120, height=25)
		i+=1

	l=Label(root, 
	  text="""Proximité:""",
	  justify = LEFT)
	l.place(x = 620, y = 30)
	i=0
	for txt, val in proximite:
		r=Radiobutton(root, 
			        text=txt,
			        indicatoron=0,
			        width = 20,
			        padx = 20, 
			        variable=v4, 
			        value=val)
		r.place(x = 620, y =80 + i*30, width=120, height=25)
		i+=1

	l=Label(root, 
	  text="""Prise de départ?""",
	  justify = LEFT)
	l.place(x = 20, y = 280)

	r=Radiobutton(root, 
		text='Oui',
		indicatoron=0,
		width = 20,
		padx = 20, 
		variable=v5, 
		value=True)
	r.place(x = 20, y =330, width=120, height=25)

	r=Radiobutton(root, 
		text='Non',
		indicatoron=0,
		width = 20,
		padx = 20, 
		variable=v5, 
		value=False)
	r.place(x = 20, y =360, width=120, height=25)

	l=Label(root, 
	  text="""Prise de fin?""",
	  justify = LEFT)
	l.place(x = 220, y = 280)

	r=Radiobutton(root, 
		text='Oui',
		indicatoron=0,
		width = 20,
		padx = 20, 
		variable=v6, 
		value=True)
	r.place(x = 220, y =330, width=120, height=25)

	r=Radiobutton(root, 
		text='Non',
		indicatoron=0,
		width = 20,
		padx = 20, 
		variable=v6, 
		value=False)
	r.place(x = 220, y =360, width=120, height=25)


	l=Label(root, 
	  text="""Numéro de prise?""",
	  justify = LEFT)
	l.place(x = 420, y = 280)
	var = StringVar()
	s = Spinbox(root, from_=0, to=20, textvariable=var, command= lambda : getValueofSpin(s))
	if prise.parametrise==True:
		var.set(prise.ordre)
	s.place(x = 420, y = 330)

	Label(root, 
      text="""Couleur:""",justify = LEFT).place(x=650, y=280)
	for l in range(1,len(couleurs)):
	    rgb='#%02x%02x%02x' % (couleurs[l][0],couleurs[l][1],couleurs[l][2])
	    Radiobutton(root, 
	                text=' ',
	                padx = 20, 
	                bg=rgb,
	                variable=v8,
	                value=l).place(x=650,y=290+l*35)
	
	Label(root, 
      text="""Tag Id:""",padx = 20).place(x=780, y=280)
	e = Entry (root, textvariable=v9)
	e.place(x=780,y=330)

	b=Button(root, text  = 'Ok', command  =  lambda : saveChoice())
	b.place(x=20,y=450)

	delete=Button(root, text  = 'Supprimer', command  =  lambda : deletePrise(bouton))
	delete.place(x=60,y=450)