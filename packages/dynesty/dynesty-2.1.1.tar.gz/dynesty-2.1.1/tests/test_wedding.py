import numpy as np
import dynesty
from utils import get_rstate, get_printing
import pytest
import scipy.special

ndim = 2

printing = get_printing()

sig = 0.2
alpha = .7


# Wedding cake function from Fowlie 2020
def loglike_inf(x):
    D = len(x)
    r = np.max(np.abs(x - 0.5))
    i = (D * np.log(2 * r) / np.log(alpha)).astype(int)
    logp = -(alpha**(2 * i / D)) / (8 * sig**2)
    return logp


# true value of the integral
ndim = 2
LOGZ_TRUE = scipy.special.logsumexp(-alpha**(2 * np.arange(100) / ndim) /
                                    (8 * sig**2) +
                                    np.arange(100) * np.log(alpha) +
                                    np.log((1 - alpha)))


def prior_transform(x):
    return x


# here are are trying to test different stages of plateau
# probing with different dlogz's
@pytest.mark.parametrize('sample,dlogz', [('unif', 1), ('rwalk', 1),
                                          ('rslice', 1), ('unif', .01),
                                          ('rwalk', .01), ('rslice', .01)])
def test_static(sample, dlogz):
    nlive = 1000
    rstate = get_rstate()
    sampler = dynesty.NestedSampler(loglike_inf,
                                    prior_transform,
                                    ndim,
                                    nlive=nlive,
                                    rstate=rstate,
                                    bound='none',
                                    sample=sample)
    sampler.run_nested(print_progress=printing, dlogz=dlogz)
    res = sampler.results
    THRESH = 3
    print(res.logz[-1], LOGZ_TRUE)
    assert np.abs(res.logz[-1] - LOGZ_TRUE) < THRESH * res.logzerr[-1]


@pytest.mark.parametrize('sample,', ['unif', 'rslice', 'rwalk'])
def test_dynamic(sample):
    rstate = get_rstate()
    nlive = 100
    sampler = dynesty.DynamicNestedSampler(loglike_inf,
                                           prior_transform,
                                           ndim,
                                           nlive=nlive,
                                           rstate=rstate,
                                           bound='none',
                                           sample=sample)
    sampler.run_nested(print_progress=printing)
    res = sampler.results
    THRESH = 3
    print(res.logz[-1], LOGZ_TRUE)
    assert np.abs(res.logz[-1] - LOGZ_TRUE) < THRESH * res.logzerr[-1]


test_static('unif', 0.1)
