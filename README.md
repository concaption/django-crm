# Django CRM Application

This is a simple Customer Relationship Management (CRM) application built with Django.
![](/screenshot.png)

## Features

- User Registration: New users can create an account.
- User Authentication: Users can log in and log out.
- Customer Records: Authenticated users can view customer records.

## Todo

[ ] Add dockerfile and dockercompose files 

## Installation

1. Clone this repository: `git clone https://github.com/concaption/django-crm.git`
2. Navigate to the project directory: `cd django-crm`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## Usage

### User Registration

New users can register by navigating to the `/register` endpoint and filling out the form.

### User Authentication

Registered users can log in by navigating to the `/login` endpoint and entering their credentials.

### Viewing Customer Records

Authenticated users can view customer records by navigating to the `/record/<id>` endpoint, where `<id>` is the ID of the customer record.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Please replace `https://github.com/concaption/django-crm.git` with the actual URL of your repository.