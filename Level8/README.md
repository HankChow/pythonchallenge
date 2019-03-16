# Level 8 - working hard?


### 本关 url

[http://www.pythonchallenge.com/pc/def/integrity.html](http://www.pythonchallenge.com/pc/def/integrity.html)


### content

真正的粉丝都是一打开关卡就直奔源代码。首先看到的是那一大串数字，但是再定睛一看，这些数字其实只是把题图中的蜜蜂圈起来，并且圈起来的部分链接到了[另一个网页](http://www.pythonchallenge.com/pc/return/good.html)中。打开这个页面，需要输入用户名和密码。

再回到关卡的源代码，原来最下方还有一段注释，标示着 un 和 pw。

如果妄想着直接把这两个字符串分别作为用户名和密码填入验证框中就可以通关，那就太天真了，这可是第 8 关啊，第 1 关都不止这么简单（其实第 1 关还是比这简单，至少不用看页面源代码……）。

仔细看会发现两个字符串是 BZh 开头的，到这里一般可以想到 bzip2 压缩。将两个字符串用 bz2 包解压缩，可以分别得到 huge 和 file。

P.S. 后来发现，其实题图的蜜蜂、标题的 working hard 都是 bees，也就暗示着 bz，但当时并没有发现……

跳转 [http://www.pythonchallenge.com/pc/return/good.html](http://www.pythonchallenge.com/pc/return/good.html) ，用户名密码分别输入 huge 和 file 进入下一关。


### 下一关

[http://www.pythonchallenge.com/pc/return/good.html](http://www.pythonchallenge.com/pc/return/good.html)
