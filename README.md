# 3HDM Hilbert Series Numerator

This repository contains the Hilbert series numerator for the three-Higgs-doublet model (3HDM).

## Data

- File: `hSeriesNumSimplified.npy`
- Shape: (65, 65, 65, 192)
- Variables: (s, t, u, q)
- Coefficients are exact large integers

## Usage

```python
import numpy as np

arr = np.load("hSeriesNumSimplified.npy", allow_pickle=True)
print(arr.shape)

## Citation

If you use this data, please cite the associated publication.
