def luck(fn):
    def mfn():
        print("Good Morning")
        fn()
        print("Choose any one number")
    return mfn
@luck
def hello():
    print("Hello Dear!!!")

def add(a,b):
    print(a+b)
hello()
add(6,11)