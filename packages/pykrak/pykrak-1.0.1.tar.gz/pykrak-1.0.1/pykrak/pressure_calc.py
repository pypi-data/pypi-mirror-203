"""
Description:
Routines for calculating pressure with various input arguments and in various cases
Has some overkill modal Doppler if you have a fast moving source
The convention is that the source has time dependence of e^{i \omega t},
so e^{-ikr} is the outward spreading wave

get_pressure is for a single source range, and whatever depths phi_zr is sampled at
get_vec_pressure is for multiple source ranges


Date:
8.3.2022

Author: Hunter Akins

Institution: Scripps Institution of Oceanography, UC San Diego

Copyright (C) 2023  F. Hunter Akins

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np
from matplotlib import pyplot as plt
from numba import njit


def get_pressure(phi_zr, phi_zs, krs, r, tilt_angle=0, zr=None):
    """
    Consistent with fourier transform of the form
    P(\omega) = \int_{-\infty}^{\infty} p(t) e^{- i \omega t} \dd t
    From modes evaluated at receiver depths,
    evaluated at source depth, 
    wavenumbers kr, and source range r
    Return pressure as column vector
    Positive angle means it's leaning towards the source, 
    the lowest element of the array is always located at a range r 
    (so it's sort of the fixed point)
    Positive angle in DEGREES 
    """
    modal_matrix = phi_zs*phi_zr
    if tilt_angle != 0:
        Z = np.max(zr) - zr
        deltaR = Z*np.tan(tilt_angle * np.pi / 180.)
        deltaR = deltaR.reshape(zr.size,1)
        r = r - deltaR #  minus so that it leans towards the source (range gets closer)
        krs = krs.reshape(1, krs.size)
        range_arg = krs * r
        range_dep = np.exp(-1j*range_arg) / np.sqrt(range_arg.real)
        prod = modal_matrix*range_dep
        p = np.sum(prod, axis=1)[:, np.newaxis]
    else:
        range_dep = np.exp(-1j*r*krs) / np.sqrt(krs.real*r)
        range_dep = range_dep.reshape(krs.size,1)
        p = modal_matrix@range_dep
    p *= np.exp(1j*np.pi/4)
    p /= np.sqrt(8*np.pi)
    return p

@njit
def get_vec_pressure(phi_zr, phi_zs, krs, rgrid, tilt_angles=None, zr=None):
    """
    Designed for source tracks, not replica calculation
    Consistent with fourier transform of the form
    P(\omega) = \int_{-\infty}^{\infty} p(t) e^{- i \omega t} \dd t
    From modes evaluated at receiver depths,
    wavenumbers kr, 
    and a vector of source depths, ranges, and tilts
    Return pressure as array zr.size, num_pts in track
    Positive angle means it's leaning towards the source, 
    the lowest element of the array is always located at a range r 
    (so it's sort of the fixed point)
    Positive angle in DEGREES 
    It's approximate in that it doesn't correct the range spreading term from tilt,
    only the phase
    """
    num_track_pts = rgrid.size
    num_depths = phi_zr.shape[0]
    full_p = np.zeros((num_depths, num_track_pts), dtype=np.complex_)
    for i in range(num_track_pts):
        modal_matrix = phi_zr * phi_zs[:,i]
        modal_matrix = modal_matrix.astype(np.complex_)
        r = rgrid[i]
        if tilt_angles is not None:
            tilt_angle = tilt_angles[i]
            Z = np.max(zr) - zr
            deltaR = Z*np.tan(tilt_angle * np.pi / 180.)
            deltaR = deltaR.reshape(zr.size,1)
            delta_phi = np.exp(-1j*np.outer(deltaR, krs))
            modal_matrix *= delta_phi
        arg = krs.reshape(krs.size,1)* r
        range_dep = np.exp(-1j*arg) / np.sqrt(arg.real)
        p = modal_matrix@range_dep
        full_p[:,i] = p[:,0]
    full_p *= np.exp(1j*np.pi/4)
    full_p /= np.sqrt(8*np.pi)
    return full_p

def get_range_correction(zr, tilt_angle):
    """
    For receiving array tilted at angle tilt_angle (degrees)
    towards the source, compute the range correction for each element in zr
    A negative angle means that the top element is closer to the source than the bottom element
    (leaning forward)
    Positive means its further away (leaning back)
    Input
    zr - np array
    ASSUMED SORTED FROM SMALLEST TO LARGEST (shallowest to deepest)
    tilt_angle - int or float in degrees
    Output
    r_corr - np array same shape as zr
    If the array is at the origin (r=0), then r_corr gives their
    corrected locations relative to the origin
    """
    tilt_rad = np.pi / 180 * tilt_angle
    zr_rel = zr - zr[0]
    r_corr = np.tan(tilt_rad)*zr_rel
    r_corr -= np.mean(r_corr)
    return r_corr

def get_grid_pressure(zr, phi_z, phi, krs, zgrid, rgrid, tilt_angle=None):
    """
    Get the field grid for pressure for receivers at zr
    Using the modes phi evaluated at the grid depths z
    For sources at all positions in the grids zgrid and rgrid
    zr - np 1d array
    phi_z - np 1d array
    phi - np 2d array
        first axis is depth, second axis is mode
    krs - np 1d array
        horizontal wavenumbers
    zgrid - np 1d array
        candidate source depths
    rgrid - np 1d array
        candidate source ranges
    tilt_angles - np 1d array
        tilt angles of the array towards the source
    Return
    pfield - np 3d array
        First axis is receiver depth, second axis is source depth, third axis is source range
    Unnormalized, so really a field calculation
    """
    Nzr = zr.size
    if tilt_angle is not None:
        r_corr = get_range_correction(zr, tilt_angle)
    else:
        r_corr = np.zeros(zr.size)
    pfield = np.zeros((Nzr, zgrid.size, rgrid.size), dtype=np.complex_)

    # interpolate the modes to the grid depths (they are ``receivers'' in reciprocity)
    phi_zr = np.zeros((zgrid.size, krs.size))
    for l in range(krs.size):
        phi_zr[:,l] = np.interp(zgrid, phi_z, phi[:,l])

    # for each receiver depth
    for i in range(Nzr):
        # use reciprocity to get modal field everywhere
        zs = zr[i]
        strength = np.zeros((1, krs.size))
        # get mode value at ``source'' (receiver) depth
        for l in range(krs.size):
            strength[0,l] = np.interp(np.array(zs), phi_z, phi[:,l])
        modal_matrix = strength*phi_zr
        modal_matrix /= np.sqrt(krs.real)
        r_mat= np.outer(krs, rgrid-r_corr[i])
        range_dep = np.exp(-1j*r_mat) / np.sqrt(r_mat.real)
        source_p = modal_matrix@range_dep
        source_p *= np.exp(1j*np.pi/4)
        source_p /= np.sqrt(8*np.pi)
        pfield[i, ...] = source_p
    return pfield

def get_doppler_vec_pressure(phi_zr, phi_zs, krs, r_ret_grid, t_ret_grid, ums, contemp_tgrid, tilt_angles=None, zr=None):
    """
    Use modal Doppler theory get pressure due to source moving along track associated with rgrid
    sample on t_ret_grid retarded time points 
    The field is the usual field but using the range r_{s}(t') (the range in the retarded time)
    To get the field in the contemporary time, first find out which time samples I have the field
    using the relationship t = t' + r_{s}(t') / u_{m} , where t is contemporary time, t' is retarded
    time, r_{s}(t') is the range of the source in retarded time, and u_{m} is the group speed of the     mth mode
    Once I have these samples, I put them onto a uniform time grid
    The way I handle tilt is a little inaccurate because I don't use the doppler shifted 
    modes to get the range offsets (and I don't change the range spreading appropriately)
    """
    rgrids = np.zeros((krs.size, contemp_tgrid.size))
    phi_zs_dopp = np.zeros((krs.size, contemp_tgrid.size))
    for i in range(krs.size):
        tgrid = t_ret_grid + r_ret_grid / ums[i] # the contemporary time points associated with my sampled retarded time ranges
        rgrid = np.interp(contemp_tgrid, tgrid, r_ret_grid)
        rgrids[i,:] = rgrid
        phi_zs_mode = np.interp(contemp_tgrid, tgrid, phi_zs[i,:])
        phi_zs_dopp[i,:] = phi_zs_mode


    Z = np.max(zr) - zr

    num_track_pts = contemp_tgrid.size
    num_zrs = phi_zr.shape[0]
    full_p = np.zeros((num_zrs, num_track_pts), dtype=np.complex_)
    for j in range(zr.size):
        modal_matrix = phi_zr[j,:].reshape(krs.size,1) * phi_zs_dopp
        modal_matrix = modal_matrix.astype(np.complex_)
        if tilt_angles is not None:
            deltaR = Z[j]*np.tan(tilt_angles * np.pi / 180.)
            zr_rgrids = rgrids + deltaR
        else:
            zr_rgrids = rgrids
        arg = (krs.reshape(krs.size, 1)* zr_rgrids)
        range_dep = np.exp(-1j*arg) / np.sqrt(arg.real)
        p = np.sum(modal_matrix*range_dep, axis=0)
        full_p[j,:] = p
    full_p *= np.exp(1j*np.pi/4)
    full_p /= np.sqrt(8*np.pi)
    return full_p

@njit
def get_doppler_vec_pressure_deriv(phi_zr, phi_zs, dphir_dk, dphis_dk, kr, r_ret_grid, t_ret_grid, um, contemp_tgrid, tilt_angles=None, zr=None):
    """
    """
    tgrid = t_ret_grid + r_ret_grid / um # the contemporary time points associated with my sampled retarded time ranges
    rgrid = np.interp(contemp_tgrid, tgrid, r_ret_grid)
    phi_zs_dopp = np.interp(contemp_tgrid, tgrid, phi_zs[0,:])
    dphis_dk_dopp = np.interp(contemp_tgrid, tgrid, dphis_dk[0,:])

    Z = np.max(zr) - zr

    num_track_pts = contemp_tgrid.size
    num_zrs = phi_zr.shape[0]
    full_deriv = np.zeros((num_zrs, num_track_pts), dtype=np.complex_)

    for j in range(zr.size):
        A = phi_zr[j,0] * phi_zs_dopp
        if tilt_angles is not None:
            deltaR = Z[j]*np.tan(tilt_angles * np.pi / 180.)
            zr_rgrid = rgrid + deltaR
        else:
            zr_rgrid = rgrid
        arg = kr*zr_rgrid
        B = np.exp(-1j*arg) / np.sqrt(arg.real)
        dBdk = -1j*zr_rgrid.real*B
        dAdk = dphir_dk[j] * phi_zs_dopp + phi_zs_dopp * dphis_dk_dopp
        #print(np.linalg.norm(A*dBdk), np.linalg.norm(dAdk*B))
        full_deriv[j,:] = A*dBdk + dAdk*B
    full_deriv *= np.exp(1j*np.pi/4)
    full_deriv /= np.sqrt(8*np.pi)
    return full_deriv


@njit
def get_simple_doppler_vec_pressure(phi_zr, phi_zs, krs, rgrid, tgrid, ums, tilt_angles=None, zr=None):
    """
    Consistent with fourier transform of the form
    P(\omega) = \int_{-\infty}^{\infty} p(t) e^{- i \omega t} \dd t
    From modes evaluated at receiver depths,
    wavenumbers kr, 
    and a vector of source depths, ranges, and tilts
    Return pressure as array zr.size, num_pts in track
    Positive angle means it's leaning towards the source, 
    the lowest element of the array is always located at a range r 
    (so it's sort of the fixed point)
    Positive angle in DEGREES 
    It's approximate in that it doesn't correct the range spreading term from tilt,
    only the phase
    """
    num_track_pts = rgrid.size
    num_depths = phi_zr.shape[0]
    full_p = np.zeros((num_depths, num_track_pts), dtype=np.complex_)
    dt = tgrid[1] - tgrid[0]     
    for i in range(num_track_pts):
        modal_matrix = phi_zr * phi_zs[:,i]
        modal_matrix = modal_matrix.astype(np.complex_)
        r = rgrid[i]
        if i == 0:
            v = (rgrid[1] - rgrid[0]) / dt
        elif i == num_track_pts - 1:
            v = (rgrid[-1] - rgrid[-2]) / dt
            print('v',v)
        else:
            v = .5*(rgrid[i+1] - rgrid[i-1]) / dt
            print('v',v)
        krsi = krs / (1+v/ums) # doppler shifted krs...
        if tilt_angles is not None:
            tilt_angle = tilt_angles[i]
            Z = np.max(zr) - zr
            deltaR = Z*np.tan(tilt_angle * np.pi / 180.)
            deltaR = deltaR.reshape(zr.size,1)
            delta_phi = np.exp(-1j*np.outer(deltaR, krsi))
            modal_matrix *= delta_phi
        arg = krsi.reshape(krsi.size,1)* r
        range_dep = np.exp(-1j*arg) / np.sqrt(arg.real)
        p = modal_matrix@range_dep
        full_p[:,i] = p[:,0]
    full_p *= np.exp(1j*np.pi/4)
    full_p /= np.sqrt(8*np.pi)
    return full_p
