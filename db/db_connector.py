import mysql.connector

class DbConnector:
  DB_HOST = 'localhost'
  DB_USER = 'root'
  DB_PASSWORD = 'password'
  DB_NAME = 'ms_multi_users_db'

  def __init__(self):
    self.db_manager = self.__manage_db()

  def find_user(self, name, password, rol_name):
    rol_id = self.find_rol(rol_name)
    query = f"SELECT * FROM USER WHERE name = '{name}' AND password = '{password}' AND RolId = '{rol_id}'"
    current_db = self.__db()
    cursor = current_db.cursor()
    cursor.execute(query)
    users = cursor.fetchall()
    if users == []:
      return False
    return users[0]
  
  def find_rol(self, rol_name):
    query = f"SELECT * FROM ROL WHERE name = '{rol_name}'"
    current_db = self.__db()
    cursor = current_db.cursor()
    cursor.execute(query)
    rol = cursor.fetchall()
    if rol:
      return rol[0][0]
    else:
      return None

  # private methods

  def __manage_db(self):
    if self.__exist_db():
      return True
    else:
      self.__create_db()

  def __exist_db(self):
    current_db = self.__connector()
    cursor = current_db.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    if databases == None:
      return False
    for db_name in databases:
      if db_name[0] == self.DB_NAME:
        return True
    return False

  def __connector(self):
    db = mysql.connector.connect(
      host = self.DB_HOST,
      user = self.DB_USER,
      password = self.DB_PASSWORD
    )

    return db
  
  def __create_db(self):
    current_db =  self.__connector()
    cursor = current_db.cursor()
    query = f"CREATE DATABASE {self.DB_NAME}"
    cursor.execute(query)

    current_db = self.__db()
    cursor = current_db.cursor()
    self.__create_tables(cursor)
    self.__insert_rol(current_db, cursor)
    self.__insert_users(current_db, cursor)
    return True
  
  def __create_tables(self, cursor):
    cursor.execute(
      "CREATE TABLE Rol (RolId int NOT NULL AUTO_INCREMENT, name varchar(20) NOT NULL, created_at datetime, PRIMARY KEY (RolId));"
    )
    cursor.execute(
      "CREATE TABLE User (UserId int NOT NULL AUTO_INCREMENT, name varchar(20) NOT NULL, password varchar(50) NOT NULL, RolId int, created_at datetime, PRIMARY KEY (UserId), FOREIGN KEY (RolId) REFERENCES Rol(RolId));"
    )

  def __insert_rol(self, db, cursor):
    query = "INSERT INTO Rol (name, created_at) VALUES (%s, %s)"
    values = [
      ('Administrador', None),
      ('Operativo', None),
      ('General', None)
    ]
    cursor.executemany(query, values)
    db.commit()

  def __insert_users(self, db, cursor):
    query = "INSERT INTO User (name, password, RolId, created_at) VALUES (%s, %s, %s, %s)"
    values = [
      ('MatyAdmin','MatyAdmin', self.find_rol('Administrador'), None),
      ('MatyOPerativo','MatyOPerativo', self.find_rol('Operativo'), None),
      ('MatyGeneral', 'MatyGeneral', self.find_rol('General'),  None)
    ]
    cursor.executemany(query, values)
    db.commit()

  def __db(self):
    db = mysql.connector.connect(
      host = self.DB_HOST,
      user = self.DB_USER,
      password = self.DB_PASSWORD,
      database = self.DB_NAME
    )
    return db
  

  