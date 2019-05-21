<!---
{"next":"Topics/functions.md","title":"Modules & Packages"}
-->

# Modules & Packages

In Python, a `module` is Python source file that contains pre-defined objects like variables, functions, classes, and other items we'll talk about soon. A Python `package`, sometimes used synonymously with the term `library`, is simply a collection of Python modules. The diagram below can show you this hierarchy visually.

![package_def](https://365datascience.com/wp-content/uploads/2018/07/image2-min-6-768x419.png)

Essentially, packages and modules are a means of `modularizing` code by grouping functions and objects into specific areas of focus. For instance, the `statsmodels` module ([here](https://www.statsmodels.org/)) contains code useful to a data scientist. The `Pyglet` library ([here](http://www.pyglet.org/)) contains code useful to game developers needing shortcuts for 3D game animation. But vice versa?

`Modular programming` allows us to break out modules and packages dealing with specific topics in order make the standard library more efficient for the general public. It's sort of like "a la carte" code. This becomes especially valuable once you scale your programs. Who needs that extra baggage?

## Global vs. Local Scope

One of the reasons Python leverages modular programming is because it helps avoid conflicts between `local` and `global` variables by creating separate `namespaces`. `Namespaces` are the place where variables are stored, and they exist on several independent levels, including **local, global, built-in, and nested namespaces**. For instance, the functions `builtin.open()` and `os.open()` are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. 

At a high level, a variable declared outside a function has `global scope`, meaning you can access a it inside or outside functions. A variable declared within a function has `local scope`, which means you can only access it within the object you created it. If you try to access it outside that, you will get a `NameError` telling you that variable is not defined.

We'll get more into how to use and interpret local and global scope as we dive into modules and functions...


## Importing Modules & Packages

Importing modules and packages is very easy and saves you a lot of time you'd otherwise spend reinventing the wheel. Modules can even import other modules! The best practice is to place all import statements at the of your script file so you can easily see everything you've imported right at the top. 

#### Importing Modules 
Let's look at a few different way to import modules and their contents. The simplest way to import a module is to simply write `import module_name`. This will allow you to access all the contents within that module. 

If you want to easily find out exactly what is in your newly imported module, you can call the built-in function `dir()` on it. This will list all types of names: variables, modules, functions, etc. 

```python
import math
dir(math)
# prints ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', ... etc.]
```

You can also import one specific object from a module like this:

```python
from math import sqrt
sqrt(25) # 5
```

Notice how we included `math.` when we called the `sqrt` function. Because of *variable scope*, you need to reference the `namespace` where `sqrt` is defined. Simply importing `sqrt` does not give it `global scope`. It still has `local scope` within the math module.

However, you can help avoid verbose code by importing modules and their items like this:

```python
from math import sqrt as s
s(25) # 5
```

By importing the `sqrt as s`, you can call the function as `s()` instead of `math.sqrt`. The same works for modules. Note the difference in how we reference the square root function though... 

```python
import math as m
m.sqrt(25) # 5.0
```

...we only renamed the module in this import and not the function. So we have to go back to the `module_name.function()` syntax. *However*, because we renamed the module on import, we can reference it in function calls by its shortened name, i.e. `m.sqrt`.

## Managing Dependencies

In addition to "built-in" modules, we have the ability in python to create, distribute and most importantly *consume* community defined python modules.

This is powerful because anyone who builds something useful has the ability to share with the larger python community. Creating and distributing python modules is outside the scope of this class, but we can consume any module we'd like by running the:

```bash
pip install [module_name]
```

Modules can be found in [**PyPI**](https://pypi.org/), or, the Python Package Index. Any registered module in pypi is installable via pip.

However, in order to safely install modules across projects (ie: perhaps project A requires module 1 v1 but then project B, started a year later needs to use module 1 v2) we need to create what are called **virtual environments**, isolated python environments where we can safely install our pip modules and rest assured that they don't interfere with other projects / the system at lare.

In order to create a virtual environment:

```bash
python3 -m venv .env
source .env/bin/activate
```

The `.env` folder contains everything needed for this **"virtualenv"**. We go *inside* the env by running the `source ./env/bin/activate` command. To deactivate, (while in virtualenv):

```bash
deactivate
```

The best part about this is not only can we install our pip modules safely, we can also do this:

```bash
pip freeze > requirements.txt
```

This will collect all the installed pip modules in the virtual env and store into a file (that we are calling `requirements.txt`). This is useful because if we ever wanted to run this software from a different computer, all we would have to do is pull down the python files, create a new virtualenv and then:

```bash
pip install -r requirements.txt
```

and this would effectively "copy" our installed modules into the new virtualenv.

## Common & Featured Modules & Packages

* [Python's `itertools` library](https://docs.python.org/3/library/itertools.html)
* [Pandas](http://pandas.pydata.org/) / ([Pandas github repo](https://github.com/pandas-dev/pandas))
* [NumPy](https://www.numpy.org/) / ([NumPy github repo](https://github.com/numpy/numpy))
* [SciPy](https://www.scipy.org/) / ([SciPy github repo](https://github.com/scipy/scipy))
* [Matplotlib](https://matplotlib.org/) / ([Matplotlib github repo](https://github.com/matplotlib/matplotlib))
* [scikit-learn](https://scikit-learn.org/) / ([scikit-learn github repo](https://github.com/scikit-learn/scikit-learn))