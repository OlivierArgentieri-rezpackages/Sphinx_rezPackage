

class User():
    """User entity class."""
    
    name = ""
    email = ""
    
    def __init__(self, name, email):
     """Constructor

     :param str name: description of name
     :param str email: description of email
     """
     self.name = name
     self.email = email
    
    
    def change_name(self, new_name):
        """change name of user
        
        :param str new_name: new name of user
        :return: new name of user
        :rtype: str
        """
        
        return new_name
        
        
    
    