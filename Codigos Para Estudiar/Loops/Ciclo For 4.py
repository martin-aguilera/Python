import sys

# #----------NO----------#
# square = []
# for i in range(20):
#     square.append(i*i)
# print(square)
# print(sys.getsizeof(square), "bytes")
# #----------NO----------#

# ----------------SI----------------#
squares = (i * i for i in range(20))
print(squares)
print(sys.getsizeof(squares), "bytes")
# ----------------SI----------------#
