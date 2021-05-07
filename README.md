# To-Do List - Web application

[![status](https://img.shields.io/badge/Live%20deployed%20version:%20-https://axelrudz23.pythonanywhere.com-purple.svg)](https://axelrudz23.pythonanywhere.com)  
![status](https://img.shields.io/badge/Default%20user:%20-admin-blue.svg) ![status](https://img.shields.io/badge/Default%20password:%20-admin-blue.svg)


## Requirements
In order to run the app are required:
- Python 3.8.5
- Virtualenv (pip version 21.0.1)
- MariaDB - 10.4.17  


### Running the script (on Linux)
The script will run assuming:
- **Database**
  - Host: ***localhost***
  - Name: ***axelrudz_DB (utf8mb4_general_ci)***
  - User: ***axelrudz***
  - Password: ***axelrudz123***  
(Tables schema in: **db/schema.sql**)
- **Virtualenv**
  - Created with the name **' venv '** in this location

### Command
```bash
$ sudo bash run_webapp.sh
```


## Estructure of the proyect

```bash
helpers           # Module used for aux functions
models            # Model (MVC)
resources         # Controllers (MVC)
templates         # View (MVC)
db.py             # Database instance
__init__.py       # App instance and ruting
```
