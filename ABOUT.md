## What is sim racing and sim drifting, and why do you need a handbrake?
### Sim Racing:
Sim-racing or "simulation racing" is a highly immersive form of virtual motorsport that accurately replicates real-world driving. ([Coach Dave Academy](https://coachdaveacademy.com/tutorials/what-is-sim-racing/))<br>
<p align="center"><img width="512" alt="image" src="https://github.com/user-attachments/assets/60a361e8-95a9-4e16-a017-7ae3f935b298" /><br><sup>A high-end sim-racing setup. Courtesy of Extreme Simracing https://extremesimracing.com/products/extreme-simracing-chassis-4-0</sup></p>
<br>

### Drifting:
Drifting is a driving technique where a driver purposely oversteers, with loss of traction, while maintaining control and driving the car through the entirety of a corner or a turn. ([Wikipedia](https://en.wikipedia.org/wiki/Drifting_%28motorsport%29)) 
That definition is really wordy and jargonistic, if that made no sense then: <br><p align="center">**drifting is intentionally sliding a car sideways**.</p><br>
<p align="center"><img width="512" alt="image" src="https://github.com/user-attachments/assets/f2edfdee-200a-46fd-bee8-87a3a59bea3f" /><br><sup>@Tyrone Bradley. Courtesy of RedBull https://www.redbull.com/int-en/what-is-drifting-guide</sup><br></p>

### Sim Drifting:
Sim drifting is just the act of drifting, in a virtual driving simulator. In real-life drifting, the handbrake allows a driver to brake and lock-up the rear wheels, in order to initiate a slide or a drift. In sim drifting, a handbrake allows users to imitate this action.

## What does it do? How does it work? How is it made?
### Core Functionality:
The core functionality of the assembly is to allow a lever to pivot on a shaft, that is attached securely to a chassis, which is mounted to a desk. The angle of the lever is measured and sent to the computer, where it is then read by the sim-racing simulator or video-game and is used to brake the rear wheels digitally.
The handbrake lever must be limited in its actuation, must return once released, and must have decent resistance to mimic real-world drifting handbrakes.
This core functionality is achieved as follows:
<p align="center"><img width="512" alt="image" src="https://raw.githubusercontent.com/bowie-dev/Sim-Racing-Handbrake/refs/heads/main/img/labeled%20diagram.png" /></p><br>
The lever pivots on the shaft and bearings inside the chassis. The lever and chassis are each connected rigidly to spring plates. A spring sits captive between the spring plates. When the lever is actuated (pulled clockwise if viewed like above), the plates get closer together and the spring compresses. The spring returns the lever to its upright position when released and provides a resistance force against the levers actuation.
The top spring plate acts as a hard-stop for the lever, it will not travel further than upright, or further than 25° from vertical. 
When the lever is pulled, the magnet that is held in the lever plate comes closer to the hall effect sensors field. The hall effect sensor can measure magnetic fields and send analogue signals to the microcontroller. The more the lever is pulled, the closer the magnet to the sensor, the stronger the field, the stronger the signal! When the lever is fully actuated (very very close to hard-stop of 25°), a bolt securing the spring plate (unimportant at this stage) presses the microswitch (small black component in-between spring plates) which sends a signal to the microcontroller.
The clamping foot is threaded into the bottom of the chassis and can be tightened onto a desk to allow for a secure mounting.

### How is it made?
Most electrical components are commercial off-the-shelf parts. The OLED display, RP2040 microcontroller, KY-035 hall effect sensor, and microswitch can all be bought online or at a local electronics store for relatively cheap. The RP2040 was picked because of its small form-factor, low cost, and good function as a HID (human interface device). 

The assembly consists also of FOUR plates, the chassis (big U-shaped plate that holds everything), the lever (long lever that has grip attached), and the large and small spring plates. These plates are laser-cut stainless steel 304 sheet metal that are tapped where necessary. They can be ordered from JLCCNC, a company that offers cheap and high-quality machining and manufacturing for all kinds of parts. I decided to order the lever powder-coated in black as it is the most visible component and a black powder-coat gives it a really nice finish.

The assembly also contains some other commercial mechanical parts, including the bearings, the shaft, the clamping foot, and the fasteners. Most of these can also be bought from JLCCNC's mechatronic components branch; JLCMC, again for ridiculously cheap prices for the quality, availability, and lead-time. 

The whole assembly is also surrounded by a case which is 3D printed from PLA.

### Firmware Write-up:
*To be completed once I have the parts and can test my code.
