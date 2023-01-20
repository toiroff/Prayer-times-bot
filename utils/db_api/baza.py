import sqlite3
import pandas as pd
from openpyxl import Workbook
import matplotlib.pyplot as plt
from reportlab.lib import pagesizes
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


bazajon = sqlite3.connect('namoz.db')

data = pd.read_sql_query("SELECT * FROM users", bazajon)
book = Workbook()
writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
writer.book = book
data.to_excel(writer, index=False)
writer.save()

data = pd.read_sql_query("SELECT * FROM users", bazajon)

# Plot the data using matplotlib
plt.plot(data['id'])
plt.plot(data['ism'])
plt.plot(data['tg_id'])
plt.plot(data['username'])
plt.plot(data['viloyat'])
plt.ylabel('Y Label')
plt.xlabel('X Label')

# Save the plot as a PNG image
plt.savefig('data.png')

# Create a PDF document with the chart or plot
c = canvas.Canvas("data.pdf", pagesize=letter)
c.drawImage('data.png', 0, 0, width=500, height=500)
c.showPage()
c.save()



def bot_stat():
    odam = bazajon.execute('''SELECT tg_id FROM users''')
    return odam.fetchall()


class Database:
    def __init__(self,path_to_db="main.db"):
        self.path_to_db= path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self,sql: str,parameters: tuple=None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters=()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data=None
        cursor.execute(sql,parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql ="""
        CREATE TABLE myfiles_teacher (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            laguage varchar(3),
            PRIMARY KEY (id)
            );
"""

    @staticmethod
    def format_args(sql, parameters:dict):
        sql += " AND ".join([
            f"{item}=?"for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str,email: str=None, laguage: str="uz"):
          # SQL_EXAMPLE ="INSERT INTO myfiles_teacher(id,name,email)VALUES(1,"john","john@hgmail.com")"

        sql="""
        INSERT INTO myfiles_teacher (id, name, email, laguage) VALUES(?,?,?,?)
        """
        self.execute(sql, parameters=(id, name, email, laguage), commit=True)

    def select_all_users(self):
        sql="""
        SELECT * FROM myfiles_teacher
        """
        return self.execute(sql, fetchall=True)

    def select_user(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"

        sql = "SELEFT * FROM myfiles_teacher WHERE"
        sql , parameters = self.format_args(sql,kwargs)
        return self.execute(sql, parameters=parameters,fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*)FROM myfiles_teacher;",fetchone=True)

    def delete_user(self):
        self.execute("DELETE FROM myfiles_teacher WHERE TRUE",commit=True)

# -------------------- O'zim ishlaganim-------------------------------

    def user_qoshish(self,  ism: str, tg_id:int,  fam: str, username : str,viloyat: str):
        # SQL_EXAMPLE ="INSERT INTO myfiles_teacher(id,name,email)VALUES(1,"john","john@hgmail.com")"

        sql="""
        INSERT INTO users (ism,fam, tg_id, username,viloyat) VALUES(?,?,?,?,?)
        """
        self.execute(sql, parameters=( ism, fam, tg_id,username,viloyat), commit=True)

    def select_all_foidalanuvchilar(self):
        sql="""
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)
    def select_royxat(self):
        sql="""
        SELECT * FROM users
        """
        return self.execute(sql, fetchone=True
                            )
    def filter_users(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)
    def barcha(self):
        return self.execute("SELECT COUNT(*)FROM users;",fetchone=True)

    def filter(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def update(self, viloyat, tg_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
        UPDATE users
         SET viloyat=? WHERE tg_id=?
        """
        return self.execute(sql, parameters=(viloyat, tg_id), commit=True)

    def count(self):
        return self.execute("SELECT COUNT(*)FROM users;",fetchone=True)

    def count_1kun(self):
        return self.execute("SELECT COUNT(*)FROM users WHERE time('now','-1 day')",fetchone=True)

    def count_1oy(self):
        return self.execute("SELECT COUNT(*)FROM users WHERE time('now','-1 month')",fetchone=True)


def logger(statement):
    print(f"""
    --------------------------------------------------------
    Executing:
    {statement}
    --------------------------------------------------------
""")

