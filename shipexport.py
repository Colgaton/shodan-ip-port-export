from __future__ import print_function
import sys
import getopt
import shodan
import time

scriptname = 'shipexport.py'


def help():

    print(scriptname, '-i <inputfile> -o <outputfile> -f <csv>,<splunk> -d <delay> -t <shodan-api-token>')
    sys.exit(2)


def main(argv):

    inputf = ''
    outputf = ''
    delay = ''
    fformat = ''
    printout = ''
    e = ''
    token = ''


    try:
        opts, args = getopt.getopt(argv, "hi:o:d:f:pt:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        help()

    for opt, arg in opts:
        #print (opt, arg)
        if opt == '-h':
            help()
        elif opt in ("-i", "--ifile"):
            inputf = arg
        elif opt in ("-o", "--ofile"):
            outputf = arg
        elif opt == "-d":
            delay = arg
        elif opt == "-f":
            fformat = arg
        elif opt == "-p":
            printout = 1
        elif opt == '-t':
            token = arg

    #print('Input file is', inputf)
    #print('Output file is', outputf)
    #print('Format is', fformat)

    if not inputf:
            help()

    if not printout:
        if not outputf:
            help()

    if not fformat:
            help()

    if not token:
            help()

    try:
         f = open(inputf, "r")

    except e:
         print(e)
    
    if not printout:
       try:
            fout = open(outputf, "w")
       except e:
            print(e)


    api = shodan.Shodan(token)

    while True:
        hostIP = f.readline()
        if not hostIP:
            break

        try:
            hostData = api.host(hostIP)
            if fformat in "splunk":
                for item in hostData['data']:
                    value = "ip=%s lastupdate=%s port=%s\n" % (
                        hostData['ip_str'], hostData['last_update'], item['port'])
                    if printout:
                        print(value)
                    else:
                        fout.write(value)
            elif fformat == "csv":
                value = ("%s, %s," % (hostData['ip_str'], hostData['last_update']))
                if printout:
                    print(value,end='')
                else:
                    fout.write(value)
                for item in hostData['data']:
                    value = " %s," % (item['port'])
                    if printout:
                        print(value)
                    else:
                        fout.write(value)

        except shodan.APIError as e:
            print("Error:", e, hostIP)

        if delay:
            time.sleep(int(delay))

    if not printout:
        fout.close()

    f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
