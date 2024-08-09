import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    x = int(input("Digite um número inteiro: "))
    y = int(input("Digite um número inteiro: "))
    
    print(f"\nA soma de {x} e {y} é %s" % str(proxy.soma(x, y)))