import zipfile

z = zipfile.ZipFile("channel.zip")
nothings = ["90052"]
while True:
    content = z.read("{seed}.txt".format(seed=nothings[-1])).decode("utf-8")
    if content.split()[-1].isdigit():
        nothings.append(content.split()[-1])
        print(z.getinfo("{seed}.txt".format(seed=nothings[-1])).comment.decode("utf-8"), end="")
    else:
        break
    
