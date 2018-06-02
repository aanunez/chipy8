# chipy8
A python-like language that compiles to Chip8 assembly.

Questions:

* Should Ld [I], Vx be used to store things to the stack, or should we instead devote VA-VE to function calls and make V0-V9 globals?
* What about arrays?
* Consider implementing without any function calls at all (to start)
* No way to take advantage of SUBN ?
* What to do with sknp and skp
* LD Vx, DT and LD DT, Vx
* LD Vx, Key
* Load BCD
* What to do with lines that have no assignment?
	
Rules:
	
* VF is flag
* VA-VE are function inputs, may not be preserved
* V0-V9 are globals

Built-in "functions":

* print( "string" )
* foo = random( mask )
* draw( x, y, height )
* image( data )
* draw_sprite( x, y, width, height ) 
* foo = x if y else z

Removed:

* Floats
* Long strings
* Decorators
* Power
* Imaginary numbers
* Matrix stuff
* Other stuff I forgot I took out


#### Reminders

    sudo apt install antlr4
    sudo pip3 install antlr4-python3-runtime

