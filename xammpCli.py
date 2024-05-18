import os  #
import sys #To check params passed  to script
#Functions
def check_xampp_installed(directory_path):
    if not os.path.isdir(directory_path):
        print("xampp is not installed.")
        exit(1)

def help_menu():
    script_name = os.path.basename(__file__)
    print(f"Usage: {script_name} [Service] <Action>")
    print("Service  :")
    print("  -ap / --apache       Select Apache")
    print("  db / --mysql        Select Database (MariadDB)")
    print("  -ftp                Select ProFTPD")
    print("  all                 Select apache ftp & database")
    print("Action   :")
    print("  on                  Turn on  the service/services")
    print("  off                 Turn off the service/services")
    exit(1)

def oneOrMulti_services(service,argument,allServices=None):
    #Check if all services 
    if allServices is True:
        if argument == "on" :
            command="sudo ./xampp startapache ; sudo ./xampp startmysql ; sudo ./xampp startftp"
            os.system(command)
        elif argument == "off" :
            command="sudo ./xampp stopapache ; sudo ./xampp stopmysql ; sudo ./xampp stopftp"
            os.system(command)
        else:
            print(f"Invalide argument with : all ")
            sys.exit()
    #Check if a service checked : apache , mysql or ftp            
    else :
        if argument == "on" :
            command="sudo ./xampp start"+service
            os.system(command)

        elif argument == "off" :
            command="sudo ./xampp stop"+service
            os.system(command)
        else:
            print(f"Invalid parameter  name : {argument} ")
            help_menu()
            
#End Functions Declaration
if len(sys.argv) == 1: #Check params passed to the script
    help_menu()
    exit(2)

Xammp_dir="/opt/lampp/"
check_xampp_installed(Xammp_dir)
os.chdir(Xammp_dir)
param = (sys.argv[1]).lower()
param2 = (sys.argv[2]).lower()
service=None

if param == "all" :
    oneOrMulti_services(service,param2,True)
    exit(1)

elif param == "-ap" or param == "--apache":
    service='apache'
    oneOrMulti_services(service,param2)
    exit(1)

elif param == "-db" or param == "--mysql":
    service='mysql'
    oneOrMulti_services(service,param2)
    exit(1)

elif param == "-ftp":
    service='ftp'
    oneOrMulti_services(service,param2)
    exit(1)

else :
    print(f"Invalid Service name : {param} ")
    exit(2)





