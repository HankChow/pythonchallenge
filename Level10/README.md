# Level 10 - what are you looking at?


### 本关 url

[http://www.pythonchallenge.com/pc/return/bull.html](http://www.pythonchallenge.com/pc/return/bull.html)


### content

这一关的明文提示是某个列表的第 31 个元素长度，点开题图中的牛，可以看到：

> a = \[1, 11, 21, 1211, 111221, 

看见这个数列，对于常常接触解密游戏的，相信已经很熟悉了吧。所以我决定使用旁路方法去解这一关……

这个数列是<ruby>外观数列<rt>Look-and-say sequence</rt></ruby>，OEIS 编号是 A005150。但 A005150 中并没有记载第 31 项的值（是因为太长了……）。

再在 OEIS 上查找，可以看到有一个数列 A005341，它的每一项是 A005150 对应项的位数，找到 A005341 的第 31 项，是5808。

跳转 [http://www.pythonchallenge.com/pc/return/5808.html](http://www.pythonchallenge.com/pc/return/5808.html) 进入下一关 。

P.S. 还是可以写 Python 计算出来的，不然就不是 Pythonchallenge 了。


### 下一关

[http://www.pythonchallenge.com/pc/return/5808.html](http://www.pythonchallenge.com/pc/return/5808.html)
