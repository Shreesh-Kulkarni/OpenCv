s=input()
a="0000000"
b="1111111"
if len(s)<7:
    print("NO")
else:    
    for i in range(len(s)):
        if s[i]=="0":
            if s[i:i+7]==a:
                print("YES")
                break
            else:
                continue
        if s[i]=="1":
            if s[i:i+7]==b:
                print("YES")
                break
            else:
                continue
    else:
        print("NO")
