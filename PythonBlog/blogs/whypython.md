#Python and Its Merits
##November 11, 2018
What makes Python so popular? The usage of Python has risen dramatically since its introduction in 1991; a graph from StackOverflow shows that Python, out of all major languages, has grown an astounding amount since 2012, surpassing even Javascript and Java. There has to be some magic sauce that keeps Python flourishing and growing.

What makes Python special is its combination of ease of usage, large library, and strong community. Beginners find it simple to jump into, while veterans and professionals still have need for Python's tools: Python is both simple and functional.

##Ease of Usage <a name="usage"></a>
The simplicity of writing a script in Python is astounding – its unecessary to mess with things like MinGW, which may be hard to install for beginners. The syntax of the language is also far more flexible and intuitive. Take, for instance, these two lists in Python:

    array = [10, 11, 1400, 10, 20, 3, 10]
    other_array = [3, 40, 130, 10, 20, 30, 10]

You can perform many operations on them. Let's find the sum of all elements in them!

    s = 0
    for i in range(len(array)):
        s += array[s]

    for j in range(len(other_array)):
        s += other_array[j]

    print(s) # Results in 1707

That was far too long to type though. Surely, there's a faster way to do it. Indeed, typing this will result in your answer.

    print(sum(array+other_array)) # This works!
    print(sum(array) + sum(other_array)) # This works too!

In the first line of the previous codeblock, `other_array` was added on the end of `array`, while in the second line, the sum was simple found for each of them. Its only a little bit of code for this operation, while in C++, the syntax is clunky and can be confusing for readers.

    #include <numeric>
    cout << accumulate(array.begin(), array.end(), 0) + accumulate(other_array.begin(), other_array.end(), 0);

Another example would be finding what numbers there are in each, sorted.

    this_set = set().union(set(array), set(other_array))
    array_union = list(this_set)

    print(sorted(array_union)) # Results in [3, 10, 11, 20, 30, 40, 130, 1400]

Pythons functions are simple to write and use, and its tracebacks provide useful information for debugging.

##Large Library
Python's library of packages is massive. According to to the [Python Package Index](https://pypi.org/), there are nearly 160,000 packages on the service. These include a multitude of machine-learning modules, packages for data science, and other tools.

These tools are a great asset to any professional programmer in Python. Its additionally simple to install these modules in the console with `pip install module-name`.

Some of the more famous examples are [numpy](http://www.numpy.org/), a useful package for Python datascientists, [Keras](https://keras.io/), a machine-learning API, and [Selenium](https://selenium-python.readthedocs.io/getting-started.html), a web-scraping package. No matter if you want to work on a project with Natural Language Processing, create a game, or build a robot, Python has the package you need.
