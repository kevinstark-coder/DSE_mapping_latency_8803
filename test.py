# import numpy as np
# K= 5
# base = np.array([[0  ,1, -1],[2  ,3,  4],[5  ,6,  7],[-1 ,-1, -1],[-1 ,-1, -1],[8  ,9, -1],[10 ,11, -1],[12 ,13, 14 ]])
# base_c = np.array([[0,2,5],[1,3,6],[-1,4,7],[-1 ,-1, -1],[-1 ,-1, -1],[8,-1,-1],[9,11,13],[10,12,14]])

# div = int(K/5)
# re = K%5
# x= base.copy()
# row = np.array([[-1,-1,-1],[-1,-1,-1]])
# column = np.array([[-1],[-1],[-1]])
# cnt =1
# for i in range(0,div-1):
#     x = np.concatenate((x,row),axis=0)
#     mask = base != -1
#     base[mask] += 15
#     x = np.concatenate((x,base),axis=0)
#     cnt+=1
# y=[]
# mask = base != -1

# base[mask] += 15
# mask_c = base_c!= -1
# base_c[mask_c] += 15*cnt
# if re!=0:
#     x = np.concatenate((x,row),axis=0)
#     if re>3: #insertthe left 3 lock
#         x = np.concatenate((x,base[:3,:]),axis=0)
#         x = np.concatenate((x,row),axis=0)
#     index = re if re<4 else re+2
#     if re>3:
#         y = (base_c.T)[:,5:index+1]
#     else:
#         y = (base_c.T)[:,0:index]
#     z = 1 if (re>3) else (3-re)
#     while(z):
#         z-=1
#         y= np.concatenate((y,column),axis=1)
#     x = np.concatenate((x,y),axis=0)
# x = x[10:,:] if div==0 else x
# indices = np.where(x != -1)
# x[indices] = np.arange(np.count_nonzero(x != -1))


# print(x)
#-------------------------------------------B.2
import numpy as np
import math
# Calculate no. of cycles for 4 dataflows
# input stationary, output stationary, weight stationary, row stationary
# Account for tiling 
# Given, convolution operation for input size (X*Y), filter size (R*S), no. of. channels (C), no. of filters (K)
# Systolic array size (array_height * array_width)
# Complete the functions as per the instructions
# Assume no padding and strides = 1

class dataflow:
    def __init__(self, X, Y, R, S, C, K, array_height, array_width):

        self.X = X
        self.Y = Y
        
        self.R = R
        self.S = S

        self.C = C
        self.K = K

        self.array_height = array_height
        self.array_width = array_width


        self.rs_compute_cycles = 0
        self.ws_compute_cycles = 0
        self.is_compute_cycles = 0
        self.os_compute_cycles = 0

        

    # For row stationary, following parameters are constant
    # R = S = array_height = array_width = 3
    def row_stationary(self):

        # Write your code here
        
        return self.rs_compute_cycles
   
    def input_stationary(self):

        Sr = (self.R* self.S * self.C)
        Sc =  (self.X - self.R+1)*(self.Y - self.S+1)
        T =   self.K
        self.is_compute_cycles = (2*self.array_height+self.array_width+T-2)*\
                                (math.ceil(float(Sr/self.array_height))*math.ceil(float(Sc/self.array_width)))-1
        return self.is_compute_cycles
    

    def output_stationary(self):
        Sr = (self.X - self.R+1)*(self.Y - self.S+1)
        Sc = self.K
        T = (self.R* self.S *  self.C)
        self.os_compute_cycles = (self.array_height+self.array_width+T-2)*\
                                (math.ceil(float(Sr/self.array_height))*math.ceil(float(Sc/self.array_width)))-1
        return self.os_compute_cycles
    

    def weight_stationary(self):
        Sr = (self.R* self.S * self.C)
        Sc =  self.K
        T =   (self.X - self.R+1)*(self.Y - self.S+1)
        self.ws_compute_cycles = (2*self.array_height+self.array_width+T-2)*\
                                (math.ceil(float(Sr/self.array_height))*math.ceil(float(Sc/self.array_width)))-1
        return self.ws_compute_cycles
#X, Y, R, S, C, K, array_height, array_width):
# a= dataflow(40,30,5,5,3,6,4,4)
# a.input_stationary()
# a.weight_stationary()
# a.output_stationary()
# print("ws",a.ws_compute_cycles,"is",a.is_compute_cycles,"os",a.os_compute_cycles)