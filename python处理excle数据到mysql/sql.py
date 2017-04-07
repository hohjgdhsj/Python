#!/usr/bin/python
#coding=utf-8


print ("____________________________________________________________________________________________________________________")

print ("excle表格数据转SQL语句Tools")

print ("Author By Jas502n")

print ("示例数据====张永梅 371323198411235528 123456 371323198411235528 潍坊市 诸城市 诸城市龙源学校 初中思想品德班 诸城市龙源学校 15762683579 初中思想品德")

print ("____________________________________________________________________________________________________________________\n")


#a = open('/root/sql/user.txt').read()

a=raw_input("大黑阔，请输入你要处理的数据=")

b=b=','.join(map(lambda x: "'%s'" % x, a.split(" ")))

c="insert into teacher values  ("

d=");"

e=c+" "+b+" "+d+"\n"

print e


with open('/root/sql/password.txt','a') as f:
    f.write(e)
