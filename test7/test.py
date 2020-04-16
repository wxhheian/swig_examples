# import example
# vi = example.vectori()      #测试vector<int>
# vs = example.vectors()     #测试vector<string>
# vi.push_back(1)
# vs.push_back("abc")
# print(vi[0])
# print(vi.size())
# vi[0] = 10
# print(vi[0])
# print(vs[0])


# #测试多维vector<string>
# import example
# strvec1 = example.vectors()
# strvec1.push_back("abc")
# strvec1.push_back("def")
# strvec2 = example.vectors()
# strvec2.push_back("ghi")
# strvec2.push_back("jkl")
# strmat = example.stringmat()
# strmat.push_back(strvec1)
# strmat.push_back(strvec2)
# print(strmat[1][1])


##测试vector<vector<point>>
# import example
# p1 = example.point()
# p2 = example.point()
# p3 = example.point()
# p4 = example.point()
# p1.i, p1.j = 1,2
# p2.i,p2.j = 3,4
# p3.i, p3.j = 5,6
# p4.i,p4.j = 7,8
# vecstr1 = example.stringvector()
# vecstr1.push_back(p1)
# vecstr1.push_back(p2)
# vecstr2 = example.stringvector()
# vecstr2.push_back(p3)
# vecstr2.push_back(p4)
# vecmat = example.stringmat()
# vecmat.push_back(vecstr1)
# vecmat.push_back(vecstr2)
# print(vecmat[0][1].i)





# import example
# b = example.Bar()
# print(b.x)
# c = example.Bar()
# c.x = b.x       #深拷贝
# print((c.x))
