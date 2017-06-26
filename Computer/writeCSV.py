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

import csv
from interface import prises2
from interface import finalHeight
from interface import finalWidth
with open('prises.csv', 'w') as csvfile:
	fieldnames = ['Prise_Id', 'Couleur_Id', 'Couleur', 'type_prise','Surface','x','y', 'difficulte','apprehension','proximite','ordre','prise_Depart','prise_Fin','tag_Id']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for i in range(len(prises2)):
		if prises2[i].suprimer==False:
			writer.writerow({'Prise_Id': prises2[i].priseId,'Couleur_Id':prises2[i].couleurId, 'Couleur': prises2[i].couleur, 'type_prise':prises2[i].type_prise, 'Surface': prises2[i].surface, 'x' : (prises2[i].centre[0]/finalWidth)*300, 'y' : (prises2[i].centre[1]/finalHeight)*450,'difficulte':prises2[i].difficulte,'apprehension':prises2[i].apprehension,'proximite':prises2[i].proximite,'ordre':prises2[i].ordre,'prise_Depart':prises2[i].prise_Depart,'prise_Fin':prises2[i].prise_Fin, 'tag_Id': prises2[i].tag_Id})
