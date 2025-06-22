from Inharitance.Parent import Parent


class Child(Parent):
    def getMe(self):
        return "Hello",self.name, "I am good"

    def childGetMe(self):
        print("I am Child Property")
