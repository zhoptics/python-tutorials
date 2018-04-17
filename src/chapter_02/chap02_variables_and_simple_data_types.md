# 第02章 变量和简单数据类型



## 1. 运行hello_world.py

作为一个合格的程序员，必须精通各种语言的”Hello, World!”，以下是学习Python的第一段代码
```python
# hello_world.py
print("Hello World!")
```



## 2. 变量

变量就是数据的别称，和数学上的变量类似。

例如上述代码用变量表示：
```python
message = "Hello World!" 
print(message)
```

变量有一定的命名规则：

- 变量名只能包含字母、数字和下划线，且不能以数字开头
- 变量名不能包含空格，一般用下划线分隔变量中的单词，也可以用驼峰命名法，但Python提倡用下划线
- Python中的关键字和自带函数不能用于变量名
- 变量名应该简短明了
- 慎用小写字母 l 和大写字母O，因为这两个字母容易被看成数字1和0

同时也请注意，Python解释器不对代码进行拼写检查，应尽量避免命名错误，比如变量名中少写个字母之类的，否则会出现NameError



## 3. 字符串

字符串就是一系列被引号括起来的字符，在Python中，引号可以是单引号，也可以是双引号，还可以是三引号。单双引增加了Python字符串的灵活性，减少了转义字符的使用，比如字符串中有且只有单引号时，最外层可以用双引号，反之亦然。三引号主要用于字符串是多行的情况，同时它也常用语注释。例子如下：
```python
"This is a string."
'This is also a string.'

'I told my friends,"Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strength is its diverse and supportive community."

"""
this is line 1;
this is line 2.
"""

'''
this is line 1;
this is line 2.
'''
```
注意，若字符串中出现了和最外层引号相同的引号时，会出现SyntaxError

**字符串首字母大写：**

字符串中每个单词首字母大写：

```python
name = "ada lovelace"
print(name.title())
```
输出结果：
```python
Ada Lovelace
```

**字符串全部大写和小写：**

```python
name = "ada lovelace"
print(name.upper())
print(name.lower())
```
输出结果：
```python
ADA LOVELACE
Ada lovelace
```

**字符串拼接：**
Python中用“+”号进行字符串拼接：
```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
```

输出结果：

```python
ada lovelace
Hello, Ada Lovelace!
```

删除字符串首尾的空白：删左空白，删右空白，删两端空白

```python
>>> temp = ' python '
>>> temp
' python ' 
>>> temp.lstrip()
'python '
>>> temp.rstrip() 
' python'
>>> temp.strip() 
'python'
```



## 4. 数字

特别注意Python中的默认除法：两个整数相除，如果除不尽，会有小数，而不是只保留整数（如C/C++, Java, Python 2）

````python
# 整数
>>> 2 + 3 
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5 # 不是1
>>> 3 ** 2 # 乘方运算
9  
>>> (2 + 3) * 4
20

# 浮点数（结果包含的小数位数可能不确定）
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.1 # 和计算机内部数字的表示方法有关
0.30000000000000004
>>> 0.1 * 3
0.30000000000000004
````

数字与字符串的拼接：

使用str()函数，否则会报TypeError

```python
age = 23
message = "Happy " + age + "rd Birthday!"
```

输出结果：

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```

正确语法：

```python
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message) 
```

输出结果：

```python
Happy 23rd Birthday!
```



## 5. 注释

Python中的注释为“#”号，从“#”号开始到本行结束的中间这部分均为注释内容，不会被执行。

```python
# Say hello to everyone
print("Life is short, you need Python！")
print("人生苦短，我用Python！")
```

输出结果：

```python
Life is short, you need Python！
人生苦短，我用Python！
```



## 6. Python之禅

在python命令行中运行如下代码，即可查看Python社区所推崇的代码原则：

```python
>>> import this
```

输出结果：

```python
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

