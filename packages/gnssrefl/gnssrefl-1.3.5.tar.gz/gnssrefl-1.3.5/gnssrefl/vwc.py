import argparse
import matplotlib.pyplot as plt
import numpy as np
import os
import subprocess
import sys

from datetime import datetime
from pathlib import Path

import gnssrefl.phase_functions as qp
import gnssrefl.gps as g
from gnssrefl.utils import str2bool, read_files_in_dir

xdir = os.environ['REFL_CODE']


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("station", help="station", type=str)
    parser.add_argument("year", help="year", type=int)
    parser.add_argument("-year_end", default=None, help="year_end", type=int)
    parser.add_argument("-fr", help="frequency", type=int)
    parser.add_argument("-plt2screen", default=None, type=str, help="boolean for plotting to screen")
    parser.add_argument("-screenstats", default=None, type=str, help="boolean for plotting statistics to screen")
    parser.add_argument("-min_req_pts_track", default=None, type=int, help="minimum number of points for a track to be kept. Default is 50")
    parser.add_argument("-polyorder", default=None, type=int, help="override on polynomial order")
    parser.add_argument("-minvalperday", default=None, type=int, help="minimum number of satellite tracks needed each day. Default is 10")
    parser.add_argument("-snow_filter", default=None, type=str, help="boolean for attempting to remove days contaminated by snow")
    parser.add_argument("-circles", default=None, type=str, help="boolean for circles instead of lines for the final VWC plot ")
    parser.add_argument("-subdir", default=None, type=str, help="use non-default subdirectory for output files")
    parser.add_argument("-tmin", default=None, type=str, help="minimum soil texture")
    parser.add_argument("-tmax", default=None, type=str, help="maximum soil texture")

    args = parser.parse_args().__dict__

    boolean_args = ['plt2screen','screenstats','snow_filter','circles']
    args = str2bool(args, boolean_args)
    # only return a dictionary of arguments that were added from the user - all other defaults will be set in code below
    return {key: value for key, value in args.items() if value is not None}


def vwc(station: str, year: int, year_end: int = None, fr: int = 20, plt2screen: bool = True, screenstats: bool = False, 
        min_req_pts_track: int = 50, polyorder: int = -99, minvalperday: int = 10, 
        snow_filter: bool = False, circles: bool=False, subdir: str=None, tmin: str=None, tmax: str=None):
    """
    Computes VWC from GNSS-IR phase estimates. It concatenates previously computed phase results,  
    makes plots for the four geographic quadrants, computes daily average phase files before converting 
    to volumetric water content (VWC).

    IMO This should be moved into a driver so that the main functions are called separately.

    Examples
    --------

    one year for station p038 
        vwc p038 2017

    three years  for station p038 
        vwc p038 2015 -year_end 207

    Parameters
    ----------
    station : str
        4 character ID of the station

    year : integer
        Year
    year_end : integer
        last year for analysis

    fr : integer, optional
        GNSS frequency. Currently only supports l2c.
        Default is 20 (l2c)

    plt2screen: bool, optional
        Whether to produce plots to the screen.
        Default is True

    min_req_pts_track : int, optional
        how many points needed to keep a satellite track
        default is 50

    polyorder : int
        polynomial order used for leveling.  Usually the code picks it but this allows to users to override. 
        Default is -99 which means let the code decide

    minvalperday: integer
        how many phase measurements are needed for each daily measurement
        default is 10

    snow_filter: boolean 
        whether you want to attempt to remove points contaminated by snow
        default is False

    circles : boolean
        whether you want circles in the final plot (lines are default)

    subdir: str
        subdirectory in $REFL_CODE/Files for plots and text file outputs
    tmin: str
        minimum soil texture value, e.g. 0.05
    tmax: str
        maximum soil texture value, e.g. 0.45

    Returns
    -------

    Daily phase results in a file at $REFL_CODE/<year>/phase/<station>_phase.txt
        with columns: Year DOY Ph Phsig NormA MM DD

    VWC results in a file at $$REFL_CODE/<year>/phase/<station>_vwc.txt
        with columns: FracYr Year DOY  VWC Month Day

    """
    if (len(station) != 4):
        print('station name must be four characters')
        sys.exit()

    if (len(str(year)) != 4):
        print('Year must be four characters')
        sys.exit()

    freq = fr # KE kept the other variable

    if not year_end:
        year_end = year

    # save soil texture values
    if tmin is None:
        tmin = 0.05
    else:
        tmin = float(tmin)

    if tmax is None:
        tmax = 0.5
    else:
        tmax = float(tmax)

    # default is station name
    if subdir == None:
        subdir = station 

    # make sure subdirectory exists
    g.set_subdir(subdir)

    if not plt2screen:
        print('no plots will come to screen. Will only be saved.')

    # this is leftover from the old code
    writeout = True

    snow_file = xdir + '/Files/snowmask_' + station + '.txt'
    snowfileexists = False
    if snow_filter:
        medf = 0.2 # this is meters
        ReqTracks = 10 # have a pretty small number here
        snowfileexists = qp.make_snow_filter(station, medf, ReqTracks, year, year_end)
        plt.close ('all')# we do not want the plots to come to the screen for the daily average

    # azimuth list
    azlist = [270, 0, 180,90 ]

    # load past analysis  for QC
    avg_exist, avg_date, avg_phase = qp.load_avg_phase(station,freq)
    if not avg_exist:
        print('WARNING: the average phase file from a previous run does not exist as yet')

    if snowfileexists and snow_filter :
        print('using snow filter code')
        # use same variables as existing code
        data_exist, year_sat_phase, doy, hr, phase, azdata, ssat, rh, amp,ext = qp.filter_out_snow(station, 
                year, year_end, fr,snow_file)
    else:
        data_exist, year_sat_phase, doy, hr, phase, azdata, ssat, rh, amp,ext = qp.load_sat_phase(station, 
                year, year_end=year_end, freq=freq)

    if not data_exist:
        print('No data were found. Check your frequency request or station name')
        sys.exit()

    
    tracks = qp.read_apriori_rh(station,freq)
    nr = len(tracks[:,1])

    if (minvalperday > nr ):
        print('The code thinks you are using ', nr, ' satellite tracks but you are requiring', minvalperday, ' for each VWC point.')
        print('Try lowering minvalperday at the command line')
        sys.exit()
    if (nr < 15 ) and (minvalperday==10):
        print('The code thinks you are using ', nr, ' satellite tracks but that is pretty close to the default (', minvalperday, ')')
        print('This could be problematic. Try lowering minvalperday at the command line')
        sys.exit()

    atracks = tracks[:, 5]  # min azimuth values
    stracks = tracks[:, 2]  # satellite names

    # column 3 is sat, 4 is azimuth, npoints is 5, azim is 6 and 7
    k = 1
    vxyz = np.empty(shape=[0, 7]) 

    # try removing these
    fig = plt.figure(figsize=(13, 10))
    ax=plt.subplots_adjust(hspace=0.2)
    plt.suptitle(f"Station: {station}", size=16)

    # this is the number of points for a given satellite track
    reqNumpts = min_req_pts_track

    # checking each geographic quadrant
    for index, az in enumerate(azlist):
        b = 0
        k += 1
        amin = az
        amax = az + 90
        # make a quadrant average for plotting purposes
        vquad = np.empty(shape=[0, 4])
        # pick up the sat list from the actual list
        satlist = stracks[atracks == amin]

        ax = plt.subplot(2, 2, index + 1)
        ax.set_title(f'Azimuth {str(amin)}-{str(amax)} deg.')
        ax.grid()
        #ax.autofmt_xdate()

        # this satellite list is really satellite TRACKS
        for satellite in satlist:
            if screenstats:
                print(satellite, amin, amax)
            # indices for the track you want to look at here
            ii = (ssat == satellite) & (azdata > amin) & (azdata < amax) & (phase < 360)
            x = phase[ii]
            t = doy[ii]
            h = hr[ii] # TODO this is never used
            y = year_sat_phase[ii]
            azd = azdata[ii]
            s = ssat[ii]
            amps = amp[ii]
            rhs = rh[ii]

            if len(x) > reqNumpts:
                b += 1
                sortY = np.sort(x)

                N = len(sortY)
                NN = int(np.round(0.20*N))

                # use median value instead
                medv = np.median(sortY[(N-NN):(N-1)])
                new_phase = -(x-medv)
                ii = (new_phase > -20)
                t = t[ii]
                y = y[ii]
                new_phase = new_phase[ii]
                azd = azd[ii]
                s = s[ii]
                amps = amps[ii]
                rhs = rhs[ii]
                if len(t) == 0:
                    print('you should consider removing this satellite track', sat, amin)

                if (len(t) > reqNumpts):
                    for l in range(0, len(t)-1):
                        if new_phase[l] > 340:
                            new_phase[l] = new_phase[l] - 360
                    ii = (new_phase > -20) & (new_phase < 60)
                    t = t[ii]
                    y = y[ii]
                    new_phase = new_phase[ii]
                    azd = azd[ii]
                    s = s[ii]
                    amps = amps[ii]
                    rhs = rhs[ii]
                    sortY = np.sort(new_phase)
                    # bottom 20% ???
                    NN = int(np.round(0.2*len(sortY)))
                    mv = np.median(sortY[0:NN])
                    new_phase = new_phase - mv
                    # probably should take out median value again

                    newl = np.vstack((y, t, new_phase, azd)).T
                    vquad = np.vstack((vquad, newl))

                    basepercent = 0.15
                    normAmps = qp.normAmp(amps, basepercent)
                    newl = np.vstack((y, t, new_phase, azd, s, rhs, normAmps)).T

                    if (len(newl) > 0) and (avg_exist):
                        # quadrant results for this satellite track
                        satdate = y + t/365.25
                        satphase = new_phase

                        # figure out intersetion with "good" results
                        inter, id1, id2 = np.intersect1d(avg_date, satdate, assume_unique=True, return_indices=True)
                        aa = avg_phase[id1]
                        bb = satphase[id2]
                        if len(aa) > 0:
                            res = np.round(np.std(aa - bb), 2)
                            addit = ''
                            if res > 5.5:
                                addit = '>>>>>  Consider Removing This Track <<<<<'
                            print(f"Npts {len(aa):4.0f} SatNu {satellite:2.0f} Residual {res:6.2f} Azims {amin:3.0f} {amax:3.0f} Amp {max(normAmps):4.2f} {addit:20s} ")
                        else:
                            print('No QC assessment could be made for this satellite track')
                    else:
                        print('No average , so no QC. You should iterate.')


                    # cumulative values
                    vxyz = np.vstack((vxyz, newl))
                    datetime_dates = []
                    for yr, d in zip(y, t):
                        datetime_dates.append(datetime.strptime(f'{int(yr)} {int(d)}', '%Y %j'))

                    ax.plot(datetime_dates, new_phase, 'o', markersize=3)
                    ax.set_ylabel('Phase')
                    #ax.set_ylimit((-20,60))
                    plt.ylim((-20,60))
                    # ???
                    plt.gcf().autofmt_xdate()


    plot_path = f'{xdir}/Files/{subdir}/{station}_az_phase.png'
    print(f"Saving to {plot_path}")
    plt.savefig(plot_path)

    # this is now done in a function. i believe this can be commented out
    #tv = np.empty(shape=[0, 4])
    # year, day of year, phase, satellite, azimuth, RH, and RH amplitude
    y1 = vxyz[:, 0]
    d1 = vxyz[:, 1]
    phase = vxyz[:, 2]
    #sat = vxyz[:, 3] # TODO this is not used
    #az = vxyz[:, 4] # TODO this is not used
    #rh = vxyz[:, 5] # TODO this is not used
    amp = vxyz[:, 6]

    # this is the number of tracks per day you need to trust the daily average
    #minvalperday = 10 - now an input
    if writeout:

        tv = qp.write_avg_phase(station, phase, fr,year,year_end,minvalperday,vxyz,subdir)
        print('Number of daily phase measurements ', len(tv))
        if len(tv) < 1:
            print('No results - perhaps minvalperday or min_req_pts_track are too stringent')
            sys.exit()

        # make datetime date array
        datetime_dates = [datetime.strptime(f'{int(yr)} {int(d)}', '%Y %j') for yr, d in zip(tv[:, 0], tv[:, 1])]

        qp.daily_phase_plot(station, fr,datetime_dates, tv,xdir,subdir)

        qp.convert_phase(station, year, year_end, plt2screen,fr,tmin,tmax,polyorder,circles,subdir)


def main():
    args = parse_arguments()
    vwc(**args)


if __name__ == "__main__":
    main()
