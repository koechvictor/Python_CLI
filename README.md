# Python_CLI

This project sets up a SQLite database to manage concerts, bands, and venues. It includes scripts to create the database schema, insert test data, and define models for interacting with the data using raw SQL queries.

## Project Structure

- `setup_database.py`: Script to set up the initial database schema.
- `insert_test_data.py` Script to insert test data into the database.
- `migration.sql` SQL script to create the [`bands`]
- `concerts_migration.sql`: SQL script to create the [`concerts`]
- `models.py`: Python file containing the `Concert`, `Venue`, and `Band` classes with methods to interact with the
- `concerts.db`: The SQLite database file.

## Setup

1. **Set up the database schema:**

   Run the `setup_database.py` script to create the necessary tables in the database.

   ```sh
   python setup_database.py
   python insert_test_data.py
   ```
