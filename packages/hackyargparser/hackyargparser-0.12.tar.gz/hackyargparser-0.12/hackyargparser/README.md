# Hacky argparser - parses arguments and changes the defaults of functions

## pip install hackyargparser

A decorator function that modifies the default arguments of a given function based on the values passed through command line arguments.
The function first checks if the input function is callable or None. It then retrieves the global dictionary of the
calling frame and defines a decorator function. The decorator function modifies the default arguments of the input
function based on the values passed through command line arguments. It does this by retrieving the variable names
and annotations of the input function and creating a dictionary of all the annotations. It then iterates through
the default arguments of the input function and tries to convert them to the appropriate data type based on the
annotations. If the conversion fails, it tries all possible data types until a successful conversion is made. The
modified default arguments are then set and the input function is called with the modified arguments.


## Create a py file 

```python

# "a2.py" in this example

from hackyargparser import add_sysargv, config

config.helptext = (
    "Error! --f2_a, --f2_b, --f1_a are mandatory!"  # The help text to be printed
)
config.kill_when_not_there(
    ("--f2_a", "--f2_b", "--f1_a")
)  # If those arguments are not passed, config.helptext will be printed, and sys.exit will be called
config.stop_after_kill = True  # Stop after printing config.helptext -> input()


@add_sysargv
def function1(
    f1_a: int | float | None = None,
    f1_b: int | float = 1,
    mvar: int = 10,
):
    print(f1_b * f1_a * mvar)
    return f1_a, f1_b, mvar


@add_sysargv
def function2(
    f2_a: int | float | None = None,
    f2_b: int | float | None = None,
    mvar: int = 10,
):
    print(f2_a * f2_b * mvar)

    return f2_a, f2_b, mvar


@add_sysargv
def function3(
    f3_a: list | tuple = (),
    f3_b: int | float = 1,
):
    for l in f3_a:
        print(l + f3_b)

    return set(f3_a)


def function4(
    f3_a: list | tuple = (),
    f3_b: int | float = 1,
):
    print("i am not decorated")
    print(f"{f3_a=}, {f3_b=}")

    return set(f3_a)


print(function2())

print(function1())

print(function3())

print(function4())


```


# Execute the py file  with arguments from the command line

```python
####################################################################################################
# use -- and the local variable name as arguments followed by the value you want to pass
# Type hints are necessary as well as default values 
# .\python.exe .\a2.py --f2_a 12 --f2_b 300 --f1_a 60
# 36000
# (12, 300, 10)
# 600
# (60, 1, 10)
# ...
####################################################################################################

# .\python.exe .\a2.py --f2_a 12 --f2_b 300
# Error! --f2_a, --f2_b, --f1_a are mandatory!
####################################################################################################
# .\python.exe .\a2.py --f2_a 12 --f2_b 300 --f1_a 60 --f3_a [1,2,3,4,5,4,4] --f3_b 22


# 36000
# (12, 300, 10)
# 600
# (60, 1, 10)
# 23
# 24
# 25
# 26
# 27
# 26
# 26
# {1, 2, 3, 4, 5}
# i am not decorated
# f3_a=(), f3_b=1
# set()

####################################################################################################
# If you get any errors, try using quotes  --f3_a "(1,2,3,4,5)"
# .\python.exe .\a2.py --f2_a 12 --f2_b 300 --f1_a 60 --f3_a "(1,2,3,4,5)" --f3_b 22

# 36000
# (12, 300, 10)
# 600
# (60, 1, 10)
# 23
# 24
# 25
# 26
# 27
# {1, 2, 3, 4, 5}
# i am not decorated
# f3_a=(), f3_b=1
# set()


####################################################################################################
```
