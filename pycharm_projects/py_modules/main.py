from utils import multiply, divide    # module
from shopping.shopping_cart import buy    # package


print(multiply(2, 3))
print(divide(2, 3))

print(buy('apple'))

if __name__ == '__main__':
    print("please run this")