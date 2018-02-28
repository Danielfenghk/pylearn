# Effective Python 读书笔记

## Item1 要知道你用什么版本的 Python

1. 通过 `print(sys.version)` 可以知道现在运行的版本信息
2. 优先使用 `python3`

## Item2 遵从 `PEP8` 标准

1. 优先遵从社区代码风格标准
2. 使用 `pylint` 来保证代码风格统一

## Item3 了解 `bytes` `str` `unicoe` 三者之间的不同之处

1. 在 `python2` 中 `str` 表示 `8bit` 比特值，`unicode` 表示 Unicode 字符，当只包含 `7bit ascii` 时，这两者可以通用。
2. 在 `python3` 中 `bytes` 表示 Unicode 字符， `str` 表示 `8ibt` 原始比特值，这两者不通用，需要互相转换。
3. 最好使用 helper function 来保证你正在运算的对象是你想用的，比如 `to_unicode` 和 `to_str` 。
4. 如果要读写二进制文件，最好使用 `wb rb` 明确文件模式。

## Item4 使用 helper 函数替代复杂的表达式

1. 如果表达式太复杂，有太多 `and` `or`，建议将复杂的逻辑抽离出来，放到一个帮助函数中。这一点跟 `C/C++` 看似不同，
其实根本上来说是一样的，每种语言都有自己的风格，只要让大家都能够毫无障碍的读懂就可以了。
2. 代码只会写一次，却会读很多次，可维护性更加重要。

## Item5 学会使用 Slice

1. 掌握 `slice[start:end]` 的含义
2. `slice[:] = new_slice` 会覆盖值
3. `a = b[:]` 将会得到完整的拷贝
4. 自定义的类如果实现了 `__getitem__` 和 `__setitem__` 也可以使用 slice

## Item6 使用 Slice 的时候尽量避免同时使用 `Slice[Start:end:stride]`

1. 尽量避免同时使用 `start:end:stride`，这会让代码变得不清晰
2. 使用 `slice[start:end:stride]` 的时候会产生一份拷贝，如果内存或者计算资源吃紧，可以使用 `itertools.islice`

## Item7 尽量用列表生成式代替 `map filter`

1. 对于简单的 map, filter 都可以用列表生成式代替，增加可读性。

## Item8 避免在列表生成式中用太多的表达式

1. 太多的表达式会让代码不好维护，对于这种情况，不要用列表生成式。

## Item9 对于太大的列表生成式，考虑用生成器表达式代替

1. 如果过大的输入，`list comprehension` 会占用大量内存资源，这时可以用 `generator expression` 代替
2. `generator expression` 会产生 `iterator`，而且可以嵌套，只有在使用的时候才会计算。

## Item10 使用 `enumerate` 代替 `range`

1. 很多人习惯用　`range` 来生成下标遍历，这种做法不 Pythonic ，可以用 `enumerate` 代替。
2. `enumerate` 可以通过第二个参数来决定遍历起始值。

## Item11 使用 `zip` 来同时迭代多个生成器

1. 需要注意在 Python2 中 `zip` 返回的是列表生成式，如果太大会有内存占用方面的问题，可以考虑用 `itertools.izip`， 
Python3 则没有这个问题。
2. 如果两个迭代器长度不同，默认是按照最短的来计算，如果你希望按最长的，那么用 `itertools.zip_longest`

## Item12 避免在使用 `for while` 外使用 `else`

1. 这种用法不够清晰，而且 `else` 只在 `while for` 中没有 `break` 才会真正运行。

## Item13 充分利用 `try except else finally`

1. `try finally` 可以让异常继续抛出，同时做一些资源清理工作。
2. `try except else` 可以让异常抛出更清晰，如果 `try` 没有抛出异常，那么运行 `else`。
3. `try except else finally` 组合使用，各司其职。

## Item14 不要让函数返回 None 来表示错误情况，应该抛出异常。

1. 因为 None 可以转换为 False，所以在 if 等条件判断中可能会产生歧义。
2. 对于特殊情况，如果返回None来表示，则需要在文档中写清楚。

## Item15 了解闭包跟变量作用域之间的关系

1. 默认情况下，闭包函数可以访问包含它的作用于中的变量
2. 闭包函数内无法直接修改包含它的作用域中的变量，Python 3 可以通过 `nonlocal`，Python 2 可以通过一个 `list[0]` 
来绕过。
3. 在 Python 中查找变量名字的顺序是 **当前函数的作用域** -> **包含此函数的作用域** -> **模块作用域 global** -> 
**内置作用域 builtin**。

## Item16 在返回值中使用生成器来代替列表

1. 使用生成器更加清晰易读，并且生成器要比返回 `list` 更加节省内存。

## Item17 防御性的去迭代参数

1. 当你在函数里多次迭代一个参数的时候，如果参数是迭代器，可能会出错，要留意！ 对于这种情况，可以建立自定义容器来避免拷贝。
2. `for sum` 等关键词、函数会调用 `iter()`， 后者会调用对象的 `__iter__()
`，而此函数需要返回一个迭代器对象，其中必须实现 `__next__()` 方法。然后 `for` 会在返回的迭代器对象上调用`next`方法。
3. 通过将`__iter__()` 定义为生成器函数可以很方便的实现可迭代的容器。
4. 对于迭代器运行 `iter` 会返回自身，对于一个容器调用 `iter` 会返回一个迭代器。

## Item18 使用位置参数 *args 来让代码更加清晰

1. 注意，对于 *args 传递生成式可能会消耗大量内存
2. 如果已经有一个 List ，可以通过 *List 的方式来传递参数

## Item19 使用关键字参数来提供可选的行为

1. 通过关键词参数可以有效的扩展函数的功能，并提供向后兼容。

## Item20 使用 `None` 和 docstring 来指定动态的默认参数

1. 默认参数的值只会计算一次，也就是在模块载入的时候。
2. 对于希望是动态的默认参数，可以设置为 None， 然后在代码和 docstring 记录清楚。

## Item21 强制使用关键词参数让函数可读性更高

1. 对于 Python3 可以使用 `def foo(args, *, arg1=True, arg2=10)` 这样来强制使用命名的关键词参数
2. 对于 Python2 可以使用 `def foo(*args, **kwargs)` 同时配合 `kwargs.pop('argname', 
'default')` 以及手动 `raise TypeError` 来实现。

## Item22 使用 helper class 来代替 字典 和 元组流水账式的记录

1. 对于记账式的代码，可以考虑用多个 helper class 来代替，使得代码更加清晰易读。

## Item23 对于简单的接口，使用 函数 来做

1. 函数可以非常方便的作为组件之间的接口
2. 如果你需要在函数中维护状态，与其用闭包函数，可以考虑使用 `__call__()`的函数对象

## Item24 使用 `@classmethod` 类的多态性来泛型的创建对象

1. Python 中每一个类只有一个构造函数 `__init__`
2. 如果想要有多个构造函数，可以使用 `@classmethod`

## Item25 使用 `super` 初始化父类

1. Python 使用 `MRO` Method Resolution Order 来解决父类初始化的问题以及钻石继承中超父类初始化多次的问题。
2. 总是使用 `super` 来对父类进行初始化。

## Item26 多重继承最好只用来继承 `Mix-in` 的工具类

1. 如果 mix-in 能够达到要求，就不要使用多重继承
2. 将简单的 mix-in 组合来完成复杂的功能。 

## Item27 尽量用公有属性代替私有属性

1. 从一开始就计划让子类能够通过内部 API 来做更多的事情
2. 使用受保护属性来引导子类合理的使用内部属性，而不是通过私有属性来封闭
3. 只有在考虑到你的属性可能会跟子类的属性重名的时候，才考虑使用私有属性。

## Item28 从 collections.abc 继承来实现自定义容器

1. 当只需要简单的容器时可以考虑继承 `list dict` 等
2. 如果需要更加完整的容器方法，从 `collections.abc` 继承。

## Item29 使用纯粹的属性来代替 get set 方法

1. 不要像 Java 一样使用 get set 来定义类的属性接口，直接用公共属性
2. 如果需要一些特殊行为，那么可以用 `@property @property.setter`
3. 不要在 `@property` 方法中使用太慢的方法。

## Item30 考虑使用 `@property` 来对属性进行扩展，就可以避免重构属性

1. 很多时候会发现现有的设计没有考虑的很周全，属性需要被重构，这个时候可以用 `@property` 动态的对属性的行为进行扩展
2. 不要过度的依赖 `@property`

## Item31 对于某些可重用验证策略的 `@property`，使用 `descriptor class` 代替

1. 很多时候有些 `@property` 的验证策略是通用的，可以定义自己的描述器。
2. 使用 `WeakKeyDictionary` 来避免内存泄漏，因为 Python 的垃圾回收是引用计数策略。

## Item32 对于 `__getattr__, __getattribute__, __setattr__` 来实现延迟属性

1. 使用 `__getattr__` 和 `__setattr__` 来懒惰加载和保存属性。
2. `__getattribute__` 和 `__setattr__` 会在每次查询、调用属性的时候调用。
3. 为了避免无限循环，在调用 `__getattribute__` 的时候使用 `super().__getattribute__` 来获得属性。
4. 可以使用 `hasattr, getattr, setattr` 等内置函数来判断、获取、存储属性。

## Item33 使用 Metaclass 来验证子类

1. 使用 metaclass 来确保子类的定义符合规范，从而在类的定义阶段就将错误捕捉，不符合要求的子类根本不能实例化对象。
2. metaclass 的 `__new__` 实在 `class` 定义的语句结束之后才运行的。
3. Python2 和 Python3 的 metaclass 定义不一样。
4. metaclass 是继承自 type 的类。

## Item34 使用 Metaclass 来自动注册类

1. 类注册是一个 Python 模块化的模式。
2. 可以使用 Metaclass 来自动化类注册功能。                                                 

## Item35 使用 Metaclass 来做类的注解

1. 使用 Metaclass 可以在类完全定义之前修改类的属性。
2. 通过配合 Metaclass 可以避免使用描述器的时候为了防止内存泄漏要用 weakref 模块。

## Item36 使用 subprocess 来管理子进程

1. 使用 subprocess 模块来启动其他程序，可以并行运行。

## Item37 对于阻塞 I/O 使用线程

1. 由于 GIL 的存在， Python 不能在多核 CPU 上同时运行字节码。
2. 可以利用多线程来处理阻塞 I/O 问题。

## Item38 在多线程中使用锁来避免竞争带来的不一致性

1. 虽然 Python 有 GIL，但是在多线程中对于同一个变量的同时读写，仍会有 race ，因为执行字节码的顺序会被线程切换打乱
2. 需要使用锁来避免 race condition， 比如 threading.Lock 这个类就是标准互斥锁的实现。

## Item39 使用队列来对多个线程进行同步

1. 对于多线程而言，使用管道是一种很好的同步方法。
2. 自己实现并发管道的时候有许多问题需要考虑：无意义的等待、如何停止 worker 以及 内存消耗
3. Queue 内置类已经很好的实现了你所需要的构架高鲁棒性的管道同步程序。

## Item40 使用协程来并发的运行多个函数

1. 协程可以让你用很低的性能消耗来同时运行很多函数，一个线程的开销大概是 8M 内存，而协程大概是 1K
2. 在一个生成器中，yield 表达式的值是生成器的 `it.send()` 传递的值。
3. 协程让你能够将代码的核心逻辑跟环境分开。

## Item41 考虑使用 concurrent.futures 来实现真正的并行

1. 对于性能敏感的部分代码，可以用 C 扩展的方式提高性能
2. 可以使用 multiprocessing 模块来使用真正的并行。
3. 由于 multiprocessing 模块太复杂，应该使用 concurrent.futures 中的 ProcessPoolExecutor 
封装来使用。

## Item42 使用 functools.wraps 来定义函数装饰器

1. Python 的装饰器可以让你拥有在运行时改变其他函数行为的能力
2. 使用 functools.wraps 来帮助你设计自己的装饰器，否则有些函数原本的元信息会丢失。

## Item43 使用 contextmanager 装饰器来代替 `try finally` 的方式

1. 可以使用 `with ` 语句来代替 `try finally` 做资源的自动释放工作。
2. `@contextmanager` 装饰器可以帮助你更好的实现 `with`，否则要自己实现 `__enter__, __exit__` 等函数。
3. `yield object` 可以支持 `with xxx as yyy` 


## Item44 使用 copyreg 让 pickle 更加可靠

1. 只在受信任的程序之间序列化和反序列化 pickle 对象，否则使用 json
2. 使用 `copyreg` 应对类的变化、参数的有无等变动对 pickle 对象的冲击。

## Item45 使用 datetime 代替 time 模块来获得本地时间

1. 在不同的时区切换时使用不要使用 `time` 模块
2. 使用 `datetime, pytz` 来做时区转换

## Item46 使用 Python 内置的数据结构和算法

1. 充分利用 Python 自带的数据结构和算法，别造这种轮子，除非你想练习基础算法。

## Item47 使用 Decimal 来支持高精度的要求

1. 使用 Decimal 可以实现高精度计算的要求，比如金融。

## Item48 在 PYPI 寻找开源社区贡献的模块

## Item49 为每一个函数、类、模块都写 docstring

1. 在模块的文档中，介绍模块是做什么的，将重要的类以及函数介绍一下
2. 在类的文档中，重要的属性、方法，以及子类继承时应当了解的信息都要提及
3. 在函数的文档中，对每一个参数、返回值、异常、行为都要详细说明
4. 使用 `doctest` 来保证文档跟代码是一致的。

## Item50 使用包来管理模块，向外界提供稳定的 API

1. 包是一个包含其他模块的模块，通常是一个文件目录里面包含 `__init__.py` ，包中可以包含其他包
2. 可以通过定义 `__all__` 来指明你的模块希望向外界暴露哪些方法、类等。
3. 如果你想向外界隐藏模块的一些私有属性，可以通过在包的 `__init__.py 中定义 __all__`，或者在方法名前面加 `_ 下划线` 

## Item51 定义一个 `Root Exception` 来隔离 API 跟 调用代码

1. 通过在模块中定义 `root exception` 可以将你的 API 跟调用者的代码隔离
2. 通过捕获模块的 `root exception` 可以检查调用者代码的 bug
3. 捕获 Python 的 根异常可以检查 API 的 bug
4. 通过定义自己的异常层次，可以确保在升级 API 的异常结构时，调用者的代码仍能够兼容。

## Item52 了解打断环形依赖的方法

1. 环形依赖是指多个模块互相依赖对方才能运行
2. 可以通过 **动态导入** 也就是在函数里 `import module` 是解决依赖问题，不过需要注意带来的开销。
3. 也可以通过定义一个 `configure()` 方法，在里面执行具体的需要其他模块的代码，然后在运行的时候，而不是导入的时候运行。
4. 最好的方式是通过重构，彻底消除这种情况。

## Item53 使用虚拟环境做隔离以及重现运行环境

1. 可以使用 `virutalenv` 或者从 Python 3.4 开始内置的 `pyvenv` 来为每一个项目做一个虚拟环境
2. 在虚拟环境中可以使用 `source bin/activate` 激活环境，以及 `deactivate` 退出环境
3. 通过 `pip freeze > requirments.txt` 来列出环境安装的模块，换到其他环境中通过 `pip install -r 
requirments.txt` 轻松构建环境。

## Item54 考虑使用模块域的代码来设置运行环境

1. 程序会运行在不同的部署环境中，通过模块里书写一些判断代码，可以根据不同的环境做出不同的行为。

## Item55 对于调试输出，使用 `repr()`

1. 可以在类中定义 `__repr__` 来指定 `repr()` 的输出内容，如果对类没有控制权限，可以访问 `obj.__dict__`
2. 在 `print("%r" % (obj))` 相当于调用 `repr(obj)`

## Item56 使用 `unittest` 来对代码进行测试

1. Python 是一个动态语言，只有测试才能保证你的代码是可用的。
2. 使用 `unittest` 来对模块、类、函数做充分的单元测试。
3. 当然，后期除了单元测试还需要做集成测试。

## Item57 使用 `pdb` 来交互式的调试代码

1. `import pdb; pdb.set_trace()` 来交互式的调试代码。

## Item58 在你尝试做性能优化之前请先 `profile` 定位到慢的代码

1. 使用 Python 内置的 `cProfile` 模块来对代码进行 profile，确定哪一块代码拖慢了运行速度，然后针对性的进行优化。

## Item59 使用 `tracemalloc` 模块来查看 Python 中的内存分配和泄漏

1. CPython 使用引用计数实现自动内存回收，可以使用 `import gc` 来查看当前存在的对象
2. 使用 `import tracemalloc` 来查看内存的分配情况，Python 3.4 以上版本支持。