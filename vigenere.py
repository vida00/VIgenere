#!/bin/env python2

import argparse
from string import lowercase as lwc

args = argparse.ArgumentParser(description="Uma simples ferramenta que Cifra/Decifra vigenere - Coded by vida")
optional = args._action_groups.pop()
required = args.add_argument_group('required arguments')
args._action_groups.append(optional)
required.add_argument('-m', '--mode', help='Modes: Cifrar (cif) / Decifrar (dec)', required=True)
required.add_argument('-k', '--key', type=str, help='Passar a Key para cifrar/decifrar', required=True)
required.add_argument('-f', '--file', help='Passa o arquivo', required=True)
args.add_argument('-o', '--outfile', help='Output file', required=False)

myargs = args.parse_args()

#-----------------------#
# Variaveis
#-----------------------#
key = myargs.key.lower()
mode = myargs.mode
output = lambda data : open(myargs.outfile, 'w').write(str(data))
file =  open(myargs.file, 'r').read().lower()

def cifdec():
	result = ''
	keyindx = 0

	for line in file:
		if line in lwc:
			indx = lwc.find(line)
			if mode == "cif":
				indx += lwc.find(key[keyindx%len(key)]) # Aritmetica Modular
			elif mode == "dec":
				indx -= lwc.find(key[keyindx%len(key)])
			result += lwc[indx%26] # Aritmetica Modular
			keyindx += 1

		else:
			result += line

	if myargs.outfile:
		output(result)

	print "[+] Output: "+result,

if __name__ == "__main__":
	cifdec()
