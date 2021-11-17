# NYC Taxi Data
API TLC Trip Record Data

Last Update: Nov, 16th 2021

This is a project to consume dataset from TLC Trip Record Data and provide an API, 

This project was developed with:
* Jupyter Notebook
* Numpy & Pandas
* Django 3.2 LTS
* Django Rest Framework
* PostgreSQL 14

To run this project localy:

LINUX/McOS
```
git clone
cd nyc-taxi-data
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
WINDOWS
```
git clone
cd nyc-taxi-data
python3 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
After initial configuration, you need to create dataset environment:

* Restore the PostgreSQL database file to your pgadmin (o arquivo está em nyc-taxi-data/backup_for_testing)
* Restore Insomnia file to your Insomnia app for requisition tests
* Check if the csv file is in the dataset folder, 
otherwise download the file from https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv
* Run dataset_loader.ipynb scripts

### If you have any suggestions, please feel free to propose a pull request.

P.S: This project is for study purposes, but I realized that there are many possibilities to scale and grow,
This project is for study purposes, but I realized that there are many possibilities to scale and grow, 
it's possible that there will be changes over time.