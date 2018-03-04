import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class ButtonLed():

    def __init__(self, numButtons= 3, pressDelay = 2, bOne = "Button 1", bTwo = "Button 2", bThree = "Button 3", bFour = "Button 4", bFive = "Button 5"):
        self.numButtons = numButtons
        self.pressDelay = pressDelay
        self.bOne = bOne
        self.bTwo = bTwo
        self.bThree = bThree
        self.bFour = bFour
        self.bFive = bFive
        
    def setup(self, pinList, valueList):

        '''
        Input Parameters :
            pinList. Type = List, Pattern = {buttonPinNumber1, LEDPinNumber1, buttonPinNumber2 , ... }, List type - integers
            valueList. Type = List, Pattern = {value1, value2, ...}, details described in further comments
        Value List Info :
            value = in (for Button input)
            value = out (for LED output)
        Example Call : 
            setup([23,24,8,25,11,9], ["in", "out", "in", "out", "in", "out"])
        '''

        self.pinList = pinList
        self.valueList = valueList

        count = 0
        while(count < numButtons * 2):
            self.setupGPIO(pinList[count], valueList[count])
            count+=1

    def startButtons(self):

        '''
        Call this function to start the functioning of buttons
        This function takes no parameters
        '''

        bList = [bOne,bTwo,bThree,bFour,bFive]
        count = 0
        
        while(true) :
            self.runButton(pinList[count], pinList[count+1], bList[count])
            count += 1
            
            if(count == numButtons):
                count = 0

    def setupGPIO(self, pinNum, value):
        if value == "in":
            GPIO.setup(pinNum, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        elif value == "out":
            GPIO.setup(pinNum, GPIO.OUT)
        pass

    def runButton(self, inPin, outPin, buttonValue):
        try:
            button_state = GPIO.input(inPin)
            if button_state == False:
                GPIO.output(outPin, True)
                print(buttonValue)
                time.sleep(pressDelay)
            else:
                GPIO.output(outPin, False)
        except:
            GPIO.cleanup()
