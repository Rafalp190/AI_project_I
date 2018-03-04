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
			print(dfs)
			for i in dfs[1:-1]:
				x = i[0]
				y = i[1]
				problem1.in_matrix[x,y] = '+'
			print('PATH COST: ')
			print(problem1.path_cost(dfs))
			print("________________________________\n")

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
			print(bfs)
			for i in dfs[1:-1]:
				x = i[0]
				y = i[1]
				problem1.in_matrix[x,y] = '+'
			print('PATH COST: ')
			print(problem1.path_cost(bfs))
			print("________________________________\n")

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
			print(as1s)
			for i in dfs[1:-1]:
				x = i[0]
				y = i[1]
				problem1.in_matrix[x,y] = '+'
			print('PATH COST: ')
			print(problem1.path_cost(as1s))
			print("________________________________\n")

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
			print("\nA*: Hypotenuse Heuristic execution\n")
			print("________________________________")
			print("Path to solution:")
			print(as2s)
			for i in dfs[1:-1]:
				x = i[0]
				y = i[1]
				problem1.in_matrix[x,y] = '+'
			print('PATH COST: ')
			print(problem1.path_cost(as2s))
			print("________________________________\n")
	elif option == "5":
		print("Adios!")
		executor = False
	else:
		option = input('Insert a valid option: ')