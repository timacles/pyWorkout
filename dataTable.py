from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
    QVBoxLayout, QHBoxLayout, QPushButton,
    QMessageBox,
    QTableView, QTabWidget, QSizePolicy)
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery

from sounds import Sounds 

MY_DB = 'workouts.db'

WORKOUT_QUERY = """
    SELECT exercise, weight, reps
    FROM workouts 
    WHERE exercise = '{}'
      AND DATE(timestamp) = DATE('now')
    ORDER BY 1 DESC
"""

FONT = QFont()
FONT.setPointSize(16)  # Set the desired font size


class CurrentWorkout(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableView()
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setFont(FONT)

        self.model = QSqlQueryModel()
        #self.refresh("deadlift")
        self.table.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def closeEvent(self, event):
        self.db.close()
        super().closeEvent(event)
        
    def register_exercise(self, in_func):
        self._exercise = in_func

    @property
    def exercise(self):
        return self._exercise()
       
    def refresh(self):
        self.model.setQuery(WORKOUT_QUERY.format(self.exercise))

class PreviousWorkout(QWidget):
    def __init__(self):
        super().__init__()

        self.sounds = Sounds()
        self.sqlTable = WorkoutTableEditable()

        buttonLayout = QHBoxLayout()

        self.delButton = QPushButton("Delete Row")
        self.delButton.setFont(FONT)
        self.delButton.clicked.connect(self.delete_row)

        buttonLayout.addWidget(self.delButton)

        layout = QVBoxLayout()
        layout.addWidget(self.sqlTable)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)

    def delete_row(self):
        self.sqlTable.delete_row()
        self.sounds.delete()

    def refresh(self):
        self.sqlTable.refresh()

    def register_exercise(self, in_func):
        self._exercise = in_func
        self.sqlTable.register_exercise(in_func)

    @property
    def exercise(self):
        return self._exercise()
 

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

    def delete_row(self):
        indices = self.selectionModel().selectedIndexes()

        for idx in indices:
            r = idx.row()
            self.model.removeRow(r)

        self.refresh()

    def register_exercise(self, in_func):
        self._exercise = in_func

    @property
    def exercise(self):
        return self._exercise()

    def update_filter(self):
        self.model.setFilter(f"exercise = '{self.exercise}'")
        self.setModel(self.model)
        self.resizeColumnsToContents()

    def refresh(self):
        'refresh the table view with latest data'
        self.model.setFilter(f"exercise = '{self.exercise}'")
        self.model.select()
        self.setModel(self.model)
        self.resizeColumnsToContents()

    def deleteRow(self):
        #TODO 
        session.delete(query)
        session.commit()
        self.products_table.removeRow(row)

class DataDisplay(QTabWidget):
    'Tabs with the database tables'
    def __init__(self):
        super().__init__()
        self.db = connectDB()
        workout_init()
        self.setSizePolicy(QSizePolicy.Policy.Preferred,
                QSizePolicy.Policy.Ignored)
        self.setFont(FONT)
        
        self.current_workout = CurrentWorkout()
        self.previous_workout = PreviousWorkout()

        self.addTab(self.current_workout, "&Current")
        self.addTab(self.previous_workout, "&Previous")
    
    def register_exercise(self, in_func):
        self.current_workout.register_exercise(in_func)
        self.previous_workout.register_exercise(in_func)

    def refresh(self):
        self.current_workout.refresh()
        self.previous_workout.refresh()
    






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
