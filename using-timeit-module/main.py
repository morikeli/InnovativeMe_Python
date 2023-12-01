# Program to determine how long it takes to print items in a list or a tuple using Python's timeit module.
import timeit

print(timeit.timeit(stmt="['mori', 22, 'Nairobi']", number=1000000))   # print the list a million times and how long it takes to
# print it.
print(timeit.timeit(stmt="('mori', 22, 'Nairobi')", number=1000000))
