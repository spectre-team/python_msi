# Spectre

![Spectre](https://user-images.githubusercontent.com/1897842/31115297-0fe2c3aa-a822-11e7-90e6-92ceccf76137.jpg)

This repository contains definition of Docker image with MATLAB Common Runtime
and MATLAB-based implementations of Mass Spectrometry Imaging datasets
processing. These have Python bindings through which should be called.

# How to run MATLAB code through Python?

```
import MatlabAlgorithms.MsiAlgorithms as mt
context = mt.initialize()
context.fetch_thresholds(...) # or other exported function
```

# Why Python 3.4?

It is the most up-to-date version allowed by MCR.
