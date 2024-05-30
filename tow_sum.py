#python3
#tow sum ---> index of tow sum
l = [5,2,9,7] 
target = 9

for index, value in enumerate(l):
    for i in range(index+1, len(l)):
        if value + l[i] == target:
            print(index,i)
