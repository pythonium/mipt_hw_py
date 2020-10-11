class WrongUserName(Exception):
    def __init__(self, username):
        self.username = username
        self.message = "no such username"
        super().__init__(self.message)

username = 'maxlaimon'
if username != 'plutonium':
	raise WrongUserName(username)

