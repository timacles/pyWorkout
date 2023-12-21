from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QHeaderView, QVBoxLayout, QMessageBox, QTableView, QTabWidget, QSizePolicy
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery

MY_DB = 'workouts.db'

WORKOUT_QUERY = """
    SELECT exercise, weight, reps
    FROM workouts 
    WHERE exercise = '{}'
    ORDER BY 1 DESC
"""
FONT = QFont()
FONT.setPointSize(16)  # Set the desired font size


class WorkoutTable(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableView()
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setFont(FONT)

        self.model = QSqlQueryModel()
        self.refresh("deadlift")
        self.table.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)
        
    def refresh(self, exercise):
        self.model.setQuery(WORKOUT_QUERY.format(exercise))

    def closeEvent(self, event):
        self.db.close()
        super().closeEvent(event)
        
       

class WorkoutTableEditable(QTableView):
    def __init__(self):
        super().__init__()
        
        self.model = QSqlTableModel(self)
        self.model.setTable("workouts")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setSort(0, 1)
        self.model.select()

        self.setModel(self.model)
        self.setFont(FONT)
        self.resizeColumnsToContents()

    def update_filter(self, exercise):
        self.model.setFilter(f"exercise = '{exercise}'")
        self.setModel(self.model)
        self.resizeColumnsToContents()

    def refresh(self, exercise):
        self.model.setFilter(f"exercise = '{exercise}'")
        self.model.select()
        self.setModel(self.model)
        self.resizeColumnsToContents()


class DataDisplay(QTabWidget):
    'Tabs with the database tables'
    def __init__(self):
        super().__init__()
        self.db = connectDB()
        workout_init()
        self.setSizePolicy(QSizePolicy.Policy.Preferred,
                QSizePolicy.Policy.Ignored)
        self.setFont(FONT)
        
        self.table1 = WorkoutTable()
        self.table2 = WorkoutTableEditable()

        self.addTab(self.table1, "&Current Lift")
        self.addTab(self.table2, "&Previous Stats")
    
    def register_selector(self, in_func):
        self.selector = in_func

    def refresh(self):
        exercise = self.selector()
        self.table1.refresh(exercise)
        self.table2.refresh(exercise)
    

def connectDB():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName(MY_DB)
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return con
 
def insert_data(exercise, weight, reps):
    # Insert data into the table
    query = QSqlQuery()
    query.prepare("""
        INSERT INTO workouts (exercise, weight, reps) 
                  VALUES (:exercise, :weight, :reps)""")
    query.bindValue(":exercise", exercise)
    query.bindValue(":weight", weight)
    query.bindValue(":reps", reps)

    if query.exec_():
        print("Data inserted successfully.")
    else:
        raise Exception("Error inserting data:", query.lastError().text())
        
def workout_init():
    query = QSqlQuery()
    query.exec_('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            exercise TEXT NOT NULL,
            weight INTEGER,
            reps INTEGER)
    ''')

if __name__ == "__main__":
    app = QApplication([])

    window = WorkoutTable2()
    window.show()

    app.exec_()