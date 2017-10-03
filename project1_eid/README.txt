#-----------------README FILE - PROJECT 1 EID ----------------------------

@author - Shivam Khandelwal
@brief - This python program creates a GUI to show current
	 temperature (in kelvin, degrees anf fahrenheit) and humidity.
@file - shivam_project1.py

#-----------------------------------------------------------------------

This program is created to fulfill the coursework requirements of ECEN 5053:002
Embedded Interface Design

#------------------------------------------------------------------------

Description - 

1) Gui setup and initialization using Text Editor (QT designer was not used to design GUI. The GUI 
   is implemented using PyQT4 command set)
2) Adafruit DHT22 sensor interfacing  with Rapberry Pi (Connected GPIO 4 pin to data pin of DHT22 sensor) 
3) VNC Viewer setup 


#----------------------------------------------------------------------------

Hardware - 

1) Rapberry Pi Model 3
2) Jumper Wires
2) 4.7k ohm resistor

Software/Environment- 

1) Raspbian Stretch
2) Vim editor

#------------------------------------------------------------------------------------

Instructions - 

1) Connect Raspberry Pi to a remote desktop using VNC viewer
	(Use 'ifconfig' to know ip address. Before this step, ensure that pi password an d username are known)
2) Connect GPIO 4 pin of Raspberry Pi to data pin of DHT22 temperature sensor through a 4.7k ohm resistor.
2) Clone github repostiory in you home directory - https:/github.com/shivam3k/git_test_repo.git
3) CRreate a directory named project1_eid in git_test_repo - 
	cd 
	cd git_test_repo
	mkdir project1_eid
4) Create a README.md and shivam_project1.py
	touch shivam_project1.py
	touch README.md
5) Open shivam_project1.py in vim editor -
	vi shivam_project1.py
6) Press 'i' to Write the python code and include Adafruit_DHT library (insert mode)
7) Write the code
8) Press 'Ctrl+O' to exit insert mode and type - ':wq' to save your code
9) Execute your code using this command - 
	python shivam_project1.py 22 4
10) Check for errors (if any) and rectify them using 'vi shivam_project1.py'(Repeat steps 5-9 until program executes successfully.)
11) A GUI window will open to show sensor data and time.

#----------------------------------------------------------------------------------------

Features - 

1) LCD display for Time, Temperature and Humidity
2) Real-time sensor data display.
3) Temperature displayed in fahrenheit, celsius and kelvin scale
4) Real-time digital clock included.
5) Push Button to refresh sensor data manually.

#----------------------------------END : README ----------------------------------------------------- 

