# 第05章 if 语句



## 1. 条件测试
包括了“相等”，“不等”，“大于”，“小于”，“大于等于”，“小于等于”，“存在于”，“与或非”等判断。值得注意的是，Python对大小写敏感：
```python
>>> car = 'Audi'
>>> car == 'audi' 
False

>>> car.lower() == 'audi'
True

>>> car != 'audi'
True

>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age >= 21
False

>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False
>>> age_0 >= 21 or age_1 >= 21
True

>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'mushrooms' not in requested_toppings
False
```



## 2. if语句

### 2.1 简单的if语句

````python
age = 19
if age >= 18:
    print("You are old enough to vote!")
````

输出结果：

```python
You are old enough to vote!
```

### 2.2 if-else 语句

```python
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

输出结果：

```python
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

### 2.3 if-elif-else 结构

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 15
    
print("Your admission cost is $" + str(price) + '.')
```

输出结果：

```python
Your admission cost is $5.
```

还可以根据需要使用任意数量的elif代码块：

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
    
print("Your admission cost is $" + str(price) + '.')
```

输出结果：

```python
Your admission cost is $5.
```

其次，Python并不要求if-elif结构后面必须有else代码块。else是一条包罗万象的语句，只要不满足前面的条件，其中的代码就会执行，这可能会引入无效甚至恶意的数据。所以如果知道最终要测试的条件，应考虑使用一个elif代码块来代替else代码块，使代码更清晰，如下：

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
    
print("Your admission cost is $" + str(price) + '.')
```

输出结果：

```python
Your admission cost is $5.
```

### 2.4 测试多个条件

if-elif-else结构功能强大，但仅适用于只有一个条件满足的情况，即只要其中一个条件满足，其余条件都会被跳过，这保证了程序的高效性。然而有时必须检查你关心的所有条件，这时则应该使用一系列不包含elif和else代码块的简单if语句：

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('extra cheese.')
    
print('\nFinished making your pizza!')
```

总之：如果你只想执行一个代码块，就用if-elif-else结构；如果要运行多个代码块，就使用一系列独立的if语句。



## 3. 使用if语句处理列表

if语句常和循环结构配合使用。

### 3.1 检查特殊元素

```python
requested_toppings = ['mushrooms', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
    	print('Sorry, we are out of green peppers.')
	else:
    	print('Adding ' + requested_toppings + '.')
    
print('\nFinished making your pizza!')
```

输出结果：

```python
Adding mushrooms.
Adding extra cheese.
Sorry, we are out of green peppers.

Finished making your pizza!
```

### 3.2 确定列表不是空的

到目前为止，对于处理的每个列表都做了一个简单的假设，即它们非空，然而实际工程中，在遍历一个列表前需要先判断该列表是否为空：

```python
requested_toppings = []

if requested_topping:
	for requested_topping in requested_toppings:
     	print('Adding ' + requested_toppings + '.')
     	print('\nFinished making your pizza!')
	else:
    	print('Are you sure you want a plain pizza?')
```

输出结果：

```python
Are you sure you want a plain pizza?
```



