RESTFul API Service for NMAP utility
====================================

This API service can be utilized to probe any remote machine/Network/Webserver for its Vulnerability.
Tool used for this is NMAP tool installed on Linux machine.
We just need to provide target machine IP/DNS name and scan option to probe target machine for its vulnerability


Advantage of this Service
============================
- Opuput of NMAP scan can be utilized for an Application, which can be used following:
	- Target machine OS
	- Traget machine open and closed ports
	- Know vulnerability

Prerequisites
================
Using Python pip install following packages:
1. pip install flasks
2. pip install requests
3. pip install socket
4. pip install NmapProcess
5. pip install xmltodict
6. pip install json

- Install NMAP tool on linux machine (yum install nmap)

How to run tool
=================
- python nmap_api.py


How to send REST request
=========================
http://<RESTAPI_URL>:5002/nmap?target=<target_machine>&options=-sV
- Example: http://192.168.0.108:5002/todo/api/nmap?target=www.metanica.com&options=-sV

Note: For "options", please read various options available for NMAP tool
