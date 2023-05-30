import socket
import sys
from faker import Faker

fake = Faker("ja-JP")
name = fake.name()
print(name)

# TCP/IPソケットの作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# サーバが待ち受けているポートにソケットを接続します
server_address = 'socket_file'
print('connecting to {}'.format(server_address))

try:
   sock.connect(server_address)
except socket.error as err:
   print(err)
   sys.exit(1)

try:

   try:
      while True:
         # データ送信
         message = input('メッセージを入力> ')
         message = "From " + name + ": " + message
         sock.sendall(message.encode('utf-8'))

         data = sock.recv(1024)
         data = data.decode('utf-8')
         if data:
            print('Server response ' + data)
         else:
            break
   except(TimeoutError):
      print('Socket timeout, ending listening for server messages')

finally:
   print('closing socket')
   sock.close()


