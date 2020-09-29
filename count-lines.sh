# e.g. ./count-lines.sh neutron_imaging/iMars3D
target=$1
cd $target
git ls-files |grep -v "\.ipynb\|\.xlsx\|\.h5\|\.png\|\.npy\|\.pdf"|xargs wc -l
