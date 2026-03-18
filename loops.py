#Tasl 1 print numbers 1 to 10 using for loop
for i in range(1,11):
    
    print(i)

#Task 2 print even number from 1 to 20
for i in range(1,21):
      if i % 2 == 0:
            print(i)

            #or
for i in range(2,21,2):
      print(i)

#Task 3 print odd number from 1 to 15
for i in range(1,16,2):
    print(i)

# Task 4  print each charector from the string
text = 'python'
for char in text:
    print(char)

# # task 5 print all the items in the list
data = ["Data", "Science","AI"]
for items in data:
    print(items)

# # #task 6 find the sum of numbers from 1 to 10
total = 0
for i in range(1,11):
    total +=i
print("sum:",total)

# #task 7 print multiplication table of 5 
for i in range(1,11):
    print("5 x", i, "=", 5 * i)

# # task8 count how many vowels in the strin g
text = "hello world"
count = 0
for char in text:
    if char.lower() in "aeiou":
        count += 1
print(count)

#task 9 print the number in reverse order of 1 t0 10
for i in range(10,0,-1):
    print(i)

#task 10 print square of number from 1 to 5
for i in range(1,6):
    print( i *i)
    # #or
    # print(i ** 2)