#!/usr/bin/python3

"""
	Python script that compares a local copy of the 'netstat -tulpn' command  and the 'passwd' file
	from a linux server	with a new copy downloaded from the server.

	Used to check if the server has new open ports or new users on the server; if these ports/users
	appeared over night, then maybe your server is compromised! Check other logs too!

	Written by: xyz666
	
"""

def file_data_getter(file):
	
	""" Opens the file and  returns the content(s) of the file"""

	with open(file, 'r') as rf:
		return  rf.readlines()


def list_filler(orgbuffer, orglinenr, newbuffer, newlinenr):

	""" 
		Fills the smaller list of data with empty 'lines' so both list
		will be on the same level for the comparison
	"""

	nr = 0

	if orglinenr < newlinenr:

		print("Local copy shorter than the new copy!")
		print("\n")

		difference = newlinenr - orglinenr
	
		while nr < difference:
			orgbuffer.append('')
			nr += 1

		# adds the number of new empty lines to th rest of the line number
		orglinenr += nr							

	elif orglinenr > newlinenr:

		print("Local copy longer than the new copy!")
		print("\n")

		difference = orglinenr - newlinenr 
		
		while nr < difference:
			newbuffer.append('')
			nr += 1		
		
		# adds the number of new empty lines to th rest of the line number
		newlinenr += nr

	else:

		print("The two files are the SAME length! Nothing to do!")
		print("\n")

	return orgbuffer, orglinenr, newbuffer, newlinenr


def check_dictionary(file_buffer, match_dict):

	"""
		Runs a check on the dictionary that was created by the 'compare' method.
		It checks if every line from the file is found in the dictionary; if not
		then itt will be appended to the dict.
		and processed further.
	"""

	for line in file_buffer:

		if line not in match_dict:

			match_dict[line] = [0, 'not found']

	return match_dict


def compare(buffer1, buffer2):
	
	"""
		Takes the two buffers (the original file data and the new one)
		and compares the lines between them;
		If there is a match, then adds a token (value = 1) and the respective
		line to a list and that list is added into a dictionary as a value
		In case there is no match the 'f2line' gets to the end of the file
		then the token (value = 0) and the empty line is added to the
		list and the list to the dictionary.
	"""

	match_nr = 0								# counts the matching lines
	match_dict = {}								# dictionary containing the matching line as key and the token and matched line as vlues

	for f1line in buffer1:

		token = 0
		data_list = []							# list containing the token and matched line

		for f2line in buffer2:
			
			if f2line == f1line:

				match_nr += 1
				token = 1

				# print(match_nr, f1line)

				data_list.append(token)
				data_list.append(f2line)

				match_dict[f1line] = data_list

			if ((f2line == '') and (token == 0)):

				data_list.append(token)
				data_list.append(f2line)

				match_dict[f1line] = data_list

	return match_nr, match_dict


def status(original_file, new_file, biggest_line_nr, matched_line_nrs, matched_line_dict):

	"""
		Method that takes all the information from the other methods and
		compiles them into messages that are returned on the screen.
	"""


	name = original_file.split('-')					#splitting the name in two

	#checking the passwd files
	if name[0] == "passwd":

		if ((name[1] == "prod") or (name[1] == "dev") or (name[1] == "cli")):

			if matched_line_nrs == biggest_line_nr:
			
				print("All Lines match from the ", original_file, " File!")
			
			else:
			
				print("Only ", matched_line_nrs, " lines, form ", original_file, " file, matched of ", biggest_line_nr, 
					"lines from ", new_file)

				for key in matched_line_dict:

					values = matched_line_dict[key]

					if values[0] == 0:

						print(key, " -> ", values[0])


	#checking the port files
	if name[0] == "open_ports":

		if ((name[1] == "prod") or (name[1] == "dev") or (name[1] == "cli")):

			if matched_line_nrs == biggest_line_nr:
			
				print("All Lines match from the ", original_file, " File!")

			else:

				print("Only ", matched_line_nrs, " lines, form ", original_file, " file, matched of ", biggest_line_nr, 
					"lines from ", new_file)

				for key in matched_line_dict:

					values = matched_line_dict[key]

					if values[0] == 0:

						print(key, " -> ", values)


def main(original, new):

	#opens the original file and reads it content into the buffer
	original_buffer = file_data_getter(original)

	#calculates the number of non-empty lines in the original file
	org_line_nr = len(original_buffer)

	#opens the newly processed file and reads it content into the buffer
	new_buffer = file_data_getter(new)

	#calculates the number of non-empty lines in the new file
	new_line_nr = len(new_buffer)

	# updates the two lists
	(updated_original_buffer, updated_org_line_nr, updated_new_buffer, updated_new_line_nr) = list_filler(original_buffer, org_line_nr, new_buffer, new_line_nr)

	
	if org_line_nr >= new_line_nr:

		(matched_nrs, matched_lines) = compare(original_buffer, new_buffer)

		checked_dict = check_dictionary(updated_original_buffer, matched_lines)

		status(original, new, org_line_nr, matched_nrs, checked_dict)

	else: 

		(matched_nrs, matched_lines) = compare(new_buffer, original_buffer)

		checked_dict = check_dictionary(updated_new_buffer, matched_lines)		

		status(original, new, new_line_nr, matched_nrs, checked_dict)
	
if __name__ == '__main__':

	# main("open_ports-prod", "new_open_ports")		#compares the processed file with the local file
	# main("passwd-cli", "pwd-cli")					#compares the processed file with the local files
