The files in this folder are `pzflow` normalizing flows. They can be loaded via:
```
from pzflow import Flow
flow = Flow(file='file-name.pkl')
```

Guide to file names:

`flow_for_runName_N.pkl` - baseline flows (with K=16), trained on galaxy colors plus r mag for the designated run. 
There are 10 independent flows for each (labeled with N=1,...,10) so that mean and scatter be computed for the metric.

`flow_for_runName_mag_trained.pkl` - same as baseline flows, except trained on galaxy magnitudes instead of colors.

`flow_for_runName_K=N.pkl` - same as baseline flows, except with varying spline resolution K.

`flow_for_runName_zphot|colors.pkl` - K=16 flow modeling p(z_phot|r,colors)

`flow_for_runName_zphot|ztrue.pkl` - K=16 flow modeling p(z_phot|z_true)

`flow_for_runName_ztrue|zphot.pkl` - K=16 flow modeling p(z_true|z_phot)