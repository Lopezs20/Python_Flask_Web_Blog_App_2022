Lopezs20/CSCI_4710/Final_Project/Simple_Blog_Website
Quick Start on Ubuntu, Mac users have similar commands.

**Local Test Setup**
Change directory to the project location that you cloned this repos from.

Update your package manager:
    sudo apt update

Install Python3 virtual environment:
    sudo apt-get install python3-venv

Make the Virtual Environment:
    python3 -m venv python_venv

Activate it now so we can use it:
    source python_venv/bin/activate

Install all dependencies:
    pip3 install -r requirements.txt

Finally run the app:
    python3 app.py

**SET UP POSTGRESQL**

To set-up with postgresql, make sure you install PGAdmin 4 with postgresql.
Make a database with sql commands in the psql shell that you want this app to connect to (e.g. CREATE DATABASE blogData).
Then navigate to PGAdmin with you credientials and use this command to replace the one in
"init.py" python file for package. 

Line 17: app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:USERNAME@localhost/DATABASE"

**To use the sql lite "database" ORM file format**
Just make sure to un-comment the follow lines:

Line 9: DB_NAME = "database.db"
Line 16: app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{{DB_NAME}}'
Line 41: if not path.exists("website/" + DB_NAME):

Then comment the followning line that has posgresql configured:

Line 17: app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:lopezs20@localhost/blogposts"