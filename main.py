from connection import db, signup, login, redefinePass
from linkStorage import LinkStorage
import subprocess
import re
import pyshorteners
import argparse

def main():
    user = None

    while True:
        if user is None:
            print("Menu:")
            print("1. Sign Up")
            print("2. Login")
            print("3. Redefine password")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                created_user = signup()
                if created_user:
                    user = created_user
            elif choice == "2":
                logged_user = login()
                if logged_user:
                    user = logged_user
            elif choice == "3":
                redefine = redefinePass()
                address = redefine['email']
                print('We are opening automatically the browser on gmail for you')
                openAddress = re.split('@|\\.', address)
                subprocess.run(["start", f"http://www.{openAddress[1]}.com"], shell=True)

            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Menu:")
            print("1. Create link")
            print("2. Read links")
            print("3. Delete a link by name")
            print("4. Update link title")
            print("5. Update entire link (link, group and title)")
            print("6. Search title")
            print("7. Update all records with the same group")
            print("8. Searching by group")
            print("9. Exit")
            print("Extra -> type 'open browser' and the DOMAIN of the website that you want to access. Without 'www' and '.com'. Only the domain\nFor example: 'gmail' -> it will open the gmail website")
    
            choice = input("Enter your choice: ")

            link_storage = LinkStorage(db)
            if choice == "1":
                    link = input("Enter link: ")
                    while not link.strip():  # Continue asking until a non-empty input is provided
                        print("Error: Link cannot be empty.")
                        link = input("Enter link: ")
                    
                    s = pyshorteners.Shortener()
                    shortLink = s.tinyurl.short(link)

                    group = input("Enter group: ")
                    while not group.strip():  # Continue asking until a non-empty input is provided
                        print("Error: Group cannot be empty.")
                        group = input("Enter group: ")

                    title = input("Enter title: ")
                    while not title.strip():  # Continue asking until a non-empty input is provided
                        print("Error: Title cannot be empty.")
                        title = input("Enter title: ")

                    # Check if the title already exists in the database
                    existing_titles = link_storage.get_existing_titles()
                    while title in existing_titles:
                        print("Error: Title already exists. Please enter a new title.")
                        title = input("Enter title: ")
                        
        # Call the create_link method with valid input
                    link_storage.create_link(shortLink, group, title)

            elif choice == "2":
                links = link_storage.read_links()
                for link_id, link_data in links.items():
                    print(f"Link ID: {link_id}\n Link: {link_data['link']}\n Group: {link_data['group']}\n Title: {link_data['title']}")
            
            elif choice == "3": #delete complete an specific link register by its title.
                title = input('Enter a title to delete: ')
                link_storage.delete_link_by_title(title)
            
            elif choice == "4": #update an specific title
                currentTitle = input('Current title: ')
                newtitle = input('New title: ')
                link_storage.update_title(currentTitle, newtitle)
            
            elif choice == '5':
                title = input("Enter the title of the link to update: ")
                new_title = input("Enter the new title: ")
                new_link = input("Enter the new link: ")
                new_group = input("Enter the new group: ")
                link_storage.update_entire_link(title, new_title, new_link, new_group)
                
            elif choice == "6":
                print('search group:')
                group = input("Enter the title to search: ")
                searching = link_storage.search_group(group)
                if not searching:
                    print('Not found main.py')
                else:
                    linkSearch = link_storage.search_title(group)
                    for link in linkSearch.each():
                        print(link.val()['title'])
            
            elif choice == "8":
                print('search group:')
                group = input("Enter the group to search: ")
                
                if group.strip():  # Check if group is not empty or contains only whitespace
                    linkSearch = link_storage.search_group(group)                    
                    # print("Debug: group =", group)
                    # print("Debug: linkSearch =", linkSearch)                    
                    linkSearchData = linkSearch.val()  # Retrieve the data using .val()
                    
                    if linkSearchData:
                        for key, record in linkSearchData.items():
                            print("Record ID:", key)
                            print("Title:", record.get("title", "N/A"))
                            # Print other fields as needed
                    else:
                        print('No matching records found.')
                else:
                    print('Group not provided. Stopping execution.')


            elif choice == "7":
                old_group = input('Group to search: ')
                new_group = input('New group for these records: ')
                link_storage.update_group_for_records(old_group, new_group)
            
            elif 'open browser' in choice.lower():
                website = input('Which website do you want to access? ')
                subprocess.run(["start", f"http:\\www.{website}.com"], shell=True)
                words = re.split('@|\\.', website)
                print(words[1])

            elif choice == "9":
                break
            
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
