import datetime

import faker

fake = faker.Faker('RU_ru')
opened = False

USERS = 15
MOUNTAINS = 10
TOURS = 10
DIFFICULTIES = 5
TAGS = 10
RESERVATIONS = 30
OFFERS = TOURS + 10
REVIEWS = 30
REGIONS = MOUNTAINS + TOURS


def append_to_insert_sql(line: str) -> None:
    global opened
    mode = 'w' if not opened and (opened := not opened) else 'a'
    with open('insert.sql', mode) as insert_sql:
        insert_sql.write(line)


def get_insert(table, **fields) -> str:
    for field in fields:
        if isinstance(fields[field], str) or isinstance(fields[field], datetime.datetime):
            fields[field] = f"'{fields[field]}'"
        elif fields[field] is None:
            fields[field] = 'null'
        else:
            fields[field] = str(fields[field])
    return f"INSERT INTO {table} ({', '.join(fields.keys())})\nVALUES ({', '.join(fields.values())});\n"


if __name__ == '__main__':
    for i in range(USERS):
        append_to_insert_sql(get_insert(
            'user',
            id=i + 1,
            login=fake.user_name(),
            password=fake.password(),
            full_name=fake.name(),
            phone=int(''.join(c for c in fake.phone_number() if c not in '()-+ ')),
            role=1 if fake.random.randint(1, 100) > 90 else 2
        ))

    for i in range(REGIONS):
        append_to_insert_sql(get_insert(
            'region',
            id=i + 1,
            name=fake.city().split(' ')[-1]
        ))

    for i in range(MOUNTAINS):
        append_to_insert_sql(get_insert(
            'mountain',
            id=i + 1,
            region_id=i + 1,
            name='TODO',
            height=fake.random.randint(1500, 4500)
        ))

    for i in range(DIFFICULTIES):
        append_to_insert_sql(get_insert(
            'difficulty',
            id=i + 1,
            name=f'TODO{i + 1}',
            rating=i + 1
        ))

    for i in range(TAGS):
        append_to_insert_sql(get_insert(
            'tag',
            id=i + 1,
            name=f'TODO{i + 1}'
        ))

    for i in range(TOURS):
        append_to_insert_sql(get_insert(
            'tour',
            id=i + 1,
            mountain_id=fake.random.randint(1, MOUNTAINS),
            difficulty_id=fake.random.randint(1, DIFFICULTIES),
            starting_point_id=i + MOUNTAINS + 1,
            name=f'TODO{i + 1}',
            description='TODO'
        ))

    k = 1
    for i in range(TOURS):
        for j in range(fake.random.randint(2, 5)):
            append_to_insert_sql(get_insert(
                'tour_tag',
                id=k,
                tour_id=i + 1,
                tag_id=fake.random.randint(1, TAGS)
            ))
            k += 1

    for i in range(OFFERS):
        starting_at = datetime.datetime(
            2022,
            fake.random.randint(11, 12),
            fake.random.randint(1, 30),
            fake.random.randint(10, 16),
        )
        append_to_insert_sql(get_insert(
            'offer',
            id=i + 1,
            tour_id=fake.random.randint(1, TOURS),
            starting_at=starting_at,
            ending_at=starting_at + datetime.timedelta(fake.random.randint(5, 10)),
            max_reservations=fake.random.randint(5, 15),
            price=fake.random.randint(10, 60) * 1000.0
        ))

    for i in range(RESERVATIONS):
        append_to_insert_sql(get_insert(
            'reservation',
            id=i + 1,
            offer_id=fake.random.randint(1, OFFERS),
            user_id=fake.random.randint(1, USERS),
            reservations=fake.random.randint(1, 3),
            status=fake.random.randint(1, 3)
        ))

    for i in range(REVIEWS):
        append_to_insert_sql(get_insert(
            'review',
            id=i + 1,
            reservation_id=fake.random.randint(1, RESERVATIONS),
            rating=fake.random.randint(1, 10),
            comment=fake.random.choice(['TODO', None]),
            created_at=fake.past_datetime()
        ))
