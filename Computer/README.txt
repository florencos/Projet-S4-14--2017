NAME
This program consists of 4 subprograms that working together will allow to make a recognition of holds (prises in french).
It begins with the image of the climbing wall and it will choose the holds of the colors chosen and finally allows the user to give characteristics to them.

PREREQUISITES
To be able to run the program it is necessary to download and install python and certain libraries.

-Download Python 3.x from https://www.python.org/
-Install Python 3.x

Once python is working (this can be checked by trying a simple print('hello world') in python shell) it is necessary to 
download the libraries used by the program. There are many ways of doing that:

Windows : (For Linux the way of using the command windows is different but the base of the process is the same)
1) by using python wheels: open CMD and move to the folder Scripts which is inside the installation folder of python.
type "pip install 'name'" where name would be the name of the librarie chosen. 

2) by using downloaded setup.py:
-Right click on "My computer"
-Click "Properties"
-Click "Advanced system settings" in the side panel
-Click "Environment Variables"
-Click the on path and EDIT
-Click NEW and add the path to the python ex: C:\Users\MyUser\AppData\Local\Programs\Python\Python36
Once ready go to the CMD, move to the folder of the setup.py of the librarie to install and type "python setup.py install"

For more information https://docs.python.org/3.6/install/

The libraries needed for this programe are:
-tkinter
-PIL
-matplotlib
-numpy
-scipy
-csv

Installing
Download the program from ZZZZZZ and put all the files in the same folder.

How to run it
It is possible to run it from the python shell or any other interpreter, text editor (sublime, anaconda) or from the CMD
The programe that should be executed is writeCSV because it will launch all of them but also creates the CSV file at the end.

EXPLANATION OF PROGAMS
There are 4 subprograms in this application. The first and most important is interface.py
-interface.py : heart of the program and it is the one that allows to open an image, to treat it, and make modifications.
-Reglages.py : Has the code of the interface to characterize the holds, this subprogramm gives the front end to the interaction with the user for the characterisation.
-Prise.py : it is the definition of the class Prise, with the attributs and methods used to define the objects that will be used by interface.
-write.CSV : it executes interface to then, by using the results, write a csv file that will be saved in the same folder of the program.

Comment:
The raison for having a different subprogram for the csv file instead of a simple function is that we found a problem between the librarie for CSV writing and PIL. It was not possible to make them work together, that is why writeCSV should be executed and this subprogram will call the main program (interface).