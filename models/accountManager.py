from utils.utils import generate_random_email,generate_random_name,generate_random_password

class AccountManager:
    def __init__(self):
        self.full_name = generate_random_name(10)
        self.email = generate_random_email(10)
        self.password = generate_random_password(10)

    def get_account_details(self):
        return self.full_name, self.email, self.password