from problem_solving import Problem
from random import randint
from math import sqrt
import numpy as np 
#Generic implementation of graph search
#@params: 
#problem: An instance of the problem framework
#remove_choice: function with path choice criteria
def generic_graph_search(problem, remove_choice):
	frontier = [[problem.state]]
	#print("frontier")
	#print(frontier)
	explored = set([])


	while True:
		if len(frontier):
			#print(len(frontier))
			path = remove_choice(frontier, problem)
			if path == None:
				return False
			#print(problem.in_matrix)
	#		print("path")
			#print(path)
			s = path[-1]
			#print(s)
			explored.add(s)
			#print("explored")
			#print(explored)
			if problem.goal_test(s):
				return path
			#print("actions")
			#print(problem.actions(s))
			#print(problem.in_matrix)

			
			for a in problem.actions(s):
				
				result = problem.result(s,a)
				#print("result")
				#print(result)
				#count = 0
				if result not in explored:
					#print("it checks")
					#count +=1
					#print("in hereee")
					#print(count)
					new_path = []
					new_path.extend(path)
						#print(new_path)
					new_path.append(problem.result(s, a))
						#print(new_path)
					frontier.append(new_path)
				


		else:
			return False
			
#Depth first implementation of the remove_choice function
#Chooses 1 path and sticks with it until the end
#Tie-breaker criteria for path choice left>right>down>up
def depth_first_search_criteria(frontier, problem):

	if len(frontier) == 1 : 
		path = frontier[0]
		frontier.remove(path)
	else :
		path = frontier[-1]
		frontier.remove(path)
		for i in frontier:
			if i[-1] == path[-1]:
				frontier.remove(i)

	return path

#Breadth first implementation of the remove_choice function
#Chooses 1 path and sticks with it until the end
#Tie-breaker criteria for node order choice up>down>left>right
def breadth_first_search_criteria(frontier, problem):
	if len(frontier) == 1 : 
		path = frontier[0]
		frontier.remove(path)
	else :
		path = frontier[0]
		frontier.remove(path)
		for i in frontier:
			if i[-1] == path[-1]:
				frontier.remove(i)
	return path

#A* implementation of the remove_choice function
#Chooses a path based on a heuristic function
#Heuristic: 
#-Straight line from current state to closest goal using the hypotenuse
#Tie-breaker criteria for node order choice up>down>left>right
def a_star1_search_criteria(frontier, problem):
	if len(frontier) == 1:
		path = frontier[0]
		frontier.remove(path)
	else : 
		where_out = np.where(problem.in_matrix == "G")
		if len(where_out[0]) == 0:
			return None
		goal_coords = []
		min_dist = 100000000
		min_path = []
		for i in range(len(where_out[0])) :
			goal_coords.append((where_out[0][i], where_out[1][i]))
		for i in frontier :
			#print(i)
			state = i[-1]
			for j in goal_coords :
				dist = sqrt(((j[0]-state[0])**2)+((j[1]-state[1])**2))
				if dist <= min_dist:
					min_dist = dist
					min_path = i
		path = min_path
		frontier.remove(path)
		for i in frontier:
			if i[-1] == path[-1]:
				frontier.remove(i)
	return path
#A* implementation of the remove_choice function
#Chooses a path based on a heuristic function
#Heuristic: 
#-Straight line from current state to closest goal using the sum of cathetus distance
#Tie-breaker criteria for node order choice up>down>left>right

def a_star2_search_criteria(frontier, problem):
	if len(frontier) == 1:
		path = frontier[0]
		frontier.remove(path)
	else : 
		where_out = np.where(problem.in_matrix == "G")
		if len(where_out[0]) == 0:
			return None
		goal_coords = []
		min_dist = 100000000
		min_path = []
		for i in range(len(where_out[0])) :
			goal_coords.append((where_out[0][i], where_out[1][i]))
		for i in frontier :
			#print(i)
			state = i[-1]
			for j in goal_coords :
				dist = sqrt(((j[0]-state[0])**2)) + sqrt(((j[1]-state[1])**2))
				#print(dist)
				if dist <= min_dist:
					min_dist = dist
					min_path = i
		path = min_path
		#print(path)
		frontier.remove(path)
		for i in frontier:
			if i[-1] == path[-1]:
				frontier.remove(i)
	return path

		
