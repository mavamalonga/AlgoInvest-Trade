your_list = 'abcd'
complete_list = []
for current in range(4):
	a = [i for i in your_list]
	for y in range(current):
		a = [x+i for i in your_list for x in a if i not in x]
	complete_list = complete_list+a

# if i not in x



a = [1, 2, 3, 4, 5]

z = a.pop(0)
a.append(z)
print(a)
