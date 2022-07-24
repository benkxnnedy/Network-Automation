import getpass
import telnetlib

print("Welcome to Ben's Telnet automation tool!")

multi = ("Are you configuring more than one device? (y/n)")

if multi == "no":
    HOST = input("Please enter the IP address of your target")
    user = input("Enter your username: ")
    password = getpass.getpass()
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode() + b"\n")

    tn.read_until(b"Password: ")
    tn.write(password.encode() + b"\n")

    tn.write(b"enable\n")
    tn.write(password.encode() + b"\n")
    tn.write(b"conf t\n")
    tn.write(b"vlan 20\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode("ascii"))

else:
    end = False
    count = 1
    hosts = []

    while end == False:
        address = input("Please enter IP address of target " + count)
        hosts.append(address)
        count+=1
        finish = input("Would you like to enter another host?")

        if finish == "n":
            end = True
        

    


