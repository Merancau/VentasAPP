import sys

clients = ['Pablo', 'Ricardo']


def _invalid_name(client_name):
    print(f'{client_name} is not in client\'s list')


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx} {client}')


def update_client(client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        updated_client_name = None

        while not updated_client_name:
            updated_client_name = input('What is the updated client name? ')
        
        clients[index] = updated_client_name
    else:
       _invalid_name(client_name)


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        _invalid_name(client_name)


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('''Welcome to PLATZI VENTAS
    
    What would you like to do today?
    
    [L]ist   client
    [C]reate client
    [D]elete client
    [U]pdate client
    [S]earch client''')


def _get_client_name():
    client_name = None

    while not client_name: 
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def run():
    _print_welcome()

    command = None

    while not command:
        command = input('> ')

    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()     
        update_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print(f'{client_name} is in the client\'s list')
        else:
            _invalid_name(client_name)
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')


if __name__ == '__main__':
    run()