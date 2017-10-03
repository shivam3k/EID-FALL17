#--------START - EID PROJECT 1 ------------------------------------
# @author - Shivam Khandelwal
#@brief - This python program creates a GUI to show current
# temperature (in kelvin, degrees anf fahrenheit) and humidity

#----------------- importing libraries -----------------------------
import sys
from PyQt4 import QtGui, QtCore
 
from time import strftime
#Adafruit DHT temperature sensor library -
import Adafruit_DHT
#--------------------------------SHIVAM_TEST IMPORT-------------
#assigning arguments to different sensors and check for sensor interfacing
sensor_args = { '11': Adafruit_DHT.DHT11,
		'22': Adafruit_DHT.DHT22,
		'2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)
#-------------------------------------------------------------
 
 #class main defined to setup the GUI
class Main(QtGui.QMainWindow):
 #
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 #initUI defined to set timer for 1000 microseconds
    def initUI(self):
 
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.show_readings)
        self.timer.start(1000)
 #LCD Number defined for time display
        self.lcd = QtGui.QLCDNumber(self)
        
#time display resize and postioning
	self.lcd.move(280,200)
	self.lcd.resize(180,50)
#----------------LABELS----------------------------------------

#labels defined for Temperature, Clock Time, celsius, fahrenheit, kelvin
        temp = QtGui.QLabel('Temperature',self)
	temp.move(20,20)

	temp_f = QtGui.QLabel('*F',self)
	temp_f.move(135,80)
	

	temp_c = QtGui.QLabel('*C',self)
	temp_c.move(135,140)

	temp_k = QtGui.QLabel('K',self)
	temp_k.move(135,200)

	humid = QtGui.QLabel('Humidity(%)',self)
	humid.move(280,20)

	tyym = QtGui.QLabel('Current Time',self)
	tyym.move(280,150)
	
	
#---------------PUSH BUTTON-------------------------------
#Push Button included to refresh temperature and humidity
	self.btn = QtGui.QPushButton('Check Temperature and Humidity', self)
	self.btn.move(120,300)
        self.btn.resize(260,40)
	self.btn.clicked.connect(self.show_readings)
	
	

#----------------------------------------------------------
	
        
#-------------------------------LCD Displays----------------------
#LCD Display setup for Temperature in fahrenheit, degree, celsius, humidity
#Frame shape, line width, segment style, geometry

#Temperature - Fahrenheit
        self.TEMP = QtGui.QLCDNumber(self)
        self.TEMP.setGeometry(QtCore.QRect(20, 80, 101, 51))
        self.TEMP.setAutoFillBackground(True)
        self.TEMP.setFrameShape(QtGui.QFrame.StyledPanel)
        self.TEMP.setLineWidth(1)
        self.TEMP.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.TEMP.setProperty("value", 0.0)
        self.TEMP.setProperty("intValue", 0)
#Temperature - celsius

	self.TEMPC = QtGui.QLCDNumber(self)
        self.TEMPC.setGeometry(QtCore.QRect(20, 140, 101, 51))
        self.TEMPC.setAutoFillBackground(True)
        self.TEMPC.setFrameShape(QtGui.QFrame.StyledPanel)
        self.TEMPC.setLineWidth(1)
        self.TEMPC.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.TEMPC.setProperty("value", 0.0)
        self.TEMPC.setProperty("intValue", 0)

#Temperature - KELVIN
        self.TEMPK = QtGui.QLCDNumber(self)
        self.TEMPK.setGeometry(QtCore.QRect(20, 200, 101, 51))
        self.TEMPK.setAutoFillBackground(True)
        self.TEMPK.setFrameShape(QtGui.QFrame.StyledPanel)
        self.TEMPK.setLineWidth(1)
        self.TEMPK.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.TEMPK.setProperty("value", 0.0)
        self.TEMPK.setProperty("intValue", 0)
        
#Humidity LCD Display setup commands
        self.HUM = QtGui.QLCDNumber(self)
        self.HUM.setGeometry(QtCore.QRect(280, 80, 101, 51))
        self.HUM.setAutoFillBackground(True)
        self.HUM.setFrameShape(QtGui.QFrame.StyledPanel)
        self.HUM.setLineWidth(1)
        self.HUM.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.HUM.setProperty("value", 0.0)
        self.HUM.setProperty("intValue", 0)
        
 
#---------Window settings --------------------------------
         
        self.setGeometry(480,400,480,400)
        self.setWindowTitle("Weather Check")
 
#-------- Slots ------------------------------------------
 
      
    
#------------new slots inserted----------------------------

    def show_readings(self):
	temperature, humidity = Adafruit_DHT.read_retry(sensor,pin)
	
        fahrenheit = temperature
        celsius = 0.56*fahrenheit - 17.78
        kelvin = 273 + celsius

        if humidity is not None and temperature is not None:
	    self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))#time reading -  LCD display command
            self.TEMP.display('{0:0.1f}'.format(fahrenheit))#fahrenheit reading -  LCD display command
            self.HUM.display('{0:0.1f}'.format(humidity)) #humidity reading -  LCD display command            self.TEMPC.display('{0:0.1f}'.format(celsius)) #celsius reading -  LCD display command
	    self.TEMPK.display('{0:0.1f}'.format(kelvin)) #kelvin reading -  LCD display command
	    if celsius > 10:
		self.result = QtGui.QMessageBox.information(self,"Information","Temperature is greater than 10 degrees")
#information alert if temperature is greater than 10 degrees
        else:
	    self.result = QtGui.QMessageBox.warning(self,"Warning","Error! (Hint: Check input pins of temperature sensor")
	    print('Failed to get reading. Try again!')
            sys.exit(1)

#----------------------------------------------------------
         
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()#main function exectuion command
    main.show()#main window show command
 
    sys.exit(app.exec_())#execution termination command
 
if __name__ == "__main__":
    main()

#---------------------- END --------------------------------------------------------