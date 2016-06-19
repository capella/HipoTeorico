default:
	@echo "\033[0;31m------------------------ Imprimindo números de  0 a 100 -----------------------\033[0m"
	@make imprime100
	@echo "\033[0;31m------------------------ Realiza operações aritméticas ------------------------\033[0m"
	@make opera
	@echo "\033[0;31m------------------------ Fibonacci --------------------------------------------\033[0m"
	@make fibonacci

	

imprime100:
	python3 copiler.py imprime100.co > imprime100.cos
	java -jar ../../logisim.jar ../FDX.circ -tty tty -load imprime100.cos 1>&1 2>/dev/null

opera:
	python3 copiler.py opera.co > opera.cos
	echo "102 48" | java -jar ../../logisim.jar ../FDX.circ -tty tty -load opera.cos 1>&1 2>/dev/null
	echo "1000 0" | java -jar ../../logisim.jar ../FDX.circ -tty tty -load opera.cos 1>&1 2>/dev/null
	echo "42 42" | java -jar ../../logisim.jar ../FDX.circ -tty tty -load opera.cos 1>&1 2>/dev/null
	echo "1001 100" | java -jar ../../logisim.jar ../FDX.circ -tty tty -load opera.cos 1>&1 2>/dev/null
	echo "10 100" | java -jar ../../logisim.jar ../FDX.circ -tty tty -load opera.cos 1>&1 2>/dev/null

fibonacci:
	python3 copiler.py fibonacci.co > fibonacci.cos
	java -jar ../../logisim.jar ../FDX.circ -tty tty -load fibonacci.cos 1>&1 2>/dev/null
