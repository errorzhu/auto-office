import threading


import socket

r = threading.RLock()


def is_port_open(ip, port):
    # 创建套接字对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置超时时间，单位为秒
    sock.settimeout(1)
    try:
        # 连接到指定 IP 地址和端口
        sock.connect((ip, port))
        # 关闭套接字
        sock.close()
        # 端口开放

        r.acquire()
        print(ip,"   ",port, "端口开放")
        r.release()
        return True
    except:
        # 关闭套接字
        sock.close()
        # 端口关闭
        return False



def scan(segment,port):
    for i in range(1,255):
        t = threading.Thread(target=is_port_open, args=(segment + str(i), port))
        t.start()


# 测试
if __name__ == '__main__':
    scan("192.168.27.",22)

