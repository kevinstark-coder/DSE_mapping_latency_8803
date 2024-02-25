from lab2A import mapper as mapper

# M and K can vary, but N is fixed as 3
M = 9
N = 3   ## WILL BE CONSTANT
K = 9
mapper = mapper(M, N, K)

# Create operand and demand matrices
mapper.create_filter_operand_mat()
mapper.create_filter_demand_mat()
# mapper.create_ifmap_demand_mat()

# Print mapping efficiency and compute cycles
print(mapper.get_avg_mapping_efficiency())
print(mapper.get_compute_cycles())