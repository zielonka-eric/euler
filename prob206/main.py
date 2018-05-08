import itertools
from decimal import *

# This will take a while to run. Just know that in advance.


# This will find the unique value in the form 1_2_3_4_5_6_7_8_9_0 that is a
# perfect square. Each _ could be any decimal digit.
#
# Because the last digit is a 0, the last underscore has to be a 0 because its
# factors all have to be perfect squares. In this case, 100 would be a factor.
#
# See https://projecteuler.net/problem=206
def find_square():
    # set the precision to 24 digits -- this provides some overhead as you only
    # need about 20 for this problem
    getcontext().prec = 24

    for i1, i2 in itertools.product(range(0, 10), repeat=2):
        print("progress: %d%d%%" % (i1, i2))
        for i3, i4, i5, i6, i7, i8 in itertools.product(range(0, 10), repeat=6):
            num = "1%d2%d3%d4%d5%d6%d7%d8%d900" % \
                  (i1, i2, i3, i4, i5, i6, i7, i8)
            #if "." not in str(Decimal(num).sqrt()):
            #    return num
            if int(Decimal(num).sqrt()) ** 2 == Decimal(num):
                return num


print(find_square())
print("done")

