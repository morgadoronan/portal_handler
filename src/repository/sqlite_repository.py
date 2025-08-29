class SQLiteRepository:
    def __init__(self, db_name='database.db'):
        import sqlite3
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                column1 TEXT,
                column2 TEXT,
                column3 TEXT
            )
        ''')
        self.connection.commit()

    def save_record(self, metadata):
        self.cursor.execute('''
            INSERT INTO records (column1, column2, column3) VALUES (?, ?, ?)
        ''', (metadata.column1, metadata.column2, metadata.column3))
        self.connection.commit()

    def fetch_records(self):
        self.cursor.execute('SELECT * FROM records')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()