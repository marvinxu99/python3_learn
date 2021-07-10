class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList([1, 2, 3, 4, 5])
super_list1.append(8)

print(len(super_list1))
print(super_list1)

print(issubclass(SuperList, list))
print(issubclass(list, object))
