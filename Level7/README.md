# Level 7 - smarty


### 本关 url

[http://www.pythonchallenge.com/pc/def/oxygen.html](http://www.pythonchallenge.com/pc/def/oxygen.html)


### content

这一关只有一张题图，没有任何其它提示，连页面源码里面也没有任何提示，只能从题图入手了。

题图里面最显眼的就是一条灰色长条，使用 PIL 去解析一下，确定了灰色长条的是一个宽 608 像素、高 9 像素的区域，并且这个区域内的每一个像素的 R、G、B 值都是相同的。

在仔细看一下，发现这个区域的每一行都是一样的，也就是一行像素重复了九次。

把重复的内容都去掉，也就是只取第一行每个像素的 R（或 G、或 B）值，可以发现，都是一些从几十到一百多不等的数字。这个时候可以联想到 ASCII 码了。

按照 ASCII 码转译一下，得到了一句话：“smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]”

再将列表里面的数字按照 ASCII 码转译一次，就得到了 integrity。

跳转 [http://www.pythonchallenge.com/pc/def/integrity.html](http://www.pythonchallenge.com/pc/def/integrity.html) 进入下一关。


### 下一关

[http://www.pythonchallenge.com/pc/def/integrity.html](http://www.pythonchallenge.com/pc/def/integrity.html)
