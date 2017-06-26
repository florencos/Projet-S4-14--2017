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

class Prise:

	priseId=0
	couleur=[]
	couleurId=0
	surface=0
	centre=(0,0)
	type_prise=0
	difficulte=0
	apprehension=0
	proximite=0
	ordre=0
	prise_Depart=False
	prise_Fin=False
	profondeur=[]
	suprimer=False
	parametrise=False
	main=0
	tag_Id='' 


	def __init__(self, tag):
		self.priseId=tag

	def set_TypePrise(self,option):
	 	self.type_prise=option		

	def set_Difficulte(self,option):
		self.difficulte=option
	
	def set_Apprehension(self,option):
	 	self.apprehension=option

	def set_Proximite(self,option):
	 	self.proximite=option

	def set_Ordre(self,option):
		 self.ordre=option

	def set_Couleur(self,option):
		 self.couleur=option

	def set_Main(self,option):
		 self.main=option

	def set_TagId(self,option):
		 self.tag_Id=option	

	def set_CouleurId(self,option):
		 self.couleurId=option

	def isPriseDepart(self,option):
	 	self.prise_Depart=option

	def isPriseFin(self,option):
	 	self.prise_Fin=option

	def isSuprimer(self,option):
	 	self.suprimer=option

	def isParametrise(self,option):
	 	self.parametrise=option

