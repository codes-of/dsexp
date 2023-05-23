from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define the array to be summed
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calculate the local sum of the elements
local_sum = np.sum(arr[rank::size])

# Reduce the local sums to obtain the global sum
global_sum = comm.allreduce(local_sum, op=MPI.SUM)

# Print the result
if rank == 0:
    print("The sum of the elements in the array is:", global_sum)
