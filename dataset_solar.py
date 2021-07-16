import pandas as pd
import numpy as np
from datetime import datetime 
import matplotlib.pyplot as plt
# import json
## reduced data
# file = "/home/claudio/Documents/profissao_DS/projetos/solar/solarflareoutput_2021-07-13T21_53_42_27.txt"

# ow = open(file , 'r')
# data = json.loads(ow.readlines()[23])
# dt = pd.DataFrame(data)
# # dt['GOES Max Temp, MK'].head(50).hist(bins=30)
# dt = dt.drop(['RHESSI energy, keV','X, arcsec','Y, arcsec', 'GOES Max Temp, MK', 'RHESSI duration, s','GOES Max EM, 10<sup>49</sup> cm<sup>-3</sup>','GOES T-EM Delay, s','RHESSI peak, counts', 'HEK peak flux', 'HEK channel, <span>&#8491;</span>'], axis=1)
# # ["string","string","string","string","string","int","string","int","int"]
# for i in dt.keys()[:5]:
#     dt.loc[:,i] = dt.loc[:, i].astype('string')
# dt.loc[:, 'GOES Class'] = dt.loc[:, 'GOES Class'].astype('string')
# for k in ['AR number', 'GOES Duration, s']:
#     dt.loc[:,k ]= dt.loc[:,k].astype(np.int32)
# dt.to_csv('SolarFlare_list_GOES.csv')
## reduced data

dt = pd.read_csv('SolarFlare_list_GOES.csv', index_col=0)
dt = dt[dt['AR number']> 0]

# print(dt)
# ndt = dt.loc[(dt['GOES Class'] > "C1.0") & (dt['GOES Class'] < "M1.0"),:]
# ndt['GOES Duration, s'].hist(bins=13)

# ndt = dt.loc[(dt['GOES Class'] > "M1.0") & (dt['GOES Class'] < "X1.0"),:]
# ndt['GOES Duration, s'].hist(bins=13)

# ndt = dt.loc[(dt['GOES Class'] > "X1.0"),:]
# ndt['GOES Duration, s'].hist(bins=13)


# event = dt[(dt['Start Time'] > '2011-09-01 00:00:00') & (dt['Start Time'] < '2011-10-01 00:00:00') & (dt['GOES Class'] > "M1.0")]
# event.plot(x="Start Time",y='AR number')
# event2 = dt[(dt['Start Time'] > '2017-09-01 00:00:00') & (dt['Start Time'] < '2017-10-01 00:00:00') & (dt['GOES Class'] >= "M1.0")]
# event2.plot(x="Start Time",y='AR number')
# event.plot(x="Start Time",y='AR number')

# plt.show()