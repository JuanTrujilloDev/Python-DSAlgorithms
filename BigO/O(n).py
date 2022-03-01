from time import process_time
nemo = ['nemo'] * 10000
t_start = process_time()

def findNemo(arr): #Linear time -> for each elements runs once
    for i in arr:
        if i == "nemo": print("Found nemo")

t_end = process_time()
findNemo(nemo)

print("Process, time: ", t_end - t_start)