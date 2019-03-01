# Level 1 - What about making trans?


### 本关 url

[http://www.pythonchallenge.com/pc/def/map.html](http://www.pythonchallenge.com/pc/def/map.html)


### content

常玩解密的人从题图的 K→M、O→Q、E→G 一般可以轻易想到凯撒移位加密，所以页面中的那一串乱码“几乎”可以迎刃而解了。

我一开始就简单粗暴地上 lambda 表达式来解密乱码：

```
lambda x: chr(ord(x) + 2)
```

结果发现 y 和 z 需要分别对应到 a 和 b，不能简单按照 ASCII 来移位。看来页面上的

> everybody thinks twice before solving this.

这一句还是说得挺对的……

把乱码解出来之后，是一句这样的话：

> i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

尽管这句话对通关没有太大的作用，但至少学到了 string.maketrans() 这个很冷门的字符串方法……

最终还是要对 url 中的 “map” 做一次同样的移位，得到 “ocr”。

跳转 [www.pythonchallenge.com/pc/def/ocr.html](www.pythonchallenge.com/pc/def/ocr.html) 进入下一关。


### 下一关

[www.pythonchallenge.com/pc/def/ocr.html](www.pythonchallenge.com/pc/def/ocr.html)
