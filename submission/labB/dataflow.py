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
