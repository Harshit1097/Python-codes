# calculate mean, median, mode

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

#mean
mean = sum(list1)/len(list1)
print(f"mean = {mean}")

# for median, sort the list
list1.sort()
print(f"sorted list: {list1}")

n = len(list1)
if n%2 == 0:
    median = (list1[n//2] + list1[(n//2)-1])/2
else:
    median = list1[(n+1)/2]
print(f"median = {median}")

# mode
dict = {}
for number in list1:
    dict.setdefault(number, 0)   # this statement adds element 0 against the key "number" in the dict
    dict[number] += 1

most_frequent = max(dict.values())    # finding the largest value in dict
for i,j in dict.items():
    if j == most_frequent:            # condition that fetched the key corresponding to the largest value in dict
        mode = i
print(f"mode = {mode}")
