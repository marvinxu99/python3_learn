# https://realpython.com/python-bytes/
# When single bytes don’t cut it, you can group them into larger units of information called words
# endianness or byte orde

data = bytes([0, 48, 140, 201])

data_little = int.from_bytes(data, byteorder="little")
data_big = int.from_bytes(data, byteorder="big")

print(data_little, data_big, sep=', ')
# 3381407744, 3181769

little_endian = format(data_little, "032b")
big_endian = format(data_big, "032b")

print(little_endian, big_endian, sep="\n")

print(little_endian == big_endian[::-1])
# False

# The internal bit numbering within each byte remains consistent and unambiguous
import textwrap
print(
     " ".join(textwrap.wrap(little_endian, 8)),
     " ".join(textwrap.wrap(big_endian, 8)),
     sep="\n"
)

# Find out youy hardware native byte order:
import sys
print(sys.byteorder)
# little
