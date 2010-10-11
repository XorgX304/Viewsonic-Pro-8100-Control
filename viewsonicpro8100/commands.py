#!/usr/bin/python

"""Command set for the Viewsonic 8100 Projector.

This file was automatically created by raw_commands_massager.py
from the source file: viewsonic_raw_commands.txt
Each command group in the documentation has a seperate list,
and all commands are available in ALL."""


######################
### Power
######################
POWER = [
  ("Power ON", "BEEF100500C6FF111101000100"),
  ("Power OFF", "BEEF02060057D02E0000000000"),
]
######################
### Source Select
######################
SOURCE_SELECT = [
  ("Computer ( Analog RGB 1)", "BEEF0206000BD2320000000000"),
  ("Component 1", "BEEF020600DAD3330000000000"),
  ("Component 2", "BEEF02060085DA5C0000000000"),
  ("S-Video", "BEEF0206006DD2340000000000"),
  ("Composite Video", "BEEF020600BCD3350000000000"),
  ("HDMI-1", "BEEF0206008FD3360000000000"),
  ("HDMI-2", "BEEF0206005ED2370000000000"),
]
######################
### KeyPad and IR
######################
KEYPAD_AND_IR = [
  ("Picture mode", "BEEF0206003BD9420000000000"),
  ("Color Temp", "BEEF020600EAD8430000000000"),
  ("Aspect Ratio", "BEEF0206005DD9440000000000"),
  ("Menu", "BEEF0206008CD8450000000000"),
  ("Exit", "BEEF020600BFD8460000000000"),
  ("Up", "BEEF0206006ED9470000000000"),
  ("Down", "BEEF02060091D9480000000000"),
  ("Left", "BEEF02060040D8490000000000"),
  ("Right", "BEEF02060073D84A0000000000"),
  ("PCS", "BEEF020600A2D94B0000000000"),
  ("Daylight Sensor", "BEEF02060015D84C0000000000"),
  ("Overscan", "BEEF020600C4D94D0000000000"),
  ("Black level", "BEEF020600F7D94E0000000000"),
  ("HQV", "BEEF02060026D84F0000000000"),
  ("Freeze", "BEEF02060049DA500000000000"),
  ("Input", "BEEF02060098DB510000000000"),
  ("V/H keystone", "BEEF020600ABDB520000000000"),
  ("Normal", "BEEF0206008ADF630000000000"),
  ("Anamorphic 1", "BEEF0206003DDE640000000000"),
  ("Anamorphic 2", "BEEF020600ECDF650000000000"),
  ("Picture Mode", "A11BEEF020600DFDF660000000000"),
  ("Cust 1", "BEEF0206000EDE670000000000"),
  ("Cust 2", "BEEF020600F1DE680000000000"),
]
######################
### Special
######################
SPECIAL = [
  ("Lens shift Right", "BEEF02060054DB5D0000000000"),
  ("Lens shift Left", "BEEF02060067DB5E0000000000"),
  ("Lens shift Up", "BEEF020600B6DA5F0000000000"),
  ("Lens shift Down", "BEEF020600B9DF600000000000"),
  ("Focus +", "BEEF020600E3DA5A0000000000"),
  ("Focus -", "BEEF02060032DB5B0000000000"),
  ("Zoom +", "BEEF02060068DE610000000000"),
  ("Zoom -", "BEEF0206005BDE620000000000"),
]
######################
### Data Get
######################
DATA_GET = [
  ("Error Code Get", "BEEF1A0C007A464F0001000000000000000000"),
  ("Filter Counter Get", "BEEF1A0C009193500001000000000000000000"),
  ("Temp Get", "BEEF1A0C00526E510001000000000000000000"),
  ("Lamp Life Get", "BEEF1A0C00566A520001000000000000000000"),
  ("Unit on time Get", "BEEF1A0C00898B5A0001000000000000000000"),
  ("Return", "1E"),
]

ALL = POWER + SOURCE_SELECT + KEYPAD_AND_IR + SPECIAL + DATA_GET
