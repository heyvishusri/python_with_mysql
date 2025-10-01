# Python MySQL User Management (simple CLI)

Simple command-line user management app using MySQL.

## Project files
- [dbhelper.py](dbhelper.py) — contains the [`DBHelper`](dbhelper.py) class with methods:
  - [`DBHelper.insert_user`](dbhelper.py)
  - [`DBHelper.fetch_all`](dbhelper.py)
  - [`DBHelper.fetch_user_by_id`](dbhelper.py)
  - [`DBHelper.delete_user_by_id`](dbhelper.py)
  - [`DBHelper.update_user_by_id`](dbhelper.py)
- [main.py](main.py) — CLI entrypoint that uses [`DBHelper`](dbhelper.py) (see [`main`](main.py)).

## Requirements
- Python 3.8+
- MySQL server accessible from this machine
- Python package: mysql-connector-python
  - Install with: `pip install mysql-connector-python`

## Setup
1. Ensure MySQL is running and you have a database available.
2. Edit connection credentials in [dbhelper.py](dbhelper.py) if needed (host, port, user, password, database).
3. The app will create the `user` table automatically on first run.

## Usage
Run the CLI:
```sh
python main.py
```
Follow the on-screen menu to insert, fetch, update, or delete users.

## Notes
- The current implementation builds SQL queries via string formatting. For production use, switch to parameterized queries to prevent SQL injection.
- To change the schema or column sizes, edit [dbhelper.py](dbhelper.py).

## Helpful links (in this repo)
- [`DBHelper`](dbhelper.py)
- [`DBHelper.insert_user`](dbhelper.py)
- [`DBHelper.fetch_all`](dbhelper.py)
- [`DBHelper.fetch_user_by_id`](dbhelper.py)
- [`DBHelper.delete_user_by_id`](dbhelper.py)
- [`DBHelper.update_user_by_id`](dbhelper.py)
- [main.py](main.py)
- [dbhelper.py](dbhelper.py)

## License
Add a license as needed.
