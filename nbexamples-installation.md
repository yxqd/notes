# Install nbexamples on jupyter-test.sns.gov

Install

```
$ conda update -c conda-forge jupyter jupyterhub jupyterlab  # update jupyter packages and remove old packages
$ conda install -c conda-forge nbexamples
```

Configuration

* create configuration file /usr/local/miniconda3/etc/jupyter/jupyter_notebook_config.py with the following content
  ```
  c.Examples.reviewed_example_dir = '/usr/local/miniconda3/share/jupyter/examples/reviewed'
  c.Examples.unreviewed_example_dir = '/usr/local/miniconda3/share/jupyter/examples/unreviewed'
  ```
* create directories to hold the shared examples
  ```
  $ mkdir -p /usr/local/miniconda3/share/jupyter/examples
  $ cd /usr/local/miniconda3/share/jupyter/examples
  $ mkdir reviewed unreviewed
  $ chgrp -R users .
  $ chmod -R g+rwX .
  ```

A user may need to restart his/her own service (in jupyter Control panel) to see it working.
