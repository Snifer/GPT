import socket



class GetIp:

  

  def __init__(self):

    

    self.ip = ""

    

  def return_ip(self, hostname):

      

      try:

  

          self.ip = socket.gethostbyname(hostname)

          print self.ip

  

      except:

  

          print "Verify your connection please :-(!"



target = raw_input("Target: http://")

ip = GetIp()

ip.return_ip(target)
