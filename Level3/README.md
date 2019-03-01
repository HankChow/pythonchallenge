# Level 3 - re


### 本关 url

[http://www.pythonchallenge.com/pc/def/equality.html](http://www.pythonchallenge.com/pc/def/equality.html)


### content

还是看页面上的提示文字：

> One small letter, surrounded by EXACTLY three big bodyguards on each of its sides. 

再查看下页面源码，注释块里面又是一大堆乱码。结合提示文字，思路就很明确了。要在这一堆乱码里面，找到“三个大写字母-一个小写字母-三个大写字母”的组合，而且这个小写字母两侧的大写字母都必须【正好】是三个大写字母。

看到这里应该就知道要用正则表达式了（当然如果熟悉 Python，看到这一关的标题就知道要用正则表达式了）。可能是因为前期关卡吧，这个正则表达式也非常入门。

直接上代码：

```
>>> import re
>>> mess = ""  # 乱码就不放了 
>>> re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', mess)
['qIQNlQSLi', 'eOEKiVEYj', 'aZADnMCZq', 'bZUTkLYNg', 'uCNDeHSBj', 'kOIXdKBFh', 'dXJVlGZVm', 'gZAGiLQZx', 'vCJAsACFl', 'qKWGtIDCj']
```

这个时候再把每组匹配结果中间的小写字母拿出来，就可以得到 linkedlist。

跳转 [http://www.pythonchallenge.com/pc/def/linkedlist.html](http://www.pythonchallenge.com/pc/def/linkedlist.html) 进入下一关。


### 下一关

[http://www.pythonchallenge.com/pc/def/linkedlist.html](http://www.pythonchallenge.com/pc/def/linkedlist.html)
