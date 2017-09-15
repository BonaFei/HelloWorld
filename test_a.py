#!/usr/bin/env python

LB_FILE = open("c:\xxxxx.conf", 'r')

def add_server_conf(server):
    for lines in LB_FILE.readlines():
        a = lines.split(" ")

        if ((len(a) > 2) and (server == a[2])):
            print(a)


def add_service_conf(servi):
    LB_FILE = open("c:\phxlb214.conf", 'r')

    for lines in LB_FILE.readlines():
        a = lines.split(" ")
        if ((len(a) > 2) and (servi == a[2]) and (a[0] == "add")):
            print(a)
            add_server_conf(a[3])

    LB_FILE.close()


# def get_service_conf():




def get_pool_conf():
    pool_conf = open("c:\Temp\pool_conf.txt", "r")
    conf_file = open("c:\phxlb214.conf", "r")

    for ser in pool_conf.readlines():
        # print (ser)
        for conf in conf_file.readlines():
            b = ser.split(" ")
            a = conf.split(" ")
            # print (b)
            # print (a)
            if ((len(b) > 4) and (len(a) > 4) and (b[2] == a[4]) and (a[0] == "bind")):
                sv = open("c:\Temp\service_conf.txt", 'a')
                sv.write(conf + '\n')

                # pool_conf.close()
                # conf_file.close()


def main():


    pool = "cfgedit-web-1-443"

    for line in LB_FILE.readlines():
        a = line.split(" ")
        if ((len(a) > 3) and (pool == a[3]) and (a[0] == "bind")):
            #   print (a)
            f_pool = open("c:\Temp\pool_conf.txt", 'a')
            f_pool.write(line + '\n')

            # try:
            #    if ((pool == a[3]) and (a[0] == "add")):
            #        print(line)
            # except Exception as e:
            #    print (e)

    sp = open("c:\Temp\pool_conf.txt", 'r')

    for sv in sp.readlines():
        b = sv.split(" ")
        if (len(b) > 3):
            # print(b[4])
            add_service_conf(b[4])

    sp.close()

    # get_pool_conf()

    LB_FILE.close()


if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    
    
  #!/usr/bin/env python

def add_server_conf(server):

    LB_FILE = open("c:\Software\xxxxxxxx.conf", 'r')

    for lines in LB_FILE.readlines():
        a = lines.split(" ")

        if ((len(a) > 2) and (server == a[2])):
            print(a)

    LB_FILE.close()



def service_conf(POOL_FILE):

    LB_FILE = open("c:\Software\phxlb214.conf","r")

    for p_lines in POOL_FILE.readlines():
        for lines in LB_FILE.readlines():
            p_line = p_lines.split(" ")
            line = lines.split(" ")

            if ((len(line) > 3) and (p_line[4] == line[2]) and (line[0] == "add")):
                #s_conf = open("c:\Temp\service_conf.txt","a")
                #s_conf.write(lines)
                #s_conf.close()

                print(lines)
                #cr = open("c:\Temp\CR.txt","a")
                #cr.write(lines)

            if ((len(line) > 3) and (p_line[4] == line[2]) and (line[0] == "bind")):
                print(lines)
                #cr = open("c:\Temp\CR.txt","a")
                #cr.write(lines)

    LB_FILE.close()


def get_pool_conf():
    pool_conf = open("c:\Temp\pool_conf.txt", "r")
    conf_file = open("c:\xxxxxxxxxx.conf", "r")

    for ser in pool_conf.readlines():
        # print (ser)
        for conf in conf_file.readlines():
            b = ser.split(" ")
            a = conf.split(" ")
            # print (b)
            # print (a)
            if ((len(b) > 4) and (len(a) > 4) and (b[2] == a[4]) and (a[0] == "bind")):
                sv = open("c:\Temp\service_conf.txt", 'a')
                sv.write(conf + '\n')

    pool_conf.close()
    conf_file.close()


def main():

    LB_FILE = open("c:\Software\phxlb214.conf", 'r')

    pool = "cfgedit-web-1-443"

    for line in LB_FILE.readlines():
        a = line.split(" ")
        if ((len(a) > 3) and (pool == a[3]) and (a[0] == "bind")):
            f_pool = open("c:\Temp\pool_conf.txt", 'a')
            #f_pool.write(line + '\n')
            f_pool.write(line)
            f_pool.close()

            cr = open("c:\Temp\CR.txt",'a')
            cr.write(line)

        elif ((len(a) > 3) and (pool == a[3]) and (a[0] == "add")):
            cr = open("c:\Temp\CR.txt",'a')
            cr.write(line)


    sp = open("c:\Temp\pool_conf.txt", "r")

    #for service in sp.readlines():
    #    service_name = service.split(" ")
    #    service_conf(service_name[4])

    service_conf(sp)

    #LB_FILE.close()

if __name__ == "__main__":
    main() 
    
