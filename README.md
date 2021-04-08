# Software-Testing-of-Shuup


###create a fork of Shuup in Github by clicking the “Fork” button at https://github.com/shuup/shuup and clone the fork to your computer.

###Setup a virtualenv and activate it.
virtualenv shuup-venv
. shuup-venv/bin/activate

install selenium,chrome webdriver, mozilla webdrier
###Finally, you’ll need to install Shuup in the activated virtualenv in development mode(inside shuup folder).
pip install -e .

### Migrate database.
python -m shuup_workbench migrate

### Import some basic data.
python -m shuup_workbench shuup_init

### Create superuser so you can login admin panel
python -m shuup_workbench createsuperuser

### Run the Django development server (on port 8000 by default).
python -m shuup_workbench runserver
