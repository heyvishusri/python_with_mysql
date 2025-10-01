# Python MySQL User Management (simple CLI)

Simple command-line user management app using MySQL.

## Project files
- `dbhelper.py` — DB helper class with CRUD methods.
- `main.py` — CLI entrypoint that uses `DBHelper`.

## Requirements
- Python 3.8+
- MySQL server accessible from this machine
- Python package: `mysql-connector-python`  
  Install: `pip install mysql-connector-python`

## Setup
1. Ensure MySQL is running and you have a database available.
2. Edit connection credentials in `dbhelper.py` if needed (host, port, user, password, database).
3. The app will create the `user` table automatically on first run.

## Usage
Run the CLI:
```sh
python main.py
```
Follow the on-screen menu to insert, fetch, update, or delete users.

## Security note
The current implementation builds SQL queries via string formatting. For production use, switch to parameterized queries to prevent SQL injection.

## License
This project is released under the MIT License. See the LICENSE file for details.

## Author
VISHWASH KUMAR — https://github.com/heyvishusri
