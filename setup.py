#!/usr/bin/env python
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
#d['packages'] = ['baxter_rr_bridge', 'baxter_external_devices']
#d['package_dir'] = {'': 'src'}
#d['package_dir'] = {'': 'src'}
#d['packages'] = ['baxter_rr_bridge']
#d['package_dir'] = {'': '/home/artlab2/ros_ws/src'}


setup(**d)
