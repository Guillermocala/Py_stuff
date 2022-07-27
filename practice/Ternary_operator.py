"syntax [on_true] if [expression] else [on_false]"

"simple method"
a, b = 10, 20
min = a if a < b else b

"""
direct method by using tuples
(if_test_false, if_test_true) [test]
# if [a < b] is true it return 1, so element with 1 index will print
# else if [a < b] is false it return 0, so element with 0 index will print
"""
print((b, a) [a < b])

"""
direct method by using dictionary
if [a < b] is true then value of True key will print
else if [a < b] is false then value of False key will print 
"""
print({True: a, False: b} [a < b])

"""
direct method by using lambda
lambda is more efficient than above two methods because in lambda we are assure that
only one expression will be evaluated unlike in tuple and Dictionary
"""
print((lambda: b, lambda: a)[a < b]())

"ternary operator can be written as nested id-else"
print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")