#!/usr/bin/env python

from distutils.core import setup

setup(
       version='0.1',
       author='reedts',
       description='Python script to get hottest submission from a subreddit.',
       scripts = ['hotreddit.py'],
       data_files=[('/etc/systemd/user', ['hotreddit.service', 'hotreddit.timer'])]
      )

