import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

        
def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)






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


def update_client(client_id, updated_client):
    global clients

    if len(clients) -1 >= client_id:
        clients[client_id] = updated_client
    else:
      print('Client not in client\'s list')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }

    return client


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


def run():
    _initialize_clients_from_storage()
    _print_welcome()

    command = None

    while not command:
        command = input('> ')
        command = command.upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
    elif command == 'D':
        list_clients()
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
    elif command == 'U':
        list_clients()
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            _invalid_name(client_name)
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')

    _save_clients_to_storage()

if __name__ == '__main__':
    run()