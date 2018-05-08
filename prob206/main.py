import itertools
from decimal import *
import multiprocessing as mp

# # This will take a while to run. Just know that in advance.
#
#
# # This will find the unique value in the form 1_2_3_4_5_6_7_8_9_0 that is a
# # perfect square. Each _ could be any decimal digit.
# # See https://projecteuler.net/problem=206
# def find_square():
#     # set the precision to 30 digits -- this provides some overhead as you only
#     # need about 20 for this problem
#     getcontext().prec = 30
#
#     for i1 in range(0, 10):
#         for i2 in range(0, 10):
#             print("progress: %d%d%%" % (i1, i2))
#             for i3 in range(0, 10):
#                 for i4 in range(0, 10):
#                     for i5 in range(0, 10):
#                         for i6 in range(0, 10):
#                             for i7 in range(0, 10):
#                                 for i8 in range(0, 10):
#                                     for i9 in range(0, 10):
#                                         # Yeah I know this is a lot of for loops
#                                         # but it is only doing this 10^9 times
#                                         # at the most. So technically it's O(1)
#                                         # since it's not dependent on the size of
#                                         # any input...
#                                         # Also I know this is indented a lot, but
#                                         # that's just python. Sorry.
#                                         num = "1%d2%d3%d4%d5%d6%d7%d8%d9%d0" % \
#                                               (i1, i2, i3, i4, i5, i6, i7, i8, i9)
#                                         if "." not in str(Decimal(num).sqrt()):
#                                             return num
#
#
# print(find_square())
# print("done")




def square_root(i1, i2, i3, i4, i5, i6, i7, i8, i9):
    num = "1%d2%d3%d4%d5%d6%d7%d8%d9%d0" % \
          (i1, i2, i3, i4, i5, i6, i7, i8, i9)
    # default decimal precision is 28 digits - more than enough
    return str(Decimal(num).sqrt())


if __name__ == '__main__':
    pool = mp.Pool(processes=4)
    print(filter(lambda x: "." not in x, [pool.apply(square_root, args=(i1, i2, i3, i4, i5, i6, i7, i8, i9,))
          for i1, i2, i3, i4, i5, i6, i7, i8, i9 in itertools.product(range(0, 10), repeat=9)] ))
    print("done")
