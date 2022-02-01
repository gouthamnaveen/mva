# Documentation  

A python package to adjust the bias of probabilistic forecasts/hindcasts using "Mean and Variance Adjustment" method.

Read documentation at [https://github.com/garovent/mva](https://github.com/garovent/mva)

_References_:

[1] Torralba, V., Doblas-Reyes, F. J., MacLeod, D., Christel, I. & Davis, M. Seasonal Climate Prediction: A New Source of Information for the Management of Wind Energy Resources. Journal of Applied Meteorology and Climatology 56, 1231–1247 (2017).

[2] Manzanas, R. et al. Bias adjustment and ensemble recalibration methods for seasonal forecasting: a comprehensive intercomparison using the C3S dataset. Clim Dyn 53, 1287–1305 (2019).

## _Installation:_

```sh
pip install mva
```

## _Parameters:_

**hindcast**: numpy.ndarray

The hindcast (or training) data. Kindly maintain the shape of the array as (years/samples,time,ensemble-members,grid-points).

**truth_hindcast**: numpy.ndarray

The observed data corresponding to the hindcast. Kindly maintain the shape of the array as (years/samples,time,grid-points).
    
**forecast**: numpy.ndarray, optional

The forecast (or test) data. Kindly maintain the shape of the array as (time,ensemble-members,grid-points).

_Note-I_: Kindly respect the array shapes even if the computation is done for one time/grid point/ensemble member.

## _Methods:_

**adjust_hindcast()**:

This method adjusts the bias of the hindcast samples using leave-one-out approach.

_Returns_:

bias_adjusted_hindcast (Note: It has the same shape as that of the original hindcast data)

**adjust_forecast()**:

This method adjusts the bias of the forecast using hindcast data. This method works only when the forecast parameter is given.

_Returns_:

bias_adjusted_forecast (Note: It has the same shape as that of the original forecast data)

## _Demonstration:_

```sh
import numpy as np
import mva.mva as mva
```

Example - 1
```sh
In [1]: pscore(np.random.uniform(2,5,50),3.5).compute()
Out[1]: (0.24374216742963792, 0.2332762342590258, 0.23589271755167882)
```

Example - 2
```sh
In [2]: crps,fcrps,acrps = pscore(np.random.uniform(1.2,7,100),8.3,50).compute()
In [3]: crps
Out[3]: 3.11890267263096
In [4]: fcrps
Out[4]: 3.109573704801023
In [5]: acrps
Out[5]: 3.129164537243891
```

