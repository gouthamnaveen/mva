# Documentation  

A python package to adjust the bias of probabilistic forecasts/hindcasts using "Mean and Variance Adjustment" method.

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

**observation**: numpy.ndarray

The truth or observations corresponding to the hindcast. Kindly maintain the shape of the array as (years/samples,time,grid-points).
    
**forecast**: numpy.ndarray, optional

The forecast (or test) data. Kindly maintain the shape of the array as (time,ensemble-members,grid-points).

_Note_: Kindly respect the array shapes even if the computation is done for one time/grid point/ensemble member.

## _Methods:_

**adjust_hindcast()**:

This method corrects the bias of the hindcast using hindcast of the remaining years in the set (i.e., leave-one-out approach) and the corresponding observations.

_Returns_:

bias_adjusted_hindcast (Note: It has the same shape as the hindcast)

**adjust_forecast()**:

This method corrects the bias of the forecast using hindcast and the corresponding observations. This method works only when the forecast parameter is given.

_Returns_:

bias_adjusted_forecast (Note: It has the same shape as the forecast)

## _Demonstration:_

```sh
import numpy as np
import mva.mva as mva
```
Let's imagine that we have loaded the data of hindcast, forecast, and observation.

Example - 1
```sh
In [1]: hcast.shape
Out[1]: (20,46,10,6)
In [2]: fcast.shape
Out[2]: (46,50,6)
In [3]: obs.shape
Out[3]: (20,46,6)
In [4]: bc = mva(hcast,obs,fcast)
In [5]: ad_hcast = bc.adjust_hindcast()
In [6]: ad_hcast.shape
Out[6]: (20,46,10,6)
In [7]: ad_fcast = bc.adjust_forecast()
In [8]: ad_fcast.shape
Out[8]: (46,50,6)
```

Example - 2
```sh
In [1]: hcast.shape
Out[1]: (20,46,10,6)
In [2]: fcast.shape
Out[2]: (48,50,6)
In [3]: obs.shape
Out[3]: (20,46,6)
In [4]: ad_hcast = mva(hcast,obs,fcast).adjust_hindcast()
In [5]: ad_hcast.shape
Out[5]: (20,46,10,6)
In [6]: ad_fcast = mva(hcast,obs,fcast).adjust_forecast()
Out[6]: Please respect the array shapes and try again!
```
