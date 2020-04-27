#  shodan-ip-port-export

Requires Shodan support, install it using:

pip install --upgrade shodan

Only tested with Python 3, YMMV.


Usage:

shipexport.py -i <inputfile> -o <outputfile> -f <csv>,<splunk> -d <delay> -t <shodan-api-token>

Where:

-i <inputfile> - file with a list of IPs, one per line, this is mandatory.
-o <outputfile> - file to save the results, mandatory unless you use -p.
-f <csv>,<splunk> - spit the results in a csv or splunk friendly format, mandatory.
-d <delay> - seconds to wait between calls, Shodan will throttle you if are quering too fast (1 is a good value). Optional, default is 0.
-t <shodan-api-toke> - api token from Shodan. Mandatory.

There is also a hidden -p option, that will print the output to the screen instead of sending it to <outputfile>.

This script works for me, my python knowledge is not great and I'm not a developer so bear with me. Also there is no check for inputs, so make sure you know
what you are passing to the script. I'm not responsible for any damage.
