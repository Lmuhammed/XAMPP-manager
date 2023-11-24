#!/bin/bash
#$this_dir="/opt/lampp/"
sleep 1
cd /opt/lampp/
bouth=false
apache=false
mysql=false
cmd=false
PS3="Command line or grific panel ? :"
select opt in cmd grafic; do
  case $opt in
    cmd)
    cmd=true
    break
    ;;
    grafic)
    sudo ./manager-linux-x64.run
    exit
    break
    ;;
    *) 
    echo "Invalid option : $REPLY"
    exit
    ;;
  esac
done 
if [ $cmd ]
then
PS3="Do you want to preform the actions on bouth (apache,mysql) or one of them :"
select opt in bouth apache mysql; do
  case $opt in
    bouth)
    bouth=true
    break
    ;;
    apache)
    apache=true
    break
    ;;
    mysql)
    mysql=true
    break
    ;;
    *) 
    echo "Invalid option : $REPLY"
    exit
    ;;
  esac
done 

fi
PS3="Enter your choice :"
select opt in start reload stop ; do
  case $opt in
    start)
    if [ $bouth ]
    then 
    sudo ./xampp start 
    #sudo ./xampp startapache 
    #sudo ./xampp startmysql
    fi
    if [ $apache ]
    then
    sudo  ./xampp startapache 
    fi
    if [ $mysql ]
    then
    sudo ./xampp startmysql
    fi
    break
    ;;
    reload)
    if [ $bouth ]
    then 
    sudo ./xampp reload
    #sudo ./xampp reloadapache 
    #sudo ./xampp reloadmysql
    fi
    if [ $apache ]
    then
    sudo ./xampp reloadapache 
    fi
    if [ $mysql ]
    then
    sudo ./xampp reloadmysql
    fi
    break
    ;;
    stop)
     if [ $bouth ]
    then 
    sudo ./xampp stop
    #sudo ./xampp reloadapache 
    #sudo ./xampp reloadmysql
    fi
    if [ $apache ]
    then
    sudo ./xampp stopapache 
    fi
    if [ $mysql ]
    then
    sudo ./xampp stopmysql
    fi
    break
    ;;
    *) 
    echo "Invalid option : $REPLY"
    exit
    ;;
  esac
done 
