import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7890))
    while True:
        send_data = input("请输入要发送的数据：") 
        udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1", 6688))
    udp_socket.close()

if __name__ == "__main__":
    main()
