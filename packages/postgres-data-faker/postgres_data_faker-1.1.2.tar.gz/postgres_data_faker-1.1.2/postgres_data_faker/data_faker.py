import os
import psycopg2

from psycopg2 import Error
from contextlib import closing
from faker import Faker

fake = Faker()


def next_value(lst):
    for tup in lst:
        for value in tup:
            yield value


def faking_table(tablename: str):
    try:
        with closing(psycopg2.connect(
                dbname=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD'),
                host=os.getenv('POSTGRES_HOST'),
                port=os.getenv('POSTGRES_PORT')
        )) as connection:

            print('Successfully connected to database')

            faked_data = []

            print('Get records from database')
            with connection.cursor() as cursor:
                selector_query = f"""SELECT id FROM {tablename}"""

                cursor.execute(selector_query)
                ids = cursor.fetchall()
                quantity = len(ids)

                my_generator = next_value(ids)

                print('Processing...')
                for i in range(quantity):
                    a = next(my_generator)

                    match tablename:
                        case 'customer' | 'recipient' as table:
                            faked_data.append(
                                (
                                    fake.email(),
                                    fake.msisdn(),
                                    fake.first_name(),
                                    fake.last_name(),
                                    a
                                )
                            )

                            update_query = f"""
                                                UPDATE {table} 
                                                SET email=%s, phone=%s, firstname=%s, lastname=%s 
                                                WHERE id=%s
                                                """
                            # print(f'Table {tablename}: processing {i} of {quantity} records...')
                        case 'customer_address' as table:
                            faked_data.append(
                                (
                                    fake.address(),
                                    fake.postcode(),
                                    a
                                )
                            )
                            update_query = f"""
                                                UPDATE {table} 
                                                SET address_text=%s, postal_code=%s 
                                                WHERE id=%s
                                                """
                            # print(f'Table {tablename}: processing {i} of {quantity} records...')
                        case _:
                            print('INVALID OR NOT IMPLEMENTED TABLENAME')
                            raise AttributeError

                cursor.executemany(update_query, faked_data)
                connection.commit()
                print('Success!')
                print(cursor.rowcount, f"Records in {tablename} was faked")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        raise Exception('Postgres connection error')


if __name__ == '__main__':
    # main(tablename='customer')
    # main(tablename='recipient')
    # main(tablename='customer_address')

    faking_table(tablename=input('Table name for faking: '))
