
# 定义函数，且传参
def add(a, b):
    return a + b

# 默认参数
def sale_car(price, length=20, hight=3):
    print(
       'price:', price,
       'length:', length,
       'hight:', hight 
    )


a = 1
b = 2

print("add(a, b): ",add(a, b))

sale_car(20)

# 全局和局部变量
# 定义一个全局变量
X = 100
b = 30
def fun():
    global b
    b = 20
    a = 10
    print("a:", a, ", X:", X)
    
fun()
print("this is a global var:", b)
