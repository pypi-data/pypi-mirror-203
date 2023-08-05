#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:16:33 2021

@author: anirbanroy
"""


import cosmolopy.distance as cd
import matplotlib.pyplot as plt
import numpy as np
from colossus.lss import bias
from hmf import MassFunction
from scipy.integrate import simps
from scipy.interpolate import interp1d

import limpy.params as p

cosmo = {"omega_M_0": 0.3, "omega_lambda_0": 0.7, "omega_k_0": 0.0, "h": 0.71}


def hmf(z):
    mf = MassFunction(Mmin=np.log10(1e10), Mmax=np.log10(1e15), hmf_model="ST")
    mf.update(z=z)
    mpc_to_m = 3.086e22

    hm, dndm = mf.m, mf.dndm

    dndm *= (mpc_to_m) ** -3

    return hm, dndm  # /0.71**4


def mhalo_to_lcp_fit(Mhalo, z):
    Mhalo = np.array(Mhalo)
    M1 = 2.39e-5
    N1 = 4.19e11
    alpha = 1.79
    beta = 0.49

    F_z = ((1 + z) ** 2.7 / (1 + ((1 + z) / 2.9) ** 5.6)) ** alpha
    Lcii = F_z * ((Mhalo / M1) ** beta) * np.exp(-N1 / Mhalo)

    return Lcii


def Il(z, line_name="CII"):
    # mass_range=np.logspace(np.log10(Mmin), np.log10(Mmax),num=500)
    mass_bin, dndlnM = hmf(z)

    L_line = mhalo_to_lcp_fit(mass_bin, z)
    L_line *= p.Lsun
    # factor= (p.c_in_m)/(4*p.Ghz_to_hz*np.pi*p.nu_rest(line_name=line_name)*p.cosmo.H_z(z))

    factor = (p.c_in_m) / (4 * 1e9 * np.pi * (1900) * cd.hubble_z(z, **cosmo))

    integrand = factor * dndlnM * L_line

    integration = simps(integrand, mass_bin)

    return (integration) / (1e-26)  # In Jy/sr unit
    # return (factor*integration)/(p.jy_unit)  # In Jy/sr unit
