import random, socket
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
print(GREEN + "HEX ULTIMATE - MR AKATSUKI hex546" + RESET)
while True:
    print("1=Check Pass 2=IP 3=Gen Pass 4=Ports 5=Exit")
    c=input("pick: ")
    if c=="1":
        p=input("Enter password: ")
        print("STRONG" if len(p)>=8 else "WEAK")
    elif c=="2":
        print(socket.gethostbyname(socket.gethostname()))
    elif c=="3":
        letters="abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!@#$"
        print("".join(random.choice(letters) for i in range(16)))
    elif c=="4":
        for port in [21,22,80,443,8080]:
            s=socket.socket()
            s.settimeout(0.5)
            r=s.connect_ex(("127.0.0.1",port))
            print(port, "OPEN" if r==0 else "closed")
            s.close()
    elif c=="5":
        break