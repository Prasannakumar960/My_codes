IMPORT PYODBC

PYODBC.CONNECT("",10.)
CURSOR.EXECUTE("SELECT * FROM TABLE WHERE DS='CO')
FILE.WRITE(CURSOR)