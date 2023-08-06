from iqrfpy.messages.responses.os.read import ReadResponse


dpa = b'\x00\x00\x02\x80\x00\x00\x00\x00\x57\x7c\x11\x81\x46\x24\xd8\x08\x00\x28\x20\x75\xe4\x82\x7f\x26\xba\x2c\x6a\xc2\x76\x54\x58\xad\x34\x1b\x56\x2e\x17\x04\x00\xfd\x26\x00\x00\x00\x00\x00\x00\x05'
json = {
   "mType": "iqrfEmbedOs_Read",
   "data": {
      "msgId": "testEmbedOs",
      "rsp": {
         "nAdr": 0,
         "hwpId": 0,
         "rCode": 0,
         "dpaVal": 0,
         "result": {
            "mid": 2165406807,
            "osVersion": 70,
            "trMcuType": 36,
            "osBuild": 2264,
            "rssi": 0,
            "supplyVoltage": 3.0013793103448276,
            "flags": 32,
            "slotLimits": 117,
            "ibk": [
               228,
               130,
               127,
               38,
               186,
               44,
               106,
               194,
               118,
               84,
               88,
               173,
               52,
               27,
               86,
               46
            ],
            "dpaVer": 1047,
            "perNr": 0,
            "embeddedPers": [
               0,
               2,
               3,
               4,
               5,
               6,
               7,
               9,
               10,
               13
            ],
            "hwpid": 0,
            "hwpidVer": 0,
            "flagsEnum": 5,
            "userPer": []
         }
      },
      "raw": [
         {
            "request": "00.00.02.00.ff.ff",
            "requestTs": "2023-04-19T08:30:37.889+02:00",
            "confirmation": "",
            "confirmationTs": "",
            "response": "00.00.02.80.00.00.00.00.57.7c.11.81.46.24.d8.08.00.28.20.75.e4.82.7f.26.ba.2c.6a.c2.76.54.58.ad.34.1b.56.2e.17.04.00.fd.26.00.00.00.00.00.00.05",
            "responseTs": "2023-04-19T08:30:37.921+02:00"
         }
      ],
      "insId": "iqrfgd2-default",
      "statusStr": "ok",
      "status": 0
   }
}

dpa_rsp = ReadResponse.from_dpa(dpa)
json_rsp = ReadResponse.from_json(json)

print(json_rsp.get_os_read_data())
