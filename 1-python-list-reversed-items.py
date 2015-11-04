import time

count = 10**5

# add integers to list and then reverse
start = time.time()
nums = []

for i in range(count):
    nums.append(i)

nums.reverse()
elapsed = time.time() - start

print("append -> ", elapsed)

# add integers to list at the beginning
start = time.time()
nums = []

for i in range(count):
    nums.insert(0, i)

elapsed = time.time() - start

print("insert -> ", elapsed)
