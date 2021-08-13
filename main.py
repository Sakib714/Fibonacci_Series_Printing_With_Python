
a = 10
print(id(a))
def function():

    a = 20
    x = globals()['a']
    print(id(x))
    print('In fun: ',a)
    globals()['a'] = 30
function()
print('Out fun: ',a)






