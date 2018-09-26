import tmsanalysis as tms 
import pandas as pd
import time
from ROOT import gROOT

gROOT.ProcessLine('.L fitShaped.C+')


start_time = time.time()
dfout = tms.ProcessFile('~/software/charge-readout-scripts/struck/ngm/tier1_SIS3316Raw_20180925173620_Co60_PSDScintTest_TriggThroughDisc_62_5MHz_1-ngm.root',save_waveforms=True,num_events=10)
end_time = time.time()

print('Time elapsed: {}s ({} min)'.format(end_time-start_time,(end_time-start_time)/60.))
