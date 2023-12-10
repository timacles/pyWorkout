import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QHeaderView, QVBoxLayout, QMessageBox, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel

MY_DB = 'my.db'
W_QUERY = f"SELECT * FROM workouts ORDER BY 1 DESC"

class WorkoutTable(QWidget):
    def __init__(self):
        super().__init__()
        self.db_path = MY_DB

        self.db = connectDB()

        # Initialize table widget
        self.table = QTableView()
        self.table.horizontalHeader().setStretchLastSection(True)

        # Create and set model
        self.model = QSqlQueryModel()
        self.model.setQuery(W_QUERY)
        self.table.setModel(self.model)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)
        
    def refresh(self):
        self.model.setQuery(W_QUERY)

    def closeEvent(self, event):
        # Close database connection on exit
        self.db.close()
        super().closeEvent(event)
    
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
        

def TabbedWidgetExampleDataTable(self):
    'This is just sample code, does not work'
    self.bottomLeftTabWidget = QTabWidget()
    self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Ignored)

    wData = qtDB.WorkoutTable()

    tab1 = QWidget()
    tableWidget = QTableWidget(10, 10)

    tab1hbox = QHBoxLayout()
    tab1hbox.setContentsMargins(5, 5, 5, 5)
    tab1hbox.addWidget(tableWidget)
    tab1.setLayout(tab1hbox)

    tab2 = QWidget()
    textEdit = QTextEdit()

    textEdit.setPlainText("TEST TEST TEST\n We'll Add something soon :)")

    tab2hbox = QHBoxLayout()
    tab2hbox.setContentsMargins(5, 5, 5, 5)
    tab2hbox.addWidget(textEdit)
    tab2.setLayout(tab2hbox)

    self.bottomLeftTabWidget.addTab(wData, "&Current Stats")
    self.bottomLeftTabWidget.addTab(tab2, "&Previous Stats")


if __name__ == "__main__":
    app = QApplication([])

    window = WorkoutTable()
    window.show()

    app.exec_()