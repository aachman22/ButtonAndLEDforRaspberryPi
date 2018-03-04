# Button and LED lights connecting code for Raspberry Pi 3 using GPIO
Use this Python Script to connect a 4 pin button and light an LED accordingly. 
Connect upto five buttons and five LEDS using this code.
Get the information about button pressed on the screen

- Use this type of 4 pin Button to connect to your Raspberry pi using a bread board :

<img width="639" alt="screen shot 2018-03-04 at 2 45 28 pm" src="https://user-images.githubusercontent.com/9898343/36944179-e541e7d0-1fbc-11e8-891b-1e8d774b919d.png">

- Connect a 4 pin button with a LED light according to the following Pin Diagram :
![untitled-sketch_bb_asal3ak7po](https://user-images.githubusercontent.com/9898343/36944167-ab33ba46-1fbc-11e8-8bb6-c3cf9e106d08.jpg)

- Use this GPIO layout to connect more number of LEDs and Buttons to the breadboard. Use non-ground GPIO serials for inputs and outputs
<img width="496" alt="screen shot 2018-03-04 at 3 03 14 pm" src="https://user-images.githubusercontent.com/9898343/36944198-3196347e-1fbd-11e8-89bc-ca0f4dbce165.png">


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
