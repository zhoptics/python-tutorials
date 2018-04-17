# 第06章 字典



## 1. 使用字典

在Python中，字典是一系列键值对。每个键都与一个值相关联，用键来访问值。Python中用花括号“{ }”来表示字典。

```python
alien = {'color': 'green', 'points': 5}
print(alien)
print(alien['color'])
print(alien['points'])
```
输出结果：
```python
{'color': 'green', 'points': 5}
green
5
```


只要内存够用，理论上字典中可以包含任意数量的键值对，并且Python中字典是一个动态结构，可随时向其中添加键值对。
 ```python
alien = {'color': 'green', 'points': 5}
print(alien)

alien['x_position'] = 0
alien['y_position'] = 25
print(alien)
 ```

输出结果：

```python
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
```

有时候，在空字典中添加键值对是为了方便，而有时候则是必须这么做，比如使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，此时通常要先定义一个空字典。

```python
alien = {}
alien['color'] = 'green'
alien['points'] = 5
print(alien)
```

输出结果：

```python
{'color': 'green', 'points': 5}
```

如果要修改字典中的值，只需通过键名访问就行。

```python
alien = {'color': 'green'}
print("The alien is " + alien['color'] + ".")
alien['color'] = 'yellow'
print("The alien is now " + alien['color'] + ".")
```

输出结果：

```python
The alien is green.
The alien is now yellow.
```

对于字典中不再需要的信息，可用del语句将相应的键值对删除：

```python
alien = {'color': 'green', 'points': 5}
print(alien)
del alien['points']
print(alien)
```

输出结果：

```python
{'color': 'green', 'points': 5}
{'color': 'green'}
```

前面的例子都是一个对象的多种信息构成了一个字典（游戏中的外星人信息），字典也可以用来存储众多对象的统一信息：

```python
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python', # 建议在最后一项后面也添加一个逗号，方便后面添加元素
}
```



## 2. 遍历字典

### 2.1 遍历所有的键值对

```python
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)
```

输出结果：

```python
Key: last
Value: fermi
    
Key: first
Value: enrico
    
Key: username
Value: efermi
```

这里有一点需要注意，遍历字典时，键值对的返回顺序不一定与存储顺序相同，Python不关心键值对的存储顺序，而只追踪键与值之间的关联关系。

### 2.2 遍历字典中的所有键

字典的方法keys()将字典中的所有键**以列表的形式返回**，以下代码遍历字典中的所有键：

```python
favorite_languages = {
languages.py 'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in favorite_languages.keys():
	print(name.title())
```

输出结果：

```python
Jen
Sarah
Phil
Edward
```

也可以用如下方法遍历字典的所有键：

```python
favorite_languages = {
languages.py 'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in favorite_languages:
	print(name.title())
```

输出结果：

```python
Jen
Sarah
Phil
Edward
```

但是带有方法keys()的遍历所表达的意思更明确。

还可以用keys()方法确定某关键字是否在字典中：

```python
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")
```

输出结果：

```python
Erin, please take our poll!
```

使用sorted()函数按顺序遍历字典中的所有键：

```python
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
print(name.title() + ", thank you for taking the poll.")
```

输出结果：

```python
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
```

### 2.3 遍历字典中的所有值

类似于遍历所有键用keys()方法，遍历所有值则使用values()方法

```python
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
```

输出结果：

```python
The following languages have been mentioned:
Python
C
Python
Ruby
```

从结果可以看出，上述代码并没有考虑去重的问题，如果想要去重，可以调用set()：

```python
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',108 Chapter 6
'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
```

输出结果：

```python
The following languages have been mentioned:
Python
C
Ruby
```



## 3. 嵌套

### 3.1 字典列表

以前面外星人为例，三个外星人组成一个列表：

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
```

输出结果：

```python
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```

### 3.2 在字典中存储列表

每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表：

```python
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)
```

输出结果：

```python
You ordered a thick-crust pizza with the following toppings:
	mushrooms
	extra cheese
```

### 3.3 在字典中存储字典

涉及到这种情况时，代码都不会简单：

```python
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
    
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
```

输出结果：

```python
Username: aeinstein
	Full name: Albert Einstein
	Location: Princeton
    
Username: mcurie
	Full name: Marie Curie
	Location: Paris
```







