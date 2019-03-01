# Level 4 - follow the chain


### 本关 url

[http://www.pythonchallenge.com/pc/def/linkedlist.php](http://www.pythonchallenge.com/pc/def/linkedlist.php)


### content

这个关卡页面没有任何文字提示，但发现题图是可以点击的。尝试点击题图，发现打开了 [http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345](http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345) 这个 url，而页面上只有一行字：

> and the next nothing is 44827

再访问 [http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827](http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827)，会提示下一个 nothing 的值。到这里应该很明确了，就是不断拿到新的 nothing 值，放到 url 里面，最后可能会拿到某些线索。

这样，从 12345 出发，不断用拿到的新值去替换 url 中的 nothing 参数，最后会在某个时候拿到 peak.html。

跳转 [http://www.pythonchallenge.com/pc/def/peak.html](http://www.pythonchallenge.com/pc/def/peak.html) 进入下一关。


**P.S.** 我是用 while 不断请求页面，用页面内容最后一个单词来充当 nothing 参数的。后来发现这一关居然还有防呆机制。在用某个数字作为 nothing 参数之后，访问页面会得到一句话：

> Yes. Divide by two and keep going.

实际上这个时候应该将当时的 nothing 参数除以 2 再放进去，但我的代码机械地将 "going." 作为 nothing 参数去请求了，居然也给我返回了一个新的 nothing 值。而如果确实用当时的 nothing 参数除以 2 作为新的 nothing 参数，得到的新 nothing 值也会不一样。不过我并没有测试过走哪一条路会比较快。


### 下一关

[http://www.pythonchallenge.com/pc/def/peak.html](http://www.pythonchallenge.com/pc/def/peak.html)
