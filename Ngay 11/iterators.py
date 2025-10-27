# Iterators bộ lặp
# là 1 đối tượng có thể u=duyệt qua các phần tử trong 1 container

# Tạo Iter bằng CLASS

class DemSo:
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            result = self.n
            self.n += 1
            return result
        else:
            raise StopIteration


dem = DemSo(5)

for so in dem:
    print(so)

#  dùng next()
dem2 = DemSo(3)
print(next(dem2))
print(next(dem2))
print(next(dem2))

# Iterator ngược
class IteratorNguoc:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


# Sử dụng
nguoc = IteratorNguoc([1, 2, 3, 4, 5])

for item in nguoc:
    print(item)
# Kết quả: 5, 4, 3, 2, 1