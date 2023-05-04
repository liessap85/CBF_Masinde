var = "4"
sum = var + 4

print(sum)




def checking(valuetocheck):
    if valuetocheck > 4:
    print("bad indent")
    
#checking(6)


def checking2(valuetocheck):
    assert (type(valuetocheck) is float), "You must enter a number"
    assert (valuetocheck > 0), "value must be greater than 0"
    if valuetocheck > 4:
        print("Greater than 4")
        

var = float(input("enter a number: "))
checking2(var)

