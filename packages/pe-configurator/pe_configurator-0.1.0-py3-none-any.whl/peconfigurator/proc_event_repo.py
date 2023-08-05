#!/usr/bin/env python3

import sys
import os.path
import numpy as np
import pesummary
from pesummary.gw.file.read import read
from configparser import ConfigParser
import argparse
import glob
from get_EOB_settings import *

# This script will iterate through a repository and check for a preferred run,
# use that to determine the seglen, srate and amp-order for Production runs,
# and Check the ini files for those

def get_preferred_result(repo_path):
    """
    Return a pesummary object for the repo
    """
    pref_file = os.path.join(repo_path,'Preferred/PESummary_metafile/posterior_samples.json')
    try:
        sumfile = read(pref_file)
    except FileNotFoundError:
        print(f'No preferred run directory for {repo_path}!')
        raise
    return sumfile

parser = argparse.ArgumentParser(description="Set up / confirm config files for O3a")
parser.add_argument("repo", metavar="repo", type=str, help="path to event repo")
parser.add_argument("--HM",default=False, action="store_true", help="Do checks with higher modes enabled")
#parser.add_argument("--approx",default="IMRPhenomPv2pseudoFourPN", type=str)
parser.add_argument("--update-conf",default=False,action="store_true")
parser.add_argument("--q-min",default=None,type=float)

args = parser.parse_args()

pesum = get_preferred_result(args.repo)

try:
    samples = pesum.samples_dict['Preferred']
except KeyError:
    k = list(pesum.samples_dict.keys())[-1]
    print(f'Pesum object in {args.repo} did not contain Preferred table')
    print(f'Using table {k}')
    samples = pesum.samples_dict[k]

mtot = samples['total_mass']
q = samples['mass_ratio']
chi1z = samples['spin_1z']
chi2z = samples['spin_2z']
dist = samples['luminosity_distance']

Prods=glob.glob(os.path.join(args.repo,'C01_offline/Prod0*.ini'))
for f in Prods:
    print(f'Reading {f}')
    P = ConfigParser()
    P.read([f])
    flows = eval(P.get('lalinference','flow'))
    flow = float(np.array(list(flows.values())).min())

    ini_approx = P.get('engine','approx')

    # Round to multiples of 5
    mtot_max = 5*(float(mtot.max()) // 5 + 1)
    mtot_min = 5*(float(mtot.min()) // 5)

    # Round up to nearest Gpc
    dist_max = 1000*(dist.max() // 1000 + 1)

    q_min = float(q.min())
    if args.q_min is not None:
        if args.q_min > q_min:
            q_min = args.q_min

    safelens, fulllens, seglens = zip(*[estimate_seglen(flow, mt, q=1.0/q, chi1z=s1z, chi2z=s2z) for mt, q, s1z, s2z in zip(mtot, q, chi1z, chi2z) ])
    max_seglen = np.max(seglens)

    real_srates, srates = zip(*[min_sampling_rate_EOB(mt, q=1.0/q, HM=args.HM, chi1z=s1z, chi2z=s2z) for mt,q,s1z,s2z in zip(mtot,q, chi1z, chi2z)])
    max_srate = np.max(srates)

    print(f'Suggested parameters for {f} based on preferred run:')
    print(f'    seglen = {max_seglen}')
    print(f'    srate = {max_srate}')
    print(f'    mtotal-min = {mtot_min}')
    print(f'    mtotal-max = {mtot_max}')
    print(f'    distance-max = {dist_max}')
    seobp_amporder, f_start, hm_dominated = get_amp_order(mtot_max, f_low = flow, HM = args.HM)
    print(f'    FOR SEOBNRv4P or other time domain wfs: amporder = {seobp_amporder}')

    ini_seglen=P.getfloat('engine','seglen')
    if ini_seglen < max_seglen:
        print(f'WARNING: seglen {ini_seglen} < {max_seglen} too short')
    ini_srate = P.get('engine','srate')
    if ini_srate != max_srate:
        print(f'WARNING: srate {ini_srate} != {max_srate}')
    try:
        ini_mtot_min = P.getfloat('engine','mtotal-min')
    except:
        ini_mtot_min = 0
        pass
    if ini_mtot_min != mtot_min:
        print(f'WARNING: mtotal-min should be {mtot_min}')

    try:
        ini_mtot_max = P.getfloat('engine','mtotal-max')
    except:
        ini_mtot_max = 0
        pass
    if ini_mtot_max != mtot_max:
        print(f'WARNING: mtotal-max should be {mtot_max}')
    try:
        ini_amporder = P.getint('engine','amporder')
    except:
        ini_amporder = 0
    if ini_amporder != seobp_amporder and 'SEOBNRv4P' in ini_approx:
        print(f'WARNING: amporder {ini_amporder} != {amporder}')

    try:
        ini_dist_max = P.getfloat('engine','distance-max')
    except:
        ini_dist_max = 2000
    if ini_dist_max < dist_max:
        print(f'WARNING: distance-max {ini_dist_max} < {dist_max}')

    if args.update_conf:
        print(f'UPDATING {f}!!')
        P.set('engine','seglen',str(max_seglen))
        P.set('engine','srate',str(max_srate))
        P.set('engine','mtotal-min',str(mtot_min))
        P.set('engine','mtotal-max',str(mtot_max))
        P.set('engine','distance-max',str(dist_max))
        P.set('engine','amporder',str(amporder))
        with open(f,'w') as fp:
            P.write(fp)

