import os

# paths
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'data.txt')

# load data
with open(filename, "r") as file:
    depths = []
    for value in file:
        value = value.strip()
        depths.append(int(value))

# Part 1
single_counter = 0 
for i in range(len(depths)-1):
    if depths[i] < depths[i+1]:
        single_counter += 1
print(f"Single counter: {single_counter}")

# Part 2
triple_counter = 0
for i in range(len(depths)-3):
    sum1 = sum(depths[i:i+3])
    sum2 = sum(depths[i+1:i+4])
    if sum1 < sum2:
        triple_counter += 1
print(f"Triple counter: {triple_counter}")
