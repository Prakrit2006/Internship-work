import numpy as np
import random as rnd
#Random matrix

random_matrix=np.random.randint(1,100,size=(3,3))
random_matrix2=np.array([[rnd.randint(0,10) for j in range(3)]for i in range(3)])
print(random_matrix)
print(random_matrix2)

#Column Sum & Row Sum
matrix_1=np.random.randint(1,100,size=(4,4))
print("The Matrix for col sum and row sum is\n",matrix_1)
column_sum=matrix_1.sum(axis=0)
print("Sum along colums is",column_sum)
row_sum=matrix_1.sum(axis=1)
print("Sum along rows is",row_sum)
mean_col=np.mean(matrix_1,axis=0)
mean_row=np.mean(matrix_1,axis=1,keepdims=True)
print("Mean along columns is",mean_col)
print("Mean along rows is\n",mean_row)

orignal_matrix=np.random.randint(1,100,size=(4,3))
print("The matrix to be transposed \n",orignal_matrix)
transposed_matrix=orignal_matrix.transpose()
transposed_matrix2=np.transpose(orignal_matrix)
print("Transposed matrix\n",transposed_matrix)
