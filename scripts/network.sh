#!/bin//sh

ifconfig eth0 up &&\
echo 'allow-hotplug eth0' >> /etc/network/interfaces &&\
echo 'iface eth0 inet static' >> /etc/network/interfaces &&\
echo 'address 192.168.1.10' >> /etc/network/interfaces &&\
echo 'netmask 255.255.255.0'>> /etc/network/interfaces &&\
sysctl -w net.ipv4.ip_forward=1
