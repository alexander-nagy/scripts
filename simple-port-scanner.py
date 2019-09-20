import socket

s = socket.socket()

rhosts = ['127.0.0.1'] # add hosts to the scope
rports = [22, 445, 80, 443, 3389] # add ports to the scope

for host in rhosts:
    for port in rports:
      try:
          print "[+] Connecting to "+host+":"+str(port)
          s.connect((host, port))
          s.send('simple port scanner')
          banner = s.recv(1024)
          if banner:
            print("[+] Port "+str(port)+" is open: "+banner)
          s.close()
      except:pass
