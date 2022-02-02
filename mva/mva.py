#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 5 09:50:58 2021

@author: gnaveen
"""
import numpy as np

class mva:
    def __init__(self, hindcast, observation, forecast=None):
        '''
        Parameters
        ----------
        hindcast : numpy.ndarray
            Hindcast data for any given forecast. Kindly respect the shape (years/samples,time,ensemble-members,grid-points).
        observation : numpy.ndarray
            The truth or observations corresponding to the hindcast data. Kindly respect the shape (years/samples,time,grid-points).
        forecast : numpy.ndarray
            Forecast data. Kindly respect the shape (time,ensemble-members,grid-points).

        Returns
        -------
        None.
        '''
        self.hcast = hindcast #shape(years/samples,time,ensemble-members,grid-points)
        self.truth_hc = observation #shape(years/samples,time,grid-points)
        self.fcast = forecast #shape(time,ensemble-members,grid_points)
        
    def adjust_forecast(self):
        '''
        This method corrects the bias of the forecasts using hindcasts and the corresponding observations through 
        Mean and Variance Adjustment (MVA) method.
        x*_i = (x_i - xmean_hc)*(sigma_ref/sigma_hc) + xmean_ref

        Returns
        -------
        bias_adjusted_forecast : numpy.ndarray
            The bias adjusted forecasts (same shape as the forecast).
        '''
        if self.fcast is None:
            return print('Kindly pass forecast data, and try again!')
        else:
            if ((self.hcast.shape[0] == self.truth_hc.shape[0]) and (self.hcast.shape[1] == self.truth_hc.shape[1] == self.fcast.shape[0]) and (self.hcast.shape[-1] == self.truth_hc.shape[-1] == self.fcast.shape[-1])):
                xmean_e = self.hcast.mean(axis=(0,2))
                sigma_e = self.hcast.std(axis=(0,2))
                xmean_ref = self.truth_hc.mean(axis=0)
                sigma_ref = self.truth_hc.std(axis=0)
                if 0 in sigma_e:
                    sigma_e = sigma_e.clip(1,None)
                cal = np.array([((self.fcast[:,i,:] - xmean_e)*(sigma_ref/sigma_e) + xmean_ref) for i in range(self.fcast.shape[1])])
                cal = np.transpose(cal,axes=(1,0,2))
                return cal
            else:
                return print("Please respect the array shapes and try again!")
    
    def adjust_hindcast(self):
        '''
        This method corrects the bias of the hindcasts using hindcasts of the remaining years in the set 
        (i.e., leave-one-out approach) and the corresponding observations through Mean and Variance Adjustment (MVA) method.
        
        Returns
        -------
        bias_adjusted_hindcast : numpy.ndarray
            The bias adjusted hindcasts (same shape as the hindcast).
        '''
        if ((self.hcast.shape[0] == self.truth_hc.shape[0]) and (self.hcast.shape[1] == self.truth_hc.shape[1]) and (self.hcast.shape[-1] == self.truth_hc.shape[-1])):
            i = 0
            cal = []
            for i in range(self.hcast.shape[0]):
                xmean_e = np.mean(np.delete(self.hcast,i,axis=0),axis=(0,2)) #use this for leave one out procedure
                sigma_e = np.std(np.delete(self.hcast,i,axis=0),axis=(0,2)) #use this for leave one out procedure
                xmean_ref = np.mean(np.delete(self.truth_hc,i,axis=0),axis=0)
                sigma_ref = np.std(np.delete(self.truth_hc,i,axis=0),axis=0)
                if 0 in sigma_e:
                    sigma_e = sigma_e.clip(1,None)
                cal_yy = np.array([((self.hcast[i,:,j,:] - xmean_e)*(sigma_ref/sigma_e) + xmean_ref) for j in range(self.hcast.shape[2])])
                cal.append(cal_yy)
            cal = np.transpose(np.array(cal),axes=(0,2,1,3))
            return cal
        else:
            return print("Please respect the array shapes and try again!")
            