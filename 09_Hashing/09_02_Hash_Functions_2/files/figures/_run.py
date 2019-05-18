import os
for s in os.listdir(os.getcwd()):
    if s[-3:] == ".py" != -1 and s[0] != '_' and s[0] != 'a':
        png = s.replace("py", "png")
        os.system("py -2.6 " + s + " "+ png)
        print s



