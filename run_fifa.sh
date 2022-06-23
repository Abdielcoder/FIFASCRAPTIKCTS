#!/bin/bash
/usr/bin/python3 /home/ubuntu/FIFA/fifa_scrap.py
cp /home/ubuntu/fifa.json /home/ubuntu/FIFA/fifa.json
sleep 10
/usr/bin/python3 /home/ubuntu/FIFA/upload_fifa.py /home/ubuntu/FIFA/fifa.json set Tikects

