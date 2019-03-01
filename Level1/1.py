words = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def caesar(char):
    if char == "y":
        return "a"
    elif char == "z":
        return "b"
    elif char.isalpha():
        return chr(ord(char) + 2)
    else:
        return char

print("".join(list(map(lambda x: caesar(x), words))))

print("".join(list(map(lambda x: caesar(x), "map"))))
