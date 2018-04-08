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

    def setUpNotif(self):
        self.setupGPIO(16, "out")
        self.setupGPIO(20, "out")
        self.setupGPIO(21, "out")

    def allNotifOn(self):
        GPIO.output(16, True)
        GPIO.output(20, True)
        GPIO.output(21, True)


    def allNotifOff(self):
        GPIO.output(16, False)
        GPIO.output(20, False)
        GPIO.output(21, False)

        
    def startProcessing(self):
        for i in range(0, 8):
            GPIO.output(16,True)
            time.sleep(1)
            GPIO.output(16,False)
            GPIO.output(21,True)
            time.sleep(1)
            GPIO.output(21,False)

    #def stopProcessing(self):
    #    GPIO.output(20, False)

    def showSuccess(self):
        GPIO.output(16,True)
        time.sleep(5)
        GPIO.output(16,False)

    def showFailure(self):
        GPIO.output(21, True)
        time.sleep(5)
        GPIO.output(21,False)

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
        while(count < self.numButtons * 2):
            self.setupGPIO(pinList[count], valueList[count])
            count+=1

    def retrieveButton(self):
        '''
        Use this function to record a single instance of clicked button
        Return Parameter :
            retVal. Type = String, value = Name assigned to the pressed button
        '''
        self.retrieveCommand = True
        self.clickFlag = False
        bList = [self.bOne,self.bTwo,self.bThree,self.bFour,self.bFive]
        count = 0
        count2 = 0
        
        while(self.clickFlag == False) :
            retVal = self.runButton(self.pinList[count], self.pinList[count+1], bList[count2])
            count += 2
            count2 += 1
            
            if(count == self.numButtons * 2):
                count = 0
                count2 = 0
            
            if(self.clickFlag == True):
                return retVal

    def startButtons(self):

        '''
        Call this function to start the functioning of buttons
        This function takes no parameters
        '''

        bList = [self.bOne,self.bTwo,self.bThree,self.bFour,self.bFive]
        count = 0
        count2 = 0
        
        while(True) :
            self.runButton(self.pinList[count], self.pinList[count+1], bList[count2])
            count += 2
            count2 += 1
            
            if(count == self.numButtons * 2):
                count = 0
                count2 = 0

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
                time.sleep(self.pressDelay)
                if(self.retrieveCommand == True):
                    self.clickFlag = True
                    return buttonValue
            else:
                GPIO.output(outPin, False)
        except:
            print("")
