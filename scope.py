name= "This is a global name"

def greet():
    name="owen"

    def hello():
        print("hello" +name)

    hello()

greet()
print(name)

x= 50

def func(x):
    print(x)
    x= 20
    print("Local x is", x)

func(x)
