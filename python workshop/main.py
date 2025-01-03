.# # # # # # # # # # # higher order function
# # # # # # # # # # pi = 3.14

# # # # # # # # # # def area_circle(radius):
# # # # # # # # # #     radius = int(input("Enter Radius : "))
# # # # # # # # # #     return (pi*(radius)**2)

# # # # # # # # # # def perimeter_circle(radius):
# # # # # # # # # #     radius = int(input("Enter radius"))
# # # # # # # # # #     return(2*3.14*radius)

# # # # # # # # # # def area0_circle(radius):
# # # # # # # # # #     radius = int(input("Enter radius"))
# # # # # # # # # #     return(4/3*radius)

# # # # # # # # # # def perimeter_triangle(a,b,c):
# # # # # # # # # #     return (a+b)+h

# # # # # # # # # # def area_trianlge(b,h):
# # # # # # # # # #     return(1/2(b*h))

# # # # # # # # # # def main(func1,func2,func3,func4,func5):
    
# # # # # # # # # #     print("Area of circlr :-")
# # # # # # # # # #     print(func1())

# # # # # # # # # #     print("perimeter of circlr :-")
# # # # # # # # # #     print(func2)

# # # # # # # # # #     print("volume of sphere :-")
# # # # # # # # # #     print(func3)

# # # # # # # # # #     print("perimeter or triangle :-")
# # # # # # # # # #     print(func4)

# # # # # # # # # #     print("Area of triangle :-")
# # # # # # # # # #     print(func5)

# # # # # # # # # # main(area_circle,perimeter_circle,area_circle,perimeter_triangle,area_trianlge)    


# # # # # # # # # # list



# # # # # # # # # list1 = []
# # # # # # # # # list2 = list("Hella")
# # # # # # # # # list3 = []
# # # # # # # # # num = int(input("Enter the number"))
# # # # # # # # # lis3.appe


# # # # # # # # list1 = []
# # # # # # # # print("Enter the number one by one")

# # # # # # # # for i in range(10):
# # # # # # # #     item = int(input("Enter the number"))
# # # # # # # #     list1.append(item)

# # # # # # # # print("ENTER THE NUMBER YOU WANT TO COUNT")
# # # # # # # # c=int(input())
# # # # # # # # print(f"the number appeared {list1.count(c)} times")



# # # # # # # list1 = [1,10,23,45,2,7,0,3,4]

# # # # # # # list1.sort()
# # # # # # # print(list1[-1])

# # # # # # # print(list1[0])
                  
# # # # # # # list1 = [1,10,23,45,2,7,0,3,4]
# # # # # # # count_even = 0
# # # # # # # count_odd = 0
# # # # # # # for i in list1:
# # # # # # #     if i % 2==0:
# # # # # # #         count_even += 1
# # # # # # #     else:
# # # # # # #         count_odd += 1

# # # # # # # print(f"Even numbers in the list are : {count_even}")            
# # # # # # # print(f"Odd numbers in the list are : {count_odd}")            



# # # # # # list1 = [1,10,23,45,2,7,0,3,4]
# # # # # # def even_odd_count(list1):
# # # # # #     even=0
# # # # # #     odd=0
# # # # # #     for i in list1:
# # # # # #         if i % 2==0:
# # # # # #             even += 1
# # # # # #         else:
# # # # # #             odd += 1
# # # # # #     return even,odd 
# # # # # # even,odd = even_odd_count(list1)       
# # # # # # print(f"Even numbers in the list are : {even}")
# # # # # # print(f"Odd numbers in the list are : {odd}")


# # # # # # reverse string


# # # # # first_text = (input("Enter your string: "))
# # # # # text = first_text.split(" ")
# # # # # reverse_statement = []

# # # # # for word in text:
# # # # #     reverse = word[::-1]
# # # # #     reverse_statement.append(reverse)

# # # # # reverse_characters = ' '.join(reverse_statement)
# # # # # print(f"Your actual string was:- {text}")
# # # # # print(f"the reverse string is:- {reverse_characters}")

# # # # name = input("Enter the name of fruit : ")
# # # # quantity = input("Enter the quantity of fruit : ")
# # # # price = input("Enter the price of fruit : ")

# # # # fruits = {"Fruit_name":name,
# # # #         "fruit_quantity":quantity,
# # # #           "fruit_price":price}
# # # # print(fruits)



# # # item = []


# # # user = int(input("Enter the number of item :-"))
# # # for i in range(user):
# # #   item_name = input("Please enter the name :-")
# # #   item_price = input("Please enter the price :-")
# # #   item_quantity = input("Please enter the quantity:-")

# # # item_map = {"name":item_name,"price":item_price,"quantity":item_quantity}
# # # item.append(item_map)


# # # for i in item:
# # #   print(f"The item {i.get("name")} is of price {i.get("price")} and it's quantity is {i.get("quantity")}")
# # # print(item) 


# # from random import *
# # num= randint(1,20)
# # for i in range (5):
       
# #        user_num = int(input("ENTER ANY NUMBER OF YOUR CHOICE :- "))

# #        if (num == user_num):
# #               print("YOUR CHOICE WAS TRUE ")
# #               break
# #        elif num >user_num:
# #               print("OHH, THE NUMBER IS BIGGER THAN YOUR CHOICE ")

# #        elif num< user_num:
# #               print("YOUR CHOICE WAS SMALER THAN THE NUMBER")
# #        else:
# #               print("INVALID CHOICE")


# from random import randint 

# def levels():
#     print("""walcome to number guessing game!
#      choose your level:
#      1. Easy (1 to 10
#      2. medium (1 to 50)
#      3. hard (1 to 200)
#      4. impossible(1 to 6000)
#      5 EXIT""")
#      choice = int(input("Enter your level in number :"))
#      while Ture:
#           if choice == 5:
#             print("Bye")
#             break
#           if choice == 1:
#             num = randint(1,10)
#             return num
            
        

# num = 5

# factorial = 1

# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)



# def isPalindrome(s):
#     original_string = s.strip().lower()
#     return original_string == original_string[::-1]


# # Driver code
# s = "mmanglu"
# ans = isPalindrome(s)

# if ans:
#     print("Yes")
# else:
#     print("No")



# def pallindrome(string):
#     original_string = string.strip().lower()
#     reverse_string = original_string[::-1]

#     if original_string == reverse_string:
#         return True
#     else:
#         return False

# string = input("Enter your string :- ")
# result = pallindrome(string)

# if result:
#     print("pallindrome")
# else:
#     print("Not pallindrome")    


# GAME


# from random import choice

# # Rock,Paper,Scissor

# inputs = ["rock","paper","scissor"]
# # print(computer)
# c_score = 0
# p_score = 0
# chance = 0
# while chance <5:
#     computer = choice(inputs)
#     player = input("Enter your choice (rock,paper,scissor):-").lower()
#         #  conditions
#     if computer == player:
#             print("Both tied")
#             c_score += 5
#             p_score += 5
#             chance += 1 
#             # player conditions
#     elif player == "rock" and computer == "scissor":
#             print("player won")
#             p_score += 10
#             chance += 1   
#     elif player == "paper" and computer == "rock":
#             print("player won")
#             p_score += 10
#             chance += 1   
#     elif player == "scissor" and computer == "paper":
#             print("player won")
#             p_score += 10
#             chance += 1
#         # computer condition  

#     elif player == "scissor" and computer == "rock":
#         print("computer won")
#         p_score += 10
#         chance += 1   
#     elif player == "paper" and computer == "scissor":
#         print("computer won")
#         p_score += 10
#         chance += 1  
#     elif player == "rock" and computer == "paper":
#         print("computer won")
#         p_score += 10
#         chance += 1 
#     else:
#         print("invalid choice")
# else:
#     if p_score > c_score:
#       print("player won the match")          
#     elif p_score < c_score:
#         print("computer won the match")
#     else:
#         print("Both Tied")    




# # Dice rolling game 

# from random import choice

# faces = [1,2,3,4,5,6]

# def roll_dice(faces):
#     return choice(faces)
# def game():
#     turns = int(input("Enter your turns : "))
#     c_score = 0
#     p_score = 0
#     for _ in range(turns):
#         comp = roll_dice(faces)
#         play = roll_dice(faces)
#         print(f"Computer Dice : {comp} and player dice : {play}")

#         if comp > play:
#             print("computer won this round")
#             c_score += 10
#         elif comp == play:
#             print("both got same")
#         else:
#             print("player won this round")
#             p_score += 10  

#     if c_score == p_score:
#         print("BOTH GOT SAME POINTS")
#     elif p_score > c_score:
#         print("player won this match")
#     else:
#         print("computer won this match")
# game()




# cart = []


# def push(cart):
#     item = input("Enter the item tp add :-")
#     cart.append(item)

# def pop(cart):
#     if not cart:
#         print("cart is empty :-")
#     else:
#         cart.pop()

# def is_empty(cart):           
#     if not cart:
#        print("cart is empty")
#     else:
#         print("cart is not empty")   

# def peek(cart):
#     last_item = [-1]
#     print(f"the last item is :- "last item")

# def display(cart):
#         if not cart:
#             print("cart is empty!")
#         else:
#             print("cart")

# def main():
#     print("""choice :
#          1. add an item
#          2. remove an item
#          3. peek an item
#          4. display full cart
#          5. check cart if it is empty
#          6 exit""")
#     while true:
#         choice = int(input("Enter your choice")) 
#         if choice == 6:
#             print(" PROGRAM EXITED")
#             break
#         if choice ==1:
#             push(cart)
#         if choice ==2:
#             pop(cart)
#         if choice ==3:
#             peek(cart)
#         if choice ==4:
#             display(cart)
#         if choice ==5:
#             is_empty(cart)
            
            
 
# main()    


# Exception error



# def main():
#     tasks = []


#     while True:
#         print("\n===== To-Do List =====")
#         print("1. Add Task")
#         print("2. Show Tasks")
#         print("3. Mark Task as Done")
#         print("4. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             print()
#             n_tasks = int(input("How may task you want to add: "))
            
#             for i in range(n_tasks):
#                 task = input("Enter the task: ")
#                 tasks.append({"task": task, "done": False})
#                 print("Task added!")

#         elif choice == '2':
#             print("\nTasks:")
#             for index, task in enumerate(tasks):
#                 status = "Done" if task["done"] else "Not Done"
#                 print(f"{index + 1}. {task['task']} - {status}")

#         elif choice == '3':
#             task_index = int(input("Enter the task number to mark as done: ")) - 1
#             if 0 <= task_index < len(tasks):
#                 tasks[task_index]["done"] = True
#                 print("Task marked as done!")
#             else:
#                 print("Invalid task number.")

#         elif choice == '4':
#             print("Exiting the To-Do List.")
#             break

#         else:
#             print("Invalid choice. Please try again.")

#         if name == "main__":
#             main()
#         else:
#             pass




#  list comprehetion




# list1 = [1,2,3,454,5,6,567,8,78,4,43,53,67789,4]
# list2 = [item for item in list1 if item % 2 == 0] 

# print(list2)



# list3 = [x**3 for x in range(68) if x % 3 == 0]
# print(list3)



# map.filter


# list1 = []
# print("Enter the name you want to add :-")
# for _ in range(5):
#     name = input("Enter name : ")
#     list1.append(name)

# title = list(map(str.title,list1))
# print(title)





# list3 = [x for x in range(91)]
# triple = list(filter (lambda x : x % 3 ==0, list3))
# print(triple)





# def load_question():
#     return[
#         {"question 69 : ye konsa question hai ?",
#         "options :" ["1. 1","1. pehla","3. 69","4. first"]
#         "answer" : "3"},

#         {"question 2 : pichla question konsa tha ?",
#         "options :" ["1. pehla","2. 69", "3. pichla","4.69"]
#         "answer": "1"},

#         {"question 3 : AMROOD KITNE RUPAY KILO THE ?  ?",
#         "options ": ["1. 100", "2. 120", "3. 10000000" , "4. 7 crore"]
#         "answer": "2"}]        #      # Function to check if a number is prime 

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True



# str1 = [1,2,3,4,5,56,7,78,10]
# print(len(str1))
# filter = list(filter(is_prime,str1))


# print(filter)




# def is_prime(n):
#     count =0 
#     for i in range(1,n+1):
#         if n%i == 0:
#             count += 1
#     if count <3:
#         return True
#     else:
#         return False
# str1 = [x for x in range(31787)]
# filter1 = list(filter(is_prime,str1))
# double = list(map(lambda x: x**2,filter1))
# print(double)



# File handling

# file_name  = "python.txt"

# file = opne(file_name,"w")
# file.write("hye kajal")
# file.close()

# with open(file_name,'w')as file:
#     content = file.read()       
# print(content)


# data = [
#     ["Hello","hii"],
#     ["Python","java","Css"]
# ]    

# with open(file_name,'w')as file:
#     for i in data:
#         for i in range(len(i)):
#             file.write(f"item : {i[j]} | \n")    




# import csv

# data = [ ['NAME','AGE','CITY'],
#     ['JOHN',25,'NEW YORK'],
#     ['ALICE',30,'LOS ANGELES'],
#     ['BOB',35,'CHICAGO']
#     ]

# with open('python.csv', 'w', newline = '') as csvfile:
#     write = csv.writer(csvfile)
#     write.writerows(data)


# with open('python.csv','r') as csvfile:
#     reader = csv.reader(csvfile) 
#     for row in reader:
#         print(row)






# import csv

# data = [["CAKE"],
#     ['APPLE','ORANGE'],
#     ['DARK CHOCO','VANILLA'],
#     ['BLACK FOREST','BUTTERSCOTCH'],
#     ]

# with open('python.csv', 'w', newline = '') as csvfile:
#     write = csv.writer(csvfile)
#     write.writerows(data)


# with open('python.csv','r') as csvfile:
#     reader = csv.reader(csvfile) 
#     for row in reader:
#         print(row)










# import 

# BASE_FILE = "python.txt"

# student_detail = [{"Name":"pooja",
#                    "Marks":90},

#                    {"Name":"radhika",
#                     "Marks":80},
                    
#                    {"Name":"mohit",
#                     "Marks":99},
                    
#                    {"Name":"kajal",
#                     "Marks":89},
                    
#                    {"Name":"siya",
#                     "Marks":70},
                    
#                    {"Name":"mohan",
#                     "Marks":70},
                    
#                    ]

# # record_limit = int(input("Enter the number of record to enter :-"))
# # for _ in range(record_limit):
# #      name = input("Enter the name of student :- ")
# #      marks = int(input("Enter the marks of student :- "))
# #      student_detail.append({"name : ",name,"marks : ",marks})


# with open(BASE_FILE,'w') as file:
#     for item in data:
#         file.write("Name" : name,"Marks"=marks)
    
    

# import csv

# BASE_FILE = "python.csv"

# data = [["apple","orange","mango"],
#         ["apple","orange","mango"],
#         ["apple","orange","mango"],
#         ["apple","orange","mango"],
#         ]

# with open( BASE_FILE,'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)    

   



# import csv


# FILE1 = "python.csv"


# data = [["pista"],
#         ["apple"],
#         ["orange"],
#         ["dark"]
# ]


# with open(FILE1,'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)

# with open (FILE1,'r') as csvfile:
#     reader = csv.reader(csvfile)
#     print("cake")
#     print("_"*6) 
#     for row in reader:
#         for item in row:
#             print(item,"cake")  
#     print("_"*6)                 








# import json

# BASE_FILE = "python.json"

# data = [{"Name":"chiku"}
# {"Name":"golu"}
# {"Name":"maadho"}
# {"Name":"kaalu"}
# ]


# def save(data):
#     with open(BASE_FILE,'w') as jsonfile:
#         data = json.dump(data,jsonfile,indent=4)

# def load():
#     with open()        





# Homework


# import csv

# # Step 1: Create 2D lists
# girls_serials = [
#     ["Anne with an E", "Little Women", "Gilmore Girls", "Stranger Things"],
#     ["The Babysitters Club", "Heartland", "Once Upon a Time", "Wizards of Waverly Place"],
#     ["The Bold Type", "Charmed", "The Secret Life of the American Teenager", "Pretty Little Liars"],
#     ["Alexa & Katie", "Good Witch", "Nancy Drew", "Veronica Mars"]
# ]

# boys_cartoons = [
#     ["Dragon Ball Z", "Teen Titans", "Batman: The Animated Series", "Avatar: The Last Airbender"],
#     ["Ben 10", "Transformers", "Spider-Man: The Animated Series", "Justice League"],
#     ["Naruto", "One Piece", "Bleach", "Samurai Jack"],
#     ["Pokémon", "Beyblade", "Digimon", "Power Rangers"]
# ]

# # Step 2: Write lists to CSV files
# def write_to_csv(filename, data):
#     with open(filename, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)

# write_to_csv("Serial_names.csv", girls_serials)
# write_to_csv("Cartoon_names.csv", boys_cartoons)

# # Step 3: Read contents of CSV files
# def read_from_csv(filename):
#     with open(filename, mode='r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         return[row for row in reader]

# girls_data = read_from_csv("Serial_names.csv")
# boys_data = read_from_csv("Cartoon_names.csv")

# # Step 4: Display the contents in a more suitable way
# print("Girls' Serial Names:")
# for row in girls_data:
#     print(", ".join(row))

# print("\nBoys' Cartoon Names:")
# for row in boys_data:
#     print(", ".join(row)




# import sqlite3

# # connection with a database

# conn = sqlite3.connect("school.db")
# c = conn.cursor


# # creating a table

# c.execute(""" CREATE TABLE IF NOT EXISTS classes 
# (id INT,
# name TEXT,
# class INT,
# roll no. INT)
# """)

# user = int(input())



# import sqlite3




# def create_table():
#     conn = sqlite3.connect("school2.db")
#     c = conn.cursor()

#     c.execute("""CREATE TABLE IF NOT EXISTS class
#           (a_id INT,
#           name TEXT,
#           classs TEXT,
#           f_name TEXT)""")
#     conn.commit()
#     conn.close()



# def insert_value():
#     conn = sqlite3.connect("school2.db")
#     c = conn.cursor()

#     stu_info = []
#     limit = int(input("ENTER THE RECORDS YOU WANT TO INSERT : -"))
#     for _ in range(limit):
#         a_id = int(input("ENTER THE ADMINSSION ID OF THE STUDENT :- "))
#         name = input("ENTER THE NAME OF THE STUDENT :- ")
#         classs = input("ENTER THE CLASS OF THE STUDENT :- ")
#         f_name = input(" ENTER THE FATHER NAME OF STUDENT :- ")
    
#     stu_info.append((a_id, name, classs,f_name))
#     c.executemany("""
#     INSERT INTO class  VALUES (?,?,?,?)
#     """, stu_info)
#     conn.commit()
#     conn.close()

# def show_all():
#     conn = sqlite3.connect("school2.db")
#     c = conn.cursor()

#     c.execute("SELECT * FROM class")
#     data = c.fetchall()
#     for info in data:
#         print(f"Student ID: {info[0]}, Name: {info[1]}, CLASS: {info[2]}, FATHER'S NAME :- {info[3]}")
        
#     conn.commit()
#     conn.close()

# create_table()
# insert_value()
# show_all()



# classes.......


# class Dog:
#     def __init__(self):
#         self.name = "Raju"

#     def show_name(self):
#         print(f"The name is : {self.name}")
# Raju = Dog()
# Raju.show_name()         


# class employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def show_details(self):
#         print(f""" THE NAME OF THE EMPLOYEE IS :- {self.name}""")
    
    
# rahul = employee("JATIN",45,60000)
# rahul.show_details()

# import sqlite3

# def create_table():
#     conn = sqlite3.connect("patient.db")
#     c = conn.cursor()

#     c.execute("""CREATE TABLE IF NOT EXISTS patient
#           (patient_id INT,
#           name TEXT,
#           age INT,
#           disease TEXT,
#           attending_doctor TEXT,
#           ward_number INT)""")

#     conn.commit()
#     conn.close()
  

# def insert_value():
#     conn = sqlite3.connect("patient.db")
#     c = conn.cursor()

#     pat_info = []
#     limit = int(input("ENTER THE RECORDS YOU WANT TO INSERT :-"))
#     for _ in range(limit):
#         patient_id = int(input("ENTER THE PATIENT ID OF THE PATIENT :- "))
#         name = input("ENTER THE NAME OF THE PATIENT :- ")
#         age = int(input("ENTER THE AGE OF PATIENT :-" ))
#         disease = input("ENTER THE DISEASE OF PATIENT :- ")
#         attending_doctor = input(" ENTER THE ATTENDING DOCTOR and PATIENT :- ")
#         ward_number = input("ENTER THE WARD NUMBER OF PATIENT :-")
        
    
#     pat_info.append((patient_id, name, age,disease,attending_doctor,ward_number))
#     c.executemany("""
#     INSERT INTO patient  VALUES (?,?,?,?,?,?)
#     """, pat_info)
#     conn.commit()
#     conn.close()

    
# def show_all():
#     conn = sqlite3.connect("patient.db")
#     c = conn.cursor()

#     c.execute("SELECT * FROM patient")
#     data = c.fetchall()
#     for info in data:
#         print(f"Patient ID: {info[0]}, NAME: {info[1]}, AGE: {info[2]}, DISEASE :- {info[3]}, ATTENTING DOCTOR :- {info[4]}, WARD NUMBER :- {info[5]}, ")
        
#     conn.commit()
#     conn.close()

# create_table()
# insert_value()
# show_all()


# import sqlite3

# def initialize_db():
#     conn = sqlite3.connect('user.db')
#     c = conn.cursor()
#     c.execute("""CREATE TABLE IF NOT EXISTS users (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         username TEXT NOT NULL UNIQUE,
#                         password TEXT NOT NULL)""")
#     conn.commit()
#     conn.close()

# def is_legible(username, password):
#     if len(username) < 4:
#         print("Username must be at least 4 characters long.")
#         return False
#     if len(password) < 6:
#         print("Password must be at least 6 characters long.")
#         return False
#     return True

# def save_user(username, password):
#     try:
#         conn = sqlite3.connect('user.db')
#         c = conn.cursor()

#         c.execute("""INSERT INTO users (username, password) VALUES (?,?)
#         """, (username, password))
#         conn.commit()
#         print("User saved successfully!")
#     except sqlite3.IntegrityError:
#         print("Error: Username already exists.")
#     finally:
#         conn.close()

# def main():
#     initialize_db()
#     print("Please provide your credentials.")
#     username = input("Enter your username:- ")
#     password = input("Enter your password:- ")

#     if is_legible(username, password):
#         save_user(username, password)
#     else:
#         print("Invalid credentials. User not saved.")

# initialize_db()
# main()







# HOMEWORK

# import sqlite3

# conn = sqlite3.conn()





# """
# ENCAPSULATION
# -------------


# import sys
# import json

# class libraryManager:
#     def __init__(self):
#         self.filename = "libraryBooks.txt"
#         self.books.list = []
#         try:
#             with open(self.filename, 'r') as f:
#                 self.books_list = json.laod(f)
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.books_list = []

#         def save_books(self):
#             with open(self.filename, 'w') as f:
#                 json.dump(self.books_list,f,indent = 4)

#         def abb_books(self):
#             while True:
#                 try:
#                     author= input("Enter the name of the author of the book: ")

#                     genre= input("Enter the name of genre/category of the book")

#                     price= float(input("Enter the price of the book (in dollars)"))
                     
                    
                    
#                     self.books_list.append({"name": name, "author":})
#                     self.save_book()
#                     print(f"The book '{name}' added to the library recodes!")
#                     auther_book = input



# class LibraryManager:
#     def  remove_books(self):
#         while True:
#             try:
#                 num = int(input("Enter the number of books you want to remove"))
#                 if num > len(self.books_list):
#                     raise ValueError(f"Tnvalid number of books. there are on")

#                 for _ in range(num):
#                     name input("Enter the name of the book to remove:- ") 
#                     for book in self.books_list:
#                         if book["name"].lower() == name.lower():
#                             self.books_list.remove(book)
#                             self.save_books()
#                             print(f"The book '{name}' is remove successfully ") 
#                             break

#                     else:
#                         print(f"The book'{namr}' not fount in the library recodes")

#                 break










# import sys
# import json

# class libraryManager:
#     def __init__(self):
#         self.filename = "libraryBooks.txt"
#         self.books.list = []
#         try:
#             with open(self.filename, 'r') as f:
#                 self.books_list = json.laod(f)
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.books_list = []

#         def save_books(self):
#             with open(self.filename, 'w') as f:
#                 json.dump(self.books_list,f,indent = 4)

#         def abb_books(self):
#             while True:
#                 try:
#                     author= input("Enter the name of the author of the book: ")

#                     genre= input("Enter the name of genre/category of the book")

#                     price= float(input("Enter the price of the book (in dollars)"))
                     
                    
                    
#                     self.books_list.append({"name": name, "author":})
#                     self.save_book()
#                     print(f"The book '{name}' added to the library recodes!")
#                     auther_book = input



# class LibraryManager:
#     def  remove_books(self):
#         while True:
#             try:
#                 num = int(input("Enter the number of books you want to remove"))
#                 if num > len(self.books_list):
#                     raise ValueError(f"Tnvalid number of books. there are on")

#                 for _ in range(num):
#                     name input("Enter the name of the book to remove:- ") 
#                     for book in self.books_list:
#                         if book["name"].lower() == name.lower():
#                             self.books_list.remove(book)
#                             self.save_books()
#                             print(f"The book '{name}' is remove successfully ") 
#                             break

#                     else:
#                         print(f"The book'{namr}' not fount in the library recodes")

#                 break
