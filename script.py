import os
import socket
import platform
import uuid
import psycopg2 as db
import shutil
import datetime

sys_info = platform.uname()
operating_system = sys_info.system + sys_info.version
print(operating_system)

hostname = sys_info.node
print(hostname)

processor_model = sys_info.processor
print(processor_model)

ipv4_addr = socket.gethostbyname_ex(hostname)[2]
print(ipv4_addr)

ping_test_ip = 'pitt.edu'
ping_result = os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + ping_test_ip)
internet_connection = ''

if ping_result == 0:
    internet_connection = 'Internet connected'
else:
    internet_connection = 'No internet connenction!'

print(internet_connection)

mac_addr = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

print(mac_addr)

postgre_connection = db.connect(
    host="******",
    database="levylab",
    user="llab_admin",
    password="******")

cur = postgre_connection.cursor()

q1 = "INSERT INTO pc_status_info.system_info VALUES(%s,%s,%s,%s);"
cur.execute(q1, (mac_addr,hostname,operating_system,processor_model))


ct = datetime.datetime.now()
print("current time:-", ct)


q2 = "INSERT INTO pc_status_info.check_record VALUES(DEFAULT,%s,%s) returning check_ID;"
cur.execute(q2, (ct,mac_addr))
check_ID = cur.fetchone()[0]


q3 = "INSERT INTO pc_status_info.network_info VALUES(%s,%s,%s);"
cur.execute(q3, (check_ID,ipv4_addr,internet_connection))

q4 = "INSERT INTO pc_status_info.storage_info VALUES(%s,%s,%s,%s,%s);"

from string import ascii_uppercase
for disk in ascii_uppercase:
    try:
        total, used, free = shutil.disk_usage(disk+'://')
        disk_partition = disk
        print(disk+": ")
        total = "%d GiB" % (total // (2**30))
        print("Total: "+total)
        used = "%d GiB" % (used // (2**30))
        print("Used: "+used)
        free = "%d GiB" % (free // (2**30))
        print("Free: "+free)
        cur.execute(q4, (check_ID, disk_partition, used, free, total))
    except:
        pass # doing nothing on exception

postgre_connection.commit()

postgre_connection.close()





