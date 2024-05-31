class father:
    def __init__(self,name,age):
        self.father_name= name
        self.father_age= age
        print("constructor is executed")

    def display(self):
        print("may father name is", self.father_name)
        print("my father age is", self.father_age)

class Son(father):
    def son_hii(self):
        print("hi i am v")
        print("my age is 20")
son_obj = Son("ash",45)
print(son_obj.father_age)

son_obj.display()