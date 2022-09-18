from mimetypes import common_types
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

class Table:

    conn = psycopg2.connect(DATABASE_URL)

    cursor = conn.cursor()

    def createTable(self,tableName, column1, columnType):
        command = (
        f"""
        CREATE TABLE {tableName}(
            ID INTEGER NOT NULL PRIMARY KEY,
            {column1} {columnType}
        );    
        """)


        Table.cursor.execute(command)
        Table.conn.commit()

    def addColumn(self,tableName, column, columnType):
        command = (
        f"""
        ALTER TABLE {tableName}
        ADD {column} {columnType};    
        """)

        Table.cursor.execute(command)
        Table.conn.commit()

    def getValue(self,table):
        command = (f"""
            SELECT * FROM {table};
        """)

        Table.cursor.execute(command)
        return Table.cursor.fetchall()


    def setValue(self, table, columns, id, values):
        
        columnWords = ""

        for column in columns:
            columnWords += f'{str(column)}' + ", "
        
        columnWords = columnWords[:len(columnWords)-2]

        valueWords = ""

        for value in values:
            valueWords += f"'{value}'" + ", "
        
        valueWords = valueWords[:len(valueWords)-2]

        command = (f"""
        INSERT INTO {table} ({columnWords})
        VALUES ({id}, {valueWords});
        """)

        Table.cursor.execute(command)
        Table.conn.commit()

    def delTable(self, table):
        command = (f"""
            DROP TABLE {table}
        """)
        Table.cursor.execute(command)
        Table.conn.commit()

    def delValue(self, table, column, value):
        command = (f"DELETE FROM {table} WHERE {column}={value};")
        Table.cursor.execute(command)
        Table.conn.commit()

if __name__ == "__main__":
    table = Table()
    table.createTable("models", "userPrompt", "STRING NOT NULL")
    table.addColumn("models","phrase", "STRING NOT NULL")
    table.setValue("models", ["ID", "userPrompt","phrase"], 1, ["you", "they"])
    table.cursor.execute("SHOW COLUMNS FROM models;")
    print(table.getValue("models"))
    table.delTable("models")
    