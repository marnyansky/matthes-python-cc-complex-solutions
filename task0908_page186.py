class User:

    def __init__(self, first_name='John', last_name='Doe', **optional_info):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        try:
            self.email = optional_info['email']
            self.phone = optional_info['phone']
            self.nickname = optional_info['nickname']
        except:
            pass

    def greet_user(self):
        return "Hello, " + self.first_name + " " + self.last_name + "! Nice to see you again.\n"

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self, *args):  # int: 1, 2
        user_main_info = [self.first_name, self.last_name]
        res = []
        if args.__contains__(1):
            res += user_main_info
        if args.__contains__(2):
            user_optional_info = [self.email, self.phone, self.nickname]
            res += user_optional_info
        return res


class Admin(User):

    def __init__(self, **optional_info):
        super().__init__(**optional_info)
        self.privileges = ()

    def set_privileges(self, *args):
        self.privileges += args
        return self.privileges

    def get_privileges(self):
        return "Current Admin privileges:", *self.privileges


class Privileges:

    def __init__(self):
        self.privileges = 'sending messages', 'deleting users', 'ban users'

    def show_privileges(self):
        return self.privileges


# test 09.7
admin1 = Admin()
admin1.set_privileges('sending messages', 'deleting users', 'ban users')
print(admin1.get_privileges())

# test 09.8
Admin.privileges = Privileges()
print(Admin.privileges.show_privileges())
admin2 = Admin()
admin2.get_privileges()
