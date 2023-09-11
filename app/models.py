from flask_login import UserMixin

class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class UserModel(UserModel):
    def __init__(self, user_data):
        """
        :param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password
        