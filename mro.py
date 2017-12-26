#mro.py
class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass

class X(C, D): pass

print("Success")
