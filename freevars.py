#freevars.py
p = "func_a passed parameter"
q = "func_b passed parameter"
r = "func_c passed parameter"
s = "func_d passed parameter"

def func_a(a_p):
    var_a = "I am var_a inside func_a"
    def func_b(b_p):
        var_b = "I am var_b inside func_b"
        def func_c(c_p):
            var_c = "I am var_c inside func_c"
            def func_d(d_p):
                print("printing local freevars")
                print()
                print("func_d prints var_a: {}".format(var_a))
                print("func_d prints var_b: {}".format(var_b))
                print("func_d prints var_c: {}".format(var_c))
                print()
                print("printing passed freevars")
                print()
                print("func_d prints passed param a_p: {}".format(a_p))
                print("func_d prints passed param b_p: {}".format(b_p))
                print("func_d prints passed param c_p: {}".format(c_p))
                print("func_d prints passed param d_p: {}".format(d_p))
            return func_d
        return func_c
    return func_b

b = func_a(p)
print(b)
print()
c = b(q)
print(c)
print()
d = c(r)
print(d)
print()
d(s)
