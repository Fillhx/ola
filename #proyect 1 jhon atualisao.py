#proyect 1

# CRUD 
#My project pharmacy

clients = "LUIS, MATEO"
def create(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        
    else:
        print("The user already exist.")


def read_client(client_name):
    global clients
    if client_name in clients:
        print("Find user")
    else:
        print("not find user")



def delete_client(client_name):
    global clients
    if client_name in clients:
        # Remove the client name and the trailing comma
        clients = clients.replace(client_name + ",", "")
        print(f"Deleted {client_name}")
        print(clients)
    else:
        print("Client not found")        


def update_client(name, update_name):
    global Clients
    if name in Clients:
        Clients = Clients.replace(name + ",",update_name+",")

    else:
        print("Error103")

def welcome():
    print("Welcome to Pharmacy Univalle")
    print("*" * 60)
    print("What would you like to do Today: ")
    print("[C]reante client")
    print("[R]ead client")    
    print("[U]ptade a client")
    print("[D]elete client or user")

def client_name():
    return input("Enter your name: ").upper()


def lis_clients():
    global clients
    print(clients)



if __name__  == "__main__":  
    welcome()
    option = input("Type your activity: ").upper()
    
    
    if option == "C":
        name = client_name()
        create(name)
        lis_clients()
    
    elif option == "R":
       name = client_name()
       read_client(name)
        
    
    elif option == "U":
        name = client_name()
        new_name = input("enter the update name: ")
        update_client(name,new_name)
        
        
    elif option == "D":
        name = client_name()
        delete_client(name)
   
    
    
    else:
        print("enter a valid option")
        
    
                                                 