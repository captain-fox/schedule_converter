import urllib

import time

import file_manager
import group_manager
import time_keeper
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QComboBox, QLabel, QCheckBox, QProgressBar


class Window(QWidget):

    rows = []
    term = []
    groups = []

    def __init__(self):
        super(Window, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.open_file_button = QPushButton('Wybierz plik .csv')
        self.open_file_button.clicked.connect(self.open_file)

        self.termlable = QLabel('Okres zajęć w semestrze źimowym: 2016/9/26 – 2017/1/25')
        self.termlable.setVisible(False)
        self.holidays = QLabel('Ferie źimowe: 2016/12/22 – 2017/1/2')
        self.holidays.setVisible(False)

        self.choose_group_label = QLabel('Wybierz grupę ćwiczeniową')
        self.list_of_groups = QComboBox()
        self.list_of_groups.addItem('Wybierz grupę ćwiczeniową')
        self.list_of_groups.setEnabled(False)
        # self.list_of_groups.pyqtSignal.connect(self.check_selection())
        self.chx = QCheckBox('Wybierz wszystkie')
        self.chx.clicked.connect(self.switch_list)
        self.chx.setEnabled(False)

        self.generate_ics_button = QPushButton("Generuj plik .ics")
        self.generate_ics_button.setEnabled(False)
        self.generate_ics_button.clicked.connect(self.create_ics)

        open_file_hbox = QHBoxLayout()
        open_file_hbox.addStretch()
        open_file_hbox.addWidget(self.open_file_button)
        open_file_hbox.addStretch()

        term_dates1 = QHBoxLayout()
        term_dates1.addStretch()
        term_dates1.addWidget(self.termlable)
        # term_dates1.addWidget(self.term_start_year)
        # term_dates1.addWidget(self.term_start_month)
        # term_dates1.addWidget(self.term_start_day)
        term_dates1.addStretch()

        term_dates2 = QHBoxLayout()
        term_dates2.addStretch()
        term_dates2.addWidget(self.holidays)
        term_dates2.addStretch()

        select_group_hbox = QHBoxLayout()
        select_group_hbox.addStretch()
        # select_group_hbox.addWidget(self.choose_group_label)
        select_group_hbox.addWidget(self.list_of_groups)
        select_group_hbox.addWidget(self.chx)
        select_group_hbox.addStretch()

        generate_ics_hbox = QHBoxLayout()
        generate_ics_hbox.addStretch()
        generate_ics_hbox.addWidget(self.generate_ics_button)
        generate_ics_hbox.addStretch()

        # self.pbar = QProgressBar()
        self.status_label_counter = QLabel()
        self.status_label_from = QLabel(' from: ')
        self.status_label_total = QLabel()
        status_hbox = QHBoxLayout()
        status_hbox.addStretch()
        status_hbox.addWidget(self.status_label_counter)
        status_hbox.addWidget(self.status_label_from)
        status_hbox.addWidget(self.status_label_total)
        status_hbox.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(open_file_hbox)
        main_layout.addLayout(term_dates1)
        main_layout.addLayout(term_dates2)
        main_layout.addLayout(select_group_hbox)
        main_layout.addLayout(generate_ics_hbox)
        main_layout.addLayout(status_hbox)
        main_layout.addStretch()

        self.setLayout(main_layout)
        self.setWindowTitle('Generator planu zajęć')
        self.setGeometry(400, 300, 550, 400)
        self.show()

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.chdir("."))
        if filename[0] is not '':
            self.rows = file_manager.parse_file(filename[0])
            print(filename[0])

            # Creating list of groups –––––––––––––––––––––––––––––––––––––––––––––––––
            self.groups = group_manager.get_groups(self.rows)
            self.list_of_groups.addItems(self.groups)

            # Sets term and holidays break
            self.term = time_keeper.set_term()
            self.termlable.setVisible(True)
            self.holidays.setVisible(True)
            self.list_of_groups.setEnabled(True)
            self.chx.setEnabled(True)
            self.generate_ics_button.setEnabled(True)

    def switch_list(self):
        if self.chx.isChecked():
            self.list_of_groups.setEnabled(False)
        else:
            self.list_of_groups.setEnabled(True)

    def create_ics(self):
        os.chdir(path)

        if self.chx.isChecked():
            self.status_label.setVisible(True)
            i = 0
            self.status_label_total.setText(str(len(self.groups)))
            for group in self.groups:
                # group_manager.preview_output_file(self.rows, group, self.term)
                group_manager.create_calendar_for(self.rows, group, self.term)
                i += 1
                print('iteration: ', i)
                self.status_label_counter.setText(str(i))
                QApplication.processEvents()
        else:
            user_group = self.list_of_groups.currentText()
            # group_manager.preview_output_file(self.rows, user_group, self.term)
            group_manager.create_calendar_for(self.rows, user_group, self.term)


app = QApplication(sys.argv)
dir = os.getcwd()
path = dir + '/Output'
# os.mkdir(path)
writer = Window()
sys.exit(app.exec_())
