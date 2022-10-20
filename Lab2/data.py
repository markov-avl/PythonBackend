import faker


fake = faker.Faker('RU_ru')


for i in range(25):
    print("INSERT INTO user (id, login, password, full_name, role)")
    print(f"VALUES ({i + 1}, '{fake.user_name()}', '{fake.password()}', '{fake.name()}', {1 if fake.random.randint(1, 100) > 90 else 2});")