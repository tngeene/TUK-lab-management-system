# TUK-lab-management-system

Main repository for tuk lab equipment allocation system

## Requirements

1. Python 3.6+ installed
2. Django
3. Text editor such as [vs code](https://code.visualstudio.com/) or sublime text
4. Git - preferrably use terminal like [gitbash](https://gitforwindows.org/)

## Setup

1. Clone the repository.
2. Change directory to the location of this repository.
3. Create a `.env` file using the included `.env.example` as an example.
4. Generate a secret key for your app and paste into the SECRET_KEY section of .env file
you can find generate the key from [here](https://miniwebtool.com/django-secret-key-generator/)
5. Create and start your preferred Python virtual environment. Install the required libraries.

```bash
pip install -r requirements.txt
```

6. After installation ``cd`` into the project path and run the following commands:

    ``` python
    python manage.py migrate
    ```

7. A local ```dbsqlite``` file will be generate at the root of the project.
8. Create a superuser by running the ``python manage.py createsuperuser`` and fill in the details.
9. After run ``python manage.py runserver`` open the browser and run  ``localhost:8000`` , login with the credentials created.
10. For details of how to get started with django, check out [this link](https://www.djangoproject.com/start/)
11. In order to work with a virtual environment, check out [this link](https://tutorial.djangogirls.org/en/installation/#pythonanywhere)

## Usage

To run locally:

```bash
python manage.py runserver
```

## Development

Pull the latest master version:

```bash
git pull origin master
```

Create local development branch and switch to it:

```bash
git branch dev
git checkout dev
```

Make desired changes then commit the branch.

```bash
git add .
git commit -m "changes to dev branch"
git push origin dev
```
