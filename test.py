a, b, c = 1, 2, 3

def addsumma(a, b):
    summa = a+b
    return summa


# N faktorialni topish fungsiyasi

def faktorial(N):
    f, i = 1, 1
    for s in range(1,N+1):
        f = f*s
        
    return f
    
#print(faktorial(5))
#print(faktorial(6))
#print(faktorial(8))


#Linearga misol fungsiya

def son_top(s=10):
    for i in range(1,s+1):
        son = input(f"Siz o'ylagan son {i} y/n:")
        if son == 'y':
            return son
    return f'Vaqtimni olma'
#print(son_top())


#2
def linear_search(list, item):
    for n in range(len(list)):
        if list[n]==item:
            return n
    return None

myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
#print(linear_search(myList1,11))



# Binaryga misol
def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
# print(linear_search(myList1,11))
# print(binary_search(myList1,11))

# myList2 = [18,12,25,1,3,4,10,5,23,4,13,89]
# myList2.sort()
# print(linear_search(myList2,13))
# print(binary_search(myList2,13))

mevalar = ['olma','anor','olcha','behi','shaftoli','anjir']
mevalar.sort()
print(mevalar)
print(binary_search(mevalar,'shaftoli'))