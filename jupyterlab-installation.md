add conda-forge channel
```
$ conda config --add channels conda-forge
```

jupyter hub
```
$ conda install jupyterhub
$ conda install notebook
```

jupyter lab
```
$ conda install jupyterlab
```

ipywidgets
```
$ conda install ipywidgets
$ jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

googledrive support: sharing notebooks
```
$ jupyter labextension install @jupyterlab/google-drive
```

Setting for google API request origin: see [jupyterlab google api advanced doc](https://github.com/jupyterlab/jupyterlab-google-drive/blob/master/docs/advanced.md). The setting is written to ~/.jupyter/lab/user-settings/@jupyterlab/google-drive/drive.jupyterlab-settings

