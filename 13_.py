import xmlrpc.client


url = 'http://www.pythonchallenge.com/pc/phonebook.php'
print(xmlrpc.client.ServerProxy(url).system.listMethods())
print(xmlrpc.client.ServerProxy(url).system.methodSignature('phone'))
print(xmlrpc.client.ServerProxy(url).system.methodHelp('phone'))
print(xmlrpc.client.ServerProxy(url).phone("Bert"))
