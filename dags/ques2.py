import pandas
import psycopg2


def create_weather_table():
    df = pandas.read_csv("Weather_Data.csv")
    create_table = """CREATE TABLE weather(
        STATE VARCHAR(30),
        DESCRIPTION varchar(30),
        TEMPERATURE decimal,
        FEELS_LIKE_TEMPERATURE decimal,
        MIN_TEMP decimal,
        MAX_TEMP decimal,
        HUMIDITY numeric,
        CLOUDS numeric)"""

    try:
        conn = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()
        cursor.execute(create_table)
        insert_query = "Insert into weather (STATE, DESCRIPTION, TEMPERATURE, FEELS_LIKE_TEMPERATURE,MIN_TEMP, " \
                       "MAX_TEMP,HUMIDITY,CLOUDS) values (%s,%s,%s,%s,%s,%s,%s,%s)"

        for index, row in df.iterrows():
            cursor.execute(insert_query, (
                row['State'], row['Description'], row['Temperature'], row['Feels_Like_Temperature']
                , row['Min_Temperature'], row['Max_Temperature'], row['Humidity'], row['Clouds']))

        conn.commit()
    except:
        print("Error in connection")
    finally:
        conn.close()
        print("No issues")
