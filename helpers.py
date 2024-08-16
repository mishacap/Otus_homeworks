from faker import Faker
import random



def get_fake_product():
    fake = Faker()
    max_length = random.randint(1, 7)  # Случайное число от 1 до 7
    text = fake.text(max_nb_chars=max_length * 10)  # Генерация текста
    text = text[:max_length]  # Обрезка текста до нужного количества символов
    return text

def get_random_index():
    index = random.randint(0, 3)
    return index

def get_user_data():
    fake = Faker()
    firstname = fake.first_name()
    lastname = fake.last_name()
    email = fake.email()
    password = "test"
    return firstname, lastname, email, password

def get_product_data():
    fake = Faker()
    productname = "test " + fake.text(max_nb_chars=5).rstrip('.')
    metatag = fake.text(max_nb_chars=5).rstrip('.')
    return productname, metatag
