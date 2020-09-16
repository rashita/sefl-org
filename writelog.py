#writetlog.py

def writelog(aText,filepath):
    with open(filepath) as f:
        l = f.readlines()
    l.insert(0, aText)
    with open(filepath, mode='w') as f:
        f.writelines(l)