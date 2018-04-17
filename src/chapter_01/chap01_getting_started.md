# 第01 章  起步



## 1.1 搭建编程环境

### 1.1.1 Python 2 和 Python 3

Python有Python 2 和 Python 3两个版本，对入门学习而言，在使用上两个版本的区别不大，选择任何一个版本都可以。但Python 2 即将在2020年停止支持，**建议选择Python 3.5/3.6的版本**，绝大部分第三方库都完美地支持了Python 3.5/3.6。

如果你使用的是**Windows XP**操作系统，只能使用Python 2.7 和Python 3.4。

如果你使用的是64位**Windows 7/10**，只能在安装Python 3.5+以上的版本安装tensorflow。

**Python 2和Python 3的区别:**

1. print 在Python 2中，print是一个语句，后面可以不加括号；在Python 3中，print是一个函数，后面必须加括号
2. 除法 “/”在Python 2中表示整除，在Python 3中表示精确的除法，Python 3中整除用“//”表示，在Python 2中可以使用`import __future__ `来体验Python 3中的函数
3. Python 2对中文支持不好，如果要输入中文字符或者注释，需要在文本文件首行标注**# -*- coding:utf-8 -*-**或者**coding=utf-8**(只识别coding和utf-8，其它字符不识别)
4. 输入函数：在Python 2中有raw_input()和input()函数, 在Python 3中只有input()
5. third-party packages的支持有所不同，Python 2更多一些，但是绝大部分的package都会支持Python 3
6. [Python 2与Python 3的区别官网详解](https://wiki.python.org/moin/Python2orPython3)


### 1.1.2 运行Python代码片段 

Python自带了一个在终端窗口中运行的解释器， 让你无需保存并运行整个程序就能尝试运行Python代码片段。 
```python
>>> print("Hello Python interpreter!") # 回车执行
Hello Python interpreter! 
```

### 1.1.3 Hello World程序 

要使用Python来编写这种Hello World程序， 只需一行代码： 

```python
print("Hello world!") 
```



## 1.2 在不同操作系统中搭建Python编程环境 

Python是一种跨平台的编程语言， 这意味着它能够运行在所有主要的操作系统中。 

### 1.2.1 在Linux系统中搭建Python编程环境 

**1. 检查Python版本**

在终端中输入python3、python3 --version、python3 -V均能查看Python 3的版本信息；

在终端中输入python、python --version、python -V均能查看Python 2的版本信息；

如果要退出Python并返回到终端窗口， 可按Ctrl + D或执行命令exit() 。

**2. 安装文本编辑器**
安装Geany：sudo apt-get install geany
建议安装Visual Studio Code或者Sublime Text 3

**3. 运行Hello World程序 **
编写hello_world.py文件，并在终端中执行：python3 hello_world.py

**4. 在终端会话中运行Python代码**
你可以打开一个终端窗口并执行命令python 或python3 ， 再尝试运行Python代码片段。 
```python
>>> print("Hello Python interpreter!")
Hello Python interpreter!
>>>
```
消息将直接打印到当前终端窗口中。 别忘了， 要关闭Python解释器， 可按Ctrl + D或执行命令exit() 。

### 1.2.2 在OS X系统中搭建Python编程环境 

**1. 检查是否安装了Python** 
在文件夹Applications/Utilities中， 选择Terminal， 打开一个终端窗口； 你也可以按Command + 空格键， 再输入terminal 并按回车。 为确定是否安装了Python， 请执行命令python
（注意， 其中的p是小写的） 。 输出将类似于下面这样， 它指出了安装的Python版本； 最后的>>> 是一个提示符， 让你能够输入Python命令。
```python
$ python
Python 2.7.5 (default, Mar 9 2014, 22:15:05)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits", or "license" for more information.
>>>
```

**2. 在终端会话中运行Python代码**

## 1.3 解决安装问题
如果在安装时遇到问题，请在向他人请教之前先尝试百度自行研究解决


