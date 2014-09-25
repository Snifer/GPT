import os
import sys
from sys import exit
import whois
import DNS

Api_Shodan = "Key Here"

def clear():

  os.system("cls" if os.name == "nt" else "clear")

def main():

    #global Mivariable
    print """           \n \n \n
                     ______  ____   _______
                    |  ____||  _ \ |__   __|
                    | |  _  | |_) |   | |
                    | | | | |   _/    | |
                    \ |_| | |  |      | |
                     \____| |__|      |_|
                           ____    _
                          /  _ \ _| |
                   __   __| | | |_  |
                   \ \ / /| | | | | |
                    \ V / | |_| | | |
                     \_/  \_____()|_|

              Develo by @Snifer @State_X
             Jose Moruno Cadima , Albert Sanchez
    """

    raw_input('Gadget Pentesting Tool . Press ENTER to continue!')
    flag = True
    while flag:

            print '\n'
            print '1)  Reconnaissance (Information Gathering)'
            print '2)  Scanning'
            print '3)  Explotacion'
            print '4)  Web Hacking'
            print '5)  Tools Gadge'
            print '6)  Backdoors & Rootkits'
            print '7) Cerrar GPT'

            try:

                option = input("Select option:")
                clear()
                if option == 1:

                  print "Reconnaissance"

                elif option == 2:

                  print "Scanning"

                elif option == 3:

                  print "Exploiting(?)"

                elif option == 4:

                  print "Web Hacking"

                elif option == 5:

                  print "Tools Gadge"

                elif option == 6:

                  print "Backdoors & Rootkits"

                elif option == 7:
                  #exit()
                  flag = False

            except:

                print option
                print "It is not a number!"

            print '\n\n'



if __name__ == "__main__":
  main()
