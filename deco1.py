def bank (fn):
    def mfn():
        print("Transaction initiated")
        fn()
        print("Transaction completed")
    return mfn
def a():
    print("In Progress")
def b():
    print("Amount Transated: xxxxxx")
a1=bank(a)

a1()
a2=bank(b)
a2()