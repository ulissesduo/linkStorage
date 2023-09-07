from connection import db, signup, login
from linkStorage import LinkStorage

def main():
    user = None

    while True:
        if user is None:
            print("Menu:")
            print("1. Sign Up")
            print("2. Login")
            print("3. Exit")
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
            print("6. Exit")
            choice = input("Enter your choice: ")

            link_storage = LinkStorage(db)
            if choice == "1":
                link = input("Enter link: ")
                group = input("Enter group: ")
                title = input("Enter title: ")
                link_storage.create_link(link, group, title)

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
                break
            
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
