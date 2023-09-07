from abc import ABC, abstractmethod

# Define an interface for the LinkStorage class
class LinkStorageInterface(ABC):
    @abstractmethod
    def create_link(self, link, group, title):
        pass

    @abstractmethod
    def read_links(self):
        pass

    @abstractmethod
    def update_link(self, link_id, link_data):
        pass
    
    @abstractmethod
    def update_title(self, currentTitle, newTitle):
        pass

    @abstractmethod
    def update_entire_link(self, title, new_title, new_link, new_group):
        pass
    
    @abstractmethod
    def delete_link(self, link_id):
        pass

    @abstractmethod
    def delete_link_by_title(title):
        pass