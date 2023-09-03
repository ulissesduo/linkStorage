import requests
import json
import os

# Define the URL of a website you want to test
link = "firebaseurl.com"

print('Welcome to LinksStorage!!')

def load():
    while True:
        opt = input('1 - New link\n2 - Get all\n3 - by title\n4 - by group\n5 - delete title\n6 - update group\n7 - select links with the same group\n8 - update all records with the same group\n9 - Help\n0 - Exit\n')
    
        if opt == '1':
            insert_data()
        elif(opt=='2'):
            get_all()
        elif(opt=='3'):
            title = input('Type a title: ')
            select_by_title(title)
        elif(opt=='4'):
            title = input('Type a group: ')
            select_by_group(title)   
        elif(opt=='5'):
            title = input('Type a title to delete: ')
            delete_link_by_title(title)
        elif(opt=='6'):
            group = input('Type a grup: ')
            update_link(group)
        elif(opt=='7'):
            group = input('Type a grup: ')
            select_same_groups(group)
        elif opt == '8':
            current_group = input('Type the current group: ')
            new_group = input('Type the new group: ')
            update_group_for_records(select_same_groups(current_group), new_group)
        elif opt == '9':
            help()
        elif(opt=='0'):
            exit()
        else:
            print('Only numbers (1-9)')
   



def get_all():
    os.system('cls') or None
    try:    
        request = requests.get(f'{link}/.json')
        print(request)
        dic_request = request.json()
        print(dic_request['yourNode'])
    except Exception as e:
        print('Banco vazio!!')

def select_by_title(title):
    os.system('cls') or None
    #print (f'{link}/yourNode/.json')
    request = requests.get(f'{link}/yourNode/.json')
    
    dic_request = request.json()

    found = False  # Initialize a flag to track if a match has been found
    try:
        for id_link in dic_request:
            data = dic_request[id_link]
            title_link = data.get('title', '')
            links = data.get('link', '')
            groups = data.get('group', '')
            if title_link == title:
                print(f'title: {title_link}, link: {links}, group: {groups}')
                found = True  # Set the flag to True to indicate a match
                id_teste = id_link
                return id_teste
        if not found:
            print('No records found')
    except Exception as e:
        print('The database is empty!')


def select_by_group(group):
    os.system('cls') or None

    request = requests.get(f'{link}/yourNode/.json')
    dic_request = request.json()
    found = False  # Initialize a flag to track if a match has been found

    try:
        for id_link in dic_request:
            data = dic_request[id_link].get('group', None)

            if data is not None and data == group:
                # Record matches the condition, print it
                print(f'FOUND: id: {id_link},group: {data}')
                found = True  # Set the flag to True to indicate a match
                return id_link
        if not found:
            print('No records found!')
    except Exception as e:
        print(f'Empty database!')


def select_same_groups(group):
    os.system('cls') or None

    same_group = []
    try:
        request = requests.get(f'{link}/yourNode/.json')
        dic_request = request.json()
        for id in dic_request:
            data = dic_request[id]['group']
            if data is not None and data == group:
                # Record matches the condition, print it
                same_group.append({'id': id, 'group': data})
                print(f'FOUND: id: {id}, group: {data}')
                print(id)
                print('same_group: ' + str(same_group))
    except Exception as e:
        print('something gets wrong ' + e)
    return same_group


def insert_data():
    os.system('cls') or None

    while True:
        title = input("title: ")
        myLinks = input("New link: ")
        linksGroup = input("Group: ")
    
        if not title or not myLinks or not linksGroup:
            print('Fullfill all the fields correctly!')
        else:
            id_teste = select_by_title(title)
            if id_teste is not None:
                print('Title already exists. Choose a different title.')
            else:
                dados = { 'title': title, 'link': myLinks, 'group': linksGroup }
                request = requests.post(f'{link}/yourNode/.json', data=json.dumps(dados))
                print(request)
                print(request.text)
                if request.status_code == 200:
                    print('Data inserted successfully!!')
                else:
                    print('Failed to insert data. Certify to fullfill all the fields!') 
                break


def update_link(group):
    os.system('cls') or None

    id = select_by_group(group)
    if id is not None:
        titles = input('title: ')
        links = input('link: ')
        groups= input('group: ')
        dados = { 'title': titles, 'link': links, 'group': groups }
        request = requests.patch(f'{link}/yourNode/{id}/.json', data=json.dumps(dados))
        print(request)
        print(request.text)
    else:
        return

def update_group_for_records(records, new_group):
    os.system('cls') or None

    try:
        for record in records:
            id = record['id']
            
            # Update the group value for each record
            updated_data = {'group': new_group}
            request = requests.patch(f'{link}/yourNode/{id}.json', json=updated_data)
            
            if request.status_code == 200:
                print(f'Record with id: {id} updated successfully.')
            else:
                print(f'Failed to update record with id: {id}.')
                print(f'Status Code: {request.status_code}')
                print(f'Response Text: {request.text}')
    except Exception as e:
        print(f'Something went wrong during update: {str(e)}')

# Call the function to retrieve records with the same 'group' value
# group_to_find = 'YourDesiredGroup'
# matching_records = select_same_groups(group_to_find)
# 
# if matching_records:
#     # Call the function to update the group for matching records to a new group
#     new_group = 'NewGroup'
#     update_group_for_records(matching_records, new_group)
# else:
#     print(f'No records found with group: {group_to_find}.')

def delete_link_by_title(title):
    os.system('cls') or None

    # get the id retrieved by title select
    id_link = select_by_title(title)  # Use select_by_title to find the record
    if id_link is not None:
        # Delete the record with the id_venda
        request = requests.delete(f'{link}/yourNode/{id_link}.json')
        print(request)
        print(request.text)     
    else:
        return

def help():
    os.system('cls') or None

    print('How does it works?')
    print('Select the actions on menu options (1-9)')
    print('1 - This action is responsible to register a new link.\nEvery link contains three properties: \nTitle: Set a title to every link to easily find your links related to an specific subject.\nLink: here we insert the link itself.\nGroup: here you set a group to every link. This resource makes easier to relate the links with the same context.\nFor example: how to connect my Python program to Firebase. If I have three links with articles/youtube videos teaching how to connect a Python program to Firebase I can add these links on the same group.')
    print('2 - This action retrieves all the links that you have been registered.')
    print('3 - This action retrieves an specific link searching by its title.')
    print('4 - This action retrieves an specific link searching by its group.')
    print('5 - This action deletes a link by its title.')
    print('6 - This action updates all the attributes of an specific link.')
    print('8 - This action updates a group: all the links of the same group will be affected.')
    print('7 - This action retrieves all the links on the same group')
    print('0 - Exit')    
    #condition to clear the console and use a input to get back to menu clearing console again.

load()

#Create a method to validate if the title, link or group already exists.