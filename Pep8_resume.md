# PEP 8 – Style Guide for Python Code

*Created: 05-Jul-2001*

This document gives coding conventions for the Python code comprising the standard library in the main Python distribution.

## A Foolish Consistency is the Hobgoblin of Little Minds

One of Guido’s key insights is that code is read much more often than it is written. The guidelines provided here are intended to improve the readability of code and make it consistent across the wide spectrum of Python code. As PEP 20 says, “Readability counts”.
A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.
However, know when to be inconsistent – sometimes style guide recommendations just aren’t applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don’t hesitate to ask!
In particular: do not break backwards compatibility just to comply with this PEP!
Some other good reasons to ignore a particular guideline:
1. When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP.
2. To be consistent with surrounding code that also breaks it (maybe for historic reasons) – although this is also an opportunity to clean up someone else’s mess (in true XP style).
3. Because the code in question predates the introduction of the guideline and there is no other reason to be modifying that code.
4. When the code needs to remain compatible with older versions of Python that don’t support the feature recommended by the style guide.

## CODE LAY-OUT

### Identation: Use 4 spaces per indentation level.

```
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

When the conditional part of an if-statement is long enough to require that it be written across multiple lines, it’s worth noting that the combination of a two character keyword

```
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

The closing brace/bracket/parenthesis on multiline constructs may either line up under the first non-whitespace character of the last line of list, as in:

```
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```

or it may be lined up under the first character of the line that starts the multiline construct, as in:

```
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

### Tabs or Spaces?

**Spaces are the preferred indentation method.**
Tabs should be used solely to remain consistent with code that is already indented with tabs.
Python disallows mixing tabs and spaces for indentation.

### Maximum Line Length

**The Python standard library is conservative and requires limiting lines to 79 characters (and docstrings/comments to 72).**

```
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

### Should a Line Break Before or After a Binary Operator?

```
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

### Blank Lines

- Surround top-level function and class definitions with two blank lines.
- Method definitions inside a class are surrounded by a single blank line.
- Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).
- Use blank lines in functions, sparingly, to indicate logical sections.

### Source File Encoding
Code in the core Python distribution should always use UTF-8, and should not have an encoding declaration.

### Imports

- Imports should usually be on separate lines

    ```
    # Correct:
    import os
    import sys
    ```
    
- Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
Imports should be grouped in the following order:
    1. Standard library imports.
    2. Related third party imports.
    3. Local application/library specific imports.
    
    You should put a blank line between each group of imports.

- Absolute imports are recommended
- When importing a class from a class-containing module, it’s usually okay to spell this:
    
    ```
    from myclass import MyClass
    from foo.bar.yourclass import YourClass
    ```
    
- If this spelling causes local name clashes, then spell them explicitly:
    
    ```
    import myclass
    import foo.bar.yourclass
    ```
    
- Wildcard imports (`from <module> import *`) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools. 

## String Quotes

In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. Pick a rule and stick to it. **When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability.**

## Whitespace in Expressions and Statements

### Pet Peeves

**Avoid** extraneous whitespace in the following situations:
- Immediately inside parentheses, brackets or braces:
    
    ```
    # Correct:
    spam(ham[1], {eggs: 2})
    ```
    
- Between a trailing comma and a following close parenthesis:
    
    ```
    # Correct:
    foo = (0,)
    ```
    
- Immediately before a comma, semicolon, or colon:
    
    ```
    # Correct:
    if x == 4: print(x, y); x, y = y, x
    ```
    
- However, in a slice the colon acts like a binary operator, and should have equal amounts on either side (treating it as the operator with the lowest priority). In an extended slice, both colons must have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is omitted:
    
    ```
    # Correct:
    ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
    ham[lower:upper], ham[lower:upper:], ham[lower::step]
    ham[lower+offset : upper+offset]
    ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
    ham[lower + offset : upper + offset]
    ```
    
- Immediately before the open parenthesis that starts the argument list of a function call:
    
    ```
    # Correct:
    spam(1)
    ```
    
- Immediately before the open parenthesis that starts an indexing or slicing:
    
    ```
    # Correct:
    dct['key'] = lst[index]
    ```
    
- More than one space around an assignment (or other) operator to align it with another:
    
    ```
    # Correct:
    x = 1
    y = 2
    long_variable = 3
    ```

### Other Recommendations

- Avoid trailing whitespace anywhere. Because it’s usually invisible, it can be confusing: e.g. a backslash followed by a space and a newline does not count as a line continuation marker.
- Always surround these binary operators with a single space on either side: assignment (`=`), augmented assignment (`+=`, `-=`, etc.), comparisons (`==`, `<`, `>`, `!=`, `<>`, `<=`, `>=`, `in`, `not in`, `is`, `is not`), Booleans (`and`, `or`, `not`).
- If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator:
    
    ```
    # Correct:
    i = i + 1
    submitted += 1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)
    ```
    
- Function annotations should use the normal rules for colons and always have spaces around the `->` arrow if present.
    
    ```
    # Correct:
    def munge(input: AnyStr): ...
    def munge() -> PosInt: ...
    ```
    
- Don’t use spaces around the `=` sign when used to indicate a keyword argument, or when used to indicate a default value for an unannotated function parameter:
    
    ```
    # Correct:
    def complex(real, imag=0.0):
        return magic(r=real, i=imag)
    ```
    
    When combining an argument annotation with a default value, however, do use spaces around the `=` sign:
    
    ```
    # Correct:
    def munge(sep: AnyStr = None): ...
    def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
    ```
    
- Compound statements (multiple statements on the same line) are generally discouraged:
    
    ```
    # Correct:
    if foo == 'blah':
        do_blah_thing()
    do_one()
    do_two()
    do_three()
    ```
    
- While sometimes it’s okay to put an if/for/while with a small body on the same line, never do this for multi-clause statements. Also avoid folding such long lines!
Rather not:
    
    ```
    # Wrong:
    if foo == 'blah': do_blah_thing()
    for x in lst: total += x
    while t < 10: t = delay()
    ```
    
    Definitely not:
    
    ```
    # Wrong:
    if foo == 'blah': do_blah_thing()
    else: do_non_blah_thing()
    
    try: something()
    finally: cleanup()
    
    do_one(); do_two(); do_three(long, argument,
                                 list, like, this)
    
    if foo == 'blah': one(); two(); three()
    ```

## When to Use Trailing Commas

Trailing commas are usually optional, except they are mandatory when making a tuple of one element. For clarity, it is recommended to surround the latter in (technically redundant) parentheses:

```
# Correct:
FILES = ('setup.cfg',)
```

When trailing commas are redundant, they are often helpful when a version control system is used, when a list of values, arguments or imported items is expected to be extended over time. The pattern is to put each value (etc.) on a line by itself, always adding a trailing comma, and add the close parenthesis/bracket/brace on the next line. However it does not make sense to have a trailing comma on the same line as the closing delimiter (except in the above case of singleton tuples):

```
# Correct:
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
```

## Comments

Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!
Comments should be complete sentences. **The first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).**

Python coders from non-English speaking countries: please write your comments in English, unless you are 120% sure that the code will never be read by people who don’t speak your language.

### Block Comments

Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a `#` and a single space (unless it is indented text inside the comment).

**Paragraphs inside a block comment are separated by a line containing a single `#`.**

### Inline Comments

**Use inline comments sparingly.**
An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a `#` and a single space.

Inline comments are unnecessary and in fact distracting if they state the obvious. Don’t do this:

```
x = x + 1                 # Increment x
```
But sometimes, this is useful:
```
x = x + 1                 # Compensate for border
```

### Documentation Strings

- Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. **This comment should appear after the `def` line.**
- PEP 257 describes good docstring conventions. Note that most importantly, the `"""` that ends a multiline docstring should be on a line by itself:
    
    ```
    """Return a foobang
    
    Optional plotz says to frobnicate the bizbaz first.
    """
    ```
    
- For one liner docstrings, please keep the closing """ on the same line:
    
    ```
    """Return an ex-parrot."""
    ```

## Naming Conventions

The naming conventions of Python’s library are a bit of a mess, **so we’ll never get this completely consistent – nevertheless**, here are the currently recommended naming standards. New modules and packages (including third party frameworks) should be written to these standards, but where an existing library has a different style, **internal consistency is preferred.**

### Overriding Principle
Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.

### Descriptive: Naming Styles
There are a lot of different naming styles. It helps to be able to recognize what naming style is being used, independently from what they are used for.

The following naming styles are commonly distinguished:
- `lowercase`
- `lower_case_with_underscores`
- `UPPERCASE`
- `UPPER_CASE_WITH_UNDERSCORES`
- `CapitalizedWords` (or CapWords, or CamelCase). This is also sometimes known as StudlyCaps.
Note: When using acronyms in CapWords, capitalize all the letters of the acronym. Thus HTTPServerError is better than HttpServerError.

- `mixedCase` (differs from CapitalizedWords by initial lowercase character!)
- `Capitalized_Words_With_Underscores` (ugly!)

In addition, the following special forms using leading or trailing underscores are recognized (these can generally be combined with any case convention):

- `_single_leading_underscore`: weak “internal use” indicator. E.g. `from M import *` does not import objects whose names start with an underscore.
- `single_trailing_underscore_`: used by convention to avoid conflicts with Python keyword, e.g.
    ```
    tkinter.Toplevel(master, class_='ClassName')
    ```
- `__double_leading_underscore`: when naming a class attribute, invokes name mangling (inside class FooBar, `__boo` becomes `_FooBar__boo`; see below).
- `__double_leading_and_trailing_underscore__`: “magic” objects or attributes that live in user-controlled namespaces. E.g. `__init__`, `__import__` or `__file__`. Never invent such names; only use them as documented.

### Prescriptive: Naming Conventions

#### Names to Avoid

**Never** use the characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single character variable names.
In some fonts, **these characters are indistinguishable from the numerals one and zero**. When tempted to use ‘l’, use ‘L’ instead.

#### Package and Module Names

**Modules should have short, all-lowercase names.** Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

#### Class Names

**Class names should normally use the CapWords convention.**
The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

#### Type Variable Names

**Names of type variables introduced in PEP 484 should normally use CapWords preferring short names:** T, AnyStr, Num. It is recommended to add suffixes _co or _contra to the variables used to declare covariant or contravariant behavior correspondingly:

```
from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)
```

#### Exception Names

Because exceptions should be classes, the class naming convention applies here. However, **you should use the suffix “Error” on your exception names** (if the exception actually is an error).

#### Global Variable Names

The conventions are about the same as those for functions.

Modules that are designed for use via `from M import *` **should use the `__all__` mechanism to prevent exporting globals**, or use the older convention of prefixing such globals with an underscore.

#### Function and Variable Names

**Function names should be lowercase, with words separated by underscores as necessary to improve readability.**
Variable names follow the same convention as function names.
mixedCase is allowed only in contexts where that’s already the prevailing style to retain backwards compatibility.

#### Function and Method Arguments

Always use `self` for the first argument to instance methods.
Always use `cls` for the first argument to class methods.
If a function argument’s name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus `class_` is better than `clss`. (Perhaps better is to avoid such clashes by using a synonym.)

#### Method Names and Instance Variables

Use the function naming rules: **lowercase with words separated by underscores as necessary to improve readability.**
Use one leading underscore only for non-public methods and instance variables.
To avoid name clashes with subclasses, use two leading underscores to invoke Python’s name mangling rules.

#### Constants

Constants are usually defined on a module level and **written in all capital letters with underscores separating words.** Examples include `MAX_OVERFLOW` and `TOTAL`.

#### Designing for Inheritance

Always decide whether a class’s methods and instance variables (collectively: “attributes”) should be public or non-public. If in doubt, choose non-public; it’s easier to make it public later than to make a public attribute non-public.

Public attributes are those that you expect unrelated clients of your class to use, with your commitment to avoid backwards incompatible changes. Non-public attributes are those that are not intended to be used by third parties; you make no guarantees that non-public attributes won’t change or even be removed.

We don’t use the term “private” here, since no attribute is really private in Python (without a generally unnecessary amount of work).

With this in mind, here are the Pythonic guidelines:
- Public attributes should have no leading underscores.
- If your public attribute name collides with a reserved keyword, append a single trailing underscore to your attribute name. This is preferable to an abbreviation or corrupted spelling.
- For simple public data attributes, it is best to expose just the attribute name, without complicated accessor/mutator methods. Keep in mind that Python provides an easy path to future enhancement, should you find that a simple data attribute needs to grow functional behavior. In that case, use properties to hide functional implementation behind simple data attribute access syntax.
- If your class is intended to be subclassed, and you have attributes that you do not want subclasses to use, consider naming them with double leading underscores and no trailing underscores. This invokes Python’s name mangling algorithm, where the name of the class is mangled into the attribute name. This helps avoid attribute name collisions should subclasses inadvertently contain attributes with the same name.

## Programming Recommendations

- Code should be written in a way that does not disadvantage other implementations of Python (PyPy, Jython, IronPython, Cython, Psyco, and such).
- Comparisons to singletons like None should always be done with `is` or `is not`, never the equality operators.
Also, beware of writing `if x` when you really mean `if x is not None`.
- Use `is not` operator rather than `not ... is`. While both expressions are functionally identical, the former is more readable and preferred:
    
    ```
    # Correct:
    if foo is not None:
    ```
    
- When implementing ordering operations with rich comparisons, it is best to implement all six operations (`__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`) rather than relying on other code to only exercise a particular comparison.
To minimize the effort involved, the `functools.total_ordering()` decorator provides a tool to generate missing comparison methods.
- Always use a `def` statement instead of an assignment statement that binds a lambda expression directly to an identifier:
    
    ```
    # Correct:
    def f(x): return 2*x
    ```
    
- Derive exceptions from `Exception` rather than `BaseException`. Direct inheritance from `BaseException` is reserved for exceptions where catching them is almost always the wrong thing to do.
- Use exception chaining appropriately. `raise X from Y` should be used to indicate explicit replacement without losing the original traceback.
- When catching exceptions, mention specific exceptions whenever possible instead of using a bare `except:` clause:
    
    ```
    try:
        import platform_specific_module
    except ImportError:
        platform_specific_module = None
    ```
    
A bare `except:` clause will catch SystemExit and KeyboardInterrupt exceptions, making it harder to interrupt a program with Control-C, and can disguise other problems. If you want to catch all exceptions that signal program errors, use `except Exception:` (bare except is equivalent to `except BaseException:`).
- When catching operating system errors, prefer the explicit exception hierarchy introduced in Python 3.3 over introspection of `errno` values.
- Additionally, for all try/except clauses, limit the try clause to the absolute minimum amount of code necessary. Again, this avoids masking bugs:
    
    ```
    # Correct:
    try:
        value = collection[key]
    except KeyError:
        return key_not_found(key)
    else:
        return handle_value(value)
    ```
