from classy import Classy

me = Classy()
me.addItem('hej')

if True:

	# Should be 0
	print(me.getClassiness())

	me.addItem("tophat")
	# Should be 2
	print(me.getClassiness())

	me.addItem("bowtie")
	me.addItem("jacket")
	me.addItem("monocle")
	# Should be 11
	print(me.getClassiness())

	me.addItem("bowtie")
	# Should be 15
	print(me.getClassiness())