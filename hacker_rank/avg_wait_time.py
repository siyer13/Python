lst = [5, 10, 15, 26, 34, 45, 54, 59]
diff = [x-y for x,y in zip(lst[::-1],lst[-2::-1])]
avg = sum(diff)/len(diff)
print(avg)
