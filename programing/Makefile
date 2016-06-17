imprime100:
	python3 copiler.py imprime100.co > imprime100.cos
	java -jar ../../logisim.jar ../FDX.circ -tty tty -load imprime100.cos 1>&1 2>/dev/null

opera:
	python3 copiler.py opera.co > opera.cos
	echo "102 48" | java -jar ../../logisim.jar ../FDX.circ -tty tty -load opera.cos 1>&1 2>/dev/null