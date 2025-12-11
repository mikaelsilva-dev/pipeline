from app.cl import Test



def test_init():
    try:
        d = Test()
        t = True
    except:
        t = False

    assert t  == True

def test_var1():
    d = Test()
    assert d.var1 == 10

def test_var2():
    d = Test()
    assert d.var2 == 20

def test_var3():
    d = Test()
    assert d.var3 == "teste"