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


# test 09.3
user = User('William', 'Smith')
print(user.describe_user(1))
user.email = 'wsmith@google.com'
user.phone = '+10123567890'
user.nickname = 'Tank'
print(user.describe_user(2))
print(' \u2022 '.join(user.describe_user(1, 2)))

print(user.greet_user())

# test 09.5
user = User('Mike', 'Carter', email='mcarter@hotmail.com', phone='+1289364276428', nickname='MCAT')
print(user.greet_user())
print(*user.describe_user(1), end='')
print("'s login attempts =", user.login_attempts)

user.increment_login_attempts()
user.increment_login_attempts()
print(*user.describe_user(1), end='')
print("'s login attempts =", user.login_attempts)

user.reset_login_attempts()
print(*user.describe_user(1), end='')
print("'s login attempts =", user.login_attempts)
