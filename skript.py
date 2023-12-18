import mysql.connector
from subprocess import check_output
from datetime import datetime

# db lietotaja pievienoshanas
db_config = {
    'host': 'localhost',
    'user': 'klavs',
    'password': 'Klavs321!',
    'database': 'python_outputs',
}

# funkcija kas izpilda citu failu un saglaba db izvadu
def execute_and_store_output(file_name):
    try:
        # izspilda py failu (kas atrodas /home)
        file_path = f'/home/{file_name}'
        output = check_output(['python3', file_path], text=True)

        # pievienojamies db izmantojot unix
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # ievieto izvadus no cita py faila file)outputs tabula
        insert_query = "INSERT INTO file_outputs (file_name, output) VALUES (%s, %s)"
        data = (file_name, output)
        cursor.execute(insert_query, data)

        connection.commit()
        connection.close()

        print(f"Output from {file_name} successfully stored in the database.")
    except Exception as e:
        print(f"Error executing {file_name}: {e}")


execute_and_store_output('joki.py')
