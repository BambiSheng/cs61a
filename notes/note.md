# Notes for cs61a
## Lec1.Function
### 1. assignment statements
  eg.
```
a=1
b=2
b,a = a+b,b
```
res: b=3 a=2
先运行等号右边，再更换左边变量与值的绑定关系（或者说用右边为左边赋值）
### 2. defining functions
assingment -> binds names to values
function definition -> binds names to expressions
one possible confusing thing:
```
>>> x=1
>>> def square(x):
...     return x*x
...
>>> square()
Traceback (most recent call last):
File "<stdin>", line 1, in <module> TypeError: square() missing 1 required positional argument:'x'
>>> square(3)
9
>>> x
1
```
- 调用函数时，相当于进入了独立于global的新的frame，并且引入变量名 x并赋值，接着顺着函数的body运行，直到return回到global frame
- 在第3部分中这个疑惑将得到更清晰的解答
### 3. Environmnet
Environments are memories that keep track of the correspondence between names and values.
As for frame:
  - The global frame alone
  - a local frame ,followed by the global frame.

An environment isa sequence of frames.
==important!== A name evaluates to the value bound to that name in the earliest frame of the current environment in which the name is found.
 
 - Look for the name in the local frame
 - not found?Look for it in the global frame. 