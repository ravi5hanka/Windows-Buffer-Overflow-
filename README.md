# Windows-Buffer-Overflow
Scripts and programs used in exploiting Windows-Based Buffer Overflow

The walkthrough is published here,

Needed tools can be downloaded via following links,
Immunity Debugger (https://www.immunityinc.com/products/debugger/)
Vulnserver (https://github.com/stephenbradshaw/vulnserver)

Spiking scripts and fuzzing python program are here.
STATS spiking script - STATS.spk ,
TRUN spiking script - TRUN.spk ,
Python fuzzing program - fuzzing.py

generic_send_tcp command,
generic_send_tcp <victim IP> <victim port> spikeFile.spk 0 0

Making python program executable,
chmod +x fuzzing.py

Running python program,
./fuzzing.py


