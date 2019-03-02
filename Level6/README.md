# Level 6 - now there are pairs


### 本关 url

[http://www.pythonchallenge.com/pc/def/channel.html](http://www.pythonchallenge.com/pc/def/channel.html)


### content

这一关作者开始向大家众筹了（笑）。

页面上同样是没有任何提示，打开源码，找来找去也就是一个 zip 注释。把 url 改成 channel.zip 的话会提示下载 `channel.zip`，那就用 wget 把 `channel.zip` 下下来。

下下来之后解压，发现是一堆 `<数字>.txt` 和 `readme.txt`，按照 `readme.txt` 的说明，看来这一关的玩法和第 4 关一毛一样。但是……所有文件都到我手里了，我还会去写循环？随意打开其中一个 txt 文件，会看到都是 "Next nothing is ..." 形式的文本，那就直接上 shell 好了：

```
$ find ./ -name "*.txt" | xargs grep -v "Next"
./46145.txt:Collect the comments.
./readme.txt:welcome to my zipped list.
./readme.txt:
./readme.txt:hint1: start from 90052
./readme.txt:hint2: answer is inside the zip
```

果然瞬间找到了要害。

但是 "Collect the comments" 是什么鬼……后来还是 `zipinfo -v channel.zip` 了一下，发现里面的每一个文件都有一个 comment，估计是要把文件的 comment 按顺序连接起来。搞到最后还是要写循环……

循环出来的结果是这样的：

```
***************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
```

如果以为答案是 hockey，跳转到 [http://www.pythonchallenge.com/pc/def/hockey.html](http://www.pythonchallenge.com/pc/def/hockey.html) 之后，作者会很友好地提醒：

> it's in the air. look at the letters. 

那就是 oxygen 啦。

跳转 [http://www.pythonchallenge.com/pc/def/oxygen.html](http://www.pythonchallenge.com/pc/def/oxygen.html) 进入下一关。


### 下一关

[http://www.pythonchallenge.com/pc/def/oxygen.html](http://www.pythonchallenge.com/pc/def/oxygen.html)
