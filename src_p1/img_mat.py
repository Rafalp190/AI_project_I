from scipy import misc, stats
import numpy as np 
from operator import add
from functools import reduce
from PIL import Image

#Function: Image to Matrix
#Convert a generic PNG or BMP into a numpy RGB ndarray
#@params image_path: Path of the image to convert
#@return: numpy_ndarray

def image_to_matrix( image_path ) :
    map_arr = misc.imread( image_path, mode = 'RGB' )
    return map_arr

#Function: Discrete Slicer
#Splits an array into N smaller arrays, calculates the RGB mean for each slice
#@params: nd_array: numpy RGB array, exp_dim: Expected resulting matrix dimensions
#@return: discrete_color_array

def discrete_slicer( 
	    nd_array, exp_dim ) :
	
	part_split = np.array_split(nd_array, exp_dim)
	split_arr = map(lambda x: np.array_split(x, exp_dim, axis= 1), part_split)
	split_arr = reduce(add, split_arr)

	mode_arr = map(lambda x: stats.mode(
		        np.array(list(
                    map(lambda y: stats.mode(y).mode, x)
                ))).mode,
			split_arr)

	mode_arr = np.array(list(mode_arr))
	mode_arr_squeezed = np.squeeze(mode_arr, axis=(1,2))
	int_arr = np.array(list(map(rgb_to_int , mode_arr_squeezed)))
		
	mode_arr_reshaped = np.reshape(int_arr, (exp_dim, exp_dim))

	int_matrix = np.matrix(mode_arr_reshaped)
	return int_matrix


def rgb_to_int(rgb_arr) :
	if int(np.mean(rgb_arr)) <= 20 :
		return "W"
	elif int(np.mean(rgb_arr)) >= 200 :
		return '-'
	elif rgb_arr[0] >= 200  and rgb_arr[1] <= 50 and rgb_arr[2] <= 50:	
		return 'S'
	elif rgb_arr[0] <= 50  and rgb_arr[1] >= 200 and rgb_arr[2] <= 50 :	
		return 'G'
	else :
		return '-'

def int_to_rgb(int_code) :
	#print(int_code)
	if int_code == "W" :
		return [0, 0, 0]
	elif int_code == '-' :
		return [255, 255, 255]
	elif int_code == 'S' :
		return [255, 0, 0]
	elif int_code == 'G' :
		return [0, 255, 0]
	elif int_code == '+' :
		return [255, 0, 255]


def repaint_image(in_matrix, dimms) :
	#print(in_matrix.flatten().tolist()[0])
	
	rgb_mat = list(map(int_to_rgb, in_matrix.flatten().tolist()[0]))
	expanded_rgb_mat = []
	for i in rgb_mat:
		#print(i)
		
		arr = np.repeat(i, 100)
		arr = np.reshape(arr, (10,10,3))
		
		print(arr)
		print("lone")
		expanded_rgb_mat.append(arr)
	#expanded_rgb_mat = np.reshape(expanded_rgb_mat,(dimms*100,dimms*100,3))
	#print(expanded_rgb_mat[0][0])
	#expanded_rgb_mat = np.vstack(expanded_rgb_mat)
	#expanded_rgb_mat = np.hstack(expanded_rgb_mat)
	#print(expanded_rgb_mat[0][0])
	#expanded_rgb_mat = np.reshape(expanded_rgb_mat, (dimms*100,dimms*100,3))
	print(np.shape(expanded_rgb_mat))
	

	return expanded_rgb_mat
	#print(np.shape(image_array))

	