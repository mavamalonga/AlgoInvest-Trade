your_list = 'abcd'
complete_list = []
for current in range(4):
    a = [i for i in your_list]
    for y in range(current):
        a = [x+i for i in your_list for x in a]
    complete_list = complete_list+a
print(complete_list)