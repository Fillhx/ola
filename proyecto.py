#CRUD
#My project 
client = "edward, gustavo, ".upper() #variable de tipo string


def createClient(client_name):
    global client
    if client_name not in client: # si no esta el nombre, esto lo añade
        client += client_name
    else:
        print("el cliente ya existe")

    
def read_client(client_name):
    global client
    if client_name in client:
        print("Find user")
    else:
        print("not find user")
        

def delete_client(client_name):
    global client
    if client_name in client:
        # Remove the client name and the trailing comma
        client = client.replace(client_name + ",", "")
        print(f"Deleted {client_name}")
    else:
        print("Client not found")


def UClient():
    global client

    client_name = _get_clientName(client)
    if (client_name in Clients):
        new_client_name = _get_clientName("Enter the new name: ")
        Clients = client.replace(client_name, new_client_name)
    else:
        print("e103")


def _print_welcome():
    print("welcome to pharmacy univalle tulua")
    print("*" * 60)
    print("that would you like to do today")
    print("[C]reate client")
    print("[R]ead client")
    print("[U]pdate client")
    print("[D]elete client")


def _get_clientName():
    return input("enter your name: ").upper()


def list_clients(): #devuelve los clientes simultaneos
    global clients
    print(client)


if __name__ == "__main__":
    _print_welcome()
    option =  input().upper()
    if option == "C":
        client_name = _get_clientName()# se obtiene el nombre del cliente
        createClient(client_name) # se envia el nombre del cliente para crear
        list_clients()
    elif option == "R":
        client_name = _get_clientName()
        read_client(client_name)
    elif option == "U":
        client_name = _get_clientName()
        list_clients()
        pass
    elif option == "D":
        client_name = _get_clientName()
        delete_client(client_name)
        list_clients()
        
    else:
        print("comando invalido")