def sstr(ch):
    if ch == '':
        return '-'
    else:
        return str(ch)

def write_key(list):
    with open('key.txt','w+') as doc:
        for key in list:
            doc.write(sstr(key) + ' ')
        doc.close()

def read_key():
    with open('key.txt','r') as doc:
        data = doc.read()
        data = data.replace(' ', '')
        lst = list(data)
        
        return lst