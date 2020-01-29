import json
import socket
import threading
import time
from _thread import *


class server:
	host = ''
	port = 42069
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def __init__(self):
		try:
			self.s.bind((self.host, self.port))
		except socket.error as e:
			print("Binding Error:\n\t" + str(e))

		self.s.listen(5)
		print('Waiting for a connection.')

		while True:
			conn, addr = self.s.accept()
			print('connected to: ' + addr[0] + ':' + str(addr[1]))
			time.sleep(1.5)
			start_new_thread(self.threaded_client, (conn,))

	def threaded_client(self, conn):
		while True:
			reply = ""
			data = conn.recv(2048)
			if data[0:1] == b'\x11':
				username = data[1:]
				reply = "NO RESPONSE YET"
			elif data[0:1] == b'\x12':
				password = data[1:]
				reply = "NO RESPONSE YET"
			elif data[0:1] == b'\x13':
				reply = self.signIn(username, password)
			elif data[0:1] == b'\x14':
				user = data[1:]
				reply = "NO RESPONSE YET"
			elif data[0:1] == b'\x15':
				user["classes"] = data[1:]
				reply = "NO RESPONSE YET"
			elif data[0:1] == b'\x16':
				self.addUser(user)
				reply = "Signed-Up"
			conn.sendall(str.encode(reply))
		conn.close()

	def signIn(self, name, password):
		with open('Confidential/Users.json', 'r') as f:
			userFile = json.load(f)
			for user in userFile['users']:
				if (name == user['Username']) & (password == user['Password']):
					return "Welcome!"
				elif (name == user['Username']) & (password != user['Password']):
					return "Password Failed"
			return "Failed"

	def addUser(self, user):
		with open('Confidential/Users.json', 'r+') as fp:
			data = json.load(fp)
			data["users"].append(user)
			fp.seek(0)
			json.dump(data, fp, indent=4)
			fp.truncate()
			fp.close()

server()
