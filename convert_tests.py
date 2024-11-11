import convert
def test_convert():
    result=convert.str_to_float("3456")
    expected=3456
    if result==expected:
        print("Passed")
    else:
        print("Failed")

def test_convert2():
    result=convert.str_to_float("hi")
    expected=None
    if result==expected:
        print("Passed")
    else:
        print("Failed")

test_convert()
test_convert2()