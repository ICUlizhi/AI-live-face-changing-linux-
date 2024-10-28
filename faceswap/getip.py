import socket

def get_local_ip():
    try:
        # 创建一个 UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接到一个远程地址（这里不需要实际连接）
        s.connect(("8.8.8.8", 80))  # Google 公共 DNS
        local_ip = s.getsockname()[0]  # 获取本地 IP 地址
    finally:
        s.close()  # 关闭 socket
    return local_ip

if __name__ == "__main__":
    print("本地 IP 地址:", get_local_ip())
