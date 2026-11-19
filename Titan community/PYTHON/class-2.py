#Arithmetic operators-are used to perform calculations on numbers
x = 12
y = 5
print(x + y)#Addition
print(x - y)#subtraction
print(x * y)#Multiplication
print(x / y)#Division
print(x ** y)#Exponential
print(x // y)#Floor division
#print(x #modulus sign y)
#Comparison operators
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)#not equal to

#Assignment operators - are used to assign values to variables
a = 5
b = 10
print(a)
print(b)

#Membership operators - are used to check if a value is a member of a particular group(list,tuple,e.t.c)
score = {10, 15, 25, 26, 70}
print(5 in score)
#Not in
score = {10, 15, 25, 26, 70}
print(5 not in score)

#String formatting -  Format method,f-string method
name = "daniel"
age = 12
print("My name is",name,"and i will be celebrating my",age,"th birthday in december")
#String formatting - Format method
print("My name is {} and i will be celebrating my {}th birthday in december".format(name,age))
#string formatting using f-string method
print(f"My name is {name} and i will be celebrating my {age}th birthday in december")

name = "Precious"
day = 31
month = "december"
print("My friend's name is {}, she wil be travelling to Abk on the {}st of {}".format(name,day,month))
print(f"My friend's name is {name}, she will be travelling to Abk on the {day}st of {month}")

name = "Wura"
position = 2
print("Congratulations, the {}nd position will be going to {}".format(position,name))
print(f"Congratulations, the {position}nd position will be going to {name}")

vacation = 3
print("I am so excited, this is my {}rd vacation in this year".format(vacation))
print(f"I am so excited, this is my {vacation}rd vacation this year")

school = "Aptech software engineering school"
comment = "is the best IT school in Nigeria"
print(school + comment)
first_name = "Olaifa"
last_name = " Daniel"
full_name = first_name + last_name
print(full_name)
#Repitition - to repeat a string multiple times using * operator
print(school*5)
#SLicing and Indexing - to extract or access a part of a string using index number
print(school[7:15])
name = {"ife", "tolu", "titi"}
school = "Aptech software engineering school"
comment = "is the best IT school in Nigeria "
print(comment[25:32])
print(school[16:27])

#STRING METHODS
statement = "I love bread and beans"
print(dir(statement))
print(statement.upper())
print(statement.upper())
print(statement.capitalize())#capitalize will make the first letter of the word in your string in caps
print(statement.title())#capitalize will make every of the first letter of the word in your string in caps
sentence = " My name is Ife "
print(sentence.strip())#TO REMOVE SPACES AT THE BEGINNING OF THE WORD
print(statement.split())#TO SPLIT A STRING (TURNS INTO A LIST)
print(sentence.replace("IFE", "Aishat"))

#.join - to concatenate a list(TURNS INTO A STRING)
full_name = ["DANIEL", "OLAIFA"]
print(" ".join(full_name))
#.Find to locate a word in a string
string = "I love python"
print(string.find("python"))
print("python" in string)
#startswith - to locate the word that begins a string
print(string.startswith("python"))
print(string.endswith("python"))
print(string.center(30))
print(string.count("o"))
#COLLECTION TYPE
Zoo = ["Lion", "Tiger", "Chicken", "Rabbit", "Girrafe"]
print(dir(Zoo))
Zoo.append("Peacock")#to add to a list
print(Zoo)
Zoo.append("Zebra")
print(Zoo)
#Insert-add a value to a specific position
Zoo.insert(1, "Pig")
print(Zoo)
Zoo.insert(4, "Monkey")
print(Zoo)
Zoo[0] = "Dog"
print(Zoo)
Zoo.remove("Chicken")#remove a value from a list
print(Zoo)
Zoo.pop(-4) #remove a value from a list(using index number)
print(Zoo)
Zoo.sort()#ascending order
print(Zoo)
print(Zoo)
Zoo.reverse()
print(Zoo)
print(Zoo.sort(reverse=True))#descending order
print(Zoo)
Animal = Zoo.copy()
print(Animal)
Animal.clear()#clear returns an empty list
print(Animal)
print(Zoo.index("Zebra"))#to get the index number of a value in a list
Rhoda_info = ("Rhoda", "Female", "20", "Cooking")
name, gender, age, hobby = Rhoda_info
print(name)
print(gender)
print(age)
print(hobby)
#*operator is used to unpack items in a tuple if the num of variables is not
python_class = ("Rhoda", "Daniel", "James", "Busayo")
first_std, second_std, *Others = python_class
print(first_std)
print(second_std)
print(Others)

fruits = ["orange", "bannana", "orange", "water-melon", "cashew"]
print(fruits)
fruits.append("apple")
fruits.remove("cashew")
print(fruits)

numbers = [10,20,30,40,50]
first_std, second_std, *Others = numbers
print(first_std)
print(numbers[-1])
print(numbers[0:3])

scores = [70,85,90,60]
scores.append(100)
scores.sort()
print(scores)
print(scores[-1])

color = ("red", "blue", "orange", "Green")
print(color[1])
print(color[-1])

values = (1,2,3)
age, day, time = values
print(age)
print(day)
print(time)
#DICTIONARY - collection of key-value pairs
Student_info = {"First_name": ["Ifeoluwa", "Azeezat", "Olamide", "Glory"],
             "Last_name": ["Jolaoso", "Benjamin", "Ogunseye", "Oluwaseun" ],
              "Age":[12,16,18,22,],
              "Gender": ["Female", "Male", "Female", "Female", ],
              "Score": [70,50,78,89]

}
print(Student_info["First_name"][3])
print(Student_info["Last_name"][3])
print(Student_info["Age"][3])
print(Student_info["Gender"][3])
print(Student_info["Score"][1])

#Dictionary methods are builts in fuctions used to manipulate dictionary
Student_info.update({"Student_id":[1, 2, 3, 4]})
print(Student_info)
#keys - to get all the keys in adictionary
print(Student_info.values())
print(Student_info.keys())
print(Student_info.items())
for key, value in Student_info.items():
    print(key, value) #to get value for eack key
    animal = ["Dog", "Cat", "Pig", "Cow"]
    print(dict.fromkeys(animal, "Mammal")) #fromkeys - to create a dictionary from a list while
    print(Student_info.get("Last_name"))#to get the value of a key in a dictionary


    #set
    score = {10, 20, 30, 26, 10}
    print(score)
    print(dir(score))
    score.add(30)
    score.pop()
    print(score)

    Product_info = {"Product": ["Table", "Dell_laptop", "Chair", "Toyota"],
                    "Category": ["Furniture", "Computer", "Furniture", "Car"],
                    "no_of_products": [8000, 8543, 500, 1000]}
    print(Product_info)
    print(Product_info.values())
    print(Product_info.items())
    print(Product_info.keys())

    