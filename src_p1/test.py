from img_mat import *
import easygui as eg
from PIL import Image
from problem_solving import Problem
from graph_search import *

#file_path = eg.fileopenbox()
#print(file_path)
dimms = 150
arr = image_to_matrix("..\maps\lab1.bmp")
splt_arr = discrete_slicer(arr, dimms)
#print(splt_arr)
#print(np.shape(splt_arr))
#img = Image.fromarray(splt_arr, 'RGB')
#img.save('my.png')
#img.show()


#print(problem1.state)
#dfs = generic_graph_search(problem1, depth_first_search_criteria)

#print(dfs)

if not any(map(len, np.where(splt_arr == "S"))):
	print("Increase size")
else: 
	problem1 = Problem(splt_arr)
	dfs = generic_graph_search(problem1,  a_star1_search_criteria)

	for i in dfs[1:-1]:
		x = i[0]
		y = i[1]
		problem1.in_matrix[x,y] = '+'
			
	print('PATH COST: ')
	print(problem1.path_cost(dfs))
	print('Solution')
	#print(problem1.in_matrix)
	np.savetxt('solution.txt', problem1.in_matrix, fmt="%s")
	f = open('solution.txt', "r")
	text = f.readlines()
	f.close()
	eg.codebox("Solution of Search Algorithm", "Search Algorithm", text)

	