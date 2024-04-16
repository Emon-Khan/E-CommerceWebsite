# Movie Data RESTAPI

### Language- Python, DRF(Django Rest Framework)
### Database- sqlite3
## Setup Instruction
Step-1: Creating & activating venv Windows:
You can name your virtual environment as you wish, but I would recommend naming it 'MovieEnv'. I've added 'MovieEnv' to my .gitignore file to prevent environment files from being pushed to the remote repository.

Step-1: Creating & activating venv Windows:
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

## Demo
This project is actually created for doing some testing like, How a django project actually created?What is the folder structure?How to manage version control tools like github?What info should a developer need to add to his project and how to make clear documentation in 'README.md' file so that whoever wants to clone this project will have a total guideline for it? How to use DRF in Django project?And many other things.

Now let's see some of this project features along with explanations.

### Make endpoint
In a normal django project we can create a superuser and using that credentials we can login into the admin  site.And there if we add content, content got added into the frontend.When we are using normal django we are using MVT(Model, View, Template) architecture.But when we are using DRF(Django Rest Framework) we create routers, seralizers to make endpoints.
