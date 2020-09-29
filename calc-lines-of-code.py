#!/usr/bin/env python
import os, sys, sh

pkg = sys.argv[1]
sum = 0
def count(pkg):
    pkgsum = 0
    print(pkg)
    files = sh.git('ls-files', _cwd=pkg)
    for f in files:
        f = f.strip()
        p = os.path.join(pkg, f)
        if '/results/' in p: continue
        if not os.path.exists(p): continue
        if os.path.isdir(p): continue
        if os.path.islink(p): continue
        b, ext = os.path.splitext(f)
        if ext in '.ipynb .xlsx .h5 .png .npy .pdf .nxs .gz'.split():
            continue
        lines = sh.wc('-l', p).strip().split()[0]
        # print(p, lines)
        pkgsum+=int(lines)
    return pkgsum

print(count(pkg))
