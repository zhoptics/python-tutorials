# 第07章 用户输入和while循环



## 1. input()函数

在Python中，使用input()函数获取用户输入，这里请注意：input()的返回值为字符串。如果输入的是数字，并且要用于后续计算，需要进行类型转换。

input()函数可以传入字符串参数作为输入提示，如下：

```python
number = input()
# 判断数据类型的两种方法
print(type(number))
print(isinstance(number, str))

print(int(number) ** 2)

# 如果提示超过一行，可以将提示放在变量中，再将变量传入input()
# 并且最好在提示后面留一个空格以区分提示和用户输入
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

输出结果：

```python
123
<class 'str'>
True
15129
Tell me something, and I will repeat it back to you: Hello, everyone!
Hello, everyone!
```

**判断奇偶**（作为对前文常见运算的补充）：取模运算 % ，返回余数

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")
```
输出结果：

```python
Enter a number, and I'll tell you if it's even or odd: 42
The number 42 is even.
```



## 2. while循环简介

for循环用于针对集合中的每个元素的一个代码块，而while循环不断地运行，直到指定的条件不满足为止。比如，让用户选择何时退出：

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)
```

输出结果：

```python
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```

### 2.1 使用标志

在上述代码中我们直接对输入数据进行判断，这样做在简单的程序中可行，但复杂的程序中，如果有多个状态同时决定while循环的继续与否，要是还用上述的方法，则while循环的条件判断将很长很复杂，这时可以定义一个变量作为标志来代替多个条件。使用标志来改写上述代码：

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)
```

在复杂的程序中，如很多事件都会导致程序停止运行的游戏中，标志很有用：在其中的任何一个事件导致活动标志变为False时，主游戏循环将退出。

### 2.2 使用break退出循环

要立即退出while或者for循环，不在执行循环中余下的代码，也不管条件测试的结果如何，可使用break语句。再将上述使用标志的代码改写为break：

```python
# cities.py
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
```

### 2.3 在循环中使用continue

如果满足某条件时要返回循环开始处，而不是跳出循环，则使用continue语句。以下是打印1到10中的所有奇数的代码：

```python
# counting.py
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)
```

输出结果：

```python
1
3
5
7
9
```

break与continue的区别：break跳过循环体内余下的所有代码，并跳出循环；continue跳过循环体内余下的所有代码，回到循环体开始处继续执行，而不是跳出循环体。

值得提醒的是，编写循环时应避免死循环，或者叫做无限循环，比如while循环忘记了变量自增。



## 3 使用while循环来处理列表和字典

### 3.1 在列表之间移动元素

将未验证用户经验证后变为已验证用户：

```python
# unconfirmed_users.py
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
		confirmed_users.append(current_user)
        
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
```

输出结果：

```python
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice
    
The following users have been confirmed:
Candace
Brian
Alice
```

### 3.2 删除包含特定值的所有列表元素

之前的章节中使用remove()函数来删除列表中的值，但只删除了列表中的第一个指定值，以下代码循环删除列表中指定的值：

```python
# pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)
```

输出结果：

```python
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

### 3.3 使用用户输入来填充字典

```python
# mountain_poll.py
responses = {}
poll.py
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	# Store the response in the dictionary:
	responses[name] = response
	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False
        
# Polling is complete. Show the results.
print("\n--- Poll Results ---")

for name, response in responses.items():
	print(name + " would like to climb " + response + ".")
```

输出结果：

```python
What is your name? Eric
Which mountain would you like to climb someday? Denali
Would you like to let another person respond? (yes/ no) yes

What is your name? Lynn
Which mountain would you like to climb someday? Devil's Thumb
Would you like to let another person respond? (yes/ no) no

--- Poll Results ---
Lynn would like to climb Devil's Thumb.
Eric would like to climb Denali.
```

