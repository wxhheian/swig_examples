#使用pointer_function
# import example
# e = example.Example()
# c = example.new_intp()  #创建int *
# e.add(3,4,c)     #调用函数
# print(example.intp_value(c))   #解除引用
#
# example.intp_assign(c,10)    #对c指向的对象进行赋值
# print(example.intp_value(c))




#使用pointer_class
# import example
# e = example.Example()
# c = example.intp()      #创建一个int*
# e.add(3,4,c)
# print(c.value())   #deference
# c.assign(10)
# print(c.value())



#测试array_functions
# import example
# c = example.new_doubleArray(10)
# for i in range(10):
#     example.doubleArray_setitem(c,i,2*i)
# example.Example().print_array(c)
# example.delete_doubleArray(c)
# example.Example().print_array(c)


#测试array_class
import example
c = example.doubleArray(10)
for i in range(10):
    c[i] =  2 * i
example.Example().print_array(c)
