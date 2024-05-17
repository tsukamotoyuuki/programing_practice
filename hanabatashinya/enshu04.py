beforeChar = input()

if "A" <= beforeChar <= "Z":
    print(chr(ord(beforeChar) - (ord("A")-ord("a"))))
elif "a" <= beforeChar <= "z":
    print(chr(ord(beforeChar) - (ord("a") - ord("A"))))