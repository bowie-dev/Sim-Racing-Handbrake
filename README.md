# Desk-Mounted Sim-Racing Handbrake
### As the name suggests, an analogue, desk-mounted, sim-racing handbrake. With 25° of travel and a 2.42" OLED display.
<img width="300" alt="image" src="https://github.com/user-attachments/assets/4f64b404-eafb-439e-9a29-accb06b1c651" />
<img width="300" alt="image" src="https://github.com/user-attachments/assets/19337345-0edf-4364-8767-2fd8c8077ce4" />

### Why was it made and what problem does it solve?

> I am quite into sim-racing and specifically sim-drifting. To initiate a drift when drifting it is nessecary to actuate the handbrake and at the moment, I do that by clicking a button on my steering wheel. This is difficult to do, especially with the wheel moving around, the button being so small, and my hands being occupied with steering or shifting. To solve this problem, many simulator setups have external handbrakes. This system offers a really cheap solution that comes really close to handbrakes that could cost significantly more. I have always wanted to have a handbrake as a part of my sim-racing setup and have always known that it would be something that I could design and engineer. What makes my solution unique is the cost-to-quality and the simple, highly compatible mounting design. Rather than needing to be bolted to an expensive frame, my solution mounts directly and securely to a variety of desktops.

### **How** is it used and how does it work?
> When sim-drifting, the user pulls on the handle of the handbrake. This is read by the potentiometer and the hall effect sensors within the assembly and is sent as analogue signals to a Seeed XIAO RP2040 microcontroller. The microcontroller then parses the signal and sends it to the computer which is then read by the games software and used to apply force to the handbrake in the game, mimicking what the user is doing in real life. The lever is connected by two bearings to the chassis, and the chassis is mounted to the desk via a built-in clamp. The users force is resisted by a spring held captive between the lever and chassis. The spring is held between two bolts and is changable for different handbrake "feels".

### Description
A low-cost, high-quality, sim-racing handbrake. Comprised mainly of stainless steel sheet metal plates and 3D printed case components. To measure the angle of the lever, a potentiometer mounted in the main shaft, a hall effect sensor interacting with a magnet on the pivot lever, and a microswitch used to know when the lever is pulled to the max. Two bearings are used to hold the shaft and the pivot plates. The spring is held between two M8 bolts, one on the pivot, one on the chassis. They are mounted to the plates through sheet metal plates that span the width of the assembly. Here is a cross section view:

<img width="400" alt="image" src="https://github.com/user-attachments/assets/93ac355b-d735-4515-aab9-bdbdf305476e" />

The hardstop is the pivot plate hitting the top sheet metal spring holder. The lever can travel 25° from vertical. The design has a 3D printed grip piece. The clamp for mounting to the desk fits desks of sizes 16.5mm to 39mm. The design features a 2.42" OLED display, a Seeed XIAO RP2040 microcontroller, and a KY-035 hall effect sensor. The plates and most of the components (springs, clamping system, bearings, fasteners, and even 3D printed parts) can be ordered from JLC.

### Component List
 - 3D Printed Case Components
 - Fasteners
 - Laser Cut Stainless Steel Plates
 - Seeed XIAO RP2040 Microcontroller
 - 2.42" OLED Display
 - KY-035 hall effect sensor

### Bill of Materials
| Part | Description | Link | Quantity | Unit Price ($AUD) | Total Price ($AUD) | Notes | Have/Need/Can Make |
|---|---|---|---|---|---|---|---|
| Chassis Plate | Stainless steel sheet metal, bent and tapped. Acts as main chassis for assembly and mounting. | N/A | 1 | 11.53 | 11.53 | 3mm Stainless Steel 304 | Need |
| Lever Plate | Stainless steel sheet metal, bent and tapped. Acts as pivot and lever arm for handbrake. | N/A | 1 | 15.89 | 15.89 | 3mm Stainless Steel 304 | Need |
| Spring Plate Small | Stainless steel sheet metal, bent and tapped. Retains spring and bolts to pivot plate. | N/A | 1 | 4.11 | 4.11 | 3mm Stainless Steel 304 | Need |
| Spring Plate Large | Stainless steel sheet metal, bent and tapped. Retains spring and bolts to chassis plate. | N/A | 1 | 4.14 | 4.14 | 3mm Stainless Steel 304 | Need |
| Shaft | Tapped rotary shaft. Supports rotational subassembly. | https://jlcmc.com/product/s/B10/BFJH/rotary-shaft-straight-bar-type-both-ends-internal-thread-type-unmachined-shaft?k=BFJH-S1W-7-D10-L41-M6-N6&productModelNumber=BFJH-S1W-7-D10-L%5B15.0~510.0%2F0.1%5D-M6-N6 | 1 | 5.6 | 5.6 | 10mm OD, M6 Tapped, 41mm  | Need |
| Flange Bearings | Flange Bearing with Dust Covers. Acts as pivot between lever and shaft. | https://jlcmc.com/product/b/C15/BR8366/deep-groove-ball-bearings-with-flange-types?k=F6700ZZ&productModelNumber=F6700ZZ | 2 | 0.38 | 0.76 | 15mm OD, 10mm ID | Need |
| Clamp Foot | Nylon clamping foot for mounting. Acts as clamping part and face to mount chassis to table. | https://jlcmc.com/product/s/D16/DACG/all-nylon-base-foot-cup-fixed-type?k=DACG-D-D50-M8-L50&productModelNumber=DACG-D-D50-M8-L50 | 1 | 0.98 | 0.98 | M8 Thread, 50mm Length | Need |
| Clamp Knob | Knob for clamping for mounting to be done by user. | https://jlcmc.com/product/s/D02/DBTJ/five-star-stud-knob?k=DBTJ-W-D40-M8&productModelNumber=DBTJ-W-D40-M8 | 1 | 0.81 | 0.81 | M8 Thread, External Thread | Need |
| 16x40mm Spring | Spring to apply return force and resistance to lever motion. | https://jlcmc.com/product/s/A04/ATKA/compression-springs-inner-diameter-reference-stainless-steel-l%C3%97(28~35)-l%C3%97(20~30)?k=ATKA-L4-P-D16-L40&productModelNumber=ATKA-L4-P-D16-L40 | 1 | 0.13 | 0.13 |  | Need |
| 16x50mm Spring | Spring to apply return force and resistance to lever motion. | https://jlcmc.com/product/s/A04/ATKA/compression-springs-inner-diameter-reference-stainless-steel-l%C3%97(28~35)-l%C3%97(20~30)?k=ATKA-L4-P-D16-L50&productModelNumber=ATKA-L4-P-D16-L50 | 1 | 0.27 | 0.27 |  | Need |
| 18x50mm Spring | Spring to apply return force and resistance to lever motion. | https://jlcmc.com/product/s/A04/ATJT/compression-springs-outer-diameter-reference-l%C3%97(27~35)?k=ATJT-D18-L50&productModelNumber=ATJT-D18-L50 | 1 | 0.2 | 0.2 |  | Need |
| 18x60mm Spring | Spring to apply return force and resistance to lever motion. | https://jlcmc.com/product/s/A04/ATJT/compression-springs-outer-diameter-reference-l%C3%97(27~35)?k=ATJT-D18-L60&productModelNumber=ATJT-D18-L60 | 1 | 0.2 | 0.2 |  | Need |
| Seeed XIAO RP2040 | Microcontroller to process signals from lever angle and communicate with PC. | https://core-electronics.com.au/seeed-xiao-rp2040-supports-arduino-micropython-and-circuitpython.html | 1 | 9.05 | 9.05 |  | Need |
| 2.42" I2C OLED | Screen to feedback information to user and useful for debugging/tuning. | https://core-electronics.com.au/large-oled-i2c-display-ssd1309.html | 1 | 20.7 | 20.7 |  | Have |
| KY-035 Hall Effect Sensor | Hall effect sensor to detect magnetic field from magnet in lever to detect angle. | https://www.jaycar.com.au/duinotech-arduino-compatible-hall-effect-sensor/p/XC4434 | 1 | 5.75 | 5.75 |  | Need |
| Microswitch | Switch to detect when lever is at full travel.  | N/A | 1 | N/A | N/A |  | Have |
| 10k Resistor | To stabilise signals as pullup or pulldown resistors. | https://www.jaycar.com.au/10k-ohm-0-5-watt-metal-film-resistors-pack-of-8/p/RR0596 | 1 | 0.85 | 0.85 | 10kΩ x8 | Need |
| 1m USB-A to USB-C Cable | For the microcontroller to communicate with the PC. | https://www.officeworks.com.au/shop/officeworks/p/keji-usb-a-to-usb-c-cable-1m-black-kejiac1mbk | 1 | 4 | 4 |  | Need |
| Jumper Wires M-M | To connect components in assembly. Male connectors on both sides. | https://core-electronics.com.au/jumper-wire-20cm-ribbon-of-40pcs.html | 1 | 3.95 | 3.95 | 200mm M-M x40 | Need |
| Jumper Wires M-F | To connect components in assembly. Male connectors on one side, female on one side. | https://core-electronics.com.au/male-female-jumper-wire-40-20cm.html | 1 | 3.95 | 3.95 | 200mm M-F x40 | Need |
| Jumper Wires F-F | To connect components in assembly. Female connectors on both sides. | https://core-electronics.com.au/solderless-breadboard-jumper-cable-wires-female-female-40-pieces.html | 1 | 3.95 | 3.95 | 200mm F-F x40 | Need |
| Main Case | 3D printed black PLA case that encases most of the assembly. | N/A | 1 | N/A | N/A |  | Can Make |
| LCD Bevel | 3D printed black PLA bevel that covers the LCD PCB. | N/A | 1 | N/A | N/A |  | Can Make |
| Fastener Hole Inserts | 3D printed black PLA hole inserts to hide the fasteners holes and fasteners. | N/A | N/A | N/A | N/A |  | Can Make |
| M6x10 Button Head | Fastens the shaft and rotating assembly to the chassis. | N/A | 2 | N/A | N/A | M6x1.0 x 10mm Button Head | Need |
| M3x5 Socket Head | Fastens spring plates to pivot and chassis. | N/A | 8 | N/A | N/A | M3x0.5 x 5mm Socket Head | Need |
| M3x6 Socket Head | Fastens case to chassis. | N/A | 10 | N/A | N/A | M3x0.5 x 6mm Socket Head | Need |
| M1.6x5 Socket Head | Fastens microswitch to chassis. | N/A | 2 | N/A | N/A | M1.6x0.35 x 5mm Socket Head | Need |
| M8x6 Socket Head | Provides seating for spring on spring plates. | N/A | 2 | N/A | N/A | M8x1.25 x 6mm Socket Head | Need |
| M3x30 Socket Head | Mounts grip to lever plate. | N/A | 2 | N/A | N/A | M3x0.5 x 30mm Socket Head | Need |

### Wiring Diagram
<img width="1920" height="1658" alt="image" src="https://github.com/user-attachments/assets/f73e9b0e-6caf-434b-a2cd-f67fceb55275" />


### Zine
<img width="1410" height="2000" alt="SIM-RACING HANDBRAKE" src="https://github.com/user-attachments/assets/463c949c-724d-4166-91d6-0a705ddb5a25" />


