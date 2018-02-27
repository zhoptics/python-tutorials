# Windows平台开发环境搭建

## 1 安装Python解释器
### 方法1：安装官网[**Python**](https://www.python.org/downloads/)

官网下载Python 3.6/3.5/2.7 版本，双击一步步安装，注意**勾选**`Add python.exe to path`和`pip`命令。

安装完成之后，进入cmd命令行输入python，如果不能进入python开发环境，请把python.exe所在的路径`C:\Python35`添加到系统环境变量Path中

cmd命令行执行 **pip install numpy-mkl matplotlib docopt opencv-python dlib**



### 方法2：安装[**WinPython**](http://winpython.github.io/)或者[**Python(x,y)**](http://python-xy.github.io)

直接安装即可，安装完成之后可直接使用Spyder, IDLE, ipython-notebook等GUI环境

学会使用Python命令行、文本文件、GUI编辑运行调试代码



### 方法3：安装[**Anaconda**](https://www.continuum.io/downloads)

直接安装即可，安装完成之后可直接使用Spyder, IDLE, ipython-notebook等GUI环境

学会使用Python命令行、后缀 `.py`文本文件、GUI编辑运行调试代码



### 方法4：使用venv等工具虚拟一个Python环境





## 2 利用文本编辑器搭建Python开发环境

### 2.1 VS Code配置Python开发环境

安装**VS Code**编辑器，并安装python插件；学会使用**VS Code**来编写、调试、运行Python代码

下载[**Visual Studio Code**](https://code.visualstudio.com/Download)



### 2.2 Sublime Text配置Python开发环境



### 2.3 [Notepad++配置Python开发环境](http://www.cnblogs.com/zhcncn/p/3969419.html)

安装[Notepad++](https://notepad-plus-plus.org/)，设置字体、行号、显示方案

启动Notepad++，点击运行-运行-输入cmd /k python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT 并保存，设置快捷键(Ctrl+Alt+P)

**注意:如果Python不是安装在默认的安装路劲，务必将上一句的cmd /k 后面的python前添加完整路径。[**举例**](http://blog.csdn.net/evabook/article/details/52261282)：如果直接将WinPython安装在C盘，则要用C:\WinPython-32bit-2.7.9.2\python-2.7.9\python.exe替换掉cmd /k 后面的python**



## 3 利用集成开发工具IDE搭建Python开发环境

### 3.1 PyCharm

**安装PyCharm之前请确保已经安装好了JRE和Python解释器**

### 3.2 Eclipse + PyDev

**使用Eclipse+PyDev之前请确保已经安装好了JRE和Python解释器**

### 3.3 Visual Studio + PTVS

安装Visual Studio 2015/2017时，勾选PTVS。



# Linux平台开发环境搭建





#  MacOS平台开发环境搭建



