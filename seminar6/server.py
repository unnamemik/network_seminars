import sys

from PyQt5 import QtWidgets, QtCore
import socket
import threading
import chat_s as q

global nickname, serv_line, port_line, server

serv_line = ''
port_line = 55444
nickname = 'Server: '
server = '', 55444
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port_line))


class LanMessenger(QtWidgets.QMainWindow, q.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.write_soc)
        self.pushButton_2.clicked.connect(self.settings)

    def write_soc(self):
        msg = self.lineEdit.text()
        self.textBrowser.append(msg)
        sock.sendto(str.encode(nickname + msg), ('127.0.0.1', port_line))
        self.lineEdit.clear()


    def serv_start(self):
        global data_lst
        client = []
        self.label.setText(str("Connected."))
        while True:
            data, address = sock.recvfrom(1024)
            if address[0] != '127.0.0.1':
                self.textBrowser.append(bytes.decode(data))
            if address not in client and address[0] != '127.0.0.1':
                client.append(address)
            for clients in client:
                if clients == address:
                    continue
                sock.sendto(data, clients)


    def conn_start(self):
        trd_serv = threading.Thread(target=self.serv_start)
        trd_serv.start()

    def settings(self):
        global nickname, server
        serv_line = self.lineEdit_3.text()
        port_line = int(self.lineEdit_3.text())
        nickname = self.lineEdit_4.text()
        server = serv_line, port_line


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LanMessenger()
    window.show()
    window.conn_start()
    app.exec_()


if __name__ == '__main__':
    main()
