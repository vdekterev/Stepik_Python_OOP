class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        import random
        import string

        chars_email = string.ascii_letters + string.digits + '_'
        email = ''.join([random.choice(chars_email)
                         for _ in range(random.randint(3, 99))]) + '@'
        email += ''.join([random.choice(chars_email)
                          for _ in range(random.randint(3, 49))]) + '.'
        email += ''.join([random.choice(chars_email)
                          for _ in range(2, 5)])
        return email

    @classmethod
    def check_email(cls, email: str):
        import string
        chars = string.ascii_letters + string.digits + '@._'
        if not cls.__is_email_str(email) or '@' not in email or '.' not in email or '..' in email:
            return False
        elif any(map(lambda l: l not in chars, email)):
            return False
        elif len(email.split('@')[0]) > 100 or len(email.split('@')[1]) >= 50 or '.' not in email.split('@')[1]:
            return False
        else:
            return True

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

