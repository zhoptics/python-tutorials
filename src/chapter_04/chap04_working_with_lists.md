# 第04章 列表操作



## 1. 遍历列表

本章主要是for循环：

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
print("Thank you, everyone. That was a great magic show!")
```

输出结果：

```python
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!
```

这里有两个值得注意的地方，一个是“冒号”：“for”关键字所在的行最后有一个冒号；一个是缩进问题，Python中的代码块都是以缩进为标准，不像C/C++，Java这样的语言以花括号表示代码块。IndentationError指缩进错误。



## 2. 创建数值列表

这有使用一个重要的生成数列的函数 range() ，以及将数据转换成列表的 list() 函数

```python
print(list(range(6))) # 结束值（不包含结束值）
print(list(range(1, 6))) # 起始值（包含），结束值（不包含）
print(list(range(1, 6, 2))) # 起始值 结束值 步长，最后一个数小于结束值
print(list(range(6, 1, -1))) # 负数步长，此时起始值要大于结束值
print(list(range(1, 6, -1))) # 负数步长，若起始值小于结束值，则输出空列表
```

输出结果：

```python
[0, 1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 3, 5]
[6, 5, 4, 3, 2]
[]
```

range()函数也常用语for循环，用于标识循环次数，或者用于生成更复杂的列表：

```python
squares = []
for value in range(1,11):
	squares.append(value**2 + 1)    
print(squares)    
```

输出结果：

```python
[2, 5, 10, 17, 26, 37, 50, 65, 82, 101]
```

对于生成列表，还有一种更简洁的写法，即列表解析式，如上述生成列表的代码可以缩短为一行：

```python
squares = [value**2 for value in range(1,11)]
print(squares)

squares_2 = [value**2 for value in range(1,11) if value % 2 == 0]
print(squares_2)
```

输出结果：

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[4, 16, 36, 64, 100]
```

列表解析式还可以更复杂，这里就不再赘述了。

**对数字列表执行简单的统计计算：**

求一个数字列表的最大、最小值以及所有元素之和：

```python
digits = list(range(10))
print(min(digits), max(digits), sum(digits))
```

输出结果：

```python
0 9 45
```



## 3. 使用列表的一部分

### 3.1 切片

切片操作用于取原始列表的一部分：

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# [起始：结束：步长]，其中，结果列表包含起始索引，但不包括结束索引
print(players[0:3])
print(players[:3]) # 如果从0开始切片，0可以省略
print(players[1:3])
print(players[2:]) # 如果要遍历到最后一个元素，结束索引可以省略，此时最后一个元素会被包含
print(players[-3:])
print(players[::2]) # 设置了步长，
print(players[:4:2])
```



切片操作的参数设置和range()函数的参数设置十分相似，起始，结束，步长都可以为负值，这里先总结一条规律：如果步长为正数，则起始位置要在结束位置的左边；若步长为负数，则起始位置要在结束位置的右边。

### 3.2 复制列表

这里有深浅复制的问题。如果直接将一个变量赋值到另一个变量，那么内存中的数据依然只有一份，而不是两份，这两个变量都指向内存中同一个存放数据的内存区域，如果用C/C++的语言来描述，Python中的变量都相当于指针，这两个变量（指针）指向的是同一片内存，对这两个变量（指针）的操作会相互影响，因为都作用于同一内存块，如下：

```python
# 浅复制
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)

names = players
names.append('emily')
print(players)
```
输出结果：
```python
['charles', 'martina', 'michael', 'florence', 'eli']
['charles', 'martina', 'michael', 'florence', 'eli'，'emily']
```

如果想在内存中将原来的数据复制出一份新的，则需要深复制，切片操作则是实现深复制的一种方法：

```python
# 深复制
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)

names = players[:]
names.append('emily')
print(names)
print(players)
```

输出结果：

```python
['charles', 'martina', 'michael', 'florence', 'eli']
['charles', 'martina', 'michael', 'florence', 'eli'，'emily']
['charles', 'martina', 'michael', 'florence', 'eli']
```



## 4. 元组（tuple）

和列表紧密联系的一个数据结构则是元组。列表非常适合用于存储在程序运行期间可能变化的数据集，列表可以被修改。然而有时你需要创建一系列不可修改的元素，这个时候则需要用到元组。

元组用圆括号来标识，以下是声明一个元组：

```python
my_tupple = () # 声明一个空元祖
one_tupple = (1,) # 声明含有一个元素的元祖，不是one_tupple = (1)
```

对元组中元素的访问以及对元组的遍历都和对列表的操作一样；不同的是，元组中的元素不能被改变。

虽然元组中的元素不能改变，但是元组变量的值可以改变。从C/C++的角度来看，元组变量是个指针，元组相当于一个const数组，数组虽然不能被改变，但指针可以指向别处。

```python
test_tupple = (1, 2, 3, 4, 5) 
print(test_tupple)
test_tupple = (2, 3, 4, 5, 6) 
print(test_tupple)
```

相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，则可使用元组。