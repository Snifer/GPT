# ALL Imports
import os
import sys
import whois
import DNS

Api_Shodan = "Key Here"

def main():

    #global Mivariable
    print '           \n \n \n \n \n \n          '
    print '             ______  ____   _______   '
    print '            |  ____||  _ \ |__   __|  '
    print '            | |  _  | |_) |   | |     '
    print '            | | | | |   _/    | |     '
    print '            \ |_| | |  |      | |     '
    print '             \____| |__|      |_|     '
    print '                   ____    _          '
    print '                  /  _ \ _| |         '
    print '           __   __| | | |_  |         '
    print '           \ \ / /| | | | | |         '
    print '            \ V / | |_| | | |         '
    print '             \_/  \_____()|_|         '
    print '     '
    print '      Develo by @Snifer @State_X     '
    print '     Jose Moruno Cadima , Albert Sanchez'
    print '\n\n\n\n\n\n'

    raw_input('Gadget Pentesting Tool . Press a button dude!')

    while 1:
        option = -1
        while ((int(option) != 1)  and (int(option) != 2)  and
               (int(option) != 3)  and (int(option) != 4)  and
               (int(option) != 5)  and (int(option) != 6)  and
               (int(option) != 7) and (int(option) != 99)):

            print '\n'
            print '1)  Reconnaissance (Information Gathering)'
            print '2)  Scanning'
            print '3)  Explotacion'
            print '4)  Web Hacking'
            print '5)  Tools Gadge'
            print '6)  Web Hacking'
            print '7)  Backdoors & Rootkits'
            print '99) Cerrar GPT'

            choice = raw_input('Select one option: ')

            try:
                option = int(choice)
            except:
                raw_input('Not is a number, -_-! .. \n')
            print '\n\n'

        if (int(option) == 1):

            print ' ****Reconnaissance***'


        if (int(option) == 99):
            print '\n \n \n '
            print ' Thanks for use GPT . ' #Path donde se almacenara la ifnormacion mensaje de salid
            print '\n \n  \n '

            exit(0)




main()
