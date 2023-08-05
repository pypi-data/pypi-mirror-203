#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 18:21:08 2021

@author: anirbanroy
"""

import matplotlib.pyplot as plt
import numpy as np
from colossus.cosmology import cosmology
from colossus.lss import mass_function
from hmf import MassFunction

cosmology.setCosmology("planck15")

Mass_bin = np.logspace(np.log10(1e8), np.log10(1e15), num=100)
mfunc_tinker = mass_function.massFunction(
    Mass_bin, 6.0, mdef="200c", model="tinker08", q_out="dndlnM"
)
mfunc_sheth = mass_function.massFunction(
    Mass_bin, 6.0, mdef="fof", model="sheth99", q_out="dndlnM"
)


plt.plot(Mass_bin, mfunc_tinker, label="Tinker")
plt.plot(Mass_bin, mfunc_sheth, label="Sheth")

plt.xscale("log")
plt.yscale("log")

plt.xlabel(r"Mass, $[h^{-1}M_\odot]$")
plt.ylabel(r"$dn/dm$, $[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$")

plt.legend(loc=0)
