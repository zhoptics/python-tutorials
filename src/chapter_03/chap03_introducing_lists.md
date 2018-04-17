# 第03章 列表简介



## 1. 列表是什么

列表由一系列按特定顺序排列的元素组成。

类似于C/C++, Java中的数组，但和他们不同的是，Python列表中的元素可以是不同类型。

Python中用中括号”[ ]”来表示列表，并用逗号分隔其中的元素。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

输出结果：

```python
['trek', 'cannondale', 'redline', 'specialized']
```

请大家注意下文中以及以后的文章中“方法”与“函数”的联系与区别，对于有基础的读者一定不陌生。“方法”与“类”这一面向对象的概念联系紧密，它一般指对象对于数据的特定操作，可以简单理解为“**方法是函数，函数不一定是方法**”。

**访问与使用列表中的元素**

大多数编程语言中，索引都是从0开始的，而不是从1开始的。以下代码是输出上述列表中的第1个元素：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
```

输出结果：

```python
trek
Trek
My first bicycle was a trek.
```

Python还支持索引为负数，表示从后往前数，“-1”表示倒数第1个元素，例如：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
```

输出结果：

```python
specialized
```

但是，不管索引是正数还是负数，都要注意**索引越界问题**，即指定索引位置要在列表的索引范围之内。



## 2. 修改、添加和删除元素

### 2.1 修改列表元素

```python
# 修改第1个元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```

输出结果：

```python
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

### 2.2 添加元素

在列表末尾添加元素，**append()**方法：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
```

输出结果：

```python
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

也可以动态建立motorcycles列表：

```python
motorcycles = [] # 声明一个列表
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
```

输出结果：

```python
['honda', 'yamaha', 'suzuki']
```

在列表中插入元素，**insert()**方法：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles.insert(4, 'harley-davidson')
print(motorcycles)
```

输出结果：

```python
['ducati', 'honda', 'yamaha', 'suzuki']
['ducati', 'honda', 'yamaha', 'suzuki', 'harley-davidson']
```

### 2.3 删除元素

使用 **del** 语句删除元素：知道元素在列表中的位置

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
```

输出结果：

```python
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
```

 **del** 可删除任意位置的列表元素，前提是知道其索引。

**使用 pop() 方法删除元素**：会返回被删除的元素，后面代码还需要操作被删除的元素时使用此方法。

默认删除列表最后一个元素，当传入参数（作为索引）时，删除指定位置的元素（但请注意越界问题）：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

last_owned = motorcycles.pop() # pop() 默认删除列表最后一个元素
print("The last motorcycle I owned was a " + last_owned.title() + ".")
print(motorcycles)

motorcycles.pop(1) # 传入参数
print(motorcycles)
```

输出结果：

```python
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
The last motorcycle I owned was a Suzuki.
['honda']
```

所以，**pop() **方法也可以删除任意位置的元素

**根据值删除元素的 remove() 方法**：当不知道元素索引，但知道元素值时

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
```

输出结果：

```python
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
```

注意，如果列表中有多个相同的值，**romve() 方法只删除第一个**。



##  3. 组织列表

### 3.1 排序

**sort()** 方法对列表永久排序（**原地操作**）：

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```

输出结果：

```python
['audi', 'bmw', 'subaru', 'toyota']
```

如果不想修改原列表，则应使用以下方法。

**使用 sorted() 函数对列表进行临时排序**：返回一个已经排序的副本

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the soted list: ")
print(sorted(cars))
      
print("\nHere is the original list again: ")
print(cars)
```

输出结果：

```python
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']  

Here is the soted list: 
['audi', 'bmw', 'subaru', 'toyota']  

Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']  
```

不管是**sort()** 方法还是 **sorted()** 函数，如果想反向排序，只需传入关键字参数“**reverse=True**”:

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
sorted(cars, reverse=True)
```

以上两种排序是按**ASCII**码进行的排序，如果想自定义排序，需要传入自定义比较函数。

**反向打印列表**：**reverse() 方法**，也是原地操作！反向打印列表的实现方法之一。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
```

输出结果：

```python
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```

### 3.2 确定列表长度

使用 **len()** 函数获得列表长度：

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
```

输出结果：

```python
4
```

