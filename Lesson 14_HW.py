import sqlite3 as lite
import pprint
import pickle
import sys

def task1():
  con = None
  try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    query_string = '''
      --DISTINCT убирает дублирующиеся строки
      SELECT DISTINCT Customer.CustomerID, Customer.FirstName, Customer.LastName, Customer.Phone, Customer.Company
      FROM Customer 
      INNER JOIN Employee ON Customer.SupportRepId = Employee.EmployeeId
      INNER JOIN Invoice ON Customer.CustomerID = Invoice.CustomerID   
      INNER JOIN InvoiceLine ON InvoiceLine.InvoiceID = Invoice.InvoiceID    
      INNER JOIN Track ON InvoiceLine.TrackID = Track.TrackID  
      INNER JOIN Genre ON Track.GenreId = Genre.GenreId
      WHERE Genre.Name NOT LIKE 'Rock' AND Employee.BirthDate < "1969-05-19"
      ORDER BY Employee.City ASC, Employee.Email DESC  --ORDER - сортировка
      LIMIT 10    
        '''
    cur = con.cursor()
    cur.execute(query_string)
    pprint.pprint(cur.fetchall())
  except Exception as e:
    print(e)
    sys.exit(1)
  finally:
    if con is not None:
      con.close()

def task2():
  con = None
  try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    query_string = '''
      
      SELECT e.FirstName, e.LastName, e.Phone, e1.FirstName, e1.LastName, e1.Phone  FROM Employee e
      LEFT JOIN Employee as e1 ON e1.EmployeeID = e.ReportsTo


            '''
    cur = con.cursor()
    cur.execute(query_string)
    pprint.pprint(cur.fetchall())
    pickle_data = cur.fetchall()
    pickle_file = open('pickle.pickle','wb')
    pickle.dump(pickle_data, pickle_file)
    pickle_file.close()
  except Exception as e:
    print(e)
    sys.exit(1)
  finally:
    if con is not None:
      con.close()


def task3():
  con = None
  try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    query_string = '''
      SELECT DISTINCT Customer.FirstName, Customer.LastName, Customer.Phone
      FROM Customer 
      LEFT JOIN Invoice ON Customer.CustomerID = Invoice.CustomerID   
      LEFT JOIN InvoiceLine ON InvoiceLine.InvoiceID = Invoice.InvoiceID    
      LEFT JOIN Track ON InvoiceLine.TrackID = Track.TrackID    
      WHERE Track.UnitPrice = (SELECT MAX(Track.UnitPrice) FROM Track)
      ORDER BY Customer.FirstName
            '''
    cur = con.cursor()
    cur.execute(query_string)
    pprint.pprint(cur.fetchall())
  except Exception as e:
    print(e)
    sys.exit(1)
  finally:
    if con is not None:
      con.close()

