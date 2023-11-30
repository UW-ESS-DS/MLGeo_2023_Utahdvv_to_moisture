import datetime
import os
import sys
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from itertools import zip_longest

#import scipy.interpolate
from scipy.interpolate import make_interp_spline, interp1d, CubicSpline, PchipInterpolator


if __name__ == '__main__':

    #-------------------------------------------#
    output_imgdir = "figure"
    if not os.path.exists(output_imgdir):
        os.makedirs(output_imgdir)
    #------------------------------------------------------#
    
    stnm=sys.argv[1] #'SPU'
    root="../../Utah_dv_modeling/UU_csv_blank/"
    utvec=np.loadtxt(root+"time.lst",dtype=float)
    
    
    # --- Read dv and factors 

    cols1=['time', 'dv', 'err','date']
    fn=root+'DV_'+stnm+'.csv'
    fiv=pd.read_csv(fn,names=cols1,header=0)
    t2 = np.array(fiv["time"])
    dvv = np.array(fiv["dv"])
    err = np.array(fiv["err"])
    vdate=np.array(fiv["date"])

    
    cols1=['ftime',  'temp_prism', 'ppt_prism', 'soil_nldas', 'snow_nldas', 'date']
    fn=root+'pretrim_'+stnm+'.csv'
    fi=pd.read_csv(fn,names=cols1,header=0)
    temp = (np.array(fi["temp_prism"]))# -np.mean(fi["temp_prism"]))   #/np.max(np.abs(fi["temp"]-np.mean(fi["temp"])))
    soil = (np.array(fi["soil_nldas"]))# -np.mean(fi["soil_nldas"]))   #/np.max(np.abs(fi["soil"]-np.mean(fi["soil"])))
    snow = np.array(fi["snow_nldas"]) #-np.mean(fi["snow_nldas"]))   
    ftime=np.array(fi["ftime"])

    #------------------------------------------------------#
    intdv = np.interp(utvec, t2, dvv)
    fint = interp1d(utvec, intdv)
    fspl = interp1d(utvec, intdv, kind='cubic')
    fcs = CubicSpline(t2, dvv)
    fcsp = PchipInterpolator(t2, dvv)
    fcsm = make_interp_spline(t2, dvv)
    cs_err = CubicSpline(t2, err)
    
    cs_temp=CubicSpline(ftime,temp)
    cs_soil=CubicSpline(ftime,soil)
    cs_snow=CubicSpline(ftime,snow)

    # --- define begin and end time
    tb=t2[0]
    te=t2[-1]
    # --- limited by soil data
    if (te>=2022.6250): # from soil
        for nt in utvec:
            if (nt>=2022.6250):    # from Lakes
                te=nt
                break
    
    Ntb=np.where(utvec==tb)[0][0]
    Nte=np.where(utvec==te)[0][0]
    print(" # --- ",stnm," Data period: ",tb,te,Nte-Ntb)
    
    vdate2=pd.date_range(vdate[0],vdate[-1],freq='D')
    data_date=pd.date_range(vdate2[0],vdate2[Nte-Ntb-1],freq='D')
    print("data range: ",data_date[0],data_date[-1])
    
    # --- define data
    data_time=utvec[Ntb:Nte]
    data_dv=fcsp(utvec)[Ntb:Nte]
    data_err=cs_err(utvec)[Ntb:Nte]
    data_temp=cs_temp(utvec)[Ntb:Nte]
    data_soil=cs_soil(utvec)[Ntb:Nte]


    fieldnames = ['utvec', 'dv','err','temp','SM_EWT','date']
    fcsv="INTERP_"+stnm+".csv"
    data={
        'utvec': data_time,
        'dv': data_dv,
        'err': data_err,
        'temp':data_temp,
        'SM_EWT':data_soil,
        'date':data_date    
    }
    
    df=pd.DataFrame(data)
    df.to_csv(fcsv,columns=fieldnames,sep=',',index = None, header=True, float_format="%.6f" )
    
    print("plotting ")
    #---plot dv/v for the debug---#
    fig, ax = plt.subplots(3, 1, figsize=(6,6))
    
    for k in range(0,3):
        ax[k].set_xlim(data_time[0],data_time[-1])
        ax[k].grid(True)
    
    #ax[0].set_ylim(-1,1)
    
    ax[0].plot(t2,dvv,'-',c='green',linewidth=10,alpha=0.5)
    #ax[0].plot(data_time,data_dv,'-',c='m')
    ax[0].plot(data_time,fcs(utvec)[Ntb:Nte],'-',c='m')
    ax[0].plot(data_time,fcsp(utvec)[Ntb:Nte],c='b',linewidth=5,alpha=0.5)
    #ax[0].plot(data_time,fcsm(utvec)[Ntb:Nte],'--',c='cyan',linewidth=1)
    ax[0].set_title(stnm)
    
    ax[1].plot(ftime,temp,  ls="-", c = "orange",linewidth=5,alpha=0.5)
    ax[1].plot(data_time,data_temp,  ls="-", c = "r")
    ax[1].set_title("Temperature (C)")
    
    ax[2].plot(ftime,soil,  ls="-", c = "blue",linewidth=5,alpha=0.5)
    ax[2].plot(data_time,data_soil,  ls="-", c = "cyan")
    ax[2].set_title("Soil moisture EWT (m)")
    
    plt.tight_layout()
    print("save")
    plt.savefig(output_imgdir+"/Data_%s.png"%(stnm), format="png", dpi=100)
    plt.close()
    print("close")
    plt.clf()