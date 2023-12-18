from subprocess import check_output
import mysql.connector

# db pievienota lietotaja konfiguracija
db_config = {
    'host': 'localhost',
    'user': 'klavs',
    'password': 'Klavs321!',
    'database': 'python_outputs',
}

def execute_and_store_output(file_name):
    try:
        # darbina py failu (tikai skript.py)
        file_path = f'./{file_name}'  # ta ka atrodas root ir vienkarshi / (ja butu home tad varetu /home)
        output = check_output(['python3', file_path], text=True)

        # pievienoju test lai atpazitu testa ievietots jokus
        output += "TEST"

        # savienojas ar mysql
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # ievieto datus datubaze lai parbauditu vai var ielikt datus db
        insert_query = "INSERT INTO file_outputs (file_name, output) VALUES (%s, %s)"
        data = (file_name, output)
        cursor.execute(insert_query, data)

        connection.commit()
        connection.close()

        print(f"Output from {file_name} successfully stored in the database.")
    except Exception as e:
        print(f"Error executing {file_name}: {e}")

def retrieve_results():
    try:
        # pievienojamies mysql
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # iegust visus datus no file_outputs tabulas
        select_query = "SELECT * FROM file_outputs"
        cursor.execute(select_query)
        results = cursor.fetchall()

        connection.close()

        return results
    except Exception as e:
        print(f"Error retrieving results from the database: {e}")
        return None

# izpilda funkciju skripta failam
execute_and_store_output("skript.py")

# panem visus rezultatus no db
all_results = retrieve_results()

# ja vis strada ka vaig datu baze vaidzetu but kaut kadam ierakstam (izprinte visus)
if all_results:
    for result in all_results:
        print(f"File: {result[1]}\nOutput: {result[2]}\n")
else:
    print("No results found in the database.")
