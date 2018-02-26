from abc import ABC, abstractmethod
import numpy as np

class AbstractProblem(ABC) :

	def __init__(self, in_in_matrix) :
		x,y = np.where(in_in_matrix == "S")
		self.state = (x,y)
		self.in_in_matrix = in_in_matrix
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


def Problem(AbstractProblem) :
	def actions(self, s) :
		"""Returns the list of actions for the state 's' """
		action_list = []
		x = self.state[0]
		y = self.state[1] 
		try :
			if self.in_matrix[x + 1, y] == '-' or self.in_matrix[x + 1, y] == 'G' :
				action_list.append('right')
		except IndexError :
			pass
		try :
			if self.in_matrix[x - 1, y] == '-' or self.in_matrix[x-1, y] == 'G' :
				action_list.append('left')
		except IndexError :
			pass
		try :
			if self.in_matrix[x, y + 1] == '-' or self.in_matrix[x, y + 1] == 'G' :
				action_list.append('up')
		except IndexError :
			pass
		try :
			if self.in_matrix[x, y - 1] == '-' or self.in_matrix[x, y - 1] == 'G' :
				action_list.append('down')
		except IndexError :
			pass
		return action_list

	def result(self, s,a) :
		"""Returns a new state after performing an action"""
		x = s[0]
		y = s[1] 
		
		if a == 'right' :
			return (x + 1, y) 
		elif a == 'left' :
			return (x - 1, y)
		elif a == 'up' :
			return (x, y + 1)
		else :
			return (x, y - 1)

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
		action_cost = 0 
		if a in ['right', 'left', 'up', 'down'] :
			action_cost = (s_i[0] - s[0]) + (s_i[1] - s[1])
		return action_cost

	def path_cost(self, s_array) :
		"""Returns the cost of performing all the actions in 's' in 's_array' """
		cost = len(s_array) - 1
		return cost