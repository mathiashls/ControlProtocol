# Remote Control with HDbitT

Protocol created to discribe and use the signals of remote controls
inside a python script with the HDbitT device. 

Prerequisites:

* Python >= 2.6
* Twisted

The control database is based on a dictionary architecture. You can create your
own remote control model and store it inside the 'control_models' folder.
Once you know the signal's hashs from the remote control, store it inside a map
with the equivalent keys and time interval between signals (See 
'control_models/example').

The protocol have five basic methods:

+ volume_down()
+ volumo_up()
+ channel_down()
+ channel_up()
+ set_channel(channel_number): the 'channel_number' is an int or string with
any length (i.e.: 12, 345, 2)

The current remote control available are:

* CR2FP (NET TV remote control)
* SKY HD TV

PROTOCOL TESTING: The 'tc_test.py' file work with the HDbitT device and have the
host and port hard-coded inside de script. Edit the host variable with
your settings and it will work.
