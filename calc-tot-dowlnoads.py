#!/usr/bin/env python
import os, sys, sh

pkg = sys.argv[1] # e.g. 'mcvine/mcvine'

versions = list(map(str.strip, sh.anaconda('show', pkg, _err_to_out=True)))
versions = [_.lstrip('+').strip() for _ in versions if _.startswith('+')]

def getDownloads(lines):
    for l in lines:
        if not l.startswith('ndownloads'): continue
        return int(l.split(':')[1])

totdownloads = 0
for ver in versions:
    verpath = '{}/{}'.format(pkg, ver)
    files = list(map(str.strip, sh.anaconda('show', verpath, _err_to_out=True)))
    files = [_.lstrip('+').strip() for _ in files if _.startswith('+')]
    verdownloads = 0
    for f in files:
        fpath = '{}/{}'.format(verpath, f)
        info = sh.anaconda('show', fpath, _err_to_out=True).splitlines()
        d = getDownloads(info)
        verdownloads += d
    print("Downloads for {}: {}".format(ver, verdownloads))
    totdownloads += verdownloads

print("Total: ", totdownloads)
