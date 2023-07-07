class rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return 2*(self.l+self.w)

rect_obj = rectangle(9,7)
print(rect_obj.area())
print(rect_obj.perimeter())