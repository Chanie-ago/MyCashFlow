import os
import sys
from src.ui_interface import *
import csv
from abc import ABC, abstractmethod
from datetime import datetime
import sqlite3
from sqlite3 import Error
from Custom_Widgets import *
from PySide6.QtWidgets import QMessageBox
from Custom_Widgets.QAppSettings import QAppSettings
from src.Funcions import GuiFunctions
from src.ui_interface import Ui_MainWindow

#DATABASE
DB_FILE = "MyCashFlow.db"

def create_connection():
    """Create a database connection to the SQLite database"""
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None


def initialize_database():
    """Initialize database and create tables if not exists"""
    income_table = """
    CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        amount REAL,
        category TEXT,
        description TEXT
    );
    """

    expense_table = """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        amount REAL,
        category TEXT,
        description TEXT
    );
    """

    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(income_table)
            conn.commit()
            conn.close()
        except Error as e:
            print(f"Error initializing database: {e}")

# Kelas abstrak untuk manajemen data
class BaseManager(ABC):
    @abstractmethod
    def add_entry(self, data):
        pass

    @abstractmethod
    def load_entries(self):
        pass

    @abstractmethod
    def delete_entry(self, entry_id):
        pass

# Kelas untuk manajemen pemasukan
class IncomeManager(BaseManager):
    def add_entry(self, data):
        """Menambahkan entri pemasukan ke database"""
        date, amount, category, description = data
        query = "INSERT INTO income (date, amount, category, description) VALUES (?, ?, ?, ?)"
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, (date, amount, category, description))
                conn.commit()
                conn.close()
            except Error as e:
                print(f"Error adding income: {e}")

    def load_entries(self):
        """Memuat data pemasukan dari database"""
        query = "SELECT * FROM income ORDER BY id DESC"
        conn = create_connection()
        rows = []
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                conn.close()
            except Error as e:
                print(f"Error loading income: {e}")
        return rows

    def delete_entry(self, entry_id):
        """Menghapus entri pemasukan berdasarkan ID"""
        query = "DELETE FROM income WHERE id = ?"
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, (entry_id,))
                conn.commit()
                conn.close()
            except Error as e:
                print(f"Error deleting income: {e}")

# Kelas untuk manajemen pengeluaran
class ExpenseManager(BaseManager):
    def add_entry(self, data):
        """Menambahkan entri pengeluaran ke database"""
        date, amount, category, description = data
        query = "INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)"
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, (date, amount, category, description))
                conn.commit()
                conn.close()
            except Error as e:
                print(f"Error adding expense: {e}")

    def load_entries(self):
        """Memuat data pengeluaran dari database"""
        query = "SELECT * FROM expenses ORDER BY id DESC"
        conn = create_connection()
        rows = []
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                conn.close()
            except Error as e:
                print(f"Error loading expenses: {e}")
        return rows

    def delete_entry(self, entry_id):
        """Menghapus entri pengeluaran berdasarkan ID"""
        query = "DELETE FROM expenses WHERE id = ?"
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, (entry_id,))
                conn.commit()
                conn.close()
            except Error as e:
                print(f"Error deleting expense: {e}")

# Fungsi untuk membuat koneksi ke database
def create_connection():
    """Create a database connection to the SQLite database"""
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Kelas utama untuk antarmuka pengguna
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Inisialisasi manajer
        self.income_manager = IncomeManager()
        self.expense_manager = ExpenseManager()

        # Gunakan ini untuk menentukan file json
        loadJsonStyle(self, self.ui, jsonFiles={
            "json-styles/style.json"
        })

        self.show()

        QAppSettings.updateAppSettings(self)

        initialize_database()
        self.setup_table_widgets()

        self.app_functions = GuiFunctions(self)

        # Hubungkan tombol
        self.ui.addIncomeButton.clicked.connect(self.add_income)
        self.ui.addExpenseButton.clicked.connect(self.add_expense)
        self.ui.refreshButton.clicked.connect(self.load_income)
        self.ui.refreshButton_2.clicked.connect(self.load_expenses)
        self.ui.incomeRefreshButton.clicked.connect(self.filter_income)
        self.ui.expenseRefreshButton.clicked.connect(self.filter_expenses)
        self.ui.downloadButton.clicked.connect(self.download_report)

        self.ui.deleteIncomeButton.clicked.connect(self.delete_income)
        self.ui.deleteExpenseButton.clicked.connect(self.delete_expense)

        self.load_income()
        self.load_expenses()

    def setup_table_widgets(self):
        """Setup untuk tabel pemasukan dan pengeluaran"""
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Tanggal", "Jumlah", "Kategori"])

        self.ui.expenseTableWidget_2.setColumnCount(3)
        self.ui.expenseTableWidget_2.setHorizontalHeaderLabels(["Tanggal", "Jumlah", "Kategori"])

    def add_income(self):
        """Menambahkan entri pemasukan"""
        data = (
            self.ui.incomeDataEdit.text(),
            self.ui.incomeAmountEdit.text(),
            self.ui.incomeCategoryEdit.text(),
            self.ui.incomeDescriptionEdit.text()
        )
        self.income_manager.add_entry(data)
        self.load_income()

    def add_expense(self):
        """Menambahkan entri pengeluaran"""
        data = (
            self.ui.expenseDateEdit.text(),
            self.ui.expenseAmountEdit.text(),  # Pastikan ini benar
            self.ui.expenseCategoryEdit.text(),
            self.ui.expenseDescriptionEdit.text()
        )
        self.expense_manager.add_entry(data)
        self.load_expenses()

    def load_income(self):
        """Memuat data pemasukan ke dalam tabel widget"""
        rows = self.income_manager.load_entries()
        self.ui.incomeTableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.ui.incomeTableWidget.setItem(i, j, QTableWidgetItem(str(value)))

    def load_expenses(self):
        """Memuat data pengeluaran ke dalam tabel widget"""
        rows = self.expense_manager.load_entries()
        self.ui.expenseTableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.ui.expenseTableWidget.setItem(i, j, QTableWidgetItem(str(value)))

    def filter_income(self):
        """Filter data pemasukan berdasarkan tanggal"""
        selected_date = self.ui.incomeDateEditFilter.date().toString("dd/MM/yyyy")
        query = "SELECT date, amount, category FROM income WHERE date LIKE ? ORDER BY id DESC"
        total_income_query = "SELECT SUM(amount) FROM income WHERE date LIKE ?"
        total_expense_query = "SELECT SUM(amount) FROM expenses WHERE date LIKE ?"

        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, (f"%{selected_date}%",))
                rows = cursor.fetchall()

                self.ui.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        self.ui.tableWidget.setItem(i, j, item)

                cursor.execute(total_income_query, (f"%{selected_date}%",))
                total_income = cursor.fetchone()[0] or 0

                cursor.execute(total_expense_query, (f"%{selected_date}%",))
                total_expense = cursor.fetchone()[0] or 0

                saldo = total_income - total_expense

                self.ui.labelTotalIncome.setText(f"Total Pemasukan: Rp {total_income:,.2f}")
                self.ui.labelSaldo.setText(f"Saldo: Rp {saldo:,.2f}")

                conn.close()
            except Error as e:
                print(f"Error saat memfilter data pemasukan: {e}")

    def filter_expenses(self):
        """Filter data pengeluaran berdasarkan tanggal"""
        selected_date = self.ui.expenseDateEditFilter.date().toString("dd/MM/yyyy")
        query = "SELECT date, amount, category FROM expenses WHERE date LIKE ? ORDER BY id DESC"
        total_query = "SELECT SUM(amount) FROM expenses WHERE date LIKE ?"

        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, (f"%{selected_date}%",))
                rows = cursor.fetchall()

                self.ui.expenseTableWidget_2.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        self.ui.expenseTableWidget_2.setItem(i, j, item)

                cursor.execute(total_query, (f"%{selected_date}%",))
                total = cursor.fetchone()[0] or 0
                self.ui.labelTotalExpense.setText(f"Total Pengeluaran: Rp {total:,.2f}")

                conn.close()
            except Error as e:
                print(f"Error saat memfilter data pengeluaran: {e}")

    def delete_income(self):
        """Menghapus data pemasukan yang dipilih"""
        current_row = self.ui.incomeTableWidget.currentRow()
        if current_row < 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Silakan pilih data yang akan dihapus")
            msg.setWindowTitle("Peringatan")
            msg.exec()
            return

        # Ambil ID dari kolom pertama (kolom ID)
        id_item = self.ui.incomeTableWidget.item(current_row, 0)
        if id_item is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Data tidak valid")
            msg.setWindowTitle("Peringatan")
            msg.exec()
            return

        income_id = id_item.text()

        # Konfirmasi penghapusan
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Anda yakin ingin menghapus data ini?")
        msg.setWindowTitle("Konfirmasi")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if msg.exec() == QMessageBox.No:
            return

        # Hapus data berdasarkan ID
        self.income_manager.delete_entry(income_id)
        self.load_income()

    def delete_expense(self):
        """Menghapus data pengeluaran yang dipilih"""
        current_row = self.ui.expenseTableWidget.currentRow()
        if current_row < 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Silakan pilih data yang akan dihapus")
            msg.setWindowTitle("Peringatan")
            msg.exec()
            return

        # Ambil ID dari kolom pertama (kolom ID)
        id_item = self.ui.expenseTableWidget.item(current_row, 0)
        if id_item is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Data tidak valid")
            msg.setWindowTitle("Peringatan")
            msg.exec()
            return

        expense_id = id_item.text()

        # Konfirmasi penghapusan
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Anda yakin ingin menghapus data ini?")
        msg.setWindowTitle("Konfirmasi")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if msg.exec() == QMessageBox.No:
            return

        # Hapus data berdasarkan ID
        self.expense_manager.delete_entry(expense_id)
        self.load_expenses()

    def download_report(self):
        """Download laporan keuangan dalam format CSV"""
        selected_date = self.ui.reportDateEdit.date().toString("dd/MM/yyyy")

        income_query = "SELECT date, amount, category, description FROM income WHERE date LIKE ?"
        expense_query = "SELECT date, amount, category, description FROM expenses WHERE date LIKE ?"

        try:
            conn = create_connection()
            cursor = conn.cursor()

            cursor.execute(income_query, (f"%{selected_date}%",))
            income_data = cursor.fetchall()

            cursor.execute(expense_query, (f"%{selected_date}%",))
            expense_data = cursor.fetchall()

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"laporan_keuangan_{timestamp}.csv"

            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Tipe', 'Tanggal', 'Jumlah', 'Kategori', 'Keterangan'])

                for row in income_data:
                    writer.writerow(['Pemasukan'] + list(row))

                for row in expense_data:
                    writer.writerow(['Pengeluaran'] + list(row))

                total_income = sum(float(row[1]) for row in income_data if row[1])
                total_expense = sum(float(row[1]) for row in expense_data if row[1])
                writer.writerow([])
                writer.writerow(['Total Pemasukan', f"Rp {total_income:,.2f}"])
                writer.writerow(['Total Pengeluaran', f"Rp {total_expense:,.2f}"])
                writer.writerow(['Saldo', f"Rp {(total_income - total_expense):,.2f}"])

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Laporan berhasil diunduh!\n\nNama file: {filename}\nLokasi: {os.path.abspath(filename)}")
            msg.setWindowTitle("Sukses")
            msg.exec()

        except Error as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Terjadi kesalahan saat mengakses database:\n{str(e)}")
            msg.setWindowTitle("Error")
            msg.exec()

        finally:
            if 'conn' in locals() and conn:
                conn.close()

# Eksekusi aplikasi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())