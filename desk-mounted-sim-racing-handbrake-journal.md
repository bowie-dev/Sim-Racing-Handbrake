# Desk Mounted Sim-Racing Handbrake — Journal Export

- Exported at: 2026-06-10T09:43:29Z
- Project ID: 2861
- Entries: 40

## Entry 1
- ID: 5079
- Author: bowie
- Created At: 2026-05-02T07:41:17Z

### Content

**# Journal Entry 1 - 02/05/26 - Electrical Ideation**
This is the first journal entry for the handbrake, i have determined some subsystems that i can break the project down into to make time management easier and more effective:
 - Electrical (PCB design, component selection, wiring)
 - Mounting (Mounting method, position)
 - Mechanical (handbrake path, sensor interaction, architecture)
 - Software (interaction with PC, deadzone controls, LCD)
 - Ergonomics (human interaction design, handbrake handle design)
 - Casing (casing shape and size, component placement)

I have began to make a GANTT chart to help manage my time as i think time management will be vital.
I also determined five steps that must take place for each subsystem, this will probably change but is my guide for now;
IDEATION
PROTOTYPING
DEVELOPMENT
INTEGRATION
TESTING
This is what the GANTT chart looks like at the moment:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzMzMsInB1ciI6ImJsb2JfaWQifX0=--96d926f3ea118117ef4903441b172eeba293800a/image.png)

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
heres a rough schematic so far:
![schematic.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzMjYsInB1ciI6ImJsb2JfaWQifX0=--77939cc3013ceb50d4b57b18fa84dd7e148d4295/schematic.png)
and other mechanical components that ill go into during mechanical ideation.

i did some testing of the potentiometer that i have and i got some data ig..
the testing was to determine the output voltage through the potentiometer at different angles.
initially i could only find 9v as a power supply, then i realised i could use my arduino uno board plugged into my pc as a 5v and 3.3v power supply.
The testing involved measuring the output voltage after running through the potentiometer at 6 different angles and 3 different input voltages.

```
POTENTIOMETER READINGS

INPUT: 8.5v
position 0*: 8.5v
position 45*: 7.5v
position 90*: 5.4v
position 135*: 3.0v
position 180*: 0.9v
position 225*: 0.0v
```
ok cool
RP2040 operates at 3.3v MAX

```
INPUT: 5v
position 0*: 4.6
position 45*: 3.9
position 90*: 3.3
position 135*: 2.7
position 180*: 2.0
position 225*: 1.7
```

ok what running it backwards:

```
INPUT: 5v
position 225*: 1.5
position 180*: 1.8
position 135*: 2.5
position 90*: 3.2
position 45*: 4.1
position 0*: 4.7
```
preeety inconsistent ohwell
```
INPUT: 4.3v
position 0*: 4.0
position 45*: 3.6
position 90*: 2.2
position 135*: 1.1
position 180*: 1.8
position 225*: 0.0
```
running it back now

```
INPUT: 4.3v
position 225*: 1.3
position 180*: 1.8
position 135*: 2.3
position 90*: 3.0
position 45*: 3.7
position 0*: 4.0
```
discrepancy with~ 90* so ill check again: 3.0
mmmmmmmok
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

heres the setup:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzMjcsInB1ciI6ImJsb2JfaWQifX0=--d5a5e7b7dffcfd2f0a5c3660d443d2d91bf077f2/image.png)
heres the data i got from the testing:
![potentiometer.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzMjksInB1ciI6ImJsb2JfaWQifX0=--b3db1c7a89cae26af84121ddfc7b3c79c348c5a7/potentiometer.png)
ok i gotta go to work so that is the jouirnal for now thatnks ang bye

1.5h








## Entry 2
- ID: 5105
- Author: bowie
- Created At: 2026-05-02T12:34:09Z

### Content

# Journal Entry 2 - 02/05/26 -
Hello again, I'm back now and I realised when submitting my first journal that I didn't actually write the requirements list, so I'm gonna do that AND (following my amazing gantt chart) begin the brainstorm for the mechanical subsystem.
Here's the outcome of my mechanical 'brainstorming':
Mechanical brainstorming
So i need to think about how the handbrake will move and stuff, wait lets check what is in the scope of the ‘mechanical section’; (handbrake path, sensor interaction, architecture, part sourcing, materials)
Okok handbrake path is the thing i wanna look at first, i know some other simracing handbrakes have some cool things going on so lemme look at those
I want it to be adjustable in height and angle

Lever radius ~200mm
Spring lever radius ~5mm

100N force at radius

I need to get kitchen scales to estimate what kinda force i want to have to put in JUST A SECOND! Okokok heres the test:
![very scientific test.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MTgsInB1ciI6ImJsb2JfaWQifX0=--c780cb2feaf77d239c5883a49a534307e438ae78/very scientific test.png)
Ok i think i want around 2-3.5 kg of force which issss
(2 to 3.5) times 9.81 = 19.6 to 34.3 newtons of force BUUUTT some forums on the interwebs said that car handbrakes are around like 5-15 kg force was expected of them idkdkd
Lets calculate for 45 newtons of force for now!
Okay so i realised just now that the part that presses on the spring is PIVOTING which means that it is not actuating the spring linearly and there are a few solutions i can think of:
 - pivots at both sides of the spring (hard to do i think)
Really high spring rate and really small radius for spring actuation part
(ie same force, low travel)
Im going to decrease the radius for the spring part for now because its an easier fix
How about 5mm, therefore with a ~20mm diameter spring and lets say like 25 degrees of full handbrake travel then ; 2.16mm displacement and to get a force of 45 newtons at 200mm 
Thats 9 Nm of torque, at 2.16mm (2.16*10^-3 m) = 0.00216,,
9/0.00216 about 4200N (4.2 kN) wow 
"Give me a lever long enough, and a fulcrum on which to place it, and I shall move the world"
So 4.2kN with displacement of 2.16mm
Is spring rate of 4200/2.16= 1944N/mm spring rate lets check the list erm
Ok lets try to minimise spring rate by maximising the radius but also keeping the spring deflection (difference between inside/outside) at like 5mm MAX
Okay if i do need a high spring-rate spring I have some motorbike valve springs that are like
39mm long
Im gonna try to measure the spring rate because im an idiot, heres the method:
![another great test.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MjIsInB1ciI6ImJsb2JfaWQifX0=--abd405f069d6a6acd6865bbb3b4558d9838fdaf6/another great test.png)
40mm uncompressed
About 6kg for 4mm displacement which means
Lets say 15mm radius
7mm spring displacement
9Nm at 15mm
Wait lets make this easier
Heres the formula for the spring rate with changing radii and max angles:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MjEsInB1ciI6ImJsb2JfaWQifX0=--c19558df173d6788e4c2108f23d18c959fdfd9ff/image.png)
Why is it so hard to find a spring
This is making me sad
https://www.bunnings.com.au/century-spring-corp-14-x-34-9-x-1-8mm-compression-spring-2-pack_p0487950
https://www.bunnings.com.au/richmond-30-x-10-x-9mm-rubber-sealed-precision-bearing-2-pack_p0103231

Once i had found the bearings and spring that i was gonna use i got straight into the CAD to help me visualise what else i would need and to layout how the project might look:
![assembly.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MjUsInB1ciI6ImJsb2JfaWQifX0=--844cfacd049a579ea2f1d6fdbcad5a0208812a04/assembly.png)
My thought process as i went everything:
(might maybe just line up with the timelapse)
first i was thinking HOW is this gonna pivot; ive seen some cool four bar linkages but i decided VERY quickly that just a single pivot on an axle is the way to go.
most systems have the pivot mounted beneath the desk so i eyeballed some dimensions to give myself (what i thought would be) enough room and it ended up nicely, i started by designing the pivot (the bit that the lever attaches to) and designed mounting holes to allow for 30* of freedom when mounting the lever to the pivot. then i went along designing the actually handbrake lever. i made it about 200mm long, which should be good with the high mount on the pivot (i used my ruler to determine a good size) and made it 30mm wide (this dimension does not matter much as a 3d printed 'grip' part will bolt over it) i added holes to the part to allow for mounting.i then started designing the ''chassis' of the system and added a slot for another plate to sit in to hold the spring, this is when i realised that i needed to 1. decide on a spring and 2. determine an optimal geometry. I spend quite a while trying to determine an appropriate spring rate. once i had a spring then i played around with the mounting for a bit. I assembled all the components.and messed around with the plates and geometry for a bit more.

TODO FOR NEXT ENTRY:
potentiometer mounting
shaft end screws + all fasteners
electrical component spacing
prototyping







## Entry 3
- ID: 5211
- Author: bowie
- Created At: 2026-05-03T03:30:52Z

### Content

# Journal 3 - 03/05 - Mounting the potentiometer???
So i gotta actually mount the potentiometer to any spinny part of the assembly so that i can get an angle measurement, the only problem with the current design? the lever and pivot are the ONLY spinny parts:(((.
![static pivot.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA3NjYsInB1ciI6ImJsb2JfaWQifX0=--61b630b5509ee73b366a83083eb67570ff06a2f9/static pivot.png)

So far i have two ideas, mount it coaxially to the pivot axis, this requires the shaft to rotate with the handbrake which is NOT achieved in the current design 
OR
Gear mesh interface (angled rack connected to pivot affecting a pinion mounted too the potentiometer) 

The shaft mount sounds way easier but it means i need to change the design a bit and may be a bit less clean lets see…
![dynamic.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA3NjcsInB1ciI6ImJsb2JfaWQifX0=--51d1b81b831fffdfd2d0dd99d503d073429c41e5/dynamic.png)
![side.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA3NjgsInB1ciI6ImJsb2JfaWQifX0=--ec039702abc7f811557e47158fa6ab252bbf77b9/side.png)
Its kinda hard to see/visualise but theres nothing really stopping the shaft/bearing assembly from shifting/falling out of the mount plates UNLIKE the static setup where bolts could be used at the ends of the shaft to retain the shaft. Ill have to find a workaround.
One solution is using flanged bearings but this means i would have to find another set of bearings and could potentially mean redesigning all of the parts.

One small problem that i encountered was when i put the new design together in the cad, the hardstops that i had implemented in the design to help me visualise where it would stop and go were bugging which meant the spring plates werent aligned properly. As the angle between the spring plates changes as the lever pivots, i set the spring plates to go from +10deg offset to -10deg offset over the 20deg movement of the lever, so that rather than going from 0deg to 20deg (20deg max spring bend), the maximum spring bend is only 10 degrees. The cad limits were set off of the actual lever (which is adjustable in angle when mounting to the pivot), so with a different setup (which i was testing) the limits were all wrong. I fixed this by changing the limit in the cad to be between the spring plates.

Back to solving the ‘mounting the potentiometer’ problem:
Flanged bearings
Different shaft/mounting setup
Rack and pinion with eccentric potentiometer mounting

I have 10mm and 1/2in shafts
Maybe i can just retain the bearings with 3dp covers, thats what im gonna go with for now
Oh but i really want flanged bearings:
Ill get back to this later bye for now


## Entry 4
- ID: 5257
- Author: bowie
- Created At: 2026-05-03T09:52:52Z

### Content

# Journal 4 - 03/05 - Casing!!
Now im getting started on the casing, to determine what the casing must actually case, i made cad parts for the RP2040 (it was impossible to find accurate drawings with the dimensions i needed), and i measured the lcd screen i had to determine its dimensions. and i made the potentiometer too.

I put the parts into the cad:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA4ODEsInB1ciI6ImJsb2JfaWQifX0=--3c59926caeb5fbf17a6f527578d6e961c7ba1d61/image.png)
then i started making the case around the components' positions.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA4ODIsInB1ciI6ImJsb2JfaWQifX0=--f3f580bda56991297d22d5f330cead3954058e4b/image.png)
cross section view:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA4ODMsInB1ciI6ImJsb2JfaWQifX0=--427252929458da69b1691bdcd5a9fd150062031a/image.png)
and i began to add fasteners but changed my mind as i wanna get the whole chassis and casing done before i bother with fasteners.
I think the project will use just M3s and either M5s/M6s.
M3s for the smaller 3DP to 3DP or board mounting and m5/m6 for structural connections.:
what the cad looks like so far:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA4ODQsInB1ciI6ImJsb2JfaWQifX0=--0e1361eb88665c9d71911bda2c854c440f8aceac/image.png)
next i wanna finish the chassis, casing and begin work on the bom
ohkay buh bye!




## Entry 5
- ID: 5424
- Author: bowie
- Created At: 2026-05-04T12:32:39Z

### Content

# Journal 5 - 04/05 - more 3dp parts!?
hey gangalang!
today i wanted to do more work on the casing and mounting so that is what i did.
i made a knob that goes under the assembly for the clamping so that you can turn it to tighten and mount it (see photos)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEzMjIsInB1ciI6ImJsb2JfaWQifX0=--ed1a404fcf17f24f6d8af444eb2b14ef79563601/image.png)
i also made a 3d printed foot 🤤 part that is the part that interacts with the desk. but it was too big :( so i made it smaller and increased the spacing between the plate and the desk, this also means it can fit more desks if i do change my desk whenever.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEzMjMsInB1ciI6ImJsb2JfaWQifX0=--7409f76b412411bbbbd99f770f62ec063fa9cdd0/image.png)
i tidied up the case that hold the electrical components but it is nowhere near finiished.
i also made a plate ![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEzMjEsInB1ciI6ImJsb2JfaWQifX0=--1c6c29affb07bfbb6fa56648d00267846f1683a7/image.png)
to mount the potentiometer but i dont like that its threaded into a part because it could come undone when in use, ill add that to the todo testing.
i wanna start doing some prototyping and testing soon so that is on the agenda for next few entries,,,
ohkay buhbye






## Entry 6
- ID: 5590
- Author: bowie
- Created At: 2026-05-05T12:47:19Z

### Content

I tidied and finished the case (still needs work, holes, manufacturing consideration)
i also made the grip piece (needs similar work)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTE2NTcsInB1ciI6ImJsb2JfaWQifX0=--217a83528e960d11fca6478da432716c2776aef5/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTE2NTgsInB1ciI6ImJsb2JfaWQifX0=--6fbdab451a6f68ed05149b661f8cd91e53f29153/image.png)
i wont start the BOM until i have all the fasteners in the cad.
next entry i will be tidying the parts and preping them for manufacture (maybe)


## Entry 7
- ID: 5737
- Author: bowie
- Created At: 2026-05-06T14:06:37Z

### Content

Journal 7 - 06/05
Today I ran FEA simulations on all of the parts that face considerable forces to determine whether or not the current design will be able to bear the expected loads.
All tested parts passed.
First I tested the lever, with the bottom two bolt holes fixed as bolted holes and a total force of 200N applied over the top bolts backwards, the maximum internal stress of the part was approximately 40MPa, this is significantly lower than Aluminium 6061's yield strength.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIwOTMsInB1ciI6ImJsb2JfaWQifX0=--cee544b289644d36f9a4f6162ff842dfc4d5706a/image.png)
The 3DP hardstops were also tested.
With 1kN of force applied to the areas where the pivot plates interact, the maximum stress was calculated to be ~6.5 MPa, this is less than PLA's yield strength of ~30MPa, the part only deformed a maximum of 2mm with this force which is acceptable given the excessive nature of the testing and the minimal impact that a deformation of that scale has on the operation of the system.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIwOTUsInB1ciI6ImJsb2JfaWQifX0=--b916ef534df4a5e547d327fdd2ce4c4801afb52a/image.png)
The pivot plate was tested with a force coming from the lever of ~400N. The axle and hardstop faces were constrained. The maximum internal stress was ~13MPa, which is significantly smaller than 6061's yield strength.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIwOTYsInB1ciI6ImJsb2JfaWQifX0=--b25bef31f2d0a8ff30fc9b52a0d84a742d300e83/image.png)
All parts with considerable forces applied to them have internal stresses significantly lower than their respective yield strengths in excessive cases.
* Note: SolidWorks amplifies the deformation in the output images for the purpose of analysis. The part deformation was either mentioned or negligible for all cases.

Now that I know that all the parts designs are feasible and able to handle the loads, I can begin to modify the parts for manufacture and start prototyping subsystems.


## Entry 8
- ID: 5890
- Author: bowie
- Created At: 2026-05-07T12:57:25Z

### Content

Journal #8 - 07/05
Today I finished the 3D printed parts and casing, they all have a nice sleek finish and hide all of the ugly parts of the internals, I considered fasteners and internal cable routing. I still need to do interference checks and I am aware of at least one problem at the moment. I got most of the fasteners into the CAD but there are a few more, and I need to work on consolidating my fastener selection.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0MDUsInB1ciI6ImJsb2JfaWQifX0=--3f68767730a3d0e61d8543c5013c89573c5e040a/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0MDYsInB1ciI6ImJsb2JfaWQifX0=--b04397ae3f0f23d5ab3018c4c070effb2be01be9/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0MDcsInB1ciI6ImJsb2JfaWQifX0=--c1bd6ffc15f56aa96886af6f305e439a5eff93f4/image.png)



## Entry 9
- ID: 6087
- Author: bowie
- Created At: 2026-05-08T13:38:09Z

### Content

# journal 9 8/5
hellow..
Due to component availability with what i have easy access to, big bolts will be M6s and small bolts, M3s.
The only place where that doesnt work is the shaft retaining bolt on the right side of the shaft, that will likely need to be an M8 bolt due to the current internal diameter of my shaft. heh..
I added in fasteners to the CAD and changed the parts to finalise the 3DP parts. 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI4MzQsInB1ciI6ImJsb2JfaWQifX0=--8d839baa946bc44902bdbab0ae330a50d23044fd/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI4MzUsInB1ciI6ImJsb2JfaWQifX0=--883cd4888ff0dfae9c8f3ebd81db515f751fcc2d/image.png)
wow isnt that bearutiful!
This is the first design finalized, next entry will be a major redesign, focusing on part count reduction and design for manufacture. I will look into:
Plastite Fasteners
Nyliner Bearings
Potentiometer Component Alternatives
Broaching Nuts
Possible alternative part manufactures (imagine the pivot part was one really cool CNC milled part…)
Tapping plates to get rid of nuts
Potentiometer mounting
i reallly wanna get started on building but this is gonna be a m,easure twice cut once kinda project, :(
ok thanks im realyly tired now



## Entry 10
- ID: 6263
- Author: bowie
- Created At: 2026-05-09T13:16:09Z

### Content

OKOKOK 
The move:
Get LCD working on my desk
PART COUNT REDUCTION:
Plastite fasteners
Nyliners
Find cool potentiometers
Broaching nuts
Tapped plates
Ok lock in

Replacing M6 bolt/nut combo in the grip-piece with two M3 plastite fasteners. Done

So the potentiometer needs an imperial nut to mount it: gross..


This is a cross-section of the grip: 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMyOTksInB1ciI6ImJsb2JfaWQifX0=--a3397bf53373725989fecf6f5c90d3c7eb1a75d0/image.png)
now it can take a plastite fastenerok


## Entry 11
- ID: 6390
- Author: bowie
- Created At: 2026-05-10T06:51:45Z

### Content

Today i wanna actually get the lcd working on my desk but i really dont know how to/which libraries to use so this might be hard


Okay i managed (after about 15 minutes) to solder one of the four pins to the board and it has continuity to the board and clears the others so im calling that a success. 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM1OTAsInB1ciI6ImJsb2JfaWQifX0=--423d20d7c74834bf8bee161a139190921d5a6eaa/image.png)
Now for the other 3…
Ok how about we plug in the soldering iron first…
Ok solder joint two works…
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM1OTEsInB1ciI6ImJsb2JfaWQifX0=--5d127b7050af1d3d05a1f596f8d67e9a0289e18c/image.png)
yikes...
Now for #3!
I might cry; these are terrible
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM1OTIsInB1ciI6ImJsb2JfaWQifX0=--1ead4d2c702b9632bc7324506e378ab7d3cb3ffa/image.png)
El quattro…
Okok i also went back and “improved” the other connections./..
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM1OTMsInB1ciI6ImJsb2JfaWQifX0=--28181f8ab36ed62dfcebe93d4345aa5aa8ea4a20/image.png)
How beautiful.
Ok now to connect themn to the board.
Ok for whatever reason i have like only two male-female jumpers…
IT WORKS!!!
The lib that im using is u8glib, it seems to work with a lot of OLEDs and i thiiink it works with mine
I couldnt find SSD1309 in the library with the I2C interface so i changed the initialisation command to work with it. 
Okokokokokok
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM1OTQsInB1ciI6ImJsb2JfaWQifX0=--0b81ec2b91aa2d8be83a549c6e8d1325f5cac0ae/image.png)
Yippeee
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM1OTUsInB1ciI6ImJsb2JfaWQifX0=--27123eebb1a608b1eae09a15f3427adbe4c1cf9a/image.png)
Ok i think thats it for today tq n bye









## Entry 12
- ID: 6572
- Author: bowie
- Created At: 2026-05-11T11:10:35Z

### Content

Okay so today i wanna get the potentiometer talking to the arduino so im pretty sure i can just use the analogue in pins from the wiper and hook up the +ve and -ve to the 5V and GND.
Lets see how this works
Getting reasonable readings from the potentiometer;
Theyre slightly jumpy and inconsistent but when i hold the wires properly into the arduino its all good.

OKOKOK adding a 10k pulldown resistor between A0 and ground made the values so incredibly consistent and stable
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQxNDcsInB1ciI6ImJsb2JfaWQifX0=--1525ece848300f0aac8f39c46717d2a9a1bedff4/image.png)
Okok so at ~883 reading is max angle,
Im gonna try to make a readout on the display
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQxNDgsInB1ciI6ImJsb2JfaWQifX0=--fc44f77b13b1e9cadcaf0f69e79bb43126d26824/image.png)
The screen can show the values but its slow, glitchy, and prone to freezing/crashing preeeety often…
Google says to use pulldowns on SDA and SCL pins which might work????
Fortunately i have a very cool two resistor pulldown harness that i had made in the past so i do not have to go through the effort of making one up

Nope
No change i dont think, still freezes
Nvm it said pull-UP, i dont think that makes a difference but ill try it.

Okoko i think the arduino was just shorting on my deskmat
Lifting it seemed to solve the freezing and speed issues but often times it will print gibberish numbers

Okoko i think the arduino was just shorting on my deskmat
Lifting it seemed to solve the freezing and speed issues but often times it will print gibberish numbers

Okay also i was on u8glib (the lib i WAS using) docs and its deprecated, so ill be switching to u8g2.

Ok using the new library solved ALL of my problems
heres the wiring layout (as described in image above)
![image](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQxNDksInB1ciI6ImJsb2JfaWQifX0=--50acbc72ec333c24c82b59e1474188c0d0090eae/WhatsApp Image 2026-05-11 at 21.00.50.jpeg)

oh yeah!!
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQxNTAsInB1ciI6ImJsb2JfaWQifX0=--365c75285276aa229b811dda07bf62126802c767/image.png)

I like how this turned out, its very responsive, stable and accurate, more so that i initially thought it would be so…
thats all for today, 
the next few entries will probably be a lot more hardware/cad focused so i can get that done and finish the rest of the project.



## Entry 13
- ID: 6766
- Author: bowie
- Created At: 2026-05-12T13:02:43Z

### Content

I tidied up the cad and finished getting all the fasteners correct, I tried implementing a nylon bushing instead of a bearing but had issues retaining the shaft. I added covers to the bottom parts of the plate to give it a finished look and looked into adding a flange that sits inside the casing and rotates with the lever to cover the internals but realised that the geometry wouldn't work so I just shrunk the opening at the front. I added the appearances and textures into the CAD and got some mock renders, just using SolidWorks. I also removed a few bolts that I had missed, the plates will be tapped as I have the equipment, it allows for smaller packaging, and means fewer parts. The internals are still quite visible during operation but I think it still has a really clean aesthetic with the black plastic and aluminium plates.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4MDMsInB1ciI6ImJsb2JfaWQifX0=--6b3e682aa61876eeaf17aa6bf098416f6218f9da/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4MDQsInB1ciI6ImJsb2JfaWQifX0=--31b5f43ef899ababe3307486f96c972b82d53537/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4MDUsInB1ciI6ImJsb2JfaWQifX0=--cd6c78aa96e9f6286c05d78f702026497a5d63c0/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4MDcsInB1ciI6ImJsb2JfaWQifX0=--0d5fa312efacc906ebf8751640d521a85c11c451/image.png)
Next I wanna print some parts for prototyping and ill start work on the 'zine.


## Entry 14
- ID: 6930
- Author: bowie
- Created At: 2026-05-13T13:27:06Z

### Content

# Journal 14 - 'Zine Time!
Im making the zine today.
First i started by looking at some posters i have made for motorbikes for some reference.
I PERSONALLY think they look pretty cool so im going from there.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUxNDcsInB1ciI6ImJsb2JfaWQifX0=--b99c7e95852960a572d40d7bac91f1ca890e9ea7/image.png)
I initially started my design in photoshop but I quickly realised that my prime PS days were behind me and booted up canva.
I set a base layout for the design and got a transparent background render of the assembly:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUxNDgsInB1ciI6ImJsb2JfaWQifX0=--a45116472db099d0c26164c10b3e76d56ce23568/image.png)
With a nice draft design, some straight YAP on the page, and school tomorrow; I decided to call it a day at this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUxNDksInB1ciI6ImJsb2JfaWQifX0=--094bde38ecd3ca118cd41875252ef7ebe1449f88/image.png)



## Entry 15
- ID: 7064
- Author: bowie
- Created At: 2026-05-14T12:20:47Z

### Content

# Journal 15
Today I got more work done on the zine. It looks pretty good so I don't think I'm gonna touch it until I start building at least. Also I lost all the code that I had written so I WILL need to rewrite that at some point in time. 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU0OTcsInB1ciI6ImJsb2JfaWQifX0=--4e24cc554d6d436301037177834a7a9a52865afc/image.png)



## Entry 16
- ID: 7244
- Author: bowie
- Created At: 2026-05-15T12:33:37Z

### Content

Journal 16
I’m gonna go through and get a list of stuff I wanna do soonest:
Today im gonna pretty much complete the initial version of the software but if time permits ill also get all the stuff that i SAID that i would do done.

That list entails:
BOM
Figuring out how to work with assetto corsa

I got the BOM done and looked into putting a micro switch in the assembly but i have yet to determine how and where its gonna work. Didnt have time to look into how it interacts with my computer but oh well.
(Possible microswitch position (removes adjustability in height (ill explain that later)):)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4MjksInB1ciI6ImJsb2JfaWQifX0=--941ab2d7aa3a6497a31820831cc4db99e7d9ca4d/image.png)
Bom:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4MzAsInB1ciI6ImJsb2JfaWQifX0=--d0182365aad190d1ec9f5ac4c59a47a886e007a3/image.png)



## Entry 17
- ID: 7397
- Author: bowie
- Created At: 2026-05-16T11:52:53Z

### Content

Journal 17
17
Today i wanna rewrite the code and get it to a point where its close to the final code. I wanna look more into how i can mount a microswitch and I wanna get a quote for the aluminium plates to see if its better just to order them.

Code:
So far the code just normalises the analogue input from the potentiometer, renders text on the screen, and draws a box to show how much the lever is pulled.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYxNzEsInB1ciI6ImJsb2JfaWQifX0=--4287e54723691cbafea70395e2c86dddda274ba2/image.png)

Microswitch
I have no idea how its gonna work:
So far im thinking:
Bolt coming out of plate, OR mounted in the case at the front

The microswitch mounts to the mounting plate on the left of the handbrake via two M1.6 bolts. An M3 bolt mounted to the pivot interacts with the switch to signify when the brake is fully compressed. It acts a bit early so that the hardstop is what takes the force and so that you dont need to pull it FULLY to actuate the switch.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYxNzIsInB1ciI6ImJsb2JfaWQifX0=--96ad40350dd459e704c93277f69607b7e19dc265/image.png)

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYxNzMsInB1ciI6ImJsb2JfaWQifX0=--a959f9fec3d681ec0a1fbc24e4d7a4115fe513ee/image.png)



## Entry 18
- ID: 7591
- Author: bowie
- Created At: 2026-05-17T11:50:56Z

### Content

Journal 18
Update BOM
Get quote for plates
Had to adjust parts for DFM and checked some quotes to get the parts machined
JLCCNC is by far the cheapest
Oh wow, quoting with JLCCNC with the parts as “CNC Machining” parts was ~160aud
Quoting them as “sheet metal parts” (technically true) and they are like 50aud total
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY1NTgsInB1ciI6ImJsb2JfaWQifX0=--ec69710aef05142564d6b2ea043b2eef92966ee4/image.png)
The only downside is ally 5052 instead of 6061
But i could also get them machined out of stainless steel for like 60aud total soooo
Strength is not a concern its really just like aesthetics and weight.
I might get black powdercoat on the lever.
Now that i am sure of the material options, i am going to re-run the simulations to check that ally 5052 WILL NOT break/yield/deform too much.
Okay at the maximum force that the plate will ever experience, the maximum deformation is 0.0028mm…
I think thats fine right.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY1NTksInB1ciI6ImJsb2JfaWQifX0=--2245c35f724ceb1f41e955bef26ddf396cb8feed/image.png)
Ok so ally 5052 is completely fine and pretty cheap.
Ok i can also get bearings from china for like 90 cents
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY1NjAsInB1ciI6ImJsb2JfaWQifX0=--cfde2b9f68cfa493ebd45717d581c7f46c75ed2e/image.png)
What this has to be incorrect
Ok so noone thought to tell me that i can get like every single part that i need from jlcmc…
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY1NjEsInB1ciI6ImJsb2JfaWQifX0=--c5a23586aac7510c3e665a5339f7b506e6777917/image.png)
What if i get the fasteners from jlc too…
No
No
No
Maybe..
Thinking about different ways of retaining the springs
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY1NjIsInB1ciI6ImJsb2JfaWQifX0=--86579152d8fd1484538ac7120130cc7044a7868e/image.png)
After an ‘external’ technical review; i have some notes that i need to consider going forward:
The square press fits wont work, they require precision tolerances for four faces per part for like 4 parts which is especially difficult if im getting the parts laser cut…
I want to find a different method of retaining the springs. I’m thinking of having sleeves going over bolts between the two main mounting plates and having cylindrical extrusions to retain the springs as can (kinda) be seen in the image.
I need to look into how much force will need to go through the clamps into the desk and consider how Im going to make the clamp work; i may need to increase the area of the foot or introduce a cam/lever to get a lot more force. I will switch the bearings to bushings as not 100% of the rotation is achieved. I also need to consider how i will axially retain the pivoting assembly.



## Entry 19
- ID: 7781
- Author: bowie
- Created At: 2026-05-18T12:09:37Z

### Content

# journal 19

Ok im stupid

I was racking my brain for like an hour in class today pondering how to mount two sheet metal plates perpendicularly. ONE MINUTE ON GOOGLE and i can just use a bracket… i feel really stupid. So the initial design relied on a press fit between two laser cut parts. And the thing is; laser cut 6mm plates are not exactly precise… so to solve this the plan is too use a bracket to mount the plates and drill/tap holes by hand that i need. But now im thinking about it, jlccnc offer tapped holes so if i specify which holes are tapped then it should be really easy for me.
Actually instead of brackets (because its impossible to find an appropriate off-the-shelf part) i will have the spring retention plates bent to mount to the main plates.

Ok so today i am going through all the parts and FINALIZING all of the hole diameters and tolerances

With the bottom plate, the width between the two pivot plates is very very small so a bent sheet part just WOULDNT fit so i am nouting the plate to the OUTSIDE!!!
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY5OTQsInB1ciI6ImJsb2JfaWQifX0=--749e26492281d680d6dd0a99bdbc57685e8ddffa/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY5OTUsInB1ciI6ImJsb2JfaWQifX0=--98b65fd5fca996cedff6da75dad629b0fdbc2834/image.png)
After redesigning the pivot and mount plates i determined that i could reduce the m6s that hold the spring plate to m3s as m3s can take 1.1kN in shear force and I have 4 operating at max ~300N shear force

max displacement for 5052 2mm part is like 0.2mm so ill just go for really thin stainless steel, also for parts to be laser cut at jlccnc they need to be like <4mm i think so should be fine>?
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY5OTIsInB1ciI6ImJsb2JfaWQifX0=--bb3b8c7a948d164c11e3d7b45a7685a56e68e73e/image.png)

The plates can be wayyy thinner too which i will change later gotta sleep now ok buhbye





## Entry 20
- ID: 7960
- Author: bowie
- Created At: 2026-05-19T13:43:29Z

### Content

# Journal 20
Hello!
today was mainly fixing the CAD and finalising changes that I made while half asleep last night.
Fixing up and changing the plates.
Also found COTS part for the foot which is nice because theyre well finished and spin on the bolt so that you can get a lot of force.
Fixed up all mates in cad
Added fasteners for the new spring plates and changed the knob/foot subassembly to one consisting of COTS parts.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTczODIsInB1ciI6ImJsb2JfaWQifX0=--699db8740a60429d7914b6b8e99df03b6f5f892d/image.png)



## Entry 21
- ID: 8151
- Author: bowie
- Created At: 2026-05-20T13:42:59Z

### Content

Journal 21
Fixed up the case geometry so that now it is flush, sleek, and actually fits together:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc4MjEsInB1ciI6ImJsb2JfaWQifX0=--7e7dd5f394a7a5c2dd4c10529c4e7bff13270b7a/image.png)
I also started adding in the wiring in the CAD, I will finish off this later. 

## Entry 22
- ID: 8306
- Author: bowie
- Created At: 2026-05-21T12:56:54Z

### Content

# Journal 22
I thinned the plates and fixed all the mates in the CAD. I also had to change the plates and 3D printed case components.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgxNzIsInB1ciI6ImJsb2JfaWQifX0=--2125e721b5a091f561bb4dbd7fe486e1b0aa43cd/image.png)
All the plates are thinner, leading to cheaper plates, a lighter assembly, and smaller packaging, without major structural disadvantages as I can make the plates out of steel for a similar price.


## Entry 23
- ID: 8462
- Author: bowie
- Created At: 2026-05-22T12:17:11Z

### Content

# Journal 23
Ok i neeeeed to get the parts finalised so that I can order them and actually get this thingo done!
I want to get 45 hours of development before submitting then ill use the 15 for assembly and debugging.
Todo list:
- GitHub REPO
- CAD Drawings for plates
- Finalise tolerances and fitments for plates
- Check plates with FEA.
- Fix 3D printed case parts.
- Finalise BOM
- Finalise ZINE

First thing i can do really easily is the FEA for the whole assembly this time.
First i suppress the elements that are out of scope for the structural analysis (elec components, wires, fasteners) this is because im only checking if the plates are fine and more components can confuse the software.
I start up SOLIDWORKS Simulation add-in and define the materials.
The plates will be made of stainless steel 304
Yeah okay theres way too many components for me to do analysis in the assembly, fortunately theres only about 5 different plates so ill just individually do them all again.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0OTMsInB1ciI6ImJsb2JfaWQifX0=--a3ed0a4615c578860798cde73b0af259d8bd99e4/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0OTQsInB1ciI6ImJsb2JfaWQifX0=--025cf0f86cddb2a45e47fc32ed32e83e671337a3/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0OTUsInB1ciI6ImJsb2JfaWQifX0=--5aaa05fa134199400287d739e0e8ba237059b234/image.png)
Removed aesthetic cutouts from plate as they drastically reduced the plates total strength and could lead to failures in extreme use cases.
Now that I have checked and fixed the plates, I am going to update the BOM.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0OTYsInB1ciI6ImJsb2JfaWQifX0=--6fc8777ef19bed3bf5b53c2f58b11f02a3be39cd/image.png)
Got rid of parts i removed, changed the sourcing of some parts that im going to get from JLC and added some new fasteners.
I also added all the images, cad, and journals to the GitHub and did some work on the readme.






# Desk-Mounted Sim-Racing Handbrake
##### As the name suggests, an analogue, desk-mounted, sim-racing handbrake. With 20° of travel and a 2.42" OLED display.

readme layout
(reqs):
name
description (what make it unique, how its used, why it was made, what problem it solves)
pictures:
 - full model
 - components
 - cross section views
 - wiring diagram
 - examples of others
 - zine


ReadMe requirements:
1. Explanation of what your project is

✓ Short description of what your project is! Highlight what makes it unique
✓ How do you use it? Be detailed! Others can’t read your mind.
✓ Why did you make it? Be personal! Are you solving a problem? Trying to make something smaller than previously thought possible?
2. Add images! A picture is worth a thousand words. Include:

✓ Screenshots of a full 3D model of your project fully assembled
✓ Screenshots of your PCB with components, if you have one
✓ A clear wiring diagram, if you’re not using a PCB
✓ Anything else that makes it clear what your project is and what it’s for

ZINE

Also gotta upload files to github



## Entry 24
- ID: 8648
- Author: bowie
- Created At: 2026-05-23T13:43:15Z

### Content

# Journal 24
24
Todo list:
- GitHub REPO
- CAD Drawings for plates
- Finalise tolerances and fitments for plates
- Check plates with FEA.
- Fix 3D printed case parts.
- Finalise BOM
- Finalise ZINE
- Firmware


First I’m going to upload all my files so far to the GitHub (everything except the CAD for now)  **DONE**
Then ill tidy up the github page, complete the readme and determine the layout _INCOMPLETE_
Then ill go through and fix up all the plates and complete some drawings _INCOMPLETE_
Then ill fix up all the case components **DONE**
Then ill upload the CAD to github _INCOMPLETE_
Then ill quote all the parts at JLC _INCOMPLETE_
Then ill update the BOM _INCOMPLETE_
Then ill complete the ZINE and the Github page _INCOMPLETE_
Then ill start some 3D prints for testing _INCOMPLETE_
Then ill work on the firmware while those are printing. _INCOMPLETE_

README:
readme layout (reqs): name description (what make it unique, how its used, why it was made, what problem it solves) pictures:
full model
components
cross section views
wiring diagram
examples of others
zine
ReadMe requirements:
Explanation of what your project is
✓ Short description of what your project is! Highlight what makes it unique ✓ How do you use it? Be detailed! Others can’t read your mind. ✓ Why did you make it? Be personal! Are you solving a problem? Trying to make something smaller than previously thought possible? 2. Add images! A picture is worth a thousand words. Include:

✓ Screenshots of a full 3D model of your project fully assembled ✓ Screenshots of your PCB with components, if you have one ✓ A clear wiring diagram, if you’re not using a PCB ✓ Anything else that makes it clear what your project is and what it’s for

ZINE

So it turns out that theres a lot to fix with the cad
**turns out im gonna be doing cad.**
I changed the last m6s to m3s and had to change a lot because of that

Solidworks also just hates me for whatever reason
(the spring is NOT supposed to be there…)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5NDEsInB1ciI6ImJsb2JfaWQifX0=--2c9d876d2edd1b83dec505407a2bbb0e2509b2b9/image.png)
I also need to calculate the ACTUAL spring rate that i need because i was thinking about it and i dont trust my past self with the calculations.

A really cool thing desmos released really recently (i know this because i follow them on instagram) is that they have developed and released a new page/feature thing where you can combine multiple sliders/calculators/graphs/geometric relations to form one dashboard-esque view and i think thats really cool because a lot of the time im using desmos to calculate things like this and this just allows for a really neat and intuitive understanding, please check it out if you have the time: https://www.desmos.com/notebook/fgedhep7ta/view
Ughhhhh
I rthink solidworks crashed
Whops
Just about every mate in my assembly has failed and after about 15 minutes straight of trying to find the problem i think my best bet is just reassembling from scratch.
:(
Nevermind
I found the bad mate
Ok now that the cad is all tidied up!
I thought about adding a dust boot at the bottom of the lever but looking at it in the cad and i changed my mind.
I miiight add one later but that will be after i have the parts.
Ok so now that the cad is actually fine now, i need to determine the spring rate
Spring goes from 37 to 26
Spring at no deformation is 40mm
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5NDUsInB1ciI6ImJsb2JfaWQifX0=--ce1b7fbeea521fcf915665e4385a2227dfb0fa69/image.png)
Spring deformation can be modelled by 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5NDIsInB1ciI6ImJsb2JfaWQifX0=--ac591b7e4037e9d1e64e51bd03dd67d310dac065/image.png)
The deformation of the spring at x=20degrees is about 13.6mm
Now i need to back calculate the force to determine the spring rate.
Whilst researching appropriate forces, i came across the fact that a lot of handbrakes on the market use either load cells or hall effect sensors. I was aware of this, and aware of the reason why they do (potentiometers can be inconsistent and wear over time). And I decided that I want to add a hall effect sensor into my solution. For now both the hall effect sensor and potentiometer will be in the solution but that may change with the final design after testing.
https://core-electronics.com.au/hall-effect-sensor-analog-threshold.html
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5NDMsInB1ciI6ImJsb2JfaWQifX0=--e62d2d9c59ffb410068e01bdd460f43dca2d3d37/image.png)
I also found out that it is easier and better (lower latency, better resolution + connectivity) to flash prebuilt adaptable firmware like freejoy or GP2040-CE to my RP2040.
Its getting late so i am going to go to sleep, anyways heres my todo for later:
Todo list:
- GitHub REPO
- CAD Drawings for plates
- Finalise tolerances and fitments for plates
- Spec hall effect sensor and magnet
- Add hall effect sensor and to CAD and determine mounting and wiring. 
- Finalise BOM
- Finalise ZINE
- Firmware (FreeJoy, GP2040-CE)
- DETERMINE SPRING RATE!@!!!!




## Entry 25
- ID: 8853
- Author: bowie
- Created At: 2026-05-24T12:32:36Z

### Content

# Journal 25
25
Todo list:
GitHub REPO
CAD Drawings for plates
Finalise tolerances and fitments for plates
Spec hall effect sensor and magnet
Add hall effect sensor and to CAD and determine mounting and wiring. 
Finalise BOM
Finalise ZINE
Firmware (FreeJoy, GP2040-CE)
DETERMINE SPRING RATE

Ok now i need to actually determine the springrate.
Ok im going for ~10kg force at the handle
Which is 98.1N of force at a distance of ~180mm
=Fd=98.10.18=17.66 Nm of torque
Spring distance from pivot is 33.6mm
F=d=17.660.0336=525.6N ok thats not gonna work; spring rate ~40.5N/mm
Hmm ok lets recalculate with 5kg, should just be half oh thats not gonna work either.
Ok lets calculate from what spring rates are available.
Im going to target the highest springrate i can for springs ~15mm diameter with ~40mm length on JLC:
https://jlcmc.com/product/s/A04/ATDC/compression-springs-inner-diameter-reference-stainless-steel-l%C3%97(25~30)
9.81N/mm

https://jlcmc.com/product/s/A04/ATKC/compression-springs-outer-diameter-reference-stainless-steel-l%C3%97(15~25)
19.58N/mm

https://jlcmc.com/product/s/A04/ATJU/compression-springs-outer-diameter-reference-l%C3%97(20~30)
9.79N/mm

https://jlcmc.com/product/s/A04/ATKA/compression-springs-inner-diameter-reference-stainless-steel-l%C3%97(28~35)-l%C3%97(20~30)
9.79N/mm

I need to check what percent the springs compress because these springs are speced by the max deformation percentage.
Spring goes from 37 to 26
(1-2640)100%=35%
I hope this isn’t due to the spring bottoming out… all the appropriate springs only allow up to 30% deformation.
The spring could be further away from the axis (increasing d in F=d, decreasing needed force) but i could only add about 5mm which would change 36 to 41mm
Wait nvm so for the springs, the minimal length is 26mm, on the specsheet it shows the minimal allowed lengths so let me check what passes with 26:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1NDEsInB1ciI6ImJsb2JfaWQifX0=--138396028f78cd057b519e8ebbacb502e3ec9eda/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1NDIsInB1ciI6ImJsb2JfaWQifX0=--3bea8d7f559d3df85b95637bd3ba61cfeafbab83/image.png)
Ok 19mm between pivot plates
Ok 18mm spring dia with 40mm length and k=waitnvm
Ok so the min size with 18mm spring is like 27.5mmuhggghghg itsa so close damnmit.
Okj lemme check if the problem is bottoming out or just recommended value
“Do not use the spring under the condition that the maximum allowable compression is exceeded. If the spring is used under the condition that the maximum compression is exceeded, the load and durability may be reduced, or even damage may occur. The L dimension of the round wire coil spring will be reduced even if the stroke exceeds the maximum compression amount only once.”
Ok so i think what theyre saying is if i go further than 27.5mm it can plastically deform.
Opk i also dont think its a physical constraint (ie spring bottoming out) as the spring has like
7 ish turns max on one side and spring dia is 2.9
7*2.9 =20.3 which is where the spring bottoms out..

Ok lets step back.
I dont think the high spring rate is really all that necessary,
2.5kg would be fine at the lever

Lemme calc from 9.8
9.8N/mm
Compression is 40-26=14mm
14*9.8=137.2N

Having thought about it, 30degrees of travel to the hardstop would be more appropriate as i want the force back through the handle to be high enough to be really hard before the hardstop but i also want the handle to be ‘pullable’ at the start of the stroke. The spring also needs preload so that initially there is force on the lever at 0 stroke.

I have had a lot of trouble determining the spring spec for a few reasons, firstly there are so many variables that I can pick, secondly JLC makes it really hard to find springs BY springrate (you have to pick everything else first THEN check if springrate is appropriate), and finally i dont know what force at the handle is appropriate.
So now that i better understand the requirements I am going to sketch out the function of force at lever per degrees of travel.
maybe something like this???
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk1NDQsInB1ciI6ImJsb2JfaWQifX0=--9ba6a6bf9b3b20f44cbb66ad759c0d6700fd2773/image.png)
I want the 20degree mark to be about the most you will pull it each time and past that just to prevent the user from hitting the hardstop.
Ok now that the requirements are really plain and simple, i need to make a calculator to find the other values from what i have.
I’ve really dragged out finding a spring so i wanna wrap it up reaaaal soon because it might also require changes in the cad.
ok bye





## Entry 26
- ID: 9106
- Author: bowie
- Created At: 2026-05-25T13:07:51Z

### Content

# Journal 26
26
Okay i want the force at the handle to ramp up as the travel nears the end, i want the force function (with respect to the angle) look like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAxNjAsInB1ciI6ImJsb2JfaWQifX0=--2807d45ba4503d9313367cf95dcacd2676adefd1/image.png)
And because the spring compression wrt angle looks like this:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAxNjIsInB1ciI6ImJsb2JfaWQifX0=--02b5d4e89a64893f76a80fdd0e355de66e8bb93f/image.png)
(according to current CAD)
I can pretty accurately estimate the needed springrates at each point here:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAxNjMsInB1ciI6ImJsb2JfaWQifX0=--a205414c0f88bfefc33e6fb0225a345b68b69954/image.png)
The spring rate hovers around ~10N/mm until the 20degree mark before 
Wait im stupid
So what i needed to be doing was getting the derivative of the force@handle-angle * lever ratio
Which gives me this function:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAxNjYsInB1ciI6ImJsb2JfaWQifX0=--95c4ff54e85de26d93035f6bb9173f017fe0bf6d/image.png)
Initial spring rate ~5N/mm
But with a preload of
F_0~100N
20mm

Ok so 60mm spring with springrate~5N/mm
But because i have no idea how to

Because the springs are also like 20 cents, I could always order a few with different rates/preloads
But for now The ‘buy list’ is
40mm @ 10N/mm
50mm @ 10N/mm
60mm @ 5N/mm
Ok lets find some springs.
https://jlcmc.com/product/s/A04/ATJT/compression-springs-outer-diameter-reference-l%C3%97(27~35)
50mm x 18mm OD @ 4.85N/mm 
60mm x 18mm OD @ 4.88N/mm
https://jlcmc.com/product/s/A04/ATKA/compression-springs-inner-diameter-reference-stainless-steel-l%C3%97(28~35)-l%C3%97(20~30)
40mm x 16mm OD @ 9.79
50mm x 16mm OD @ 9.79
Ok springs specced yippee

What next…
GitHub REPO
CAD Drawings for plates
Finalise tolerances and fitments for plates
Spec hall effect sensor and magnet
Add hall effect sensor and to CAD and determine mounting and wiring. 
Finalise BOM
Finalise ZINE
Firmware (FreeJoy, GP2040-CE)

Ill work on the repo now
Ok i really fleshed out the readme

Looks nice and good to know that that is out of the way for now and i can get into really finalising the design.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAxNjcsInB1ciI6ImJsb2JfaWQifX0=--8442968c7faf0017cac599892c2933642fdd712e/image.png)


## Entry 27
- ID: 9657
- Author: bowie
- Created At: 2026-05-27T14:00:22Z

### Content

# Journal 27
TODO:
CAD Drawings for plates
Finalise tolerances and fitments for plates
Spec hall effect sensor and magnet
Add hall effect sensor and to CAD and determine mounting and wiring. 
Finalise BOM
Finalise ZINE
Firmware (FreeJoy, GP2040-CE)

Ok lets put these tasks in order, I can’t do the BOM until I know my components, so that comes after the hall effect sensor. And can’t finalise the CAD for the plates until I know the hall effect sensor position. Can’t make the drawings before the parts are finalised.
Spec and add hall effect sensor and magnet to CAD
Finalise tolerances and fitments
CAD Drawings
BOM
ZINE
FIRMWARE

First I gotta find a hall effect sensor.
I THINK that the kY-035 is appropriate. But i have no idea what distance is appropriate between the magnet and sensor. I will make it (obviously) adjustable in software, but maybe physically too.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE0MzAsInB1ciI6ImJsb2JfaWQifX0=--7d263f8964a84f1931905a11fe89184fa8057cb8/image.png)
The 3D printed spacer now bolts to the pivot plate and can hold up to two 0.125” cube magnets.
https://core-electronics.com.au/magnet-square-0-125.html
A washer and M3 bolt both hold the magnets AND secure the magnet holder to the plate.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE0MzEsInB1ciI6ImJsb2JfaWQifX0=--d2c157d69076aba4f9fdb4873d612822927f731a/image.png)
I also had to adjust the bottom case to be able to fit and house the PCB, i had to flatten the curve and remove a slot.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE0MzIsInB1ciI6ImJsb2JfaWQifX0=--64ef1682b113b91484423049d4f866c14f3467bf/image.png)



## Entry 28
- ID: 9909
- Author: bowie
- Created At: 2026-05-28T13:52:34Z

### Content

28
Firmware requirements:
Hall effect sensor AnalogIO pin A0
Vout = 2.5v to 4v

Because I need a lot of signal processing (changing where the axes start and end) I think that rather than using a preconfigured firmware, I will write my own firmware to get the controls I want. I think that other firmware could work but I want to develop my own for now.
Some configurable firmware packages that I could use are:
GP2040-CE
FreeJoy
JoyCore-FW

CAD Drawings for plates
Finalise tolerances and fitments for plates
Spec hall effect sensor and magnet
Add hall effect sensor and to CAD and determine mounting and wiring. 
Finalise BOM
Finalise ZINE
Firmware (FreeJoy, GP2040-CE)

Started making drawings then got tired
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjIwNTEsInB1ciI6ImJsb2JfaWQifX0=--7d09c0a8501b1187cb7c85419679389a160b3d9f/image.png)



## Entry 29
- ID: 10128
- Author: bowie
- Created At: 2026-05-29T12:57:47Z

### Content

# Journal 29
29
Okay today will probably just be a tonne of cad work, the model needs a lot of refining and i think if i just put my head down i can get it done really quickly, i wanna check that everything is really good before i get the drawings:
OK so the plates that need drawings:
2x Mount plates
1x tapped pivot plate

Also I had to move the microswitch so that it didnt hit the plate
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI4NzEsInB1ciI6ImJsb2JfaWQifX0=--419fe841fbebd853dc0dfb9f4ad7c522c14f3128/image.png)
Also the more i think about it the less i want to use a potentiometer
Removed potentiometer and could reduce size of case drastically:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI4NzIsInB1ciI6ImJsb2JfaWQifX0=--e9987a0024fcf88bd98f5aea1ccf4e3cdf71f721/image.png)
I decided to redo the fasteners so that I can put them into the BOM and because I needed to reconsider all the fastening for the drawings.
Ok i think all the cad is good good


Nope still need to to the top half of the case

Ok so my assembly just exploded uhoh
Ok set myself back like 10 mins oh well
I also need to consider clips for cable routing inside the case!

I have spend some time reworking the case part that holds the OLED. It now can be symmetrical with the assembly:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI4NzMsInB1ciI6ImJsb2JfaWQifX0=--d4f43387c19dc97c92dfbe9ec3291cc7361d7910/image.png)
Also i thought about how its assembled and how its manufactured, and these parts of the case can be a part of the main case part:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI4NzQsInB1ciI6ImJsb2JfaWQifX0=--a7bf27b46284e4d7a02fefd5992fa7ae370fa3e7/image.png)
TODO: 
reposition hall effect sensor:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI4NzksInB1ciI6ImJsb2JfaWQifX0=--3b1e658aa51e5e93560caa3dabe325ec71147732/image.png)
I am going to move the sensor to the side plate so that the mounting is more robust.


## Entry 30
- ID: 10384
- Author: bowie
- Created At: 2026-05-30T12:16:50Z

### Content

# Journal 30
30
TODO:
Reposition hall effect sensor
CAD Drawings for plates
Finalise tolerances and fitments for plates
Spec hall effect sensor and magnet
Add hall effect sensor and to CAD and determine mounting and wiring. 
Finalise BOM
Finalise ZINE
Firmware (FreeJoy, GP2040-CE)

I also just realised that i was using the solidworks toolbox parts instead of the mcmaster carr library but now i realise that i cant upload the cad for all the fasteners so imma upload the cad for the mcmaster carr separately later.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjM1NDMsInB1ciI6ImJsb2JfaWQifX0=--2a2b32e47e874876c944f69002ee7eb83e6b4390/image.png)
I changed the way that the magnets are mounted but im still figuring out how to mount the hall effect sensor:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjM1NDQsInB1ciI6ImJsb2JfaWQifX0=--46eaddbb3b409b6d317d210758a0391234ae88af/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjM1NDUsInB1ciI6ImJsb2JfaWQifX0=--1296414de29851fa6af18c5e5efc9088c692e1d7/image.png)
i also made drawings for the pivot plates:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjM1NDYsInB1ciI6ImJsb2JfaWQifX0=--63fbb63f23b67f119c53120194b5235f3264ebba/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjM1NDcsInB1ciI6ImJsb2JfaWQifX0=--228cfb742300761041e0c123f5b3eecf2d6b2061/image.png)
Theyre not full drawings just references for JLCCNC because these parts are tapped.
good night.


## Entry 31
- ID: 10647
- Author: bowie
- Created At: 2026-05-31T12:54:52Z

### Content

Journal 31
TODO:
Reposition hall effect sensor
Replace all fasteners for McMaster Carr
CAD Drawings for plates
Finalise tolerances and fitments for plates
Spec hall effect sensor and magnet
Add hall effect sensor and to CAD and determine mounting and wiring. 
Finalise BOM
Finalise ZINE
Firmware (FreeJoy, GP2040-CE)

OKAY i really gotta lock in to get this done so i need drawings very very soon i want them done by tonight

As for mounting the potentiometer to the side plate;
I dont know the exact pitch between the mounting holes so i am adding a slot along with using nuts to hold the plate in, this also makes it adjustable in position to allow for different positions in front of the magnets.
It removes a lot of material in what seems to be a structurally significant area but according to FEA analysis it is fine sooo:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjQyNzYsInB1ciI6ImJsb2JfaWQifX0=--978ce341be4a062c4139457a45a155f47c016ef5/image.png)
I also had to remove the case mounting hole that was just below the bearing hole, this is fine as the case already mounts in many other places and this hole was superfluous. 
Yeah okay im stupid
Dont know how i didnt think of this but:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjQyNzcsInB1ciI6ImJsb2JfaWQifX0=--a5fefbea9cb427e1b4096f6285b763cdfa3068ef/image.png)
the board significantly extrudes from the plate. It may be small enough for me to just dig out a hole in the case let me check.
Okay i cant because it pokes out of the case.
Oh nvm it wasnt even mounted.
Okay so the position is adjustable:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjQyNzksInB1ciI6ImJsb2JfaWQifX0=--29748e7b61a92f5974161ca57a42ab8a6a6b56c2/image.png)
With the magnet mounting i have decided that a press fit is a lot easier so i am gonna look for a cylindrical magnet.
Also thought about the possibility of the pivot parts being one bent sheet metal part:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjQyODEsInB1ciI6ImJsb2JfaWQifX0=--f602ba95071b0ef49f7c33d5fbb933728198a13d/image.png)
Thats all for today
okay i really gotta put my head down the next few days to finish this.


## Entry 32
- ID: 10876
- Author: bowie
- Created At: 2026-06-01T11:53:31Z

### Content

# Journal 32 
Changed the magnet to be on the plate and a cylinder magnet rather than the two square magnets:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjQ4MjgsInB1ciI6ImJsb2JfaWQifX0=--7ac7a4a4d31af17a6a0c0f43096d0b1a9d5f2c67/image.png)



## Entry 33
- ID: 11375
- Author: bowie
- Created At: 2026-06-03T13:33:08Z

### Content

# Journal 32
Journal 32
Today i am finishing the grip/pivot plate,
Considering whether it should be one part or two
Designed and made the sheet metal part for the handle to be one part


Wooh look pretty cool imo
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYzNDQsInB1ciI6ImJsb2JfaWQifX0=--c7f0f4f9f640c58e06fed16d5ccec180fecce45f/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYzNDUsInB1ciI6ImJsb2JfaWQifX0=--32713c325e6ac1a0807d79fedc5c821f0c872786/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYzNDYsInB1ciI6ImJsb2JfaWQifX0=--711ed5845e8950ef97df4cad68c1ecea5c75950f/image.png)
As one part, its cheaper to order and a LOT easier to assemble.


## Entry 34
- ID: 11837
- Author: bowie
- Created At: 2026-06-05T14:07:56Z

### Content

# Journal 33
33
I started by tidying up the bend relief cuts for the sheet metal part:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc2MzEsInB1ciI6ImJsb2JfaWQifX0=--55f532b0de7dc2f54c426d538b8083cd917120a7/image.png)
List of sheet metal part drawings
Lever
Mount plate left
Mount plate right
Spring plate lower
Spring plate upper
Maybe the mount plates could be one plate too…
Ill make technical drawings for that too just incase

Also quickly consider fastener access, for example:

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc2MzIsInB1ciI6ImJsb2JfaWQifX0=--58129a89e766f6cf00261e1d066ab32d1c229e23/image.png)
These fasteners could come from the outside, making assembly way easier..
This is the mount plate as one part:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc2MzMsInB1ciI6ImJsb2JfaWQifX0=--d44bd9f4d90b4b3820aabc7f8b329871bce01a69/image.png)
The assembly is getting really messy so im going to start from scratch.
Okay so; going through all the holes in order to make the drawings, i realised that with the new designs, half of the holes in the lever are unnecessary:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc2MzQsInB1ciI6ImJsb2JfaWQifX0=--4ea027a53085871aada21785d3db395dc1859014/image.png)
Case mount Holes | M3 TAPPED | x4
Shaft holes | M6 CLEARANCE | just one :)
hall effect slots | M2 CLEARANCE | x2
microswitch holes | M1.6 TAPPED | x2
spring plate mount holes | M3 CLEARANCE | x2
SAME ON BOTH SIDES
BOTTOM
clamp screw hole | M6 TAPPED | x1

pivot part
RIGHT SIDE
grip mount holes | M3 TAPPED | x2
spring plate mount holes | M3 TAPPED | x2
bearing hole | 15mm PRESS FIT | just one :)


LEFT SIDE
grip mount holes | M3 CLEARANCE | x2
spring plate mount holes | M3 TAPPED | x2
bearing hole | 15mm PRESS FIT | just one :)
magnet holes | 6mm PRESS FIT



SMALL SPRING PLATE
spring hold hole | M8 TAPPED
mount holes | M3 CLEARANCE

LARGE SPRING PLATE
spring hold hole | M8 TAPPED
mount holes | M3 TAPPED

CONSIDERATIONS:
laser cutting really isnt all that; if the precision is really important: make hole smaller and drill myself
 
Ok time to make the drawings!
Ok all the drawings are done:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc2MzUsInB1ciI6ImJsb2JfaWQifX0=--d06c50fd544be64496f9847a50b2d142d8bd9ec6/image.png)
Here’s one for your viewing pleasure.
Jlc quote, just need to add in fasteners and finish case now
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc2MzYsInB1ciI6ImJsb2JfaWQifX0=--390d037cfd68f9bdebf3784202367f19fe510235/image.png)



## Entry 35
- ID: 11986
- Author: bowie
- Created At: 2026-06-06T04:06:33Z

### Content

Journal 34
Im on my laptop today so no solidworks
Imma import some of the CAD into onshape so that i can better visualise it to write the BOM.
I started writing the BOM, I split it up into sections; sheet metal parts, JLC components, electronics components, 3DP parts, fasteners.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjgwNzUsInB1ciI6ImJsb2JfaWQifX0=--91872df4091185d5657820316eb7d80673b9591c/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjgwODMsInB1ciI6ImJsb2JfaWQifX0=--5b3cf22d8ae6cdc84ccebe5ecbb3bd7e51faf1f1/image.png)



## Entry 36
- ID: 12172
- Author: bowie
- Created At: 2026-06-07T01:34:47Z

### Content

# Journal 35
I finished the wiring diagram and finalized the components. The I2C needs pullup resistors so those are there:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg1ODMsInB1ciI6ImJsb2JfaWQifX0=--892c64dd03ac84178663b52bc2a5867d7ed79ae1/image.png)
I tried adding the case to onshape to get a render for my zine but I think I’m better off just waiting until I can use solidworks.
The total cost is around ~92 USD including shipping.
Next what I need to do is render the handbrake and finalize the zine.
TODO to ship:
Firmware
Bom.csv
Step files
Solidworks files
Libraries references

I’m going to get started on the updated firmware now
Firmware requirements:
Hall effect sensor AnalogIO pin A0
Vout = 2.5v to 4v


pseudocode

INITIALIZE OLED LIBRARY
INITIALIZE PINS:
 - Analog IN A0 "hall effect"
 - SDA/SCL I2C

Just a very rough framework (actually nothing)



## Entry 37
- ID: 12289
- Author: bowie
- Created At: 2026-06-07T14:07:53Z

### Content

#Journal 36
TODO to ship:
Firmware
Bom.csv
Step files
Solidworks files
cad assm
zine/render
Libraries references

First im redesigning the case for the new assembly:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg4MTUsInB1ciI6ImJsb2JfaWQifX0=--2833ea0c4b6dd4a2549862d1971f6464caa38896/image.png)
And im thinking about how it will come together and be assembled, so far im thinking:
left and right (pros: really easy to print and assemble, cons: MIGHT leave huge seam line down middle of case)
Case and plate, one side of case fully encompasses assembly and plate finished on left side.

I Think ill just split it down the middle for now unless i can find another way, the screen is ~70mm wide so the case at the top has to step up to that width to house it, and theres not enough room above the top mounting plates si i added more thickness in the case to house the oled and the bevel.


## Entry 38
- ID: 12479
- Author: bowie
- Created At: 2026-06-08T11:48:29Z

### Content

# Journal 37
TODO to ship:
Firmware
Bom.csv
Step files
Solidworks files
cad assm
zine/render
Libraries references

The agenda for today is finishing the case, if it clamps together from the sides, i realized that the bevel can be included in the case part, meaning the case is only two parts.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkzOTEsInB1ciI6ImJsb2JfaWQifX0=--deedd4d2b5874ec242ed9de9282aa540071fe71a/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkzOTIsInB1ciI6ImJsb2JfaWQifX0=--a8a9be84ed04d06023acacac5764af0144ccef0c/image.png)
Ok lets add fasteners to the CAD
Added in about half the fasteners:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkzOTQsInB1ciI6ImJsb2JfaWQifX0=--8fd1a762148a5c0b16520d6e56f0ceec4d2a713e/image.png)
I also cut out the inside of the case so that bolts and nuts can protrude a bit without breaking/hitting the case

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkzOTUsInB1ciI6ImJsb2JfaWQifX0=--44fdb10c8d3b9d160dbb2368dc7d1e705cf70f8b/image.png)



## Entry 39
- ID: 12756
- Author: bowie
- Created At: 2026-06-09T13:31:36Z

### Content

# Journal 38
38
TODO to ship:
Firmware
Bom.csv
Step files
Solidworks files
cad assm
zine/render
Libraries references
TONIGHT:
Finish cad
Render
Zine
Github
Firmware
I had to make the cutouts in the inside of the case a bit bigger to fit the M6 button head shaft screws so I added ribs so that the especially thin section of the part doesnt cause too much trouble:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjk5NTMsInB1ciI6ImJsb2JfaWQifX0=--68637fb9ce85973af8117ff71559418b5537b811/image.png)
The part will be split in 3 for the purpose of 3d printing:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjk5NTQsInB1ciI6ImJsb2JfaWQifX0=--7a349ee1f7f67992f747a82ec5365a787708bcf2/image.png)
I added in all the fasteners to the assembly and added a locknut to the screw mounting:
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjk5NTUsInB1ciI6ImJsb2JfaWQifX0=--7dda86252619d6d91c7ca29f6ccbecc8a0c18e12/image.png)
Then i rendered the assembly and updated the zine
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjk5NTYsInB1ciI6ImJsb2JfaWQifX0=--4fee4386bcf5cf6796332e47ce5436becda990aa/image.png)
Ooooh shinyyyy
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjk5NTcsInB1ciI6ImJsb2JfaWQifX0=--41c21e68f63ce8563879b9381abe541c301b4297/image.png)
TODO to ship:
- Start AND Finish Firmware
- Update and Upload Bom.csv
- Upload CAD/Drawings
- Finish GitHub page (readme, references)


## Entry 40
- ID: 12980
- Author: bowie
- Created At: 2026-06-10T09:42:01Z

### Content

39
TODO to ship:
Start AND Finish FirmwareDONE
Update and Upload Bom.csvDONE
Upload CAD/DrawingsDONE
Finish GitHub page (readme, references)DONE

I updated the BOM and my readme on github
Now im going to get started on my firmware,
Im going to use circuitpython.
I wrote setup files, drivers and the main firmware for the handbrake
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA1NDQsInB1ciI6ImJsb2JfaWQifX0=--8e62de86c100837d269f12b95c006c487287844c/image.png)
Updated and finished github to had everything i am now ready to ship!
I will do a full firmware and debugging writeup once i have the parts and can confirm that my code is actually coding! okay
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA1NDUsInB1ciI6ImJsb2JfaWQifX0=--7adea516f90b8e638870058c299ffdbd23f864b6/image.png)


