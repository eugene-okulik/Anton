import random
import string
from faker import Faker


fake = Faker()
fake_data_for_account = {
    'first_name': fake.name().split()[0],
    'last_name': fake.name().split()[1],
    'email': fake.email().replace('@', f'{random.choice(string.ascii_lowercase)}@'),
    'password': fake.password()
}
