QTableView
--
`QTableView`可以绑定一个模型数据用来更新控件上的内容，可用的模式如下表：

|名称|含义|
|:---------|:------------|
|QStringListModel|存储一组字符串|
|QStandardItemModel| 存储任意层次结构的数据|
|QDirModel| 对文件系统进行封装|
|QSqlQueryModel| 对SQL的查询结果集进行封装|
|QSqlTableModel| 对SQL中的表格进行封装|

<br/>

- 代码示例
```python
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class WinForm(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView表格视图控件的例子")
        self.resize(500, 300)
        self.model = QStandardItemModel(4, 4) # 数据模型定义
        # 增加表头
        self.model.setHorizontalHeaderLabels(["Label1", "Label2", "Label3", "Label4"])
        for row in range(4):
            for column in range(4):
                # 定义数据项
                item = QStandardItem("row{}, column{}".format(row, column))
                # 向数据模型中增加数据项
                self.model.setItem(row, column, item)

        self.tableView = QTableView()  # 定义数据表控件
        self.tableView.setModel(self.model)  # 添加数据模型
        dlg_layout = QVBoxLayout()
        dlg_layout.addWidget(self.tableView)
        self.setLayout(dlg_layout)
        self.model.appendRow([QStandardItem("1"), QStandardItem("2"), QStandardItem("3"), QStandardItem("4")])
        self.tableView.clicked.connect(self.func)

    def func(self, model_index):
        # 删除鼠标指定的行
        self.model.removeRow(self.tableView.currentIndex().row())
        # self.model.removeRow(model_index.row())  # 两种方式都可以
```

- `QListView`和`QTableView`类似，以下只列出重点代码：
```python
listView = QListView()
listModel = QStringListModel()
listModel.setStringList(['Item 1', 'Item 2', 'Item 3', 'Item 4'])
listView.setModel(listModel)
```

<br/>

- `QListWidget`是`QListView`派生的控件，常用的方法包括：

|方法|描述|
|:---|:---|
|addItem() | 添加QListWidgetItem对象或字符串|
|addItems() | 同时添加多个条目|
|clear() | 删除列表中的内容|
|setCurrentItem() | 指定条目| 


示例代码如下：
```python
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import logging

logging.basicConfig(level=logging.INFO, filename='log.txt', format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")
logger = logging.getLogger(__name__)


class WinForm(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        self.addItem("Item 1")
        self.addItems(["Item 2", "Item 3", "Item 4"])
        self.itemClicked.connect(self.func)

    def func(self, item):
        QMessageBox.information(self, "ListWidget", item.text())
        logger.info("clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lv = WinForm()
    lv.show()
    sys.exit(app.exec_())
```

- `QTableWidget`是最常用的数据表格控件

`QTableWidget`是`QTableView`的子类，使用标准数据模型，其单元格数据通过`QTableWidgetItem`对象来实现，
整个表格就是用各单元格构建起来的，其常用方法如下：

|方法|描述|
|:---|:---|
|setRowCount(int row)|设置QTableWidget表格控件的行数|
|setColumnCount(int col)|设置QTableWidget表格控件的列数|
|setHorizontalHeaderLabels()|设置QTableWidget表格控件的水平标签|
|setVerticalHeaderLables()|设置QTableWidget表格控件的垂直标签|
|setItem(int, int, QTableWidgetItem)|设置QTableWidget表格控件的每个单元|
|horizontalHeader()|获得表头，以便隐藏|
|rowCount()|获得行数|
|columnCount()|获得列数|
|setEditTriggers(EditTriggers triggers)|设置表格是否可编辑，设置编辑规则的枚举值|
|setSelectionBehavior()|设置表格的选择行为|
|setTextAlignment()|设置单元格内文字的对齐方式|
|setSpan(int row, int col, int rowSpanCount, int colSpanCount)|合并单元格|
|setShowGrid()| **True**: 显示网格/ **False**:不显示网格 |
|setColumnWidth(int col, int width)|设置单元格行宽度|
|setRowHeight(int row, int height)|设置单元格列高度|

- 示例程序
```python
class WinForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(500, 400)
        layout = QHBoxLayout()
        tw = QTableWidget()
        tw.setRowCount(4)
        tw.setColumnCount(3)
        tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tw.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tw.setSelectionBehavior(QAbstractItemView.SelectRows)
        tw.verticalHeader().setVisible(False)
        tw.horizontalHeader().setVisible(True)
        layout.addWidget(tw)
        tw.setHorizontalHeaderLabels(['姓名', '性别', '体重'])
        tw.setItem(0, 0, QTableWidgetItem('张三'))
        tw.setItem(0, 1, QTableWidgetItem('男'))
        tw.setItem(0, 2, QTableWidgetItem('84'))
        combox = QComboBox()
        combox.addItem("Male")
        combox.addItem("Female")
        tw.setCellWidget(1, 0, combox)
        btn_search = QPushButton("Button")
        btn_search.setDown(True)
        btn_search.setStyleSheet("background-color:#DDDDDD")
        tw.setCellWidget(1, 1, btn_search)
        self.setLayout(layout)
```

当`tableWidget`表格的行数很多时，可以通过输入行号进行直接定位并显示，比如输入10，就直接显示第10行
```python
item  = tableWidget.findItems(text, QtCore.Qt.MatchExactly)
row = item[0].row()
self.tableWidget.verticalScrollBar().setSliderPosition(row)
```

示例代码如下：
```python
class WinForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 800)
        layout = QHBoxLayout(self)
        tw = QTableWidget()
        tw.setRowCount(30)
        tw.setColumnCount(4)
        layout.addWidget(tw)
        for i in range(30):
            for j in range(4):
                tw.setItem(i, j, QTableWidgetItem("({}, {})".format(i, j)))
                logger.info("abc")
        text = "(25, 1)"
        items = tw.findItems(text, Qt.MatchExactly)
        item = items[0]
        item.setForeground(QBrush(QColor(255, 0, 0)))
        item.setFont(QFont("Times", 12, QFont.Black))
        row = item.row()
        tw.verticalScrollBar().setSliderPosition(row)
```
可以使用`tableWidget.sortItems(2, QtCore.Qt.DescendingOrder)`对第三列进行降序排序，也可以使用`Qt.AscendingOrder`进行升序排列

使用`widgetItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)`使单元格内容右对齐并与底部对齐

- 合并单元格

`tableWidget.setSpan(0,0,3,1)`将表格中第一行第一列的单元格，更改为占据3行1列
示例代码如下:
```python
class WinForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 800)
        layout = QHBoxLayout(self)
        tw = QTableWidget()
        tw.setRowCount(4)
        tw.setColumnCount(4)
        tw.setHorizontalHeaderLabels(['Name', 'Sex', 'Weight', 'Age'])
        tw.setSpan(0, 0, 3, 1)
        tw.setItem(0, 0, QTableWidgetItem("AAA"))
        tw.setItem(0, 1, QTableWidgetItem('Male'))
        tw.setItem(0, 2, QTableWidgetItem('160'))
        tw.setItem(0, 3, QTableWidgetItem('36'))
        layout.addWidget(tw)
```

`tableWidget.setColumnWidth(0, 150)`将第一列的单元格宽度设置为150， `tableWidget.setRowHeight(0,120)`将第一行的单元格高度设置为120

`tableWidget.setShowGrid(True)`设置显示分割线。

- 为单元格添加图片以及增加右键菜单
  
可以使用`tableWidget.setItem(x, y, QTableWidgetItem(QIcon("./images/bao1.png"), "backpack"))`添加图片，
或者也可以使用`tableWidgetItem.setIcon(QIcon('path'))`,然后再添加到`tableWidget`中

>Qt中的部件的弹出菜单(ContextMenu)，依据ContextMenuPolicy的值的不同，有四种形式：
一、默认菜单
此时，ContextMenuPolicy的值为Qt::DefaultContextMenu，这是默认值，其将显示部件定义的默认菜单
二、无菜单
此时,ContextMenuPolicy的值为Qt::NoContextMenu
三、由Action定义菜单
此时，ContextMenuPolicy的值为Qt::ActionsContextMenu,要为此部件定义这种菜单，很简单，只要把已经定义好的Action部件插入到要显示此菜单的部件中，部件将自动按顺序显示菜单。
QWidget::addAction(QAction *action);
四、自定义菜单
此时，ContextMenuPolicy的值为Qt::CustomContextMenu，这回，有两种方式来定义菜单，一种是响应
customContextMenuRequested()这个signal，在响应的槽中显示菜单(QMenu的exec()方法)。第二种是需要从这个部件的类中派生一个类，重写contextMenuEvent()这个函数显示菜单(QMenu的exec()方法显示)。

- 示例代码：
```python
class WinForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 800)
        layout = QHBoxLayout(self)
        self.tw = QTableWidget()
        self.tw.setRowCount(4)
        self.tw.setColumnCount(4)
        self.tw.setHorizontalHeaderLabels(['Picture', 'Picture', 'Picture', 'Picture'])
        self.tw.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw.setIconSize(QSize(300, 300))
        for i in range(4):
            self.tw.setColumnWidth(i, 300)
            self.tw.setRowHeight(i, 300)

        for i in range(4):
            for j in range(4):
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemIsEnabled)
                item.setIcon(QIcon('dinosaur.png'))
                self.tw.setItem(i, j, item)
        layout.addWidget(self.tw)
        self.tw.setContextMenuPolicy(Qt.DefaultContextMenu)

    def contextMenuEvent(self, event):
        menu = QMenu()
        a = menu.addAction("1")
        b = menu.addAction("2")
        item = self.tw.itemAt(event.pos())
        c = menu.exec_(self.mapToGlobal(event.pos()))
        if c == a:
            print(a.text())
        else:
            print(item.row(), item.column())
```