import socket
import os
from faker import Faker

fake = Faker("ja-JP")
name = fake.name()
print(name)

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "socket_file"

# ファイルが既に存在しないことを確認する
try:
   os.unlink(server_address)
except FileNotFoundError:
   pass

# ソケットをアドレスに紐付ける
print("Starting up on {}".format(server_address))
sock.bind(server_address)

# 接続
sock.listen(1)

# サーバが常に接続を待ち受けるためのループ
while True:
   
   connection, client_address = sock.accept()
   try:
      print("connection from", client_address)

      while True:
         data = connection.recv(1024)
         data_str = data.decode("utf-8")
         print("Received " + data_str)
         if data:
               message = input('メッセージを入力> ')
               # 現在のクライアントにメッセージを送り返す
               response = "From " + name + ": "+ message
               connection.sendall(response.encode())
         else:
               print("no data from", client_address)
               break

   finally:
      # 接続のクリーンアップ
      print("Closing current connection")
      connection.close()
