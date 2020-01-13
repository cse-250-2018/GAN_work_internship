class A:
    id = -1
    name = 'dummy'
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def show(self):
        print(self.id, self.name)


a = A(101, 'Sarfaraz')
a.show()
a2 = A(102, 'Alam')
a2.show()
