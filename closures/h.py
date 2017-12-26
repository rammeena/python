def f1(): #outer function
    x = 1
    def f2(a): #inner function
        x = 4
        print(a + x)
    print(x)
    f2(2)

f1()
