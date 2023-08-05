#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: © 2021 Massachusetts Institute of Technology.
# SPDX-FileCopyrightText: © 2021 Lee McCuller <mcculler@caltech.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.
"""
"""

import numpy as np
import scipy
import scipy.signal

from . import zpk_algorithms


def pade_delay(delay_s, order=1, rescale=None):
    if rescale is None:
        rescale = 2 / delay_s
        factor = 1
    else:
        factor = rescale * delay_s / 2
    val = 1
    n = 1

    c = [1]
    val = 1
    for idx in range(1, order + 1):
        n = n * idx
        val = factor * val / idx
        c.append(val)

    num = np.asarray(c)
    den = np.copy(num)
    num[1::2] *= -1

    ABCDE = zpk_algorithms.poly2ss(num, den, rescale_has=rescale)

    return ABCDE


def bessel_delay(delay_s, order=1, rescale=None):
    # take the poles of this normalized bessel filter (delay=1s)
    z, p, k = scipy.signal.besselap(order, norm="delay")

    # now rescale for desired delay
    roots = p / delay_s * 2
    if order % 2 == 0:
        k = 1
    else:
        k = -1

    select_real = abs(roots.imag) <= 1e-8

    Rr = roots[select_real].real
    # and take the positive roots
    Rc = roots[roots.imag > 1e-8]

    pdict = dict(c=Rc, r=Rr)
    zdict = dict(c=-Rc.conjugate(), r=-Rr)

    return zdict, pdict, k


def bessel_delay_ABCDE(delay_s, order=1, rescale=None):
    zdict, pdict, k = bessel_delay(delay_s, order=order, rescale=rescale)
    return zpk_algorithms.ZPKdict(
        zdict=zdict,
        pdict=pdict,
        k=k,
        convention="scipy",
    )
