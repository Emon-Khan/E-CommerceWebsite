# E-CommerceWebsite

E-CommerceWebsite is a practice project built with Django, a high-level Python web framework. The project uses SQLite3, the default database that comes with Django, to store data.




## Prerequisites

To run this project, you'll need:

- Python (version 3.12.2 or higher)
- Django (version 5.0 or higher)
- SQLite3 (pre-installed with Python)

## Setup Instruction
Step-1: Creating & activating venv Windows:

You can name your virtual environment as you wish, but I would recommend naming it 'MovieEnv'. I've added 'MovieEnv' to my .gitignore file to prevent environment files from being pushed to the remote repository.

```
python -m venv env
./env/Scripts/activate
```
For Linux:
```
python -m venv env
source env/bin/activate
```
Step-2: Installing Dependencies
```
  pip install -r requirements.txt
```
Step-3: Running application Windows:
```
  > $env:PYTHONDONTWRITEBYTECODE=1;
  > py manage.py runserver
```
For Linux:
```
  > export PYTHONDONTWRITEBYTECODE=1 
  > py manage.py runserver
```
## Common Issues
1. Run this cli command it will disable creating new pycache files
```
  $env:PYTHONDONTWRITEBYTECODE=1
```

For Linux:
```
export PYTHONDONTWRITEBYTECODE=1
```

## Common Errors
1. While activating venv this error occures in Windows:
```
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
Solution:

```
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Future Improvements

  - Integration with a real database (e.g., PostgreSQL or MySQL)
  - Adding payment gateway support
  - Enhanced UI/UX with responsive design
  - API support for mobile apps

