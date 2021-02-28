# **easierlog**: the easy way to inspect variables in Python

![GitHub Workflow Status (event)](https://img.shields.io/github/workflow/status/dilsonlira/easierlog/Python%20package)
![GitHub](https://img.shields.io/github/license/dilsonlira/easierlog)

## 1. Basic usage

Roughly every software developer needs to check how variables behave in runtime. In Python, this can be done by using `print()` function, that prints out the value of the passed variable. Sometimes, instead, the variable value is not enough. This is specially true when there are many variables to be inspected, or even when the same variable needs to be inspected in many parts of the code. 

To inspect both variable name and value, `print()` is not so straightforward:

    print('some_variable =', some_variable)

It became a little bit easier since Python 3.8:

    print(f'{some_variable=}')

But not so easy when comparing to easierlog:

    log(some_variable)

This can better understood in the script:

```python
 1  # script1.py
 2  
 3  def function1():
 4      a = 4
 5      print(a)
 6
 7
 8  def function2():
 9      a = 3
10      b = 'Hello World'
11      print(a)
12      print(b)
13
14
15  function1()
16  function2()
17
```
Running the script above, it will result:
```
4
3
Hello World
```
By using easierlog, the script would become:

```python
 1  # script2.py
 2  
 3  from easierlog import log
 4  
 5
 6  def function1():
 7      a = 4
 8      log(a)
 9 
10  
11  def function2():
12      a = 3
13      b = 'Hello World'
14      log(a)
15      log(b)
16
17
18  function1()
19  function2()
20
```

Running the script above, it will result:

```
[script2.py (line 08) in function1] (int) a = 4
[script2.py (line 14) in function2] (int) a = 3
[script2.py (line 15) in function2] (str) b = 'Hello World'
```

As shown above, `log()` provides information about where it was called:
- File name
- Line number
- Function name

And about the variable passed as argument:
- Variable type
- Variable name
- Variable value
 

## 2. Multiple variables

It is also possible to pass multiple variables at once:

```python
 1  # script3.py
 2  
 3  from easierlog import log
 4 
 5 
 6  def function():
 7      x = 2.3
 8      y = 1.5
 9      z = 0.1
10      log(x, y, z)
11
12 
13  function()
14
```

It will result:

```
[script3.py (line 10) in function] (float) x = 2.3
[script3.py (line 10) in function] (float) y = 1.5
[script3.py (line 10) in function] (float) z = 0.1
```

## 3. All variables

Calling `log()` without any arguments it will log all declared variables in the function:

```python
 1  # script4.py
 2  
 3  from easierlog import log
 4 
 5 
 6  def function():
 7      x = 2.3
 8      y = 1.5
 9      z = 0.1
10      log()
11
12 
13  function()
14
```

It will result:

```
[script4.py (line 10) in function] (float) x = 2.3
[script4.py (line 10) in function] (float) y = 1.5
[script4.py (line 10) in function] (float) z = 0.1
```

<!-- This also can be useful not only to inspect a specific variable, but to check if a piece of code was executed.

```python
if condition:
    log('condition is met')
```

## 4. String as argument
Sometimes we use `print()` not to check a specific variable, but just to check if a piece of code was executed.

# Installation

To install the latest release, type:

```pip install easierlog``` -->
