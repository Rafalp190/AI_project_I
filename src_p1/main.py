from img_mat import *
import easygui as eg
from PIL import Image
from problem_solving import Problem
from graph_search import *


executor = True
while executor:
	print("Welcome!")
	print("Choose an option")
	print("1. Depth First Search execution")
	print("2. Breadth First Search execution")
	print("3. A*: Hypotenuse Heuristic execution")
	print("4. A*: Sum of Cathetus Heuristic execution")
	print("5. Exit\n")

	option = input('Option: ') 
	img = ""
	arr = []
	splt_arr = []
	if option == "1" :
		img = eg.fileopenbox()
		dimms = input('Choose the dimensions of Discrete Matrix: ')
		try :
			dimms = int(dimms)
		except :
			dimms = input('The dimensions of Discrete Matrix must be a number! try again!: ')
		arr = image_to_matrix(img)
		splt_arr = discrete_slicer(arr, dimms)
		while not any(map(len, np.where(splt_arr == "S"))):
			print("Couldn't find a start point, please increase size")
			dimms = input('Choose the dimensions of Discrete Matrix: ')
			try :
				dimms = int(dimms)
			except :
				dimms = input('The dimensions of Discrete Matrix must be a number! try again!: ')
				dimms = int(dimms)
			arr = image_to_matrix(img)
			splt_arr = discrete_slicer(arr, dimms)
		else :
			problem1 = Problem(splt_arr)
			dfs = generic_graph_search(problem1,  depth_first_search_criteria)
			print("\nDepth First Search execution")
			print("________________________________")
			print("Path to solution:")
			if dfs == False:
				print("Couldn't find solution")
				print("________________________________\n")
				
			else:
				print(dfs)
				for i in dfs[1:-1]:
					x = i[0]
					y = i[1]
					problem1.in_matrix[x,y] = '+'
				print('PATH COST: ')
				print(problem1.path_cost(dfs))
				print("________________________________\n")
				np.savetxt('solution.txt', problem1.in_matrix, fmt="%s")
				f = open('solution.txt', "r")
				text = f.readlines()
				f.close()
				eg.codebox("Solution of Depth First Search Algorithm", "Search Algorithm", text)

	elif option == "2" :
		img = eg.fileopenbox()
		dimms = input('Choose the dimensions of Discrete Matrix: ')
		try :
			dimms = int(dimms)
		except :
			dimms = input('The dimensions of Discrete Matrix must be a number! try again!: ')
		arr = image_to_matrix(img)
		splt_arr = discrete_slicer(arr, dimms)
		while not any(map(len, np.where(splt_arr == "S"))):
			print("Couldn't find a start point, please increase size")
			dimms = input('Choose the dimensions of Discrete Matrix: ')
			try :
				dimms = int(dimms)
			except :
				dimms = input('The dimensions of Discrete Matrix must be a number! try again!: ')
				dimms = int(dimms)
			arr = image_to_matrix(img)
			splt_arr = discrete_slicer(arr, dimms)
		else :
			problem1 = Problem(splt_arr)
			bfs = generic_graph_search(problem1,  breadth_first_search_criteria)
			print("\nBreadth First Search execution\n")
			print("________________________________")
			print("Path to solution:")
			if bfs == False:
				print("Couldn't find solution")
				print("________________________________\n")
				
			else:
				print(bfs)
				for i in bfs[1:-1]:
					x = i[0]
					y = i[1]
					problem1.in_matrix[x,y] = '+'
				print('PATH COST: ')
				print(problem1.path_cost(bfs))
				print("________________________________\n")
				np.savetxt('solution.txt', problem1.in_matrix, fmt="%s")
				f = open('solution.txt', "r")
				text = f.readlines()
				f.close()
				eg.codebox("Solution of Breadth First Search Algorithm", "Search Algorithm", text)

	elif option == "3" :
		img = eg.fileopenbox()
		dimms = input('Choose the dimensions of Discrete Matrix: ')
		try :
			dimms = int(dimms)
		except :
			dimms = input('The dimensions of Discrete Matrix must be a number! try again!: ')
		arr = image_to_matrix(img)
		splt_arr = discrete_slicer(arr, dimms)
		while not any(map(len, np.where(splt_arr == "S"))):
			print("Couldn't find a start point, please increase size")
			dimms = input('Choose the dimensions of Discrete Matrix: ')
			try :
				dimms = int(dimms)
			except :
				dimms = input('The dimensions of Discrete Matrix must be a number! try again!: ')
				dimms = int(dimms)
			arr = image_to_matrix(img)
			splt_arr = discrete_slicer(arr, dimms)
		else :
			problem1 = Problem(splt_arr)
			as1s = generic_graph_search(problem1, a_star1_search_criteria)
			print("\nA*: Hypotenuse Heuristic execution\n")
			print("________________________________")
			print("Path to solution:")
			if as1s == False:
				print("Couldn't find solution")
				print("________________________________\n")
			else:
				print(as1s)
				for i in as1s[1:-1]:
					x = i[0]
					y = i[1]
					problem1.in_matrix[x,y] = '+'
				print('PATH COST: ')
				print(problem1.path_cost(as1s))
				print("________________________________\n")
				np.savetxt('solution.txt', problem1.in_matrix, fmt="%s")
				f = open('solution.txt', "r")
				text = f.readlines()
				f.close()
				eg.codebox("Solution of A*: Hypotenuse Heuristic Search Algorithm", "Search Algorithm", text)

	elif option == "4" :
		img = eg.fileopenbox()
		dimms = input('Choose the dimensions of Discrete Matrix: ')
		try :
			dimms = int(dimms)
		except :
			dimms = input('The dimensions of Discrete Matrix must be a number! try again!: ')
			dimms = int(dimms)
		arr = image_to_matrix(img)
		splt_arr = discrete_slicer(arr, dimms)
		while not any(map(len, np.where(splt_arr == "S"))):
			print("Couldn't find a start point, please increase size")
			dimms = input('Choose the dimensions of Discrete Matrix: ')
			try :
				dimms = int(dimms)
			except :
				dimms = input('The dimensions of Discrete Matrix must be a number! try again!: ')
				dimms = int(dimms)
			arr = image_to_matrix(img)
			splt_arr = discrete_slicer(arr, dimms)
		else :
			problem1 = Problem(splt_arr)
			as2s = generic_graph_search(problem1, a_star2_search_criteria)
			print("\nA*: Sum of Cathetus Heuristic execution\n")
			print("________________________________")
			print("Path to solution:")
			if as2s == False:
				print("Couldn't find solution")
				print("________________________________\n")
				
			else:
				print(as2s)
				for i in as2s[1:-1]:
					x = i[0]
					y = i[1]
					problem1.in_matrix[x,y] = '+'
				print('PATH COST: ')
				print(problem1.path_cost(as2s))
				print("________________________________\n")
				np.savetxt('solution.txt', problem1.in_matrix, fmt="%s")
				f = open('solution.txt', "r")
				text = f.readlines()
				f.close()
				eg.codebox("Solution of A*: Sum of Cathetus Heuristic Search Algorithm", "Search Algorithm", text)
	elif option == "5":
		print("Adios!")
		executor = False
	else:
		print("Insert a valid option")