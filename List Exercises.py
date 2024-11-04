#1 Create a list of 5 of your favorite fruits. Print the list:
Fruits=['Apple' , 'Banana' , 'Mango' , 'Orange']
print(Fruits)

#2 Given the list colors = ['red', 'blue', 'green', 'yellow', 'purple'], print the first, third, and last color in the list: 
Colors=['red' ,'blue', 'green', 'yellow', 'purple']
print("First element:", Colors[0])
print("Third element:", Colors[2])
print("Last element:", Colors[-1])

#3  Create a list numbers with values [10, 20, 30, 40, 50]. Change the second item to 25 and add 60 to the end of the list. Print the modified list:

Numbers=['10', '20', '30', '40', '50']
Numbers[1] = "25"
Numbers.append(60)
print(Numbers)

#4 Using the list names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma'], create a new list subset containing only the first three names. Print subset:
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = (names[:3])
print(subset)

#5 Create a list of numbers from 1 to 10 and use a loop to print each number squared:
squares = [x**2 for x in range(1, 10)]
print(squares)

#6 Create an empty list called shopping_cart. Add the items 'milk', 'bread', and 'eggs' to it using the .append() method. Then use .extend() to add ['butter', 'cheese'] to the list. Print the final list:
Shopping_Cart=[]
Shopping_Cart.append('Milk')
Shopping_Cart.append('Bread')
Shopping_Cart.append('Eggs')
New_Cart= ['Butter', 'Cheese']
Shopping_Cart.extend(New_Cart)
print(Shopping_Cart)

#7 Write a program to find the maximum and minimum values in the list numbers = [45, 22, 88, 56, 92, 33]:
numbers=['45', '22', '88', '56', '92', '33']
print("Maximum Value:", max(numbers))
print("Minimum Value:", min(numbers))

#8 Given the list letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd'], count how many times the letter 'a' appears in the list:
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_of_a = letters.count('a')
print("Count of a:", count_of_a)

#9 Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list:
def squares(start, end):
	return [ n*n for n in range(start, end+1) ]
print(squares(0, 10)) 

#10 Given the list nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7], write a program to remove duplicates and print the unique elements only:
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = list(set(nums))
print(unique_nums)  