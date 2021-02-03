# -*- coding: utf-8 -*-
import mysql.connector





mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Zebobin10@"
)


if mydb.is_connected():
	db_info = mydb.get_server_info()
  	print("Conectado ao banco de dados: ",db_info)
	cursor = mydb.cursor()
	cursor.execute("CREATE DATABASE OlaMundo")
	linha = cursor.fetchone()
	print("Conectado ao banco de dados", linha)










if mydb.is_connected():
	cursor.close()
	mydb.close()
	print("Encerrada")




	


