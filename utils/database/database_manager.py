import pymysql
import os 
import json
import requests
from colorama import Fore, Style
from datetime import datetime, timedelta
import pytz  # Import pytz module for timezone conversion# Define the UTC timezone
import re 
import subprocess
import random
import time

admin_db_host = "your_dp_ip" # Can be "localhost"
admin_db_user =  "your_db_username"
admin_db_password = "your_db_password"

# Function to establish a database connection
def connect_to_database(database):
    return pymysql.connect(
        host=admin_db_host,
        user=admin_db_user,
        password=admin_db_password,
        db=database,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

# Function to execute SQL queries and fetch data
def execute_sql_query(database, query, params=None):
    connection = connect_to_database(database)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        connection.commit()  # Commit the changes to the database
    finally:
        connection.close()
    return result

# Function to fetch proxies based on country code
def get_proxies_by_country(country_code, database="webshare", table="proxies"):
    if country_code == "ALL":
        # Return all proxies
        query = f"SELECT CONCAT(proxy_address, ':', port) AS proxy FROM {table}"
        try:
            results = execute_sql_query(database, query)
            proxies = [result['proxy'] for result in results]
        except Exception as e:
            print("Failed to fetch proxies from the database:", str(e))
            proxies = []
    else:
        # Fetch proxies based on the specified country code
        query = f"SELECT CONCAT(proxy_address, ':', port) AS proxy FROM {table} WHERE country_code = %s"
        try:
            results = execute_sql_query(database, query, (country_code,))
            proxies = [result['proxy'] for result in results]
        except Exception as e:
            print(f"Failed to fetch {country_code} proxies from the database:", str(e))
            proxies = []

    return proxies