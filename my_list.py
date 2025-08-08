#append numbers to a list
# This script appends numbers to a list
numbers = [10, 20, 30, 40]
print("Original list:", numbers)

#inserting a number at a specific position
numbers.insert(1, 15)
print("List after inserting 15 at the 2nd pos:", numbers)

#extending the list with another list
numbers_to_extend = [50, 60, 70]
numbers.extend(numbers_to_extend)
print("List after extending]:", numbers)   

#removing a number from the list
numbers.remove(70)
print("List after REMOVAL:", numbers)

#Arranging the list in ascending order  
numbers.sort()
print("sorted list:", numbers)

#finding and printing the index of a number
index_of_30 = numbers.index(30)
print("Index of 30:", index_of_30)