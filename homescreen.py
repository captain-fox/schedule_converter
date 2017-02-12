
import file_manager
import group_manager
import time_keeper
import os
import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QComboBox, QLabel, QCalendarWidget, QMessageBox
from PyQt5 import QtCore


class Window(QWidget):

    rows = []
    term = []

    def __init__(self):
        super(Window, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.open_file_button = QPushButton('Wybierz plik .csv')
        self.open_file_button.clicked.connect(self.open_file)

        self.term = QLabel('Okres zajęć w semestrze źimowym: 2016/9/26 – 2017/1/25')
        self.holidays = QLabel('Ferie źimowe: 2016/12/22 – 2017/1/2')

        self.choose_group_label = QLabel('Wybierz grupę ćwiczeniwą')
        self.list_of_groups = QComboBox()

        self.generate_ics_button = QPushButton("Generuj plik .ics")
        self.generate_ics_button.setEnabled(False)
        self.generate_ics_button.clicked.connect(self.create_ics)

        open_file_hbox = QHBoxLayout()
        open_file_hbox.addStretch()
        open_file_hbox.addWidget(self.open_file_button)
        open_file_hbox.addStretch()

        term_dates1 = QHBoxLayout()
        term_dates1.addStretch()
        term_dates1.addWidget(self.term)
        term_dates1.addStretch()

        term_dates2 = QHBoxLayout()
        term_dates2.addStretch()
        term_dates2.addWidget(self.holidays)
        term_dates2.addStretch()

        select_group_hbox = QHBoxLayout()
        select_group_hbox.addStretch()
        select_group_hbox.addWidget(self.choose_group_label)
        select_group_hbox.addWidget(self.list_of_groups)
        select_group_hbox.addStretch()

        generate_ics_hbox = QHBoxLayout()
        generate_ics_hbox.addStretch()
        generate_ics_hbox.addWidget(self.generate_ics_button)
        generate_ics_hbox.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(open_file_hbox)
        main_layout.addLayout(term_dates1)
        main_layout.addLayout(term_dates2)
        main_layout.addLayout(select_group_hbox)
        main_layout.addLayout(generate_ics_hbox)
        main_layout.addStretch()

        self.setLayout(main_layout)
        self.setWindowTitle('Schedule converter')
        self.setGeometry(400, 300, 450, 300)
        self.show()

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.chdir("."))
        self.rows = file_manager.parse_file(filename[0])
        print(filename[0])

        # Creating list of groups –––––––––––––––––––––––––––––––––––––––––––––––––
        groups = group_manager.get_groups(self.rows)
        self.list_of_groups.addItems(groups)

        # Sets term and holidays break
        self.term = time_keeper.set_term()

        self.generate_ics_button.setEnabled(True)

    def create_ics(self):
        user_group = self.list_of_groups.currentText()
        group_manager.preview_output_file(self.rows, user_group, self.term)
        # group_manager.create_calendar_for(self.rows, user_group, self.term)



app = QApplication(sys.argv)
writer = Window()
sys.exit(app.exec_())