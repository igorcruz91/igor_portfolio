# Import required modules and libraries
from airflow import DAG
from datetime import timedelta, datetime
from airflow.providers.http.sensors.http import HttpSensor
import json
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
import pandas as pd

# Function to convert temperature from Kelvin to Celsius
def kelvin_to_celsius(temp_in_kelvin):
    temp_in_celsius = (temp_in_kelvin - 273.15)
    return temp_in_celsius

# Function to transform and load weather data into S3
def transform_load_data(task_instance):
    data = task_instance.xcom_pull(task_ids="extract_weather_data")

    # Extract relevant weather information from the API response
    city = data["name"]
    weather_description = data["weather"][0]['description']
    temp_celsius = kelvin_to_celsius(data["main"]["temp"])
    feels_like_celsius= kelvin_to_celsius(data["main"]["feels_like"])
    min_temp_celsius = kelvin_to_celsius(data["main"]["temp_min"])
    max_temp_celsius = kelvin_to_celsius(data["main"]["temp_max"])
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    time_of_record = datetime.utcfromtimestamp(data['dt'] + data['timezone'])
    sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])

    # Create a dictionary to store the transformed data
    transformed_data = {"City": city,
                        "Description": weather_description,
                        "Temperature (C)": temp_celsius,
                        "Feels Like (C)": feels_like_celsius,
                        "Minimun Temp (C)":min_temp_celsius,
                        "Maximum Temp (FC)": max_temp_celsius,
                        "Pressure": pressure,
                        "Humidty": humidity,
                        "Wind Speed": wind_speed,
                        "Time of Record": time_of_record,
                        "Sunrise (Local Time)":sunrise_time,
                        "Sunset (Local Time)": sunset_time                        
                        }
    # Create a DataFrame from the transformed data
    transformed_data_list = [transformed_data]
    df_data = pd.DataFrame(transformed_data_list)

    # Prepare a timestamp for the filename
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    dt_string = 'current_weather_data_sp_' + dt_string

    # Save the DataFrame as a CSV file in an S3 bucket
    df_data.to_csv(f"s3://openweather-bucket-etl/{dt_string}.csv", index=False)

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 25),
    'email': [],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

# Define the DAG object and its tasks
with DAG('weather_dag',
        default_args=default_args,
        schedule_interval = '@daily',
        catchup=False) as dag:

        # Task to check if the weather API is ready
        is_weather_api_ready = HttpSensor(
        task_id ='is_weather_api_ready',
        http_conn_id='weathermap_api',
        endpoint='/data/2.5/weather?q=São+Paulo&APPID=d595edac46421f25e46c7ae29d971ddb'
        )

        # Task to extract weather data from the API
        extract_weather_data = SimpleHttpOperator(
        task_id = 'extract_weather_data',
        http_conn_id = 'weathermap_api',
        endpoint='/data/2.5/weather?q=São+Paulo&APPID=d595edac46421f25e46c7ae29d971ddb',
        method = 'GET',
        response_filter= lambda r: json.loads(r.text),
        log_response=True
        )

        # Task to transform and load weather data into S3
        transform_load_weather_data = PythonOperator(
        task_id= 'transform_load_weather_data',
        python_callable=transform_load_data
        )

        # Define the task dependencies
        is_weather_api_ready >> extract_weather_data >> transform_load_weather_data