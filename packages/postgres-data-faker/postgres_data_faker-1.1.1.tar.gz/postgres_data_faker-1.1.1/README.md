# Postgres data faker

---

- install package with:
  - pip: `pip install postgres-data-faker`
  - poetry: `poetry add postgres-data-faker`
- import module with `from postgres_data_faker import data_faker`
- using func `data_faker.faking_table(enter name of your table here)`
---
- available table names:
  - customer: will fake columns (**ordered!**):
    - phone
    - email
    - firstname
    - lastname
  - recipient: similar to customer
  - customer address: will fake columns (**also ordered!**):
    - address_text
    - postal_code
---

- connection data stored ad `.env` file, so you must create and fill it with your database parameters