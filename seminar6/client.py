import sys
import time

from PyQt5 import QtWidgets, QtCore
import socket
import threading
import chat_c as q

global nickname, serv_line, port_line

serv_line = '192.168.0.105'
port_line = 55444
nickname = 'Client: '
server = serv_line, port_line
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55444))
sock.sendto(str.encode(nickname + ' connected'), (serv_line, port_line))


class LanMessenger(QtWidgets.QMainWindow, q.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.write_soc)
        self.pushButton_2.clicked.connect(self.settings)

    def read_soc(self):
        while True:
            data = sock.recv(1024)

            self.textBrowser.append(bytes.decode(data))

    def write_soc(self):
        msg = self.lineEdit.text()
        self.textBrowser.append(msg)
        sock.sendto(str.encode(nickname + msg), (serv_line, port_line))
        self.lineEdit.clear()


    def conn_start(self):
        trd_client_r = threading.Thread(target=self.read_soc)
        trd_client_r.start()

    def settings(self):
        global nickname, serv_line, port_line
        serv_line = self.lineEdit_2.text()
        port_line = int(self.lineEdit_3.text())
        nickname = self.lineEdit_4.text()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LanMessenger()
    window.show()
    window.conn_start()
    app.exec_()


if __name__ == '__main__':
    main()