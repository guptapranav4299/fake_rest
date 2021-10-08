import xmltodict

mydict = {
    'text':{
        '@color':'red',
        '@stroke':'2',
        '#text':'This is a text'
    }
}

print(xmltodict.unparse(mydict, pretty=True))