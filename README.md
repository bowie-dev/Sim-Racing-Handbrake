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

The hardstop is the pivot plate hitting the top sheet metal spring holder. The lever can travel 25° from vertical. The design has a 3D printed grip piece. The clamp for mounting to the desk fits desks of sizes 16.5mm to 39mm. The design features a 2.42" OLED display, a Seeed XIAO RP2040 microcontroller, a B100k linear potentiometer, and a KY-035 hall effect sensor. The plates and most of the components (springs, clamping system, bearings, fasteners, and even 3D printed parts) can be ordered from JLC.

### Component List
 - 3D Printed Case Components
 - Fasteners
 - Laser Cut Stainless Steel Plates
 - Seeed XIAO RP2040 Microcontroller
 - 2.42" OLED Display
 - B100k Potentiometer
 - KY-035 hall effect sensor

### Wiring Diagram
<img width="785" height="678" alt="image" src="https://github.com/user-attachments/assets/5a59feda-6ff5-4a90-9e41-811890c0f5c8" />

### Zine
<img width="1410" height="2000" alt="SIM-RACING HANDBRAKE" src="https://github.com/user-attachments/assets/463c949c-724d-4166-91d6-0a705ddb5a25" />


