The files in this folder are `pzflow` normalizing flows. The regular `Flow` objects are saved as `pzflow_flow_for_run_...`, while the `FlowEnsemble` objects are saved as `pzflow_ensemble_for_run_...`.

The flows can be loaded via
```
from pzflow import Flow
flow = Flow(file='file-name.pkl')
```

The ensembles can be loaded via
```
from pzflow import FlowEnsemble
ens = FlowEnsemble(file='file-name.pkl')
```

The ensembles all consist of 10 Flows, each with a single RQ-NSC with K=16. The flows are are individual flows, each consisting of a single RQ-NSC with K equal to the number given in the file name.

This file also contains pickled dictionaries of the training losses. Loading these dictionaries allows you to access all of these losses without rerunning the training.