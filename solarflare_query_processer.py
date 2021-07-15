###################################################################
# # __author__   = "Viacheslav M Sadykov"                        ##
# # __maintainer__   = "Ryan Spaulding"                          ##
# # __email__    = "Ryan.C.Spaulding@nasa.gov"                   ##
# # __project__  = "data.nas.nasa.gov"                           ##
# # __version__  = "3.0.1"                                       ##
# # __status__   = "released"                                    ##
###################################################################

# # DESCRIPTION: The SolarFlare Query Processer is used to read the query
# # result files from https://data.nas.nasa.gov/helio/portals/solarflares/webapp.html to the
# # Python structured array.
# # INPUT:    infile - file like "solarflareoutput_yyyy-mm-ddThh-mm-ss_rr.txt"
# # OPTIONAL: output_info - should be 1 do display information about available dictionary keys.
# # OUTPUT:   solarflare_obj - dictionary containing information about the flare events.
# # Please refer to the program output for the details of usage!
# # EXAMPLE: solarflare_obj = solarflare_query_processer('solarflareoutput_2017-02-06T19-53-24_40.txt', output_info = 1)

import json

def solarflare_query_processer(infile, output_info=1):
    # opening the file
    f = open(infile, 'r')
    # reading json part
    for line in f:
        if (line[0] == '{'):
            solarflare_obj = json.loads(line)
            break
    f.close()
    
    if (output_info == 1):
        print "----------------------------------"
        print "Possible dictionary keys (fields):"
        print "----------------------------------"
        for key in solarflare_obj.keys():
            print key
        print "---------------------------------------"
        print "Example: use solarflare_obj['SOLID'][2] to access SOLID for the third flare"
    
    # returning headers and records
    return solarflare_obj
