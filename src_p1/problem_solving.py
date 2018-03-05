from abc import ABC, abstractmethod
import numpy as np

class AbstractProblem(ABC) :

	def __init__(self, in_matrix) :

		wherein = np.where(in_matrix == "S")
		
		x = wherein[0][0]
		y = wherein[1][0]
		self.state = (x,y)
		self.in_matrix = in_matrix
		super().__init__()

	@abstractmethod
	def actions(self, s) :
		"""Returns the list of actions for the state 's' """
		return 

	@abstractmethod
	def result(self, s,a) :
		"""Returns a new state after performing an action"""
		return

	@abstractmethod
	def goal_test(self, s) :
		"""Returns a Boolean if the state 's' is a positive goal test"""
		return

	@abstractmethod
	def step_cost(self, s, a , s_i) :
		"""Returns the cost of performing action 'a' over state 's' resulting in state 's_i'"""
		return

	@abstractmethod
	def path_cost(self, s_array) :
		"""Returns the cost of performing all the actions 's' in 's_array' """
		return


class Problem(AbstractProblem) :

	def actions(self, s) :
		"""Returns the list of actions for the state 's' """
		action_list = []
		x = s[0]
		y = s[1] 
		try :
			if self.in_matrix[x + 1, y] == '-' or self.in_matrix[x + 1, y] == 'G' :
			
				action_list.append('down')
		except IndexError :
			pass
		try :
			if (self.in_matrix[x - 1, y] == '-' or self.in_matrix[x-1, y] == 'G') and x - 1 != -1:

				action_list.append('up')
			else :
				pass
		except IndexError :
			pass
		try :
			if self.in_matrix[x, y + 1] == '-' or self.in_matrix[x, y + 1] == 'G' :

				action_list.append('right')
		except IndexError :
			pass
		try :
			if (self.in_matrix[x, y - 1] == '-' or self.in_matrix[x, y - 1] == 'G') and y - 1 != -1 :

				action_list.append('left')
			else :
				pass
		except IndexError :
			pass
		if len(action_list):	
			return action_list
		else:
			return None

	def result(self, s,a) :
		"""Returns a new state after performing an action"""
		x = s[0]
		y = s[1] 
		#self.in_matrix[x,y] = '.'
		if a == 'down' :
			return (x + 1, y) 
		elif a == 'up' :
			return  (x - 1, y)
		elif a == 'right' :
			return  (x, y + 1)
		elif a == 'left' :
			return  (x, y - 1)
		else: 
			return 0

	def goal_test(self, s) :
		"""Returns a Boolean if the state 's' is a positive goal test"""
		x = s[0]
		y = s[1] 
		if self.in_matrix[x, y] == 'G':
			return True
		else:
			return False

	def step_cost(self, s, a , s_i) :
		"""Returns the cost of performing action 'a' over state 's' resulting in state 's_i'"""
		action_cost = 1
		return action_cost

	def path_cost(self, s_array) :
		"""Returns the cost of performing all the actions in 's' in 's_array' """
		cost = len(s_array) - 1
		return cost


