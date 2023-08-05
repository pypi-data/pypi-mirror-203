![PyPI Latest Release](https://img.shields.io/pypi/v/dimensionality_reductions_jmsv.svg)
![Package Status](https://img.shields.io/pypi/status/dimensionality_reductions_jmsv.svg)
![Python Versions](https://img.shields.io/pypi/pyversions/dimensionality_reductions_jmsv)

### What is it?

**dimensionality_reductions_jmsv** is a Python package that provides three methods (PCA, SVD, t-SNE) to apply dimensionality reduction to any dataset.

### Installing the package

Requests is available on PyPI:

```bash
pip install dimensionality_reductions_jmsv
```

**_Try your first TensorFlow program_**

```python
from dimensionality_reductions_jmsv.decomposition import PCA
import numpy as np

X = (np.random.rand(10, 10) * 10).astype(int)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print("Original Matrix:", '\n', X, '\n')
print("Apply dimensionality reduction with PCA to Original Matrix:", '\n', X_pca)
```

### License
[MIT](https://mit-license.org/)
