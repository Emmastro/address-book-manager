
# README #

### Prompt ###

In order for us to see how you approach software development, using whatever
technologies you prefer and taking no longer than 2 hours, develop a small address
book manager web application that allows for storing and searching of the name,
phone number, and address of people. We should be able to either use it through
an already hosted website or run it locally.

## Installation

Make sure you have python3 installed with venv. If you don't have [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/), you can install it with:


Clone the repository:

```bash
git clone git@github.com:Emmastro/address-book-manager.git
```

cd on the root folder of the project, and create the virtual environment with

```bash
make create_environment
```

Then, you can activate it with:
```bash
source env/bin/activate
```

And install dependencies with:
```bash
make install
```

Last step, make a copy of the .env.development file, and rename it to .env. Then, set a value to the secret key


## Usage

Migrate the database

```
python manage.py makemigrations
python manage.py migrate
```

Populate test data

```
python manage.py init_contacts
```

Run the server
```
python manage.py runserver
```

### Next steps ###



## License

