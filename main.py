import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Sergio',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer'
    }
]


def _invalid_name(client_name):
    print(f'{client_name} is not in client\'s list')


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))


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


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')

    return field


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
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_client(client)
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