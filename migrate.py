import mysql.connector

#datubazes lietotaja konfiguracija
db_config = {
    'host': 'localhost',
    'user': 'klavs',
    'password': 'Klavs321!',
    'database': 'python_outputs'
}


connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

#nav nepiecieshams bet man patik kad varu izpildit migraciju kad es gribu izdzest visu kas ir ievietots tabula
drop_table_query = '''
DROP TABLE IF EXISTS file_outputs
'''
#iveidoju tabulu
create_table_query = '''
CREATE TABLE file_outputs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    output TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
'''

#vispirms isaucu lai tabulu izdzestu
cursor.execute(drop_table_query)

#pectam izsaucu tabulas izveidi
cursor.execute(create_table_query)


connection.commit()
connection.close()

print("Migration completed successfully.")
