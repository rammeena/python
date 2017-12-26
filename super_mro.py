class a:
    def foo(self):
        print("a-foo")
    def bar(self):
        print("a-bar")
class b:
    def foo(self):
        print("b-foo")
    def bar(self):
        print("b-bar")
class c1(a,b):
    def foo(self):
        print("c1-foo")
    def bar(self):
        print("c1-bar")
class c2(a,b):
    def foo(self):
        print("c2-foo")
    def bar(self):
        print("c2-bar")
class abcd(c1,c2):
    def foo(self):
        print("abcd-foo")
    def bar(self):
        print("abcd-bar")
class c3(a,b):
    def foo(self):
        print("c3-foo")
    def bar(self):
        print("c3-bar")
class c4(a,b):
    def foo(self):
        print("c4-foo")
    def bar(self):
        print("c4-bar")
class efgh(c3,c4):
    def foo(self):
        print("efgh-foo")
    def bar(self):
        print("efgh-bar")
class ram(abcd, efgh): pass
