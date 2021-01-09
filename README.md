# Pangani Football Academy

Football Academy management System

## Requirements

1. Python 3.6+ installed
2. Text editor such as [vs code](https://code.visualstudio.com/) or sublime text
3. Git - preferrably use terminal like [gitbash](https://gitforwindows.org/)

## Setup

1.Create and start your preferred Python virtual environment. For
more information on how to set up a virtual environment, check the instructions on [this link](https://tutorial.djangogirls.org/en/django_installation/).
Install the required libraries by running the command below

        pip install -r requirements.txt
        
2.Clone the repository in the directory you have created the environment in.       
3.Change directory to the location of the cloned repository.

4. On the terminal, run the following command:

        python manage.py migrate

5. A local ```dbsqlite``` file will be generated at the root of the project.
6. Create a superuser by running the ``python manage.py createsuperuser`` and fill in the details.
7. After creating superuser run ``python manage.py runserver`` open the browser and run  ``127.0.0.1:8000/admin`` , login with the credentials created.
8.On the browser, the address  ''127.0.0.1:8000'' will take you to the landing page.
9.From there, with the admin credentials you craeted,you can login and be directed to the admin dashboard.


## Usage

To run locally:

    python manage.py runserver
To see player functionalities, register from the dashboard of the landing page.
Activate the player as the admin to be able to login
To view the trainer dashboard,create a trainer from the admin dashboard
To view the m-pesa fee payment use the url-http://127.0.0.1:8000/lipa
