#   USAGE:
#   submatrix(parent_matrix, sub_matrix_order) - for 2D square sub matrices from 2D parent matrix
#   submatrix(parent_matrix, (sub_matrix_row, sub_matrix_col)) - for 2D rectangular sub matrices
#   submatrix(parent, sub, p=True) - for printing 2D sub matrices seperated by new line

def submatrix(matrix, suborder, p=False):
	'''Returns all the 2D sub matrices from the 2D parent matrix'''
	final_res = []
	if type(suborder) != int:
	    sub_row = suborder[0]
	    sub_col = suborder[1]
	else:
	    sub_row, sub_col = suborder, suborder
	    
	mat_len = len(matrix)
	mat_row_len = len(matrix[0])
	for down_step in range(mat_len-sub_row+1):                                        #   sub matrix step down
	    for fwd_step in range(mat_row_len-sub_col+1):                                 #   sub matrix step right
	        temp = []
	        for iteration in range(sub_row):                                          #   sub matrix sweep vertically
	            temp.append(matrix[down_step+iteration][fwd_step:fwd_step+sub_col])   #   sub matrix sweep horizontally
	        final_res.append(temp)
	        if p == True:
	            for each in temp:
	                print(each)
	            print()
	return final_res
