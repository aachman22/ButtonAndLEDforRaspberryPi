# ButtonAndLEDforRaspberryPi
Use this Python Script to connect a 4 pin button and light an LED accordingly. 
Connect upto five buttons and five LEDS using this code.
Get the information about button pressed on the screen

## To run the code 

To run the code with Three buttons connected and introduce a delay of 2 seconds between two consecutive presses
Considering that the the pair of Button and Led are connected at these pairs :
- Button 23 - LED 24
- Button 8 - LED 25
- Button 11 - LED 9

```python
import buttonLed

btObject = buttonLed(numCandidates = 3, pressDelay = 2)
btObject.setup([23,24,8,25,11,9],["in","out","in","out","in","out"])
btObject.startButtons()
```
