# Remote Control with HDbitT

Protocol created to discribe and use the signals of remote controls
inside a python script with the HDbitt device. 

The control_models folder have files that contains the codification of any
remote control that can be discribed. Just create a new ControlProtocol instance
with a valid control model and call it's methods to send the equivalent code
through the HDbitT device.

Supported flags:

* CHANNEL_UP
* CHANNEL_DOWN
* VOLUME_UP
* VOLUME_DOWN
* NUMBER_1
* NUMBER_2
* NUMBER_3
* NUMBER_4
* NUMBER_5
* NUMBER_6
* NUMBER_7
* NUMBER_8
* NUMBER_9
* NUMBER_0

Supported control models:

* CR2FP (NET TV)
