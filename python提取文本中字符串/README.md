##使用方法：
##假设文件存放在：/root/other/password.txt

##python user.py 

####//提取username password

example：
2014124203	1225gbb17
2013111120	19931210sjq
2014122221	XILY19950906
2014131214	a9301136
201314E214	sunrui4869
———————————————————————————————————————————————————————
##python password.py

####//提取username&password

example：

username=2013144127&password=dianzi336143
username=2014121111&password=w4207065
username=2014150203&password=624000FAN
username=2013132113&password=gg940726
username=201414A219&password=ljy19591973
username=2013119227&password=1945fank

———————————————————————————————————————————————————
#使用linux的awk提取字符

#使用方法
awk '{pattern + action}' {filenames}
—————————————————————————————————————————————————
#1.命令行方式
awk [-F  field-separator]  'commands'  input-file(s)
其中，commands 是真正awk命令，[-F域分隔符]是可选的。 input-file(s) 是待处理的文件。
在awk中，文件的每一行中，由域分隔符分开的每一项称为一个域。通常，在不指名-F域分隔符的情况下，默认的域分隔符是空格。

#2.shell脚本方式
将所有的awk命令插入一个文件，并使awk程序可执行，然后awk命令解释器作为脚本的首行，一遍通过键入脚本名称来调用。
相当于shell脚本首行的：#!/bin/sh
可以换成：#!/bin/awk

#3.将所有的awk命令插入一个单独文件，然后调用：
awk -f awk-script-file input-file(s)
其中，-f选项加载awk-script-file中的awk脚本，input-file(s)跟上面的是一样的。
http://www.cnblogs.com/ggjucheng/archive/2013/01/13/2858470.html
————————————————————————————————————————————————
cat password.txt | grep password | awk -F ' ' '{print $7}' | awk -F '?' '{print $2}' | awk -F '&' '{print $1"&"$2}' 

example：
username=2013111120&password=19931210sjq
username=2014122221&password=XILY19950906
username=2014131214&password=a9301136
username=201314E214&password=sunrui4869
