import numpy as np
import scipy.sparse as sps

import lenskit.matrix as lm

from pytest import mark
import lk_test_utils as lktu


@mark.parametrize('copy', [True, False])
def test_csr_from_sps(copy):
    # initialize sparse matrix
    mat = np.random.randn(10, 5)
    mat[mat <= 0] = 0
    smat = sps.csr_matrix(mat, copy=copy)
    # make sure it's sparse
    assert smat.nnz == np.sum(mat > 0)

    csr = lm.csr_from_scipy(smat)
    assert csr.nnz == smat.nnz
    assert csr.nrows == smat.shape[0]
    assert csr.ncols == smat.shape[1]

    assert all(csr.rowptrs == smat.indptr)
    assert all(csr.colinds == smat.indices)
    assert all(csr.values == smat.data)
