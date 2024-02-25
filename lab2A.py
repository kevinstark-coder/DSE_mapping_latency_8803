import numpy as np

# Use wight stationary dataflow to multiply two operand matrices MxN and NxK using a 3x3 systolic array (size of each tile is 3x3)
# On the condition that one of the PE's MAC (first row, third column) is faulty (always outputs 0)
# Complete the functions as per the instructions
# N = 3 (fixed), M and K can vary

class mapper:
    def __init__(self, M, N, K):

        self.M = M
        self.N = N
        self.K = K

        # Use the following two constant parameters to complete the given functions 
        self.array_height = 3 # Height of the systolic array
        self.array_width = 3 # Width of the systolic array

        self.filter_operand_matrix = np.zeros((1,1))

        self.filter_demand_matrix = np.zeros((1,1))
        self.ifmap_demand_matrix = []

        self.compute_cycles = 0
        self.mapping_efficiency = 0

        

    # Your task is to create filter operand matrix of the shape NxK
    # Filter operand matrix is the matrix that contains addresses of the filter matrix and has the same size
    # Start filling your matrix with 0 and keep assigning +1 values to the next element in the same row
    # assuming the filter matrix is stored in row-major order
    # For example, if N = 3 and K = 2, create the matrix as
    # 0 1  
    # 2 3 
    # 4 5 
    def create_filter_operand_mat(self):

        # Write your code here

        x = np.linspace(0,self.N*self.K-1,self.N*self.K)
        x = x.reshape(self.N,self.K)
        self.filter_operand_matrix = x
   


    # Your task is to create self.filter_demand_matrix from filter operand matrix NxK 
    # Filter demand matrix conatins the tiles demanded by the systolic array from memory 
    # You need to create tiles as shown below. Refer to slides mentioned in part A2 of the pdf document
    # Use two rows of '-1' values to differntiate between tiles
    # For N = 6 and K = 2, the demand matrix will be a 8x3 matrix as shown below:



        
    def create_filter_demand_mat(self):
        base = np.array([[0  ,1, -1],[2  ,3,  4],[5  ,6,  7],[-1 ,-1, -1],[-1 ,-1, -1],[8  ,9, 10],[-1 ,11, 12],[-1 ,13, 14 ]])
        base_c = np.array([[0,2,5],[1,3,6],[-1,4,7],[-1 ,-1, -1],[-1 ,-1, -1],[8,-1,-1],[9,11,13],[10,12,14]])
        div = int(self.K/5)
        re = self.K%5
        x= base.copy()
        row = np.array([[-1,-1,-1],[-1,-1,-1]])
        column = np.array([[-1],[-1],[-1]])
        cnt =1
        for i in range(0,div-1):
            x = np.concatenate((x,row),axis=0)
            mask = base != -1
            base[mask] += 15
            x = np.concatenate((x,base),axis=0)
            cnt+=1
        y=[]
        mask = base != -1
        base[mask] += 15
        mask_c = base_c!= -1
        base_c[mask_c] += 15*cnt
        if re!=0:
            x = np.concatenate((x,row),axis=0)
            if re>3: #insertthe left 3 lock
                x = np.concatenate((x,base[:3,:]),axis=0)
                x = np.concatenate((x,row),axis=0)
            index = re if re<4 else re+2
            if re>3:
                y = (base_c.T)[:,5:index+1]
            else:
                y = (base_c.T)[:,0:index]
            z = 1 if (re>3) else (3-re)
            while(z):
                z-=1
                y= np.concatenate((y,column),axis=1)
            x = np.concatenate((x,y),axis=0)
        x = x[10:,:] if div==0 else x
        indices = np.where(x != -1)
        x[indices] = np.arange(np.count_nonzero(x != -1))

        self.filter_demand_matrix = x




    # Ifmap demand matrix in ideal case (no faulty PE) given is given below for M = 9 and K = 3, 
    # row 0: -1 -1 a8 a7 a6 a5 a4 a3 a2 a1  a0
    # row 1: -1 b8 b7 b6 b5 b4 b3 b2 b1 b0  -1
    # row 2: c8 c7 c6 c5 c4 c3 c2 c1 c0 -1  -1
    # These three rows will be stremed from left to right in the systolic array
    # In first cycle, a0 will be sent to the PE at first row, first column 
    # In second cycle, a1 will be sent to the PE at first row, first column 
    # In second cycle, b0 will be sent to the PE at second row, first column 
    # In thirs cycle, a2, b1 and c0 will be sent to PEs in first column 
    # and so on ...
    # Note N is fixed to 3 but M can vary. 
    # Since N is fixed, there is no tiling required in ifmap demand matrix
    # Note that in ideal case (no faulty PE), 2 filter tiles will be created for N = 3 and K = 6
    # For both tiles, same ifmap matrix is streamed from left to right
    # Use this to calculate number of cycles
    # You have full access of the control unit
    # You are free to use the entire ifmap demand matrix 
    # or you can use them in parts as per your mapping strategy
        
    def create_ifmap_demand_mat(self):
        self.ifmap_demand_matrix=[]
        lisa=["-1","-1"] #a
        len = self.M
        while(len):
            lisa.append(f'a{len-1}')
            len-=1

        len = self.M
        lisb=["-1"] #b
        while(len):
            lisb.append(f'a{len-1}')
            len-=1
        lisb.append("-1")
        
        lisc=[] 
        len = self.M
        while(len):
            lisc.append(f'a{len-1}')
            len-=1
        lisc.append("-1")
        lisc.append("-1")
        rows=[]
        rows+=[lisa,lisb,lisc]

        div = self.K/5
        re = self.K%5
        a = 1 if re<4 else 2
        num_tiles = div*2 + a
        while(num_tiles):
            self.ifmap_demand_matrix+[rows[0], rows[1], rows[2], '-1', '-1']
            num_tiles-=1
            if(not num_tiles):
               break
            self.ifmap_demand_matrix+[rows[2], rows[1], rows[0], '-1', '-1']
        self.ifmap_demand_matrix.pop()
        self.ifmap_demand_matrix.pop()

        # ideal case (no faulty PEs). You need to change this as per your mapping stategy
        
        # Two '-1' values has been used to differntiate between tiles
        

    # Don't change this function
    def get_filter_demand_mat(self):

        return self.filter_demand_matrix
    
    # Don't change this function
    def get_ifmap_demand_mat(self):

        return self.ifmap_demand_matrix

    # Your task is to calculate average mapping efficiency using filter demand matrix
    # If filters are stored in all the 8 non-faulty PEs, mapping efficieny will be 100%
    # If filters are stored in 6 out of the 8 non-faulty PEs, mapping efficieny will be 75%
    # Calculate mapping effiecieny for every tile and return the average value
    # Note: Mapping efficiency is independent of ifmap_demand_matrix
    def get_avg_mapping_efficiency(self):

        # Write your code here
        div = int(self.K/5)
        re = self.K%5
        a = 1 if re<4 else 2
        num_tiles = div*2 + a
        self.mapping_efficiency = float(self.K *3 / (num_tiles*8))
        return self.mapping_efficiency

    # Your task is to calculate compute_cycles using filter and ifmap demand matrices (can also use M, N and K values)
    # Assume 0 memory stalls: Memory stalls are basically the memory load latencies.
    # We are assuming that each demand by the systolic array is instantly met by the memory
    # Ignore the cycles for a tile of weights to drains out and a new tile of weights to fill in
    # Cycle starts when first input reaches the first PE and ends when 
    # final output partial product drains out of systolic array as happens in weight stationary dataflow
    def get_compute_cycles(self):
    
        # Write your code here
        div = int(self.K/5)
        re = self.K%5
        part = (self.M+4)*div*2
        if(re==0):
            self.compute_cycles = part
        elif(re<4):
            self.compute_cycles = part+ self.M+2+ re-1
        else:
            self.compute_cycles = part+ (self.M+4) + (self.M+3)
        return self.compute_cycles
