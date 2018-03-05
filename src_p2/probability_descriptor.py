from probability_parser import *
import easygui as eg

file_path = eg.fileopenbox()
test_list =  probability_parser(file_path)
print(test_list)


def semantic_check(in_list) :

	nw_descr = []
	for i in in_list:
		if len(i[0]) == 1 :
			nw_descr.append([i[0][0], i[1], None]) 
	

	print( nw_descr )
	
def compact_form(in_list) :
	return None


semantic_check(test_list)