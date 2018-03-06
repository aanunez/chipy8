https://tomassetti.me/parsing-in-python/#parseTree
https://github.com/antlr/grammars-v4/tree/master/python3-py
http://www.antlr.org/download.html


# chipy8
A (poorly designed) language for the Chip8

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
	VF is flag
	VA-VE are function inputs, may not be preserved
	V0-V9 are globals

Built-in "functions":
	print( "string" )
	foo = random( mask )
	draw( x, y, height )
	image( data )
	draw_sprite( x, y, width, height ) 
	foo = _ if _ else _

Keywords:
	clear
	return
	spin
	and
	or
	%
	&
	|
	=
	==
	!=
	>
	<
	>=
	<=
	+
		c = a + b
			LD Vc, Va
			ADD Vc, Vb
		c = a + N
			LD Vc, Va
			ADD Vc, N
		c = N + b
			LD Vc, Vb
			ADD Vc, N
		c = N + M
			LD Vc, N+M		
	-
	*
	/
	^
	++
	--
	+=
	-=
	>>
	<<
	not
	def
	if
	else
	while
	switch	
