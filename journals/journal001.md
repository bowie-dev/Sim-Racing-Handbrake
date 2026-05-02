This is the first journal entry for the handbrake, i have determined some subsystems that i can break the project down into to make time management easier and more effective:
Electrical (PCB design, component selection, wiring)
Mounting (Mounting method, position)
Mechanical (handbrake path, sensor interaction, architecture)
Software (interaction with PC, deadzone controls)
Ergonomics (human interaction design, handbrake handle design)
Casing (casing shape and size, component placement)

I have began to make a GANTT chart to help manage my time as i think time management will be vital.
I also determined four steps that must take place for each subsystem, this will probably change but is my guide for now;
IDEATION
PROTOTYPING
INTEGRATION
TESTING

I began the ideation stage for the electrical subsystem and determined that the deadzone that i initially thought to add as a requirement would be out of scope, as this is adjustable in most sim-racing games
I also started to consider which components would comprise the electrical side of the project and thought how they would work together and integrate.
Elec IDEATION:
Microcontroller:\
Usb interface to PC
Potentiometer for angle sensing?
Momentary switch for 100%?
LEDs to show actuation amount?
DEADZONE CONTROL OUT OF SCOPE - POSSIBLE IN GAME SOFTWARE

MICROCONTROLLER:
 - surface mounted or board with internal wiring
surface mounted requires a custom PCB with other surface mount components and does not allow for easy prototyping/changes after the board is ordered
I have used Seeed XIAO RPs before and I think they match my requirements in that they:
 - have USB interface; makes talking between controller and computer really easy
 - have analogue inputs to allow for a potentiometer to give a signal
 - are nice and small allowing for nice packaging
 - have ample IO ports to handle what i need
For now; im going with the seeed xiao RP2040
i have some components already, including:
 - i2c lcd display (i reaaaally want to use this somehow but idk yet so i guess we'll see)
 - potentiometer b100k, im doing some research to determine whether this is appropriate (but its pretty big and it may be nessecary to buy another, more appropriate one)
 - switches (i plan on having a switch to tell when its at 100 percent handbrake actuation)
 - wires
 - LEDs
 - cool series voltmeter 
 - optical sensors (could be used to design a no-wear detection system idk)

and other mechanical components that ill go into during mechanical ideation.

i did some testing of the potentiometer that i have and i got some data ig..
"""
POTENTIOMETER READINGS

INPUT: 8.5v

position 0*: 8.5
position 45*: 7.5
position 90*: 5.4v
position 135*: 3.0v
position 180*: 0.9v
position 225*: 0.0v
ok cool


RP2040 operates at 3.3v MAX


sooooo power supply usb gives 5v then board steps down to 3.3

using rp power supply through pot should giv

INPUT: 5v

position 0*: 4.6
position 45*: 3.9
position 90*: 3.3
position 135*: 2.7
position 180*: 2.0
position 225*: 1.7
ok what running it back
pos 225: 1.5
180: 1.8
135: 2.5
90: 3.2
45: 4.1
0: 4.7 
preeety inconsistent ohwell



INPUT: 4.3v

position 0*: 4.0
position 45*: 3.6
position 90*: 2.2
position 135*: 1.1
position 180*: 1.8
position 225*: 0.0
running it back now
225: 1.3

pos 180: 1.8
135: 2.3
90: 3.0
45: 3.7
0: 4.0

discrepancy with~ 90* so ill check again: 3.0mmmmmmmok
90 at 3.2v at t=0 seems to stay consistent, maybe i should just get new pot

ok idk why but pot Vout decreases over time i reaaally wanna hook this up to an osciliscope or something but i dont hav eone
ok now its increasing
kinda feels like theres some electrical backlash idkk
:(((wait

mayube how long it has been powered has something to do with it
after being powered a while,Vin = 4.3 *=180, Vout=2.18, disconnecting power and reconnecting...;
vout = 2.05 hmmm 2.16
ohhi i think my desk mat was messing with it, imma insulate the bottom now wait
ok a biiit better
"""
![potentiometer testing](https://github.com/bowie-dev/)
![current schematic](https://github.com/bowie-dev/)

ok i gotta go to work so that is the jouirnal for now thatnks ang bye

1.5h

