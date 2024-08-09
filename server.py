from xmlrpc.server import SimpleXMLRPCServer

def soma(x, y):
    print("\nRequisição recebida com os argumentos " + str(x) + " e " + str(y))
    
    return x + y

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(soma, "soma")
server.serve_forever()