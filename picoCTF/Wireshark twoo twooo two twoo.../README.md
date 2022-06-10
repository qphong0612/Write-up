## Wireshark twoo twooo two twoo...

### Description
Can you find the flag? [shark2.pcapng](https://mercury.picoctf.net/static/a7b4ce62a4f4313a6e5b0b03b97be953/shark2.pcapng)
> 100 points

### Hints
Did you really find _the_ flag?

Look for traffic that seems suspicious.

statistics -> Capture file properties
statistics -> Conversations
statistics -> Protocol Heirarchy


    tcp.stream eq [0:]

<div align="center">
<img src="https://user-images.githubusercontent.com/83420725/173086068-c92172a1-290a-4291-ac29-e7cf1f4fa8c7.png">
</div>

    picoCTF{bfe48e8500c454d647c55a4471985e776a07b26cba64526713f43758599aa98b}

<div align="center">
<img src="https://user-images.githubusercontent.com/83420725/173091726-41575ac5-514c-4fe0-a0c5-86e9ca7ee81d.png">
</div>

http contain 'picoCTF{}' string 

    tshark -nr ./shark2.pcapng -Y "((ip.addr == 18.217.1.57) ) && (_ws.expert) && http" -e http.file_data -Tfields

dns 
  
    ((dns) && (dns.flags.response == 0)) && !(dns.qry.name contains "amazonaws") && !(dns.qry.name contains "win") && ip.dst == 18.217.1.57

dns exfiltration
        
      1633	9.334169	192.168.38.104	18.217.1.57	DNS	93	Standard query 0xdf26 A cGljb0NU.reddshrimpandherring.com
      2042	11.870534	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x3a30 A RntkbnNf.reddshrimpandherring.com
      2444	14.503146	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x531d A M3hmMWxf.reddshrimpandherring.com
      3140	16.404809	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x99dd A ZnR3X2Rl.reddshrimpandherring.com
      3429	18.239530	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x16f6 A YWRiZWVm.reddshrimpandherring.com
      3969	20.266171	192.168.38.104	18.217.1.57	DNS	89	Standard query 0xbe68 A fQ==.reddshrimpandherring.com
      4361	22.481648	192.168.38.104	18.217.1.57	DNS	89	Standard query 0xa740 A fQ==.reddshrimpandherring.com
      

Final command
    
      tshark -nr ./shark2.pcapng -Y "((dns) && (dns.flags.response == 0)) && !(dns.qry.name contains "amazonaws") && !(dns.qry.name contains "win") && ip.dst == 18.217.1.57"  | awk '{ print $12 }' | awk -F. '{ print $1 }' | base64 -d

      
> picoCTF{dns_3xf1l_ftw_deadbeef}
