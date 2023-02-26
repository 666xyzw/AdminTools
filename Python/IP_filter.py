#!/usr/bin/python3

"""
    This script is used to filter IP addresses from the SSH log files,
    IPs that have attempted to bruteforce their way into your servers.
    Thos IPs are compiled into a csv file, which can be later used to
    insert them into a firewall.

    Written by: xyz666

"""


import csv  #used to generate the csv files
import os   #used for listing files
import re   #used for regex


def open_file(file):

    """
    Function that parses the log files and puts each line into a separate
    list.
    """

    char_list=[]    # list of each separate character
    string_list=[]  # list of strings
    matrix=[]       # this will contain the the whole line


    with open(file,'r') as rf: 
        lines = rf.readlines()

        for line in lines:

            element=[]

            # goes through each character in the line
            for ch in line: 

                # the characters are added to the "element list"
                element.append(ch) 

                if ch=='\n':
                    
                    #if "ch" variable is at the end of the line then the list of "element" is put into "char_list" list
                    char_list.append(element) 

        for li in char_list: 

            st=[]

            for ch in li:

                st.append(ch)

                # if "ch" is a " " then
                if ch == ' ': 

                    # the previously parsed charcters are joined into a string
                    string_list.append(''.join(st))  
                    
                    # the list is emptied
                    st=[]

                # if "ch" is at the end of the line then
                if ch == '\n': 
                    
                    # the whole string list is added into the matrix list as a sub-list
                    matrix.append(string_list) 

                    # list is emptied
                    string_list = [] 

    return matrix

def ip_selector(matrix):

    """
    Selects the IP addresses from the given matrix
    """
    all_ip_list = [] # list of all the IP addresses
    
    for inside_list in matrix:
        
        for list_element in inside_list:
            
            #searches for the IP address with regex
            for nr in re.finditer('\d[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', list_element): 
                
                # if IP address is found it adds the IP address to the all_ip_list list
                all_ip_list.append(nr.group(0)) 

   
    ips=[] # list of IP addresses; does not contain duplicates

    for ip1 in all_ip_list:

        # checks if the current IP is already present in the new list; if not then
    	if ip1 not in ips: 
        
            ips.append(ip1)
            
    return ips


def ip_writer(list_of_main_ip_addresses):

    """
        Generates a csv file with the IPs from the last function
    """

    with open("ips.csv", 'w+') as csv_write:

        csv_write.write('IP\n')

        for element in list_of_main_ip_addresses:

            csv_write.write(element+'\n')

ip_writer(ip_selector(open_file("file_name")))
