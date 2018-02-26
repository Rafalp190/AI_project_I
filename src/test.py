from img_mat import *
import easygui as eg
from PIL import Image
#file_path = eg.fileopenbox()
#print(file_path)
arr = image_to_matrix("..\maps\map1.py")
splt_arr = discrete_slicer(arr, 30)
print(splt_arr)
#print(np.shape(splt_arr))
#img = Image.fromarray(splt_arr, 'RGB')
#img.save('my.png')
#img.show()