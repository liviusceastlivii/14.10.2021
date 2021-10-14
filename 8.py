a="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
for i in range(len(a)):
    if a[i]!=' ' and a[i]!='Z':
        a=a.replace(a[i],chr(ord(a[i])+1))
    if a[i]=='Z':
            a=a.replace(a[i],'A')
    if a[i]==' ':
        a=a.replace(a[i],'-')
print(a)
