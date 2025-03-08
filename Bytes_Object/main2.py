data = [0x52, 0x65, 0x61, 0x6c, 0x20, 0x50, 0x79, 0x74, 0x68, 0x6f, 0x6e]
print(data)

data_str = "".join(map(chr, data))
print(data_str)

# You can quickly check whether a given object supports the buffer protocol by calling memoryview() on it

text_bytes = bytes([0x63, 0x61, 0x66, 0xc3, 0xa9])
text = text_bytes.decode("utf-8")

mem_view = memoryview(text_bytes)
print(mem_view)
# <memory at 0x764ca33de5c0>

try:
    obj = memoryview(text)

except TypeError :
    print("does not support memoryview.")

