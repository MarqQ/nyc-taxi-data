# NYC Taxi Data
ETL and API for Taxi and Limousine Commission (TLC) Trip Record Data

Last Update: Nov, 16th 2021

This is a project to consume dataset from TLC Trip Record Data and provide an API, 

This project was developed with:
* Jupyter Notebook
* Numpy & Pandas
* Django 3.2 LTS
* Django Rest Framework
* PostgreSQL 14

To run this project locally:

LINUX/macOS
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
After initial configuration, you need to create a dataset environment:

* You can restore the PostgreSQL database file to your pgAdmin (the file is in nyc-taxi-data/backup_for_testing directory)
* You can restore Insomnia file to your Insomnia app for requisition tests
* Check if the csv file is in the dataset folder, the extract comes from this directory, 
  otherwise download the file from https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv
* Run dataset_loader.ipynb scripts

### Here are some queries for PostgreSQL after ETL process:

Taxi trips less than $5
```
SELECT COUNT (total_amount)
	FROM public.nyc_taxi_data
	WHERE total_amount <= 5.0 AND total_amount >= 0.0;
```
Amount average
```
SELECT AVG(total_amount)::numeric(10,2)
FROM public.nyc_taxi_data;
```
Tips average
```
SELECT AVG(tip_amount)::numeric(10,2)
FROM public.nyc_taxi_data;
```
These queries will be available on Jupyter in an upcoming release

### If you have any suggestions, please feel free to propose a pull request.

NOTE: This project is for study purposes, but working on it, I realized that there are many possibilities to scale and grow, so
it is possible that there are changes over time.
