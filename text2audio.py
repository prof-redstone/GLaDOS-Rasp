

import os
import sys 
import subprocess


def get_line():
	line = ''
	for i in range(1,len(sys.argv)):
		t = sys.argv[i]
		if t != "?" and t != "/" and t != "\\" and t != "°" :
			line = line + t + '-'		
	print(line)
	play_sound(line)


def play_sound(text):
	commande = 'cvlc --play-and-exit '
	url = 'http://192.168.1.101:8124/synthesize/'+'"'+text+'"'
	c = commande + url
	os.system(c)
	
get_line()
