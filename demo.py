
"""
1文件的使用方式，打开-操作-关闭(文件的存储状态和文件的占用状态之间的转换)
2文本文件&二进制文件.open(文件的路径和文件名,打开模式)，和.close()
3七种文件打开模式，r(只读模式),w(覆盖写模式),x(创建写模式),a(追加写模式),b,t,+(和rwxa一同使用，在原有的功能上增加同时读写功能)
4文件内容的读取：.read().readline().readlines()
5数据的文件写入：.write().writelines().seek

f.write("啊对对对")
ls = ["小米","华为","苹果"]
f.writelines(ls)#将列表的各个元素直接拼接，没有换行操作
f.seek(0)#改变当前文件操作指针的位置，0-文件开头，1-当前位置，2-文件结尾
"""

fname = input("请输入文件名：")
f = open(fname,"a+")
f.write("啊对对对")

ls = ["小米","华为","苹果"]
f.writelines(ls)#将列表的各个元素直接拼接，没有换行操作，写完之后，指针在文件的末尾
f.seek(1)#改变当前文件操作指针的位置，0-文件开头，1-当前位置，2-文件结尾
#for line in f:
#    print(line)

f.close()
