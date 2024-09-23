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

#myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
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

#mevalar = ['olma','anor','olcha','behi','shaftoli','anjir']
#mevalar.sort()
#print(mevalar)
#print(binary_search(mevalar,'shaftoli'))


class Node:
    """Tugun (node) obyekti"""
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    """Linked List obyekti"""
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def push(self,new_data):
        """List boshiga tugun qo'shish"""
        # Yangi node yaratamiz
        new_node = Node(new_data)
        # List boshini keyingi o'ringa suramiz
        new_node.next = self.head
        # Yangi nodeni list boshiga qo'yamiz
        self.head = new_node
        
    def insertAfter(self,prev_node, new_data):
        """O'rtasiga tugun qo'shish"""
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        # Yangi tugun qo'shamiz
        new_node = Node(new_data)
        # Yangi tugunni keyingi tugunga bog'laymiz
        new_node.next = prev_node.next
        # Avvalgi tugunni yangi tugunga bog'laymiz
        prev_node.next = new_node
    
    def append(self, new_data):
        """List oxiriga tugun qo'shish"""
        # Yangi tugun yaratamiz
        new_node = Node(new_data)
        # List bo'sh emasligini tekshriamiz
        if self.head is None:
            # Bo'sh bo'lsa yangi tugun list boshiga tushadi
            self.head = new_node
            return
        # Aks holda List oxiriga boramiz
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def deleteNode(self,key):
        """Listdan qiymat o'chirish"""
        # List boshini topib olamiz
        temp = self.head
        # Birinchi tugunni tekshiramiz
        if (temp and temp.data == key):
            self.head = temp.next
            temp = None
            return
        # Aks holda keyingi tugunlarni qarab chiqamiz
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # Agar qiymat topilmasa
        if temp==None:
            return
        # Tugunni listdan o'chiramiz
        prev.next = temp.next
        temp = None
        
        
        
#dushanba = LinkedList()
#dushanba.head = Node('Dushanba')
#seshanba = Node("Seshanba")
#chorshanba = Node('Chorshanba')

#dushanba.head.next = seshanba
#seshanba.next = chorshanba
#print(seshanba.next.data)
        

# selection sort 
def findMax(array):
    max = array[0]
    max_index = 0
    for n in range(1,len(array)):
        if array[n]>max:
            max = array[n]
            max_index = n
    return max_index

def selectSort(array):
    newArray = []
    for n in range(len(array)):
        max_index = findMax(array)
        newArray.append(array.pop(max_index))
    return newArray

array = [3, 4, 1, 6, 10, 20, 9, 8]
#newArray = selectSort(array)
#print(newArray)


#Recursion fungsiya
def fact(x):
    print(x,end=' ')
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

#print(fact(5))

def sum(list):
    if list == []:
        return 0
    return list[0]+sum(list[1:])


son = [1,2,3,45,6,7,8]
#print(sum(son))


# Quick sort

from random import randrange

def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list.pop(randrange(len(list)))
        kichik = [ i for i in list if i < pivot ]
        katta = [i for i in list if i > pivot]
        return quick_sort(kichik) + [pivot] + quick_sort(katta)
    
    
list = [21,324,11.2143,45]
#print(quick_sort(list))

# Bubble sort

def bubbleSort(array: list):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)
                
                
                
array = [32,53,22,55,432,31]
bubbleSort(array)