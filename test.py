<<<<<<< Updated upstream
# write a program to print hello world
print("Hello World")
=======
# function composition
def make_adder(n):
  def adder(x):
      return x + n
  return adder

def square(x):
  return x * x

def triple(x):
  return 3 * x

def composel(f, g):
  def h(x):
    return f(g(x))
  return h
>>>>>>> Stashed changes
