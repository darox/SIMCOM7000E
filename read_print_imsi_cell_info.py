#!/usr/bin/python

#Created by Dario Mader @ Swisscom - 21.12.2018

import serial
import time
import re
ser = serial.Serial('/dev/ttyS0', 115200, timeout=0)


try:
        ser.write('AT+CPSI?\r'.encode())
        time.sleep(1)
        ser.readline()
        time.sleep(1)
        ci = ser.readline()
        ci =  ci.split(',')
        rat = ci[0]
        ser.write('AT+CIMI\r'.encode())
        time.sleep(1)
        imsi = int(re.search(r'\d+', ser.read(40)).group())
        if (rat == "+CPSI: LTE CAT-M1"):
                rat = 1
        elif (rat == "+CPSI: LTE NB-IOT"):
                rat = 2
        else:
                rat = 0

        eci = ci[4]
        rsrp = ci[11]
        rssi = ci[12]
        snr = ci[13]
        snr = snr.rstrip("\n\r")
        print("")
        print("****************** SIMCOM Cell Info ******************")
        print("")
        print("IMSI:  " + str(imsi))
        if (rat == 1):
                print("RAT:   CAT M1")
        else:
                print("RAT:   NB-IOT")
        print("ECI:   " +str(eci))
        print("RSRP:  " + str(rsrp) + " dBm")
        print("RSSI:  " + str(rssi) + " dBm")
        print("SNR:   " + str(snr) + "  db")
        print("")
        print("******************************************************")

except:
        print("There was an error while executing AT+CPSI? to get cell info")
        pass
