import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 6688))
    tcp_server_socket.listen(128)
    while True:
        print("等待一个新的客户端的到来...")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来:%s" % str(client_addr))
        while True:
            recv_data = new_client_socket.recv(1024)
            if recv_data:
                new_client_socket.send("ok".encode("utf-8"))
            else:
                break
            print("客户端发送过来的请求是:%s" % recv_data.decode("utf-8"))
        new_client_socket.close()
        print("已经为这个客户端服务完毕....")
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
