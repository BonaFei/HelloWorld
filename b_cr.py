#!/usr/bin/env python

def uni_sort_cr():

    unsort_cr = open("c:\Temp\cr.txt", "r")
    lines = set(unsort_cr.readlines())

    uni_cr = open("c:\Temp\_uni_cr.txt",'w')
    uni_cr.writelines(lines)

    unsort_cr.close()
    uni_cr.close()

    uni_cr = open("c:\Temp\_uni_cr.txt",'r')
    result = []
    iter_f = iter(uni_cr)
    for line in iter_f:
        result.append(line)

    uni_cr.close()
    result.sort()

    sorted_cr = open("c:\Temp\sorted_cr.txt",'w')
    sorted_cr.writelines(result)
    sorted_cr.close()

def server_conf(serverName):

    LB_FILE = open("c:\Software\ASDFQWER.conf", 'r')

    for lines in LB_FILE:
        line = lines.split(" ")
        if((line[0] == 'add') and (len(line)>2) and (serverName == line[2])):
            cr=open("c:\Temp\cr.txt","a")
            cr.write(lines)
            cr.close()

    LB_FILE.close()

def service_conf(serviceName):

    LB_FILE = open("c:\Software\ASDFQWER.conf", 'r')

    for lines in LB_FILE:
        line = lines.split(" ")
        if ((line[0] == 'add') and (len(line)>4) and (serviceName == line[2])):
            cr=open("c:\Temp\cr.txt",'a')
            cr.write(lines)
            cr.close()

            p_service=open("c:\Temp\pool_service.txt",'a')
            p_service.write(lines)
            p_service.close()

        if ((line[0] == 'bind') and (len(line) > 4) and (serviceName == line[2])):
            cr = open("c:\Temp\cr.txt", 'a')
            cr.write(lines)
            cr.close()

    LB_FILE.close()

def vip_conf(vipName):

    LB_FILE = open("c:\Software\ASDFQWER.conf", 'r')

    for lines in LB_FILE:
        line = lines.split(" ")
        if((line[0] == 'add') and (len(line)>2) and (vipName == line[3])):
            cr=open("c:\Temp\cr.txt","a")
            cr.write(lines)
            cr.close()

        if ((line[0] == 'bind') and (len(line) > 2) and (vipName == line[3])):
            cr = open("c:\Temp\cr.txt", "a")
            cr.write(lines)
            cr.close()

    LB_FILE.close()


 #def get_pool_conf():
#    pool_conf = open("c:\Temp\pool_conf.txt", "r")
#    conf_file = open("c:\ASDFQWER.conf", "r")
#
#    for ser in pool_conf.readlines():
#        # print (ser)
#        for conf in conf_file.readlines():
#            b = ser.split(" ")
#            a = conf.split(" ")
#            # print (b)
#            # print (a)
#            if ((len(b) > 4) and (len(a) > 4) and (b[2] == a[4]) and (a[0] == "bind")):
#                sv = open("c:\Temp\service_conf.txt", 'a')
#                sv.write(conf + '\n')
#
#    pool_conf.close()
#    conf_file.close()

def format_file():
    SRC_LB_FILE = open("c:\Software\ASDFQWER_src.conf", 'r')
    NEW_LB_FILE = open("c:\Software\ASDFQWER.conf", 'w')
    for line in SRC_LB_FILE:
        line = line.rstrip('\n') + " \n"
        NEW_LB_FILE.write(line)

    SRC_LB_FILE.close()
    NEW_LB_FILE.close()

    pf = open("c:\Temp\pool_conf.txt", 'w')
    pf.write("")
    pf.close()

    sf = open("c:\Temp\pool_src.txt", 'w')
    sf.write("")
    sf.close()

    Sf = open("c:\Temp\pool_service.txt", 'w')
    Sf.write("")
    Sf.close()

    new_cr = open("c:\Temp\cr.txt", 'w')
    new_cr.write("")
    new_cr.close()



def main():

    format_file()

    LB_FILE = open("c:\Software\ASDFQWER.conf", 'r')

    pool = "cfgedit-web-1-443"


    for lines in LB_FILE.readlines():
        line = lines.split(" ")
        if ((len(line) > 3) and (pool == line[3]) and (line[0] == "bind")):
            f_pool = open("c:\Temp\pool_conf.txt", 'a')
            #f_pool.write(line + '\n')
            f_pool.write(lines)
            f_pool.close()

            cr = open("c:\Temp\CR.txt",'a')
            cr.write(lines)
            cr.close()

        if ((len(line) > 3) and (pool == line[3]) and (line[0] == "add")):
            cr = open("c:\Temp\CR.txt",'a')
            cr.write(lines)
            cr.close()

        if ((line[0] == "bind") and (len(line) > 4) and (pool == line[5])):
        #if ((len(line) > 4) and ("bind" == line[0]) and (pool == line[5])):
            v_pool = open("c:\Temp\pool_vip.txt",'a')
            v_pool.write(lines)
            v_pool.close()

            cr = open("c:\Temp\CR.txt",'a')
            cr.write(lines)
            cr.close()


    POOL_FILE = open("c:\Temp\pool_conf.txt", "r")
    NEW_POOL_FILE = open("c:\Temp\pool_src.txt","a")
    for line in POOL_FILE:
        line = line.rstrip('\n') + " \n"
        NEW_POOL_FILE.write(line)
    POOL_FILE.close()
    NEW_POOL_FILE.close()

    NEW_POOL_FILE = open("c:\Temp\pool_src.txt", "r")
    for p_lines in NEW_POOL_FILE.readlines():
        p_line = p_lines.split(" ")
        service_name = p_line[4]
        service_conf(service_name)


    SERVER_FILE = open("c:\Temp\pool_service.txt","r")
    for s_lines in SERVER_FILE.readlines():
        s_line = s_lines.split(" ")
        server_name = s_line[3]
        server_conf(server_name)

    VIP_FILE = open("c:\Temp\pool_vip.txt","r")
    for v_lines in VIP_FILE.readlines():
        v_line = v_lines.split(" ")
        vip_name = v_line[3]
        vip_conf(vip_name)

    POOL_FILE.close()
    #LB_FILE.close()

    uni_sort_cr()

if __name__ == "__main__":
    main()
