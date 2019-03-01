# Level 2 - ocr


### 本关 url

[http://www.pythonchallenge.com/pc/def/ocr.html](http://www.pythonchallenge.com/pc/def/ocr.html)


### content

首先看页面文字：

> recognize the characters. maybe they are in the book, but MAYBE they are in the page source.

尽管这一关的名称叫做 ocr，但如果想从题图这种渣画质的图片里 ocr 到什么有用的信息，还是不可能的。所以还是按照提示去看页面的源码吧（这个伎俩在网页加密游戏里面已经是三板斧的存在了）。

打开页面的源码会看到注释里有一大堆的符号，前面还有一行字：

> find rare characters in the mess below:

也就是要在这一堆符号里找到仅有的字母。

熟悉 Python 的人恐怕一下子就想到了三种以上的方法，所以我还是选择了 string.isalpha() 这种最简单的方式，再上一个 filter，答案立即出现。

```
>>> mess = ""  # 乱码就不放了
>>> print("".join(list(filter(lambda x: x.isalpha(), mess))))
equality
```

跳转 [www.pythonchallenge.com/pc/def/equality.html](www.pythonchallenge.com/pc/def/equality.html) 进入下一关。


### 下一关

[www.pythonchallenge.com/pc/def/equality.html](www.pythonchallenge.com/pc/def/equality.html)
