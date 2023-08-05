#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:31:19 2022

@author: anirbanroy
"""


import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as nf

# make a 3D grid


def densgas():
    fn = "/Users/anirbanroy/Desktop/updated_smoothed_deltax_z007.60_512_80Mpc"
    with open(fn, "rb") as f:
        dens_gas = np.fromfile(f, dtype="f", count=-1)

    return dens_gas


def grid_to_fft(grid):
    return nf.fftn(grid)


def get_grid_freq(ngrid_x, ngrid_y, ngrid_z):
    x_grid_coor = np.arange(ngrid_x)
    y_grid_coor = np.arange(ngrid_y)
    z_grid_coor = np.arange(ngrid_z)

    kx_f = 2 * np.pi * nf.freq(x_grid_coor, d=(x_grid_coor[1] - x_grid_coor[0]))
    ky_f = 2 * np.pi * nf.freq(y_grid_coor, d=(y_grid_coor[1] - y_grid_coor[0]))
    kz_f = 2 * np.pi * nf.freq(z_grid_coor, d=(z_grid_coor[1] - z_grid_coor[0]))

    return kx_f, ky_f, kz_f
