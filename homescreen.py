from PyQt5 import QtCore
from datetime import *
import file_manager
import group_manager
import time_keeper
import calendar
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

        # self.termlable = QLabel('Okres zajęć w semestrze źimowym: 2016/9/26 – 2017/1/25')
        # self.termlable.setVisible(False)
        # self.holidays = QLabel('Ferie źimowe: 2016/12/22 – 2017/1/2')
        # self.holidays.setVisible(False)

# Term & Holidays –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

        years = ['2016', '2017', '2018', '2019', '2020']
        months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

# Semester start ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        self.term_start_label = QLabel('Semestr zaczyna się: ')
        self.term_start_year = QComboBox()
        self.term_start_year.setEnabled(False)
        self.term_start_year.setFixedWidth(80)
        self.term_start_year.addItems(years)
        self.term_start_year.activated[str].connect(self.get_days_start_sem)
        self.term_start_months = QComboBox()
        self.term_start_months.setEnabled(False)
        self.term_start_months.setFixedWidth(60)
        self.term_start_months.addItems(months)
        self.term_start_months.activated[str].connect(self.get_days_start_sem)
        self.term_start_days = QComboBox()
        self.term_start_days.setEnabled(False)
        self.term_start_days.setFixedWidth(60)

        semester_start_hbox = QHBoxLayout()
        semester_start_hbox.addStretch()
        semester_start_hbox.addWidget(self.term_start_label)
        semester_start_hbox.addWidget(self.term_start_year)
        semester_start_hbox.addWidget(self.term_start_months)
        semester_start_hbox.addWidget(self.term_start_days)
        semester_start_hbox.addStretch()

# Semester end ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        self.term_end_label = QLabel('Semestr kończy się: ')
        self.term_end_year = QComboBox()
        self.term_end_year.setEnabled(False)
        self.term_end_year.setFixedWidth(80)
        self.term_end_year.addItems(years)
        self.term_end_year.activated[str].connect(self.get_days_end_sem)
        self.term_end_months = QComboBox()
        self.term_end_months.setEnabled(False)
        self.term_end_months.setFixedWidth(60)
        self.term_end_months.addItems(months)
        self.term_end_months.activated[str].connect(self.get_days_end_sem)
        self.term_end_days = QComboBox()
        self.term_end_days.setEnabled(False)
        self.term_end_days.setFixedWidth(60)


        semester_end_hbox = QHBoxLayout()
        semester_end_hbox.addStretch()
        semester_end_hbox.addWidget(self.term_end_label)
        semester_end_hbox.addWidget(self.term_end_year)
        semester_end_hbox.addWidget(self.term_end_months)
        semester_end_hbox.addWidget(self.term_end_days)
        semester_end_hbox.addStretch()

# Holidays start ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        self.hol_start_label = QLabel('Ferie zaczną się: ')
        self.hol_start_year = QComboBox()
        self.hol_start_year.setEnabled(False)
        self.hol_start_year.addItems(years)
        self.hol_start_year.activated[str].connect(self.get_days_start_hol)
        self.hol_start_month = QComboBox()
        self.hol_start_month.setEnabled(False)
        self.hol_start_month.addItems(months)
        self.hol_start_month.activated[str].connect(self.get_days_start_hol)
        self.hol_start_days = QComboBox()
        self.hol_start_days.setEnabled(False)

        holidays_start_hbox = QHBoxLayout()
        holidays_start_hbox.addStretch()
        holidays_start_hbox.addWidget(self.hol_start_label)
        holidays_start_hbox.addWidget(self.hol_start_year)
        holidays_start_hbox.addWidget(self.hol_start_month)
        holidays_start_hbox.addWidget(self.hol_start_days)
        holidays_start_hbox.addStretch()

# Holidays end ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        self.hol_end_label = QLabel('Ferie skończą się:')
        self.hol_end_year = QComboBox()
        self.hol_end_year.setEnabled(False)
        self.hol_end_year.addItems(years)
        self.hol_end_year.activated[str].connect(self.get_days_end_hol)
        self.hol_end_month = QComboBox()
        self.hol_end_month.setEnabled(False)
        self.hol_end_month.addItems(months)
        self.hol_end_month.activated[str].connect(self.get_days_end_hol)
        self.hol_end_days = QComboBox()
        self.hol_end_days.setEnabled(False)

        holidays_end_hbox = QHBoxLayout()
        holidays_end_hbox.addStretch()
        holidays_end_hbox.addWidget(self.hol_end_label)
        holidays_end_hbox.addWidget(self.hol_end_year)
        holidays_end_hbox.addWidget(self.hol_end_month)
        holidays_end_hbox.addWidget(self.hol_end_days)
        holidays_end_hbox.addStretch()



# Groups ComboBox ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
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

        select_group_hbox = QHBoxLayout()
        select_group_hbox.addStretch()
        select_group_hbox.addWidget(self.list_of_groups)
        select_group_hbox.addWidget(self.chx)
        select_group_hbox.addStretch()

        generate_ics_hbox = QHBoxLayout()
        generate_ics_hbox.addStretch()
        generate_ics_hbox.addWidget(self.generate_ics_button)
        generate_ics_hbox.addStretch()

        self.pbar = QProgressBar()
        self.pbar.setVisible(False)
        self.status_label = QLabel()
        self.placeholder = QLabel()
        self.status_label.setText('Gotowe!')
        self.status_label.setVisible(False)
        status_hbox = QHBoxLayout()
        status_hbox.addStretch()
        status_hbox.addWidget(self.pbar)
        status_hbox.addWidget(self.placeholder)
        status_hbox.addWidget(self.status_label)
        status_hbox.addStretch()

# Main layout ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(open_file_hbox)
        main_layout.addLayout(semester_start_hbox)
        main_layout.addLayout(semester_end_hbox)
        main_layout.addLayout(holidays_start_hbox)
        main_layout.addLayout(holidays_end_hbox)
        main_layout.addLayout(select_group_hbox)
        main_layout.addLayout(generate_ics_hbox)
        main_layout.addLayout(status_hbox)
        main_layout.addStretch()

        self.setLayout(main_layout)
        self.setWindowTitle('Generator planu zajęć')
        self.setGeometry(400, 300, 550, 400)
        self.show()

# Controller ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.chdir("."))
        if filename[0] is not '':
            self.rows = file_manager.parse_file(filename[0])
            print(filename[0])

            # Filling days
            self.term_start_year.setEnabled(True)
            self.term_start_months.setEnabled(True)
            self.term_start_days.setEnabled(True)

            self.term_end_year.setEnabled(True)
            self.term_end_months.setEnabled(True)
            self.term_end_days.setEnabled(True)

            self.hol_start_year.setEnabled(True)
            self.hol_start_month.setEnabled(True)
            self.hol_start_days.setEnabled(True)

            self.hol_end_year.setEnabled(True)
            self.hol_end_month.setEnabled(True)
            self.hol_end_days.setEnabled(True)


            self.get_days_start_sem()
            self.get_days_end_sem()
            self.get_days_start_hol()
            self.get_days_end_hol()
            # Creating list of groups –––––––––––––––––––––––––––––––––––––––––––––––––
            self.groups = group_manager.get_groups(self.rows)
            self.list_of_groups.addItems(self.groups)


            # Sets term and holidays break
            # self.term = time_keeper.set_term()
            # self.termlable.setVisible(True)
            # self.holidays.setVisible(True)
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
        sem_str_y = int(self.term_start_year.currentText())
        sem_str_m = int(self.term_start_months.currentText())
        sem_str_d = int(self.term_start_days.currentText())
        term_start = date(sem_str_y, sem_str_m, sem_str_d)
        print('Sem start: ', term_start)

        sem_end_y = int(self.term_end_year.currentText())
        sem_end_m = int(self.term_end_months.currentText())
        sem_end_d = int(self.term_end_days.currentText())
        term_end = date(sem_end_y, sem_end_m, sem_end_d)
        print('Sem end: ', term_end)

        hol_str_y = int(self.hol_start_year.currentText())
        hol_str_m = int(self.hol_start_month.currentText())
        hol_str_d = int(self.hol_start_days.currentText())
        holidays_start = date(hol_str_y, hol_str_m, hol_str_d)
        print('Hol start: ', holidays_start)

        hol_end_y = int(self.hol_end_year.currentText())
        hol_end_m = int(self.hol_end_month.currentText())
        hol_end_d = int(self.hol_end_days.currentText())
        holidays_end = date(hol_end_y, hol_end_m, hol_end_d)
        print('Hol end: ', holidays_end)

        self.term = time_keeper.set_term(term_start, term_end, holidays_start, holidays_end)

        self.generate_ics_button.setEnabled(False)
        self.status_label.setVisible(False)
        self.placeholder.setVisible(False)

        if self.chx.isChecked():
            self.pbar.setVisible(True)
            i = 0
            max = int(len(self.groups))
            self.pbar.setRange(i, max)
            for group in self.groups:
                # group_manager.preview_output_file(self.rows, group, self.term)
                group_manager.create_calendar_for(self.rows, group, self.term)
                i += 1
                self.pbar.setValue(i)
                QApplication.processEvents()
        else:
            user_group = self.list_of_groups.currentText()
            group_manager.create_calendar_for(self.rows, user_group, self.term)

        self.pbar.setVisible(False)
        self.status_label.setVisible(True)
        self.generate_ics_button.setEnabled(True)

    def get_days_start_sem(self):
        self.term_start_days.clear()
        year = int(self.term_start_year.currentText())
        month = int(self.term_start_months.currentText())
        days_in_month = calendar.monthrange(year, month)[1]
        for day in range(days_in_month):
            self.term_start_days.addItem(str(day+1))

    def get_days_end_sem(self):
        self.term_end_days.clear()
        year = int(self.term_end_year.currentText())
        month = int(self.term_end_months.currentText())
        days_in_month = calendar.monthrange(year, month)[1]
        for day in range(days_in_month):
            self.term_end_days.addItem(str(day+1))

    def get_days_start_hol(self):
        self.hol_start_days.clear()
        year = int(self.hol_start_year.currentText())
        month = int(self.hol_start_month.currentText())
        days_in_month = calendar.monthrange(year, month)[1]
        for day in range(days_in_month):
            self.hol_start_days.addItem(str(day+1))

    def get_days_end_hol(self):
        self.hol_end_days.clear()
        year = int(self.hol_end_year.currentText())
        month = int(self.hol_end_month.currentText())
        days_in_month = calendar.monthrange(year, month)[1]
        for day in range(days_in_month):
            self.hol_end_days.addItem(str(day+1))


app = QApplication(sys.argv)
directory = os.getcwd()
path = directory + '/Output'
if not os.path.exists(path):
    os.makedirs(path)
writer = Window()
sys.exit(app.exec_())
