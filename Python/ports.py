#!/usr/bin/python3

"""
	Python script that formats the newly downloaded, 'open_ports' file
	from a linux server. The file contains the output of 'netstat -tulpn'
	linux command.
	That data is formated so the 'differ.py' can understand it!
	By each run the script creates a new file called 'new_open_ports';
	in case the file already exists it will overwrite it!

	Writen by: xyz666

"""

import os


def open_file(test):

	first_part = []		#list that will hold the first part of the string
	second_part = []	#list that will hold the second part of the string
	new_line = []		#list that will hold the modified first part + second part of the string

	with open(test, 'r+') as rf:	#opens the file downloaded from the server
		lines = rf.readlines()		#reads the lines from the file


	#opening a new file and streaming the data into it
	with open("new_op", 'w') as wf:

		for line in lines:

			element = line.split("/")


			split1 = element[0].split(' ')

			#removeing the PID
			del split1[-1]				

			split2 = element[1].split(' ')


			if split2[-1] == '\n':
				del split2[-1]

			#appending the non-space characters to split1
			for e in split2:			
				if e != ' ':
					split1.append(e)

			#writing the outpur stream to the file
			for e in split1:			
				wf.write(e)
			wf.write('\n')

	with open("new_op", 'r') as rf:

		text = rf.readlines()

	#creating new output file 'new_open_ports'
	with open("new_open_ports", 'w') as wf:
		for e in text:

			#removing the " " from the beggining of the lines
			line = e.replace(" ", "")					

			wf.write(line)

	#removing the new_op file after finishing the process
	os.remove("new_op")


open_file("op-prod")