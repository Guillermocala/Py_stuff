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
All identifiers in the Python standard library MUST use ASCII-only identifiers, and SHOULD use English words wherever feasible (in many cases, abbreviations and technical terms are used which aren’t English).

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

### Module Level Dunder Names
Module level “dunders” (i.e. names with two leading and two trailing underscores) such as `__all__`, `__author__`, `__version__`, etc. should be placed after the module docstring but before any import statements except from `__future__` imports. Python mandates that future-imports must appear in the module before any other code except docstrings:
```
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

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









