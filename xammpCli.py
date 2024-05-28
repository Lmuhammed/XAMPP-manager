import os        #
import sys      #To check params passed  to script
import platform #To check the operating system

#Functions
#0- App Banner :p
def print_header():
    # Website used to create this piece of art :D : https://www.asciiart.eu/text-to-ascii-art
    header = r"""
  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |     ______   | || | ____    ____ | |
| | |_  _||_  _| | || |   .' ___  |  | || ||_   \  /   _|| |
| |   \ \  / /   | || |  / .'   \_|  | || |  |   \/   |  | |
| |    > `' <    | || |  | |         | || |  | |\  /| |  | |
| |  _/ /'`\ \_  | || |  \ `.___.'\  | || | _| |_\/_| |_ | |
| | |____||____| | || |   `._____.'  | || ||_____||_____|| |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  """
    print(header)

#1-Check if Xammp installed

def check_xampp_installed(directory_path):
    if not os.path.isdir(directory_path):
        print("xampp is not installed.")
        exit(1)

#2- Check OS and return Xammp path

def check_os():
    system = platform.system()
    if system == 'Windows':
        #Later commands will be dynamics ;if windows commands will start without sudo
        print("Support for windows will be added later")
        exit(1)
        #return "C:\\xampp"
    elif system == 'Linux':
        return "/opt/lampp/"
    else:
        print("Unknown OS")
        exit(1)

#3-Display help menu if no args passed to script

def help_menu():
    script_name = os.path.basename(__file__)
    print(f"Usage: {script_name} [Service] <Action>")
    print("---> Service  :")
    print("  -ap / --apache      Select Apache")
    print("  db / --mysql        Select Database (MariadDB)")
    print("  -ftp                Select ProFTPD")
    print("  all                 Select apache ftp & database")
    print("---> Action   :")
    print("  On                  Turn on  the service/services")
    print("  Off                 Turn off the service/services")
    print("  Reload              Reload  the service/services")
    exit(1)

#4-Action on one or multi services

def oneOrMulti_services(service,argument,allServices=None):
    #Check if all services 
    if allServices is True:
        if argument == "on" :
            command="sudo ./xampp startapache ; sudo ./xampp startmysql ; sudo ./xampp startftp"
        elif argument == "off" :
            command="sudo ./xampp stopapache ; sudo ./xampp stopmysql ; sudo ./xampp stopftp"
        elif argument == "reload" :
            command="sudo ./xampp reloadapache;sudo ./xampp reloadmysql;sudo ./xampp reloadftp"
        else :
            print(f"Invalide argument : {argument} with : all services ")
            sys.exit()
        #Execute commands
        os.system(command)
        exit(1)
        
    #Check if a service checked : apache , mysql or ftp            
    else :
        if argument == "on" :
            command="sudo ./xampp start"+service
            os.system(command)

        elif argument == "off" :
            command="sudo ./xampp stop"+service
            os.system(command)
        elif argument == "reload" :
            command="sudo ./xampp reload"+service
            os.system(command)
        else:
            print(f"Invalid parameter  name : {argument} ")
            help_menu()


            
#End Functions Declaration
print_header()
if len(sys.argv) == 1: #Check params passed to the script
    help_menu()
    exit(2)

Xammp_dir=check_os()
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





