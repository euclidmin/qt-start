from PySide2.QtCore import QDir, Qt, QModelIndex, QStringListModel
from PySide2.QtWidgets import QApplication, QSplitter, QFileSystemModel, QTreeView, QListView, QTableView

def model_view():
    app = QApplication()
    splitter = QSplitter()

    model = QFileSystemModel()
    model.setRootPath(QDir.currentPath())
    parentIndex = model.index(QDir.currentPath())

    tree = QTreeView(splitter)
    tree.setModel(model)
    tree.setRootIndex(parentIndex)

    list = QListView(splitter)
    list.setModel(model)
    list.setRootIndex(parentIndex)

    table = QTableView(splitter)
    table.setModel(model)
    table.setRootIndex(parentIndex)


    splitter.setWindowTitle("Two views onto the same file system model")
    splitter.show()
    app.exec_()

def using_model():
    app = QApplication()
    numbers = ['One', 'Two', 'Three', 'Four', 'Five']

    model = QStringListModel()
    model.setStringList(numbers)

    list = QListView()
    list.setModel(model)

    firstTableView = QTableView()
    secondTableView = QTableView()

    firstTableView.setModel(model)
    secondTableView.setModel(model)


    list.show()
    firstTableView.show()
    secondTableView.show()
    app.exec_()




if __name__ == "__main__":
    # model_view()
    using_model()
    
    




