from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QHeaderView, QVBoxLayout, QMessageBox, QTableView, QTabWidget
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel

MY_DB = 'my.db'
W_QUERY = f"SELECT * FROM workouts ORDER BY 1 DESC"

class WorkoutTable(QWidget):
    def __init__(self):
        super().__init__()

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
    



class WorkoutTable2(QTableView):
    def __init__(self):
        super().__init__()
        self.db = connectDB()
        self.model = QSqlTableModel(self)
        self.model.setTable("workouts")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        #self.model.setHeaderData(0, Qt.Horizontal, "Exercise")
        #self.model.setHeaderData(1, Qt.Horizontal, "Weight")
        #self.model.setHeaderData(2, Qt.Horizontal, "Reps")
        self.model.select()
        # Set up the view
        super().__init__()
        self.setModel(self.model)
        self.resizeColumnsToContents()


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


class dataDisplay(QTabWidget):
    'This is just sample code, does not work'
    def __init__(self):
        super().__init__()
        
        #self.setSizePolicy(QSizePolicy.Policy.Preferred,
        #        QSizePolicy.Policy.Ignored)
        
        #self.bottomLeftTabWidget = QTabWidget()
        #self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Policy.Preferred,
                #QSizePolicy.Policy.Ignored)

        table1 = WorkoutTable()
        table2 = WorkoutTable2()

        self.addTab(table1, "&Current Stats")
        self.addTab(table2, "&Previous Stats")


if __name__ == "__main__":
    app = QApplication([])

    window = WorkoutTable2()
    window.show()

    app.exec_()