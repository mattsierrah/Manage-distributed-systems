from db.db_connector import DbConnector

class LoginController:
  def __init__(self, request):
    self.request = request

  # public methods

  def login(self):
    if self.__valid_login():
      return True
    else:
      return False
    
  # private methods

  def __valid_login(self):
    db = DbConnector()
    users = db.find_user(self.__username(), self.__password(), self.__rol())
    if users:
      return True
    else:
      return False

  def __username(self):
    return self.request.form['username']

  def __password(self):
    return self.request.form['password']
  
  def __rol(self):
    return self.request.form['rol']
  