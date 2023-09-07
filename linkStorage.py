from interface import LinkStorageInterface

class LinkStorage(LinkStorageInterface):
    def __init__(self, db):
        self.db = db

    def create_link(self, link, group, title):
        new_link = {
            "link": link,
            "group": group,
            "title": title,
        }
        self.db.child("Produtos").push(new_link)

    def read_links(self):
        return self.db.child("Produtos").get().val()

    def update_link(self, link_id, link_data):
        self.db.child("Produtos").child(link_id).update(link_data)

    def update_title(self, currentTitle, newtitle):
        links = self.db.child("Produtos").get()
        for link in links.each(): #select speciic record with specific title value
            if link.val()['title'] == currentTitle:
                self.db.child("Produtos").child(link.key()).update({'title':newtitle})

    def update_entire_link(self, title, new_title, new_link, new_group):
        # Search for links with the given title
        links = self.db.child("Produtos").get().val()
        updated = False
       
        for link_id, link_data in links.items():
            if link_data['title'] == title:
                # Update the link with the new data
                link_data['title'] = new_title
                link_data['link'] = new_link
                link_data['group'] = new_group
                self.db.child("Produtos").child(link_id).update(link_data)
                updated = True
                print(f"Link with title '{title}' updated successfully.")
                break  # Exit the loop once the link is found and updated

        if not updated:
            print(f"Link with title '{title}' not found in the database.")


    def delete_link(self, link_id):
        self.db.child("Produtos").child(link_id).remove()

    def delete_link_by_title(self, title):
        #title = input('Enter a title to delete class: ') 
        links=self.db.child("Produtos").get()
        for link in links.each(): #select speciic record with specific title value
            if link.val()['title'] == title:
                self.db.child("Produtos").child(link.key()).remove()

   
            