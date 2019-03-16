from PIL import Image

with Image.open('oxygen.png') as im:
    # 从以下部分代码结果可以看出，灰色长条的 height 范围为 [43, 51]
    # width, height = im.size
    # for h in list(range(height)):
    #     print(h, [im.getpixel((w, h)) for w in list(range(5))])
     
    # 从以下部分代码结果可以看出，灰色长条的 width 范围为 [0, 607]
    # width, height = im.size
    # for h in list(range(43, 52)):
    #     print([im.getpixel((w, h)) for w in list(range(width - 30, width))])
    
    # 从以下部分代码结果可以看出，灰色长条的高度为 9，但每一行都是相同的，可以仅分析一行
    # for h in list(range(43, 51)):
    #     print([im.getpixel((w, h)) for w in list(range(0, 608))] == [im.getpixel((w, h + 1)) for w in list(range(0, 608))])
    
    # 从以下部分代码结果可以看出，每个每个灰色像素的 R,G,B 值都是相同的，且 alpha 通道都是 255
    # print([im.getpixel((w, 43)) for w in list(range(0, 608))])

    print(''.join([chr(im.getpixel((w, 43))[0]) for w in list(range(0, 608))][::7]))

    print(''.join([chr(x) for x in [105, 110, 116, 101, 103, 114, 105, 116, 121]]))
