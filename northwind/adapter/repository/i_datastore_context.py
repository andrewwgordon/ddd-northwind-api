from abc import ABC, abstractclassmethod

class IDatastoreContext(ABC):    
  
    @abstractclassmethod
    def open(self):
        pass

    @abstractclassmethod
    def get_connection(self):
        pass

    @abstractclassmethod
    def close_connection(self):
        pass