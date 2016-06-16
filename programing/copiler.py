 #!/bin/python3
from sys import argv
import re

def multipleReplace(text, wordDict):
    for key in wordDict:
    	if key[0] == "$":
    		text = re.sub("\\"+key+"$", wordDict[key], text)
    	else:
        	text = re.sub(key, wordDict[key], text)
    return text

script, file = argv
code = open(file)
code = code.read().split('\n')

vars = 250
variaveis = {}
memory = [format(0, '04x')] * 256

# limpa e cria variaveis
for x in range(len(code)):
	code[x] = re.sub("\#.*", "", code[x])
	code[x] = re.sub("\t", "", code[x])
	if len(code[x]) >= 2 and code[x][0] == "$":
		get = re.match("(\$\w+)", code[x])
		if get:
			char = get.group(1)
			getn = re.match("\$\w+\s+(\d+)", code[x])
			n = 0
			if getn:
				n = getn.group(1)
			variaveis[char] = format(vars, '02x')
			memory[vars] = format(int(n), '04x')
			vars = vars - 1
		code[x] = ""

code = [x for x in code if x != '']

count = 0
references = {}
# limpa pulos
for x in range(len(code)):
	if len(code[x]) > 2 and code[x][:2] == "__":
		get = re.match("(\_\_\w+)", code[x])
		if get:
			char = get.group(1)
			references[char] = format(int(count), '02x')
		code[x] = ""
	else:
		count += 1
code = [x for x in code if x != '']

funcs1 = {
	"AC from":"0b",
	"AC to ":"0c",
	"if \<\= go":"34",
	"if \<\> go":"35",
	"if \! go":"35",
	"if \!\= go":"35",
	"if \> go":"36",
	"if \= go":"37",
	"if \=\= go":"37",
	"if \< go":"38",
	"if \>\= go":"39",
	"end": "4600",
	"AC \+": "15",
	"AC \-": "16",
	"AC \*": "17",
	"AC \/": "18",
	"AC \%": "19",
	"read": "1f",
	"print": "29",
	"null": "0000"
}

funcs2 = {
	"go": "1b"
}

for x in range(len(code)):
	code[x] = multipleReplace(code[x], references)
	code[x] = multipleReplace(code[x], variaveis)
	code[x] = multipleReplace(code[x], funcs1)
	code[x] = multipleReplace(code[x], funcs2)
	code[x] = re.sub("\s+", "", code[x])
	memory[x] = code[x]

print ("v2.0 raw")
for x in memory:
	print (x)

#print (variaveis)
