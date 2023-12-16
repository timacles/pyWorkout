import sqlite3
from utils import today

class Database:
    conn = sqlite3.connect('my.db')
    cursor = conn.cursor()

    def __init__(self):
        self.workout_init()

    def workout_init(self):
        self.exec('''
            CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                exercise TEXT NOT NULL,
                weight INTEGER,
                reps INTEGER
            )
        ''')

    def insert_set(self, exercise, weight, reps):
        self.exec(
            'INSERT INTO workouts (exercise, weight, reps) VALUES (?, ?, ?)',
            (exercise, weight, reps))
    
    def get_exercise(self, exercise):
        sql = """
            SELECT * 
            FROM workouts 
            WHERE exercise = ?
        """ 
        self.exec(sql, (exercise,))
        return self.cursor.fetchall()
    
    def exec(self, sql, params=[]):
        self.cursor.execute(sql, params)
        self.conn.commit()


