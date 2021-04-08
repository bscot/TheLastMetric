The files in this folder are `pzflow` normalizing flows. They can be loaded via:
```
from pzflow import Flow
flow = Flow(file='file-name.pkl')
```

Guide to file names:

`flow_for_run_runname.pkl` - original baseline flows, trained on galaxy colors plus r mag for the designated run.

`flow_for_run_runname_mag_trained.pkl` - same as baseline flows, except trained on galaxy magnitudes instead of colors.

`flow_for_run_runname_K=N.pkl` - same as baseline flows, except with varying spline resolution K.