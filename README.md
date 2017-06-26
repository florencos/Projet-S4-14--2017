# Projet-S4-14--2017
"Guide vertical pour les déficients visuels"/ "Vertical Guide for the Visually Impaired"

This projet consist of a set of 3 sub-projects that were developped with the aim of helping a blind climber during the practice of the sport. It was conceived to be used inside the climbing gym. The idea is to offer the climber two functionalities: 1) the possibility of exploring the wall before actually starting to climb and allow him this way to imagine the way he/she is about to follow. 2) The next step consists of guiding the climber during his way on the wall.

To do so, the three programs present in this respository are needed: 

1) Computer program: it will get all the information of the wall by processing an image taken by a Kinect camera. The person who runs the program (normally the monitor of the climbing gym) will have to provide some essential information during this part of the process in order to be able to continue. To do so, a graphic interface has been developped with instructions that with guide the user all along its utilisation. Is during this part of the project that the climbing way is determined. At the end of this part, a CSV file is generated which gathers all the information needed to offer the climber the two fonctionalities mentionned above. 
        
2) Tablet application for Android: it receives the CSV file generated in the previous part and after some configuration, shows in the screen all the climbing holds wished. The climber scrolls with his finger the screen and when he touches a hold the appliction will return a sound that will indicate him that one hold has been found. This process can be repeated as many times as wished, and it accomplish the objective of helping the climber imagine his way in the wall.

3) Smartphone application for Android: it receives the CSV file generetade by the computer program and extracts the information of the climbing way. When the person is climbing, he/she will scan with a special reader the climbing hold that has been taken, and send that information via Bluetooth to the smarthphone. Te application will use the information sent by the reading to identify if the hold belongs to the climbing way and will provide the climber with instructions to get the following. 
