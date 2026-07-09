# format=manual-md

title: BN2-20 INS2 EN
source_pdf: BN2-20_INS2_EN.pdf
machine: vinyl-printer-cutter
pages: 62

---

# BN2-20 INS2 EN

## Page 1

Thank you very much for purchasing this product.
• To ensure correct and safe usage with a full understanding of this product's performance, please be sure to read through this manual
completely.
• Unauthorized copying or transferal, in whole or in part, of this manual is prohibited.
• The specifications of this product and the contents of this operation manual are subject to change without notice.
• The operation manual and the product have been prepared and tested as much as possible. If you find any misprints or errors, please
inform us.
• Roland DG Corporation assumes no responsibility for any direct or indirect loss or damage that may occur through use of this product,
regardless of any failure to perform on the part of this product.
• Roland DG Corporation assumes no responsibility for any direct or indirect loss or damage that may occur with respect to any article made
using this product.
Copyright © 2023 - 2026 Roland DG Corporation
R5-260401
https://www.rolanddg.com/

## Page 2

Introduction............................................................................................................. 2
About the Documentation for This Machine .................................................................................... 3
System Requirements/Overview.................................................................................................. 4
System Requirements ........................................................................................................ 4
Software to Be Used ......................................................................................................... 5
Network Configuration Diagram............................................................................................ 6
Network Settings.................................................................................................................... 7
Setting the Computer's Network ........................................................................................... 7
Installing the Software ............................................................................................... 10
Software Setup.....................................................................................................................11
Downloading and Installing Roland DG Connect Hub...................................................................11
Creating a New Roland DG Connect ID ...................................................................................13
Registering the Machine to Roland DG Connect Hub...................................................................14
Installing VersaWorks from Roland DG Connect Hub ...................................................................15
Configuring the Settings in VersaWorks ..................................................................................16
Actions to Take When Machine Information Is Not Displayed in Roland DG Connect Hub ..............................19
Directly Connecting to the Computer ....................................................................................19
Initial Printer Settings ................................................................................................ 25
Installing the Cutting Tool ........................................................................................................26
Step 1:  Assembling the Cutting Tool.....................................................................................26
Step 2:  Installing the Cutting Tool .......................................................................................27
Loading Media ......................................................................................................................28
Loading Roll Media ..........................................................................................................29
Ink Filling and Initial Adjustment ...............................................................................................33
Step 1:  Filling with Ink.....................................................................................................33
Step 2:  Loading Media .....................................................................................................37
Step 3:  Nozzle Drop-out Test .............................................................................................47
Step 4:  Performing Automatic Correction ..............................................................................48
Step 5:  Blade Adjustment .................................................................................................49
Step 6:  Print & Cut Position Adjustment ................................................................................51
Adjusting the Amount of Blade Extension......................................................................................54
Adjustment When Not Cutting the Backing Paper (Normal Cut) .....................................................54
Adjustment When Cutting the Backing Paper (Perforated Cut) ......................................................55
Fixing Dot Drop-out and Dot Displacement ....................................................................................56
Normal Cleaning .............................................................................................................56
Medium Cleaning ............................................................................................................57
Powerful Cleaning ..........................................................................................................58
Manual Cleaning .............................................................................................................59
Contents
1

## Page 3

Introduction
About the Documentation for This Machine ......................................................... 3
System Requirements/Overview ...................................................................... 4
System Requirements............................................................................. 4
Software to Be Used .............................................................................. 5
Network Configuration Diagram ................................................................ 6
Network Settings ........................................................................................ 7
Setting the Computer's Network ................................................................ 7
2
 Introduction

## Page 4

The following instruction manuals are included to ensure proper use of the machine.
• Safety Precautions
This manual contains important precautions for using the machine.
• Quick Access Guide
This guide contains the setup flow for this machine as well as links to procedures.
• Regular Maintenance Guidelines
These guidelines include links to maintenance items listed in the manual. Scan the QR code to open
the maintenance instructions directly.
• Machine Installation
This guide contains details on how to install the machine.
• Installing the Software and Configuring Its Initial Settings
This guide contains information on how to configure the initial settings of the machine.
• User's Manual
This manual contains details such as how to use and maintain the machine as well as an FAQ (a set of
frequently asked questions).
• Roland DG Connect Designer User's Manual
This guide contains basic operating instructions for the design and output software.
• Videos
These are the support videos for the manuals. The videos help guide users through explanations that
are not easily understood through text and illustrations only.
View the manuals and videos from the following URL.
https://downloadcenter.rolanddg.com/BN2-20
MEMO
Screen captures from Windows are used for Utility windows in these manuals.
About the Documentation for This Machine
Introduction
3

## Page 5

System Requirements
Prepare a computer that matches the requirements.
Windows
Mac
Operating system (OS)
Windows 11
macOS 26, 15, 14
CPU
Intel Core i5 4670 or higher
Apple Silicon
Memory
16 GB or more
8 GB or more
Video card, monitor
Full HD (1,920 × 1,080 pixels, 24-bit color)
1,280 × 1,024 pixels or above
Solid state drive
256 GB or more free space
128 GB or more
Hard disk
500 GB or more free space
Others
Internet connectivity, web browser, and Ethernet port
System Requirements/Overview
4
 Introduction

## Page 6

Software to Be Used
The software to be used is listed below.
In this manual, "Roland DG Connect Hub" is written as "Connect Hub," "Roland DG Connect Designer" as
"Designer," "VersaWorks 7" as "VersaWorks," and “BN2 Utility" as "Utility."
Connect Hub
System hub software. The major functions are shown below.
• Starting Designer, VersaWorks, and Utility
• Transferring data between Designer and VersaWorks
• Transferring printer status and operating information required for the Ro-
land DG Connect service
Designer
Design software used on Roland DG Connect.
The software makes it easy to create print data, set print settings such as
media and quality, and output via VersaWorks.
VersaWorks 7
Software RIP (Raster Image Processor).
For more information on the functions, see the VersaWorks 7 manuals.
Utility
Software that is needed to operate the machine. The major functions are
shown below.
• Settings and adjustments
• Management of ink remaining amount
• Maintenance
• Display of messages and error messages
Designer
(VersaWorks)
Connect Hub
Utility
When using commercially available design software such as Adobe Illustrator or CorelDRAW, the created
data (.pdf, .ai, etc.) can be imported into Designer for editing. The data can also be directly imported into
VersaWorks and output after configuring the print properties.
System Requirements/Overview
Introduction
5

## Page 7

Network Configuration Diagram
System Requirements/Overview
6
 Introduction

## Page 8

Setting the Computer's Network
The machine and computer are connected using an IP address that is automatically assigned via DHCP.
IMPORTANT
Windows
This manual contains operation explanations for the following versions. Operations and names may vary
depending on the version and build of the OS.
• Windows 11
Version 24H2
Procedure
1.
Log on to Windows as the [Administrator] or a member of the [Administrators] group.
2.
Open Control Panel.
Search for "Control Panel" from the taskbar.
3.
Click [Network and Sharing Center].
4.
Click [Ethernet] or [Wi-Fi].
5.
Click [Properties].
If the [User Account Control] dialog box appears, click [Continue].
The [Ethernet Properties] or [Wi-Fi Properties] dialog box appears.
Network Settings
Introduction
7

## Page 9

6.
Select [Internet Protocol Version 4 (TCP/IPv4)], and then click [Properties].
If the [Internet Protocol] check box is clear, select it.
7.
Select [Obtain an IP address automatically] and click [OK].
8.
Click the following buttons to return to the original state.
a. [Close] in the [Ethernet Properties] or [Wi-Fi Properties] dialog box
b. [Close] in the [Ethernet Status] or [Wi-Fi Status] dialog box
Network Settings
8
 Introduction

## Page 10

Mac
This manual contains operation explanations for the following versions. Operations and names may vary
depending on the version and build of the OS.
• Mac
macOS 15.2
Procedure
1.
Log on to the Mac as the "Administrator."
2.
From the Apple menu, click [System Settings...].
3.
Click [Network]>[Wi-Fi] or the network name (when using Ethernet).
4.
Click [Details...].
5.
Click [TCP/IP].
6.
Select [Using DHCP] for [Configure IPv4].
7.
Click [OK].
Network Settings
Introduction
9

## Page 11

Installing the Software
Software Setup..........................................................................................11
Downloading and Installing Roland DG Connect Hub .......................................11
Creating a New Roland DG Connect ID........................................................13
Registering the Machine to Roland DG Connect Hub........................................14
Installing VersaWorks from Roland DG Connect Hub........................................15
Configuring the Settings in VersaWorks .......................................................16
Actions to Take When Machine Information Is Not Displayed in Roland DG Connect
Hub .................................................................................................19
Directly Connecting to the Computer.........................................................19
10
 Installing the Software

## Page 12

Downloading and Installing Roland DG Connect Hub
A connection to the Internet is required to download the software.
IMPORTANT
Windows
Operation methods may vary depending on the version and build of the OS.
MEMO
Procedure
1.
Start the computer and log on as the "Administrator" or an "Administrators" account.
Shut down all other programs.
Only the account with "Administrators" rights that was used to install this software can use it.
MEMO
2.
Access the following website on the computer where the software will be downloaded.
https://downloadcenter.rolanddg.com/BN2-20/#software
Depending on where you live, you may be asked to complete user registration before downloading the soft-
ware.
MEMO
3.
Click [Roland DG Connect / Connect Hub].
4.
Click [Installer / Updater].
The explanation window for Roland DG Connect appears.
5.
Click [Go to Download].
6.
Read the license agreement for the software. If you agree with the contents, click [Agree].
7.
Download [RolandDG_Connect_Setup.zip] to an arbitrary location.
8.
Right-click the downloaded file [RolandDG_Connect_Setup.zip], and then click [Extract All].
9.
Click [Browse], specify the folder in which to extract the files, and then click [Extract].
10.
Double-click [RolandDG_Connect_Setup.exe] in the extracted folder [RolandDG_Connect_Setup].
When the [User Account Control] window appears, click [Yes] (or [Allow]).
11.
Select the language to use from the pull-down list, and then click [OK].
The setup menu screen appears automatically.
Software Setup
Installing the Software
11

## Page 13

Follow the on-screen instructions to carry out the installation.
For details on installation and registration, refer to the Initial_Setting_Guide in the extracted folder, [Ro-
landDG_Connect_Setup].
MEMO
Mac
The following operation procedure uses macOS 15.1. Operation methods may vary depending on the version of Mac OS
or the build of the OS.
MEMO
Procedure
1.
Start the computer, and then log on with the "Administrator" account.
Shut down all other programs.
Only the account with "Administrators" rights that was used to install this software can use it.
MEMO
2.
Access the following website on the computer where the software will be downloaded.
https://downloadcenter.rolanddg.com/BN2-20/#software
Depending on where you live, you may be asked to complete user registration before downloading the soft-
ware.
MEMO
3.
Click [Roland DG Connect / Connect Hub].
4.
Click [Installer / Updater [20**-**-**] for macOS].
The explanation window for Roland DG Connect appears.
Review the information and follow the onscreen instructions to download the file.
5.
Double-click the downloaded [RolandDGConnectHub-installer.dmg] file, and then double-click the [Ro-
landDGConnectHub-installer.pkg] file.
Follow the instructions of the installation wizard and perform installation.
Software Setup
12
 Installing the Software

## Page 14

Creating a New Roland DG Connect ID
Start Roland DG Connect Hub, click [New], and register the new ID. If you select the [Start Roland DG
Connect Hub] checkbox in the Roland DG Connect Hub setup wizard, Roland DG Connect Hub will start
automatically after setup finishes.
If you already have an ID, sign in and proceed to Registering the Machine to Roland DG Connect Hub(P.
14).
Software Setup
Installing the Software
13

## Page 15

Registering the Machine to Roland DG Connect Hub
Refer to the procedure below to register the printer to Connect Hub.
https://support.rolanddg.com/hc/en-us/categories/6469527154585-Roland-DG-Connect
Software Setup
14
 Installing the Software

## Page 16

Installing VersaWorks from Roland DG Connect Hub
Use Roland DG Connect Hub to install VersaWorks.
Procedure
1.
Start [Roland DG Connect Hub].
• Windows
Click the [Roland DG Connect Hub] icon in the notification area.
• Mac
Click the [Roland DG Connect Hub] icon on the Dock.
2.
In the main window, select the machine to use.
3.
Click the VersaWorks icon.
The sidebar is displayed on the right side of the window.
4.
Click [Install].
The software installation starts.
After installation completes, click the VersaWorks icon to start this piece of software.
Software Setup
Installing the Software
15

## Page 17

Configuring the Settings in VersaWorks
Procedure
1.
Make sure the power to the printer is switched on.
2.
Click the VersaWorks icon on the Roland DG Connect Hub home screen.
The sidebar is displayed on the right side of the home screen.
3.
Click [Open].
4.
Set the printer to connect.
To register a printer in VersaWorks for the first time, click [Add New Printer]. The [Printer
Registration] window is displayed, and VersaWorks will search for the connectable printers.
If the search finds zero printers, you will have to register printers manually. If the search finds five
or more printers, select the printer to register.
If you have used VersaWorks before, the machine information will be displayed on the home screen.
MEMO
Software Setup
16
 Installing the Software

## Page 18

When the detected number of printers is one to four:
(1) Check the list of detected printers and click [OK] to register all of them.
If there is a printer you do not want to register, click [Skip]. Register printers manually,
referring to the situation in which no printers are detected.
When five or more printers are detected:
(1) Select the printer to register, and then click [Register].
The printer details window appears.
(2) Click [OK].
(3) Repeat steps (1) and (2) to register printers.
When no printers are detected:
If printer search is not possible, check the LAN cable connection status.
MEMO
(1) Click [Manual Registration].
(2) Enter the IP address and click [Verify].
Items such as the [Model Name] and [Ink Type] are displayed.
(3) If there are no problems, click [Register].
(2)
(2)
(2)
(2)
(3)
(3)
The VersaWorks home screen shows the registered printer(s).
5.
Click
 to the right of the registered printer, and then click [Create Virtual Printer].
Perform this action on all the registered printers.
Software Setup
Installing the Software
17

## Page 19

6.
If you have backed up the VersaWorks settings and job data, restore them.
The previously used VersaWorks settings, etc. are applied to the newly installed computer.
This completes setup.
Software Setup
18
 Installing the Software

## Page 20

• If machine information is not displayed in Roland DG Connect Hub, refer to the following information
and bring the computer and this machine into the same subnet mask.
P. 6 Network Configuration Diagram
• If the computer and this machine cannot be brought into the same subnet mask, refer to Directly Con-
necting to the Computer(P. 19) and connect them directly, and then configure the network settings
for the computer and printer.
Directly Connecting to the Computer
This section explains the setting procedure for connecting one computer and one machine directly, not
over a network.
IP addresses that start with "192.168." can be used freely by anyone. Use one of these addresses when
connecting one computer and one machine in an environment separate from other networks.
1. Make the Network Settings on the Printer
Procedure
1.
On the Utility home screen, click
.
2.
Click [System Information], and then clear the [Obtain IP Address Automatically] check box under [Net-
work].
3.
Enter the [IP Address] and [Subnet Mask].
(1) Enter the [IP Address] and .
Item
Address to enter
IP address
192.168.0.XXX
Subnet mask
255.255.255.0
Note: Here, "XXX" may be any number you want from 1 to 254.
Here, "192.168.0.3" is entered by way of example.
(2) Enter the [Subnet Mask] and .
Enter the same subnet mask as the one used by the computer.
Actions to Take When Machine Information Is
Not Displayed in Roland DG Connect Hub
Installing the Software
19

## Page 21

192.168.0.3
255.255.255.0
4.
Click [Apply].
Actions to Take When Machine Information Is Not Displayed in Roland DG Connect Hub
20
 Installing the Software

## Page 22

2. A: Setting the Computer's Network (Windows)
Operation methods may vary depending on the version and build of the OS.
MEMO
Procedure
1.
Log on to Windows as the [Administrator] or a member of the [Administrators] group.
2.
Open Control Panel.
Search for "Control Panel" from the taskbar.
3.
Click [Network and Sharing Center].
4.
Click [Ethernet].
5.
Click [Properties].
If a [User Account Control] window appears, click [Continue].
The [Ethernet Properties] screen appears.
6.
Select [Internet Protocol Version 4 (TCP/IPv4) Properties], and then click [Properties].
If the [Internet Protocol] check box is clear, select it.
Actions to Take When Machine Information Is Not Displayed in Roland DG Connect Hub
Installing the Software
21

## Page 23

7.
Select [Use the following IP address], enter the IP address and subnet mask, and click [OK].
The addresses in the following table are examples used for the explanations in this manual. Enter the desired
IP address and subnet mask.
MEMO
Item
Address to enter
IP address
192.168.0.XXX
Subnet mask
255.255.255.0
"XXX" represents a number from 1 to 254. However, do not use the same number as set in "Make
the Network Settings on the Printer."
Actions to Take When Machine Information Is Not Displayed in Roland DG Connect Hub
22
 Installing the Software

## Page 24

8.
Click the following buttons to return to the original state.
a. [Cancel] in the [Ethernet Properties] window
b. [Cancel] in the [Ethernet Status] window
Actions to Take When Machine Information Is Not Displayed in Roland DG Connect Hub
Installing the Software
23

## Page 25

2. B: Setting the Computer's Network (Mac)
The following operation procedure uses macOS 15.1. Operation methods may vary depending on the version of Mac OS
or the build of the OS.
MEMO
Procedure
1.
Log on to the Mac as the "Administrator."
2.
From the Apple menu, click [System Settings...].
3.
Click the network name from [Network].
4.
Click [Details...].
5.
Click [TCP/IP].
6.
Select [Manually] for [Configure IPv4].
7.
Enter the [IP address] and [Subnet mask].
The addresses in the following table are examples used for the explanations in this manual. Enter the desired
IP address and subnet mask.
MEMO
Item
Address to enter
IP address
192.168.0.XXX
Subnet mask
255.255.255.0
Here, "XXX" can be any number from 1 to 254. Ensure that it is different from the numbers of other
equipment.
8.
Click [OK].
Actions to Take When Machine Information Is Not Displayed in Roland DG Connect Hub
24
 Installing the Software

## Page 26

Initial Printer Settings
Installing the Cutting Tool.............................................................................26
Step 1:  Assembling the Cutting Tool..........................................................26
Step 2:  Installing the Cutting Tool ............................................................27
Loading Media...........................................................................................28
Loading Roll Media ...............................................................................29
Ink Filling and Initial Adjustment ....................................................................33
Step 1:  Filling with Ink .........................................................................33
Step 2:  Loading Media ..........................................................................37
Step 3:  Nozzle Drop-out Test ..................................................................47
Step 4:  Performing Automatic Correction ...................................................48
Step 5:  Blade Adjustment......................................................................49
Step 6:  Print & Cut Position Adjustment.....................................................51
Adjusting the Amount of Blade Extension ..........................................................54
Adjustment When Not Cutting the Backing Paper (Normal Cut) ..........................54
Adjustment When Cutting the Backing Paper (Perforated Cut)...........................55
Fixing Dot Drop-out and Dot Displacement.........................................................56
Normal Cleaning..................................................................................56
Medium Cleaning .................................................................................57
Powerful Cleaning ...............................................................................58
Manual Cleaning ..................................................................................59
Initial Printer Settings
25

## Page 27

This operation is unnecessary if you will not use the cutting tool. Tighten the print-head carriage screw
lightly when no cutting tool is installed. Keeping the screw firmly tightened causes the cutting tool
insertion hole to become gradually smaller, making installation difficult.
Be sure to perform operations as specified by the instructions, and never touch any area not
specified in the instructions.
Sudden movement of the machine may cause injury.
WARNING
Never touch the tip of the knife.
Doing so may result in injury. The cutting performance of the blade will also be impaired.
CAUTION
Step 1: Assembling the Cutting Tool
Procedure
1.
Insert the pin into the blade holder.
Insert the pin until the tip protrudes about 3 to 5 mm (0.12 to 0.19 in.).
2.
Insert the blade into the blade holder.
Insert the blade into the hole so the blade tip is on the outside.
Installing the Cutting Tool
26
 Initial Printer Settings

## Page 28

Step 2: Installing the Cutting Tool
Procedure
1.
Open the front cover.
2.
Loosen the print-head carriage screw.
1
2
3
3.
Install the cutting tool in the print-head carriage.
OK
Not OK
1
2
3
4.
Tighten the screw.
5.
Close the front cover.
Installing the Cutting Tool
Initial Printer Settings
27

## Page 29

Media type
In this manual, the paper used for output is called "media." The two main types of media used in this
machine are shown below.
• Roll media: Media wound onto a paper tube
• Sheet media: Media not wound onto a paper tube such as standard-size media
Various paper qualities of roll media and sheet media are selectable according to the purpose. For detailed
information about each media, contact your media supplier. Media can also be purchased from our web-
site.
https://www.rolanddg.com/
Usable media
This machine cannot print on every kind of media. Before selecting media, be sure to perform trial
printing to check whether satisfactory output quality is obtained.
Size
Usable Media
BN2-30
BN2-20/BN2-20A
Width *1
150 to 762 mm (5.91 to 30.00 inches)
150 to 515 mm (5.9 to 20.3 inches)
Cuttable media thick-
ness*1
Max. 0.22 mm (8.66 mil; depending on the media composition)
Maximum media thick-
ness (including backing
paper)*1
When only printing: 1.0 mm (39.4 mil)
When performing cutting: 0.4 mm (15 mil)
Maximum roll outer di-
ameter
165 mm (6.5 in.)
150 mm (5.9 in.)
Paper tube (core) inner
diameter
76.2 mm (3 in.) or 50.8 mm (2 in.)
 
*1
Applies to both roll and sheet media
 
Maximum roll weight
• BN2-30: 12 kg (26.46 lb.)
• BN2-20/BN2-20A: 6 kg (13.23 lb.)
 
 
Other conditions
Media such as the following cannot be used.
• Media whose end is attached to the paper tube (core)
• Media that is severely warped or that has a strong tendency to reroll
• Media that cannot withstand the heat of the media heating system
• Media whose paper tube (core) is bent or crushed
• Media that bends under its own weight when loaded
• Media on a sagging roll
• Media that is rolled unevenly
 
 
Loading Media
28
 Initial Printer Settings

## Page 30

Loading Roll Media
Load the roll media onto the media flange and then load it in the machine. This procedure is not necessary
when using sheet media.
Use the following link to view a reference video for this procedure. We recommend that you view this video to
understand the overall flow of work.
https://vimeo.com/1003476467/d0c94b8c81
MEMO
Procedure
1.
Remove the media shaft from the machine.
2.
Open the lock lever (
) on the left media flange in the direction of the arrow, and remove the flange
from the media shaft.
3.
Check the orientation of the right media flange (
).
With the factory default settings, the right media flange is installed so that loading of roll media
with a 3-inch paper tube inner diameter is possible.
To load roll media with a 2-inch paper tube inner diameter, change the orientation of the right
media flange using the following procedure.
(1) Remove the snap pin (
) and pull out the mounting pin (
).
(2) Remove the right media flange from the media shaft (
).
(3) Change the orientation of the right media flange and install it on the media shaft with the 3-inch
side (
) facing the stopper (
).
(4) Secure the right media flange and media shaft with the mounting pin, and then attach the snap pin.
Loading Media
Initial Printer Settings
29

## Page 31

1
6
4
3
2
5
4.
Load the roll media onto the media flange.
Place the flange side of the media shaft at the bottom and load the roll media so that the media
feeds in the clockwise direction when viewed from above.
Media cannot be loaded correctly if the direction of the roll media is incorrect.
Install the roll media so there is no gap between it and the media flange.
To keep the printing result from being negatively affected, prevent contact with the media print surface as
much as possible.
MEMO
5.
Install the left media flange.
Install the media flange so there is no gap between it and the roll media.
Loading Media
30
 Initial Printer Settings

## Page 32

6.
Secure the left media flange in place.
Close the lock lever in the direction of the arrow to secure the left media flange in place.
7.
Load the roll media on the printer.
When loading the media, hold by the media flange to prevent contact with the media print surface.
IMPORTANT
(1) Align the stopper (
) with the guide (
).
(2) Press the left and right ends of the media shaft into the shaft holder until you hear a click.
Loading Media
Initial Printer Settings
31

## Page 33

Loading Media
32
 Initial Printer Settings

## Page 34

Fill the machine with ink and perform initial adjustment.
Step 1: Filling with Ink
Use BN2 Utility to operate the machine.
In this manual, BN2 Utility is referred to as "Utility."
Procedure
1.
Close the front cover.
2.
Turn on the main power switch.
3.
Press the sub power button.
When the sub power button indicator changes from flashing to steady, startup is finished.
After turning on the main power, wait some time before pressing the sub power button.
Firmware initialization starts when the main power is turned on, and there will be no response when pressing
the sub power button until initialization is complete.
MEMO
4.
Click the utility icon on the Roland DG Connect Hub home screen.
The sidebar is displayed on the right side of the home screen.
Ink Filling and Initial Adjustment
Initial Printer Settings
33

## Page 35

5.
Click [Open].
6.
When the Operation Guide window appears, click [Next].
7.
Select the type of ink being used for filling, and then click [Next].
A window appears with selections of the type of ink being used for filling.
The ink types displayed in the Utility window vary depending on the model.
IMPORTANT
If the current selection is correct, click [Next]. To change the selection, click [Back].
8.
Perform [Manual Cleaning before Initial Ink Filling].
To prevent discharging problems, perform cleaning before filling the machine with ink.
Ink Filling and Initial Adjustment
34
 Initial Printer Settings

## Page 36

[Manual Cleaning before Initial Ink Filling] is not necessary when filling with pigment ink.
MEMO
Ink filling begins after manual cleaning is performed twice.
Do not stop in the middle of the procedure.
If the main or sub power is turned off accidentally during initial ink filling, you will need to start over from
manual cleaning.
MEMO
• Never use any implements other than the included cleaning sticks.
Fabric or other lint-producing items may damage the heads.
• Use new cleaning sticks.
Reusing cleaning sticks may reduce print quality.
• Do not put used cleaning sticks in the cleaning liquid. Doing so will deteriorate the cleaning liquid.
• Never rub the nozzle surface of the heads.
IMPORTANT
Click [Next]. Proceed with the work by following the instructions in the Utility window.
9.
Insert the ink cartridge to fill the machine with ink.
Be sure to use an unused ink cartridge when filling the machine with ink.
IMPORTANT
Before inserting ink cartridges, shake each of them 50 times (about 20 seconds).
The precipitation of the ingredients in the ink disables printing in normal color. So that the ink mixes well,
shake the ink cartridge horizontally with a stroke length of around 5 cm (2 in.) from each end of the ink
cartridge.
IMPORTANT
Ink Filling and Initial Adjustment
Initial Printer Settings
35

## Page 37

Open the left cover and insert the ink cartridge with the same color as the ink label in the ink slot.
Insert the ink cartridge all the way until a beep is heard.
10.
When the [The ink tanks have been filled.] window appears, click [Next].
Ink Filling and Initial Adjustment
36
 Initial Printer Settings

## Page 38

Step 2: Loading Media
When [Load the media, and then make sure that the loading lever is lowered. Start setup.] is dis-
played, load the media while referring to the loading instructions for the media being used.
Perform printing tests and various adjustments. Load media that is at least 400 mm (15.75 in.) wide and 600 mm (23.63
in.) long.
IMPORTANT
• When using roll media
P. 37 Loading Roll Media
• When using sheet media
P. 42 Loading Sheet Media
Loading Roll Media
Use the following link to view a reference video for this procedure. We recommend that you view this video to
understand the overall flow of work.
https://vimeo.com/1003476339/5eb7f8a611
MEMO
Procedure
1.
Open the front cover.
2.
Move the right pinch roller (
) and the right media clamp (
) to the right end.
Press the part indicated by the arrow on the right pinch roller to move the roller and the right
media clamp together.
1
2
Ink Filling and Initial Adjustment
Initial Printer Settings
37

## Page 39

3.
Move the left pinch roller (
) and the left media clamp (
) to the left end.
Press the part indicated by the arrow on the left pinch roller to move the roller and the left media
clamp together.
1
2
4.
Use the following procedure to load the media.
(1) Pull out the media and load it from above the plate in front with the arrow stickers.
OK
(2) Pass the media (
) between the right grit roller (
) and right pinch roller (
).
If the left edge of the media is left of the left pinch roller, pass the media between the left grit roller
and left pinch roller as well.
MEMO
Ink Filling and Initial Adjustment
38
 Initial Printer Settings

## Page 40

1
2
3
(3) Pass the media (
) under the right media clamp (
), and pull it out about 20 cm (7.87 in.) from
the edge of the apron (
).
If the left edge of the media hits the left media clamp, pass the media under the left media clamp.
MEMO
You will hear a beep. Approximately 2 seconds later, you will hear two beeps, and then the suction
fan will activate. While this fan is operating, the position of the media will be maintained even if you
remove your hands from it.
MEMO
1
2
3
(4) Hold the media holder flange and take up about 20 cm (7.87 in.) of media.
Do not take up so much media (
) that the sensor (
) becomes visible.
MEMO
Ink Filling and Initial Adjustment
Initial Printer Settings
39

## Page 41

If you take up too much media, you will hear two short beeps and the suction fan will stop. If the media
comes off or is not straight, take up the media and redo the procedure from step 4.
2
1
5.
Place the left media clamp and the left pinch roller.
Place the left pinch roller (
) within the grit pattern (
).
Ensure that margin A from the left edge of the media to the left edge of the left pinch roller is at
least 10 mm (0.4 in.).
1
2
6.
Lower the loading lever.
7.
Line up the edges of the media with the centers of the holes of the left media clamp.
Ink Filling and Initial Adjustment
40
 Initial Printer Settings

## Page 42

8.
Close the front cover.
9.
Click [OK].
Ink Filling and Initial Adjustment
Initial Printer Settings
41

## Page 43

Loading Sheet Media
When loading sheet media in the machine, use the right edge of the media as a reference. This is because
the range of movement of the right pinch roller is fixed.
Place the media in a position where the following conditions are met and where media waste will be
minimized.
• Position of right edge of media
Within the right pinch roller movable range and where about 10 mm (0.39 in.) between the right roller
edge of the right pinch roller and the right edge of the media can be secured.
• Position of left edge of media
Where 10 mm (0.39 in.) or more between the left edge of the roller and the left edge of the media
can be secured when placing the left pinch roller within the range of the grit pattern.
Use the following link to view a reference video for this procedure. We recommend that you view this video to
understand the overall flow of work.
https://vimeo.com/1003475093/b41e56efdf
MEMO
Procedure
1.
Open the front cover.
2.
Move the right pinch roller (
) and the right media clamp (
) to the right end.
Press the part indicated by the arrow on the right pinch roller to move the roller and the right
media clamp together.
Ink Filling and Initial Adjustment
42
 Initial Printer Settings

## Page 44

1
2
3.
Move the left pinch roller (
) and the left media clamp (
) to the left end.
Press the part indicated by the arrow on the left pinch roller to move the roller and the left media
clamp together.
1
2
4.
Use the following procedure to load the media.
(1) Pass the media (
) under the right media clamp (
).
If the left edge of the media hits the left media clamp, pass the media under the left media clamp.
MEMO
Lifting the tip of the media clamp to pass the media through may cause the blade to come into contact
with the media. Be careful not to allow contact with the blade.
MEMO
2
1
(2) Pass the media (
) between the right grit roller (
) and right pinch roller (
) to the back.
Feed the media and line up the edge of the media with the edge of the apron (
).
Ink Filling and Initial Adjustment
Initial Printer Settings
43

## Page 45

If the left edge of the media is left of the left pinch roller, pass the media between the left grit roller
and left pinch roller as well.
MEMO
1
3
2
4
5.
Straighten the media.
OK
Not OK
6.
Press lightly on the media, and place the left media clamp and left pinch roller on the media.
Place the left pinch roller (
) within the grit pattern (
).
Ensure that margin A from the left edge of the media to the left edge of the left pinch roller is at
least 10 mm (0.4 in.).
1
2
Ink Filling and Initial Adjustment
44
 Initial Printer Settings

## Page 46

If at least 10 mm (0.4 in.) cannot be ensured for margin A from the left edge of the media to the left edge of
the left pinch roller, move the right pinch roller and the media to the left to provide the margin.
The range of motion of the right pinch roller is fixed. Place the right pinch roller within the movable range in
a position that ensures margin A from the right edge of the media to the right edge of the right pinch roller is
about 10 mm (0.39 in.).
A
MEMO
7.
Lower the loading lever.
8.
Line up the edges of the media with the centers of the holes of the left media clamp.
9.
Close the front cover.
10.
Click [OK].
Ink Filling and Initial Adjustment
Initial Printer Settings
45

## Page 47

Ink Filling and Initial Adjustment
46
 Initial Printer Settings

## Page 48

Step 3: Nozzle Drop-out Test
Check the print head ink discharge conditions.
Use the following link to view a reference video for this procedure. We recommend that you view this video to
understand the overall flow of work.
https://vimeo.com/1003475749/6df9f81a6c
MEMO
Procedure
1.
Click [Output].
Printing of the test pattern starts.
2.
Check whether there is dot drop-out or dot displacement in the test pattern.
Missing blocks indicate dot drop-out. Collapsed or inclined blocks indicate dot displacement.
• If there is no dot drop-out or dot displacement, click [OK].
• If dot drop-out or dot displacement is present, perform cleaning.
P. 56 Fixing Dot Drop-out and Dot Displacement
Ink Filling and Initial Adjustment
Initial Printer Settings
47

## Page 49

Step 4: Performing Automatic Correction
Automatically correct the media feed amount and ink landing position.
Procedure
1.
Click [OK].
A test pattern will be printed for automatic correction.
Automatic correction may not finish depending on the characteristics of media such as transparent media and
silver media with high light reflectance.
In these situations, click [Skip].
Clicking [Skip] applies the standard value.
MEMO
When correction is complete, the blade adjustment window will be displayed.
Ink Filling and Initial Adjustment
48
 Initial Printer Settings

## Page 50

Step 5: Blade Adjustment
Adjust the media cutting quality.
Use the following link to view a reference video for this procedure. We recommend that you view this video to
understand the overall flow of work.
https://vimeo.com/1003474895/208e3298e2
MEMO
Procedure
1.
Make sure the cutting tool is installed, and then click [Next].
If no cutting tool has been installed, install one.
Installing the Cutting Tool
2.
Click [Output].
A cutting test will be performed.
3.
Check the cutting results.
Check item
Result
Setting item
Adjustment
Check the shape.
The cut shape is distorted.
[Cutting Speed]
Reduce
Peel off the circle.
The square also peels off.
[Blade Force]
Increase
Some uncut areas remain.
[Cutting Speed]
Reduce
Ink Filling and Initial Adjustment
Initial Printer Settings
49

## Page 51

Check item
Result
Setting item
Adjustment
Peel off the square.
The blade leaves faint traces on the backing
paper.
[Cutting Speed]
No change
The blade trace is indistinct.
Increase
The blade trace is too deep and cuts into the
backing paper.
Reduce
Check the shape of the
square you have peel-
ed off.
The corners are not
rounded and do not
have "horns."
[Blade Offset]
No change
The corners are round-
ed.
Increase
The corners have
"horns."
Reduce
4.
Enter the value for the area to be changed.
For information on adjusting the amount of blade extension, refer to "Adjusting the Amount of
Blade Extension."
P. 54 Adjusting the Amount of Blade Extension
Cutting condition
Setting details
Default settings
[Blade Force]
Set the force (pressure) of the blade.
50 gf
[Cutting Speed]
Set the speed of cutting.
15 cm/s (5.91 in./s)
[Blade Offset]
Set the blade offset. Enter the listed
offset value for the blade.
The offset value for the included blade
is 0.250 mm (9.8 mil).
0.250 mm (0.010 in.)
[Rise Movement Speed]
Set the blade's up speed during cutting
(the speed at which the blade travels
when it moves to the next cutting line
after cutting one cutting line). If the
media comes loose during no-load feed
and the blade damages the surface of
the media, reduce the speed.
15 cm/s (5.91 in./s)
5.
Click [Apply].
6.
Continue adjusting the cutting conditions until the settings are optimized.
Repeat steps 2 to 6 to adjust the conditions.
Once adjustment is complete, click [OK].
Ink Filling and Initial Adjustment
50
 Initial Printer Settings

## Page 52

Step 6: Print & Cut Position Adjustment
Adjust any printing or cutting position misalignment.
Use the following link to view a reference video for this procedure. We recommend that you view this video to
understand the overall flow of work.
https://vimeo.com/1003475897/fd4a2d1bdd
MEMO
Procedure
1.
Click [Output 1].
The machine will print a test pattern and perform a cutting test.
2.
Check the results of [Output 1].
Check for misalignment between the printed square and cut square.
• Adjustment is not necessary if there is no misalignment. Click [OK] and proceed to step 9.
• If there is misalignment, proceed to step 3 to perform adjustment.
3.
Click [Output 2].
The machine will print a test pattern for adjustment and perform a cutting test.
4.
Check the results of [Output 2].
The point where the cutting line (A) intersects the correction-value scale (B) is the correction
value. In the following figure, the correction value is "−0.3."
Cutting will be performed along the red lines in the following figure. Peel the media from the backing paper
for checking.
MEMO
Ink Filling and Initial Adjustment
Initial Printer Settings
51

## Page 53

Check along the FEED (media feed direction) and SCAN (print-head carriage movement direction)
axes.
5.
Enter the correction values for the FEED (media feed direction) and SCAN (print-head carriage movement
direction) axes.
a. Enter the FEED (media feed direction) correction value as a new value for [Feed (F) Adjust-
ment Value].
b. Enter the SCAN (print-head carriage movement direction) correction value as a new value for
[Scan (S) Adjustment Value].
6.
Click [Apply].
7.
Click [Output 1].
The machine will print a test pattern for adjustment and perform a cutting test.
8.
Check the results of [Output 1].
If the printing and cutting lines are aligned, adjustment is complete. Click [OK].
If further adjustment is needed, repeat steps 3 to 8.
Default settings
• [Feed (F) Adjustment Value] (correction value of the media feed direction): 0.00 mm
• [Scan (S) Adjustment Value] (correction value of the print-head carriage movement direction): 0.00 mm
MEMO
9.
On the initial settings completion window, select whether to register the media being used.
• To register the media
Enter the media name, and then click [Yes].
Ink Filling and Initial Adjustment
52
 Initial Printer Settings

## Page 54

Enter a name to save the configured adjustment and correction values.
Registering the media makes it possible to set up the media without having to perform adjustment or
correction again when using the same media.
MEMO
The operation is complete once the following window is displayed.
• To continue without registering
Click [No].
The operation is complete once the following window is displayed.
Ink Filling and Initial Adjustment
Initial Printer Settings
53

## Page 55

Adjustment When Not Cutting the Backing Paper (Normal Cut)
When you want to perform accurate and fine adjustment of the cutting-in amount, such as when cutting
media with thin backing paper, you can obtain good results by adjusting the amount of blade extension
(
). Turn the cap portion of the blade holder to adjust the amount of blade extension. Each indicator tick
corresponds to 0.1 mm (3.9 mil), and adjustment for 0.5 mm (19.7 mil) can be made by rotating the cap
one full turn.
Note that making the amount of blade extension too small may cause the tip of the blade holder cap to
touch the printed surface, soiling and damaging it. It is important to be especially careful about this when
you are using media that has poor ink-adhesion properties.
The amount of blade extension (
) is 0 mm (
) at minimum and 2.5 mm (98.42 mil) (
) at maximum.
Set the amount of blade extension (
) to an amount that is the sum of the thickness of the media portion
(
) and half (
) the thickness of the backing paper (
).
Adjusting the Amount of Blade Extension
54
 Initial Printer Settings

## Page 56

Adjustment When Cutting the Backing Paper (Perforated Cut)
Perforated cut is used when you want to cut the backing paper, such as when you want to cut out the
printed part.
Perforated cut is a function provided only with the BN2-30.
This function specifies the perforation location in the print data and performs the cutting. It is different from the
perforated sheet cutting that cuts the backing paper at regular intervals when performing the sheet cutting that is used
when separating the media.
MEMO
Turn the cap portion of the blade holder to adjust the amount of blade extension. Each indicator tick
corresponds to 0.1 mm (3.9 mil), and adjustment for 0.5 mm (19.7 mil) can be made by rotating the cap
one full turn.
The amount of blade extension (
) is 0 mm (
) at minimum and 2.5 mm (98.42 mil) (
) at maximum.
Set the amount of blade extension (
) so that when the cutter pierces the media (
), the blade extends
slightly.
Pushing the blade out too far will damage the blade and blade protector and hasten their deterioration, so exercise
caution.
IMPORTANT
Adjusting the Amount of Blade Extension
Initial Printer Settings
55

## Page 57

Clean the print heads to improve ink discharge conditions such as dot drop-out and dot displacement.
Normal Cleaning
If the media has already been set up, the [After cleaning, perform a printing test] menu appears. When this is turned
on, a printing test is performed after cleaning.
MEMO
Procedure
1.
Select [Head Cleaning]>[Normal Cleaning].
2.
Click [Execute].
[Normal Cleaning] is executed.
3.
Click [Output].
Printing of the test pattern starts.
4.
Check whether there is dot drop-out or dot displacement in the test pattern.
• If there is no dot drop-out or dot displacement, click [OK] and proceed to Step 4: Performing
Automatic Correction.
• If the problem persists, try performing [Normal Cleaning] again.
If the problem persists even after performing [Normal Cleaning] two or three times, perform
[Medium Cleaning].
Fixing Dot Drop-out and Dot Displacement
56
 Initial Printer Settings

## Page 58

Medium Cleaning
If dot drop-out and dot displacement persist even after performing [Normal Cleaning], perform the more
forceful [Medium Cleaning].
If the media has already been set up, the [After cleaning, perform a printing test] menu appears. When this is turned
on, a printing test is performed after cleaning.
MEMO
Procedure
1.
Select [Head Cleaning]>[Medium Cleaning].
2.
Click [Execute].
[Medium Cleaning] is executed.
3.
Click [Output].
4.
Check whether there is dot drop-out or dot displacement in the test pattern.
• If there is no dot drop-out or dot displacement, click [OK] and proceed to Step 4: Performing
Automatic Correction.
• If the problem persists, try performing [Medium Cleaning] again.
If the problem persists even after performing [Medium Cleaning] two or three times, perform
[Powerful Cleaning].
Fixing Dot Drop-out and Dot Displacement
Initial Printer Settings
57

## Page 59

Powerful Cleaning
If dot drop-out and dot displacement persist even after performing [Medium Cleaning], perform the more
forceful [Powerful Cleaning].
If the media has already been set up, the [After cleaning, perform a printing test] menu appears. When this is turned
on, a printing test is performed after cleaning.
MEMO
Procedure
1.
Select [Head Cleaning]>[Powerful Cleaning].
2.
Click [Execute].
[Powerful Cleaning] is executed.
3.
Tap [Output].
4.
Check whether there is dot drop-out or dot displacement in the test pattern.
• If there is no dot drop-out or dot displacement, click [OK] and proceed to Step 4: Performing
Automatic Correction.
• If the problem persists, try performing [Powerful Cleaning] again.
If the problem persists even after performing [Powerful Cleaning] two or three times, perform
[Manual Cleaning].
Fixing Dot Drop-out and Dot Displacement
58
 Initial Printer Settings

## Page 60

Manual Cleaning
If dot drop-out and dot displacement persist even after performing [Powerful Cleaning], perform the
[Manual Cleaning].
Use the following link to view a reference video for this procedure. We recommend that you view this video to
understand the overall flow of work.
https://vimeo.com/1003475976/9d9107a314
MEMO
Procedure
1.
Remove any media.
2.
Click [Execute] next to Manual cleaning.
The print-head carriage moves to the left edge.
3.
Open the left cover.
4.
Follow the instructions in the Utility window to perform [Manual Cleaning].
Important notes on cleaning
• Use one cleaning stick per cleaning session, and then discard the stick after use. Reusing cleaning sticks
may reduce print quality.
• Never use any implements other than the included cleaning sticks.
• Do not put a cleaning stick that has been used for cleaning into the cleaning liquid. Doing so will deterio-
rate the cleaning liquid.
• Never rub the nozzle surface of the heads.
IMPORTANT
5.
When [Manual Cleaning] is complete, click [Finish All].
The nozzle drop-out test window appears.
Perform a nozzle drop-out test.
Fixing Dot Drop-out and Dot Displacement
Initial Printer Settings
59

## Page 61

Step 3: Nozzle Drop-out Test(P. 47)
Fixing Dot Drop-out and Dot Displacement
60
 Initial Printer Settings

## Page 62

_(no extractable text on this page)_
