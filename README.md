# Remote Control with HDbitT

Protocol created to discribe and use the signals of remote controls
inside a python script with the HDbitT device. 

The control database is based on a dictionary architecture. Once you know
the signals hashs from the remote control, you store it inside a map with 
the equivalent keys.

The protocol itself use the dictionary to send signals from the keyboard to
the HDbitT device. The standard keys are:

+ volume_down
+ volumo_up
+ channel_down
+ channel_up
+ 0
+ 1
+ 2
+ 3
+ 4
+ 5
+ 6
+ 7
+ 8
+ 9

The current remote control available are:

* CR2FP (NET TV remote control)
* SKY HD TV
