class Users:
    users = []
    def append(self,user):
        self.users.append(user)
    def getUsers(self):
        return self.users
    def getUser(self,idx):
        return self.users[idx]
    def toString(self):
        strBuffer =""
        for user in self.users: strBuffer += user.toString()
        return strBuffer