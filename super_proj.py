# --------START - EID PROJECT 1 ------------------------------------
# @author - Shivam Khandelwal
# @brief - This python program creates a GUI to show current
# temperature (in kelvin, degrees anf fahrenheit) and humidity

# ----------------- importing libraries -----------------------------

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
from time import strftime, gmtime
import sys
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from PyQt4 import QtGui, QtCore

butter_count = 0
cheese_count = 0
milk_count = 0
yogurt_count = 0
sugar_count = 0

butter_stock_count = 0
cheese_stock_count = 0
milk_stock_count = 0
yogurt_stock_count = 0
sugar_stock_count = 0

# -------------------------------------------------------------

class Enter_Stock(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Enter_Stock, self).__init__(parent)

        self.setGeometry(601, 400, 601, 400)
        self.setWindowTitle("Retail Store - Stock Entry")

        enter_stock_textbox = QtGui.QTextEdit(self)
        enter_stock_textbox.move(20, 20)
        enter_stock_textbox.resize(561, 192)
        enter_stock_textbox.show()

        self.sell_sugar_button = QtGui.QPushButton('Sugar', self)
        self.sell_sugar_button.move(320, 230)
        self.sell_sugar_button.resize(71, 31)
        self.sell_sugar_button.clicked.connect(self.sell_sugar_widget)

        self.sell_butter_button = QtGui.QPushButton('Butter', self)
        self.sell_butter_button.move(50, 230)
        self.sell_butter_button.resize(71, 31)
        self.sell_butter_button.clicked.connect(self.sell_scan_widget)

        self.sell_milk_button = QtGui.QPushButton('Milk', self)
        self.sell_milk_button.move(140, 230)
        self.sell_milk_button.resize(71, 31)
        self.sell_milk_button.clicked.connect(self.sell_scan_widget)

        self.sell_cheese_button = QtGui.QPushButton('Cheese', self)
        self.sell_cheese_button.move(410, 230)
        self.sell_cheese_button.resize(71, 31)
        self.sell_cheese_button.clicked.connect(self.sell_scan_widget)

        self.sell_yogurt_button = QtGui.QPushButton('Yogurt', self)
        self.sell_yogurt_button.move(230, 230)
        self.sell_yogurt_button.resize(71, 31)
        self.sell_yogurt_button.clicked.connect(self.sell_scan_widget)

        self.add_button = QtGui.QPushButton('OK', self)
        self.add_button.move(500, 230)
        self.add_button.resize(71, 31)
        self.add_button.clicked.connect(self.add_widget)

        self.sell_button = QtGui.QPushButton('Add', self)
        self.sell_button.move(310, 290)
        self.sell_button.resize(121, 31)
        self.sell_button.clicked.connect(self.sell_widget)

        self.discard_button = QtGui.QPushButton('Discard', self)
        self.discard_button.move(450, 290)
        self.discard_button.resize(121, 31)
        self.discard_button.clicked.connect(self.discard_widget)

    def sell_sugar_widget(self):
        print('enter_sugar clicked')

    def sell_scan_widget(self):
        print('enter_scan clicked')

    def sell_widget(self):
        print('enter clicked')

    def discard_widget(self):
        print('enter discard clicked')

    def add_widget(self):
        print('enter add clicked')

class Sell_items(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Sell_items, self).__init__(parent)

        self.setGeometry(601, 400, 601, 400)
        self.setWindowTitle("Retail Store - Sell Items")

        sell_item_textbox = QtGui.QTextEdit(self)
        sell_item_textbox.move(20, 20)
        sell_item_textbox.resize(561, 192)
        sell_item_textbox.show()

        self.sell_scan_button = QtGui.QPushButton('Scan', self)
        self.sell_scan_button.move(410, 230)
        self.sell_scan_button.resize(71, 31)
        self.sell_scan_button.clicked.connect(self.sell_scan_widget)

        self.weigh_button = QtGui.QPushButton('Weigh', self)
        self.weigh_button.move(500, 230)
        self.weigh_button.resize(71, 31)
        self.weigh_button.clicked.connect(self.weigh_widget)

        self.sell_button = QtGui.QPushButton('Sell', self)
        self.sell_button.move(310, 290)
        self.sell_button.resize(121, 31)
        self.sell_button.clicked.connect(self.sell_widget)

        self.discard_button = QtGui.QPushButton('Discard', self)
        self.discard_button.move(450, 290)
        self.discard_button.resize(121, 31)
        self.discard_button.clicked.connect(self.discard_widget)

    def sell_scan_widget(self):
        print('sell_scan clicked')
        scan_mfrc522_run()

    def sell_widget(self):
        global butter_stock_count
        global milk_stock_count
        global cheese_stock_count
        global yogurt_stock_count
        global sugar_stock_count

        global milk_count
        global butter_count
        global cheese_count
        global yogurt_count
        global sugar_count

        get_rs_stock_query()
        put_rs_sales_item()
        rs_stock_table()



        print('sell clicked')
    def discard_widget(self):
        global milk_count
        global butter_count
        global cheese_count
        global yogurt_count
        milk_count = 0
        butter_count = 0
        yogurt_count = 0
        cheese_count = 0
        print('discard clicked')
    def weigh_widget(self):
        print('add clicked')

class Get_Recent_Sales(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Get_Recent_Sales, self).__init__(parent)

        self.setGeometry(480, 480, 480, 480)
        self.setWindowTitle("Retail Store Stock Sales")

        self.get_recent_sales_button = QtGui.QPushButton('Get Recent Sales', self)
        self.get_recent_sales_button.move(20, 40)
        self.get_recent_sales_button.resize(100, 21)
        self.get_recent_sales_button.clicked.connect(self.get_sales_widget)

    def get_sales_widget(self):
        print('Select button pressed - sales.')

        stock_sales_status_item_quantity = 'Last Sales Record\n'
        stock_sales_status_batch_item_quantity = ' '

        selct_sales_item_textbox = QtGui.QTextEdit(self)
        selct_sales_item_textbox.move(150, 20)
        selct_sales_item_textbox.resize(241, 91)
        selct_sales_item_textbox.show()


        selct_sales_item_batch_textbox = QtGui.QTextEdit(self)
        selct_sales_item_batch_textbox.move(20, 150)
        selct_sales_item_batch_textbox.resize(420, 220)
        selct_sales_item_batch_textbox.show()


        sugar_1 = 1
        sugar = sugar_1
        milk_1 = 2
        milk = milk_1
        butter_1 = 3
        butter = butter_1
        cheese_1 = 4
        cheese = cheese_1
        yogurt_1 = 5
        yogurt = yogurt_1
        timestamp_1 = 20171213022934
        timestamp = timestamp_1


        for items in range(1, 10):
            sugar += 1
            milk += 1
            butter += 1
            cheese += 1
            yogurt += 1
            timestamp += 1
            stock_sales_status_batch_item_quantity += '\nTimestamp: '+str(timestamp)+'   Sugar: '+str(sugar)+'   Butter: '+str(butter)+'   Milk: '+str(milk)+'   Cheese: '+str(cheese)+'   Yogurt: '+str(yogurt)

        stock_sales_status_item_quantity += 'Timestamp: '+str(timestamp_1)+'\nSugar: '+str(sugar_1)+'\nButter: '+str(butter_1)+'\nMilk: '+str(milk_1)+'\nCheese: '+str(cheese_1)+'\nYogurt: '+str(yogurt_1)

        selct_sales_item_textbox.setText(stock_sales_status_item_quantity)
        selct_sales_item_batch_textbox.setText(stock_sales_status_batch_item_quantity)

class Get_Stock_Status(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Get_Stock_Status, self).__init__(parent)

        self.setGeometry(413, 480, 413, 480)
        self.setWindowTitle("Retail Store Stock Status")

        self.selct_item_comboBox = QtGui.QComboBox(self)
        self.selct_item_comboBox.addItem("Sugar")
        self.selct_item_comboBox.addItem("Butter")
        self.selct_item_comboBox.addItem("Milk")
        self.selct_item_comboBox.addItem("Cheese")
        self.selct_item_comboBox.addItem("Yogurt")
        self.selct_item_comboBox.move(20,40)
        self.selct_item_comboBox.resize(81,21)
        self.selct_item_comboBox.activated[str].connect(self.select_item_combo)

        select_item_label = QtGui.QLabel('Select Item', self)
        select_item_label.move(20, 10)
        select_item_label.resize(100, 21)



    def select_item_widget(self):
        print('Select button pressed.')

    def select_item_combo(self,text):

        stock_status_item_quantity = 'Current Stock Status\n'
        stock_status_batch_item_quantity = ' '

        selct_item_textbox = QtGui.QTextEdit(self)
        selct_item_textbox.move(150, 20)
        selct_item_textbox.resize(241, 91)
        selct_item_textbox.show()
        selct_item_textbox.setText(stock_status_item_quantity)

        selct_item_batch_textbox = QtGui.QTextEdit(self)
        selct_item_batch_textbox.move(20, 150)
        selct_item_batch_textbox.resize(371, 220)
        selct_item_batch_textbox.show()
        selct_item_batch_textbox.setText(stock_status_batch_item_quantity)

        quantity_1 = 1
        quantity = quantity_1
        timestamp_1 = 20171213022934
        timestamp = timestamp_1

        if text == "Sugar":
            stock_status_batch_item_quantity = 'Item: Sugar'
            for items in range(1,10):
                quantity += 1
                timestamp += 1
                stock_status_batch_item_quantity += '\nQuantity: ' + str(quantity) + ' grams\tTimestamp: ' + str(timestamp)
            stock_status_item_quantity += 'Item: Sugar\nQuantity: '+str(quantity_1)+'\nTimestamp: '+str(timestamp_1)
        elif text == "Butter":
            stock_status_batch_item_quantity = 'Item: Butter'
            for items in range(1, 10):
                quantity += 1
                timestamp += 1
                stock_status_batch_item_quantity += '\nQuantity: ' + str(quantity) + '\tTimestamp: ' + str(timestamp)
            stock_status_item_quantity += 'Item: Butter\nQuantity: '+str(quantity_1)+'\nTimestamp: '+str(timestamp_1)
        elif text == "Milk":
            stock_status_batch_item_quantity = 'Item: Milk'
            for items in range(1, 10):
                quantity += 1
                timestamp += 1
                stock_status_batch_item_quantity += '\nQuantity: ' + str(quantity) + '\tTimestamp: ' + str(timestamp)
            stock_status_item_quantity +='Item: Milk\nQuantity: '+str(quantity_1)+'\nTimestamp: '+str(timestamp_1)

        elif text == "Cheese":
            stock_status_batch_item_quantity = 'Item: Cheese'
            for items in range(1, 10):
                quantity += 1
                timestamp += 1
                stock_status_batch_item_quantity += '\nQuantity: ' + str(quantity) + '\tTimestamp: ' + str(timestamp)
            stock_status_item_quantity += 'Item: Cheese\nQuantity: '+str(quantity_1)+'\nTimestamp: '+str(timestamp_1)

        else:
            stock_status_batch_item_quantity = 'Item: Cheese'
            for items in range(1, 10):
                quantity += 1
                timestamp += 1
                stock_status_batch_item_quantity += '\nQuantity: ' + str(quantity) + '\tTimestamp: ' + str(timestamp)
            stock_status_item_quantity +='Item: Cheese\nQuantity: '+str(quantity_1)+'\nTimestamp: '+str(timestamp_1)

        selct_item_textbox.setText(stock_status_item_quantity)
        selct_item_batch_textbox.setText(stock_status_batch_item_quantity)
    # class main defined to setup the GUI

class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        # class main defined to setup the GUI

        # ----------------LABELS----------------------------------------

        # labels defined

        get_rs_stock_label = QtGui.QLabel('Get Stock Status', self)
        get_rs_stock_label.move(40, 40)
        get_rs_stock_label.resize(121, 21)

        get_recent_sales_label = QtGui.QLabel('Get Recent Sales', self)
        get_recent_sales_label.move(40, 90)
        get_recent_sales_label.resize(121, 21)

        sell_items_label = QtGui.QLabel('Sell Items', self)
        sell_items_label.move(40, 140)
        sell_items_label.resize(121, 21)

        enter_stock_label = QtGui.QLabel('Enter Stock', self)
        enter_stock_label.move(40, 190)
        enter_stock_label.resize(121, 21)

        # ---------------PUSH BUTTONS-------------------------------
        # Push Button included to perform Retail Store Operations

        self.get_rs_stock_button = QtGui.QPushButton('Get', self)
        self.get_rs_stock_button.move(210, 40)
        self.get_rs_stock_button.resize(70, 21)
        self.get_rs_stock_button.clicked.connect(self.get_rs_stock_widget)
        self.get_rs_stock_show = Get_Stock_Status(self)

        self.get_recent_sales_button = QtGui.QPushButton('Get', self)
        self.get_recent_sales_button.move(210, 90)
        self.get_recent_sales_button.resize(70, 21)
        self.get_recent_sales_button.clicked.connect(self.get_recent_sales_widget)
        self.get_recent_sales_show = Get_Recent_Sales(self)

        self.sell_items_button = QtGui.QPushButton('Get', self)
        self.sell_items_button.move(210, 140)
        self.sell_items_button.resize(70, 21)
        self.sell_items_button.clicked.connect(self.sell_items_widget)
        self.sell_items_show = Sell_items(self)

        self.enter_stock_button = QtGui.QPushButton('Enter', self)
        self.enter_stock_button.move(210, 190)
        self.enter_stock_button.resize(70, 21)
        self.enter_stock_button.clicked.connect(self.enter_stock_widget)
        self.enter_stock_show = Enter_Stock(self)
    # ---------Window settings --------------------------------

        self.setGeometry(310, 254, 310, 254)
        self.setWindowTitle("Retail Store")


# -------- Slots ------------------------------------------

    def get_rs_stock_widget(self):
        print('\nClicked get_rs_stock_button.\n')
        self.get_rs_stock_show.show()


    def get_recent_sales_widget(self):
        print('\nClicked get_recent_sales_button.\n')
        self.get_recent_sales_show.show()

    def sell_items_widget(self):
        print('\nClicked sell_items_button.\n')
        self.sell_items_show.show()

    def enter_stock_widget(self):
        print('\nClicked enter_stock_button.\n')
        self.enter_stock_show.show()

# ----------------------------------------------------------

def scan_mfrc522_run():

# Capture SIGINT for cleanup when the script is aborted
    def end_read(signal, frame):
        print "Ctrl+C captured, ending read."
        GPIO.cleanup()


    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(36, GPIO.IN)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    # Welcome message
    print "Welcome to the MFRC522 data read example"
    print "Press Ctrl-C to stop."

    

    flag = False
    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while flag is not True:

        # Scan for cards
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        if GPIO.input(36):
            print "Hello World!"
            time.sleep(3)
        # If a card is found
        if status == MIFAREReader.MI_OK:
            print "Card detected"

        # Get the UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            print "Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3])
            time.sleep(2)
            # This is the default key for authentication
            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 4, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                butter_list = [0,0,0,0,1,1,1,1,16,16,16,16,17,17,17,17]
                milk_list =   "[1,1,1,1,16,16,16,16,17,17,17,17,0,0,0,0]"
                yogurt_list = "[16,16,16,16,17,17,17,17,0,0,0,0,1,1,1,1]"
                cheese_list = "[17,17,17,17,16,16,16,16,1,1,1,1,0,0,0,0]"
                if MIFAREReader.MFRC522_Read(4) == str(butter_list):
                    global butter_count
                    butter_count += 1
                    print("butter count incremented")
                elif MIFAREReader.MFRC522_Read(4) == cheese_list:
                    global cheese_count
                    cheese_count += 1
                    print("cheese count incremented")
                elif MIFAREReader.MFRC522_Read(4) == milk_list:
                    global milk_count
                    milk_count += 1
                    print("milk count incremented")
                elif MIFAREReader.MFRC522_Read(4) == yogurt_list:
                    global yogurt_count
                    yogurt_count += 1
                    print("yogurt count incremented")
                else:
                    print("Unknown item or Scan Unsucessful")
                MIFAREReader.MFRC522_StopCrypto1()
                print("\n\nScan Successful!\n\n")
                flag = True
            else:
                print "Authentication error"

    flag = False
    GPIO.cleanup()

def get_rs_stock_query():
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table("rs_stock_status")

    response = table.query(
        KeyConditionExpression=Key('node').eq(3),
        Limit=1,
        ScanIndexForward=True
    )

    for i in response['Items']:
        global butter_stock_count
        butter_stock_count = int(i['butter'])
        print(butter_stock_count)

        global milk_stock_count
        milk_stock_count = int(i['milk'])
        print(milk_stock_count)

        global cheese_stock_count
        cheese_stock_count = int(i['cheese'])
        print(cheese_stock_count)

        global yogurt_stock_count
        yogurt_stock_count = int(i['yogurt'])
        print(yogurt_stock_count)

        global sugar_stock_count
        sugar_stock_count = int(i['sugar'])
        print(sugar_stock_count)

def put_rs_sales_item():

    dynamo3 = boto3.resource('dynamodb')
    table3 = dynamo3.Table("rs_sales")

    global milk_count
    global butter_count
    global cheese_count
    global yogurt_count
    global sugar_count
    print(sugar_count)
    sugar_put = sugar_count
    print(sugar_put)
    milk_put = milk_count
    cheese_put = cheese_count
    yogurt_put = yogurt_count
    butter_put = butter_count
    timestamp_put = int(strftime("%Y%m%d%H%M", gmtime()))

    table3.put_item(
        Item={
            'node': 3,
            'id_num': timestamp_put,
            'butter':butter_put,
            'milk': milk_put,
            'cheese': cheese_put,
            'yogurt': yogurt_put,
            'sugar': sugar_put
        })
    print("table updated 30")

def rs_stock_table():

    dynamo2 = boto3.resource('dynamodb')
    table2 = dynamo2.Table("rs_stock_status")

    response = table2.query(
        KeyConditionExpression=Key('node').eq(3),
        Limit=1,
        ScanIndexForward=True
    )


    for i in response['Items']:

        global milk_count
        global butter_count
        global cheese_count
        global yogurt_count
        global sugar_count

        update_butter = int(i['butter'])
        if butter_count <= update_butter:
            update_butter  = update_butter - butter_count
            print(update_butter)
        else:
            print("couldnt update butter stock")

        update_sugar = int(i['sugar'])
        if sugar_count <= update_sugar:
            update_sugar = update_sugar - sugar_count
            print(update_sugar)
        else:
            print("couldnt update sugar stock")

        update_milk = int(i['milk'])
        if milk_count <= update_milk:
            update_milk = update_milk - milk_count
            print(update_milk)
        else:
            print("couldnt update milk stock")

        update_cheese = int(i['cheese'])
        if cheese_count <= update_cheese:
            update_cheese = update_cheese - cheese_count
            print(update_cheese)
        else:
            print("couldnt update cheese stock")

        update_yogurt = int(i['yogurt'])
        if yogurt_count <= update_yogurt:
            update_yogurt = update_yogurt - yogurt_count
            print(update_yogurt)
        else:
            print("couldnt update yogurt stock")

        print(update_butter)

        timestamp_put = int(strftime("%Y%m%d%H%M", gmtime()))

        table2.put_item(
            Item={
                'node': 3,
                'id_num': timestamp_put,
                'butter': update_butter,
                'milk': update_milk,
                'cheese': update_cheese,
                'yogurt': update_yogurt,
                'sugar': update_sugar
            })

        print("rs stock table updated successfully")



def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()  # main function exectuion command
    main.show()  # main window show command

    sys.exit(app.exec_())  # execution termination command


if __name__ == "__main__":
    main()

    # ---------------------- END --------------------------------------------------------
