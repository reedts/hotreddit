#!/usr/bin/env python
import os
import sys
import praw
import random

import configparser

from os.path import expanduser

home = expanduser("~")

wdir = home + "/.hotreddit/"
msgpath = wdir + "msg"
cfgpath = wdir + "config"


if __name__ == "__main__":

    os.makedirs(os.path.dirname(wdir), exist_ok=True)

    config = configparser.ConfigParser()

    if not os.path.isfile(cfgpath):
        config['CONNECTION'] = {'client_id': ' ' ,
                                'client_secret' : ' ',
                                'user_agent': ' '
                               }
        config['SUBREDDITS'] = {'subs': 'showerthoughts'}

        with open(cfgpath, 'w+') as cfgfile:
            config.write(cfgfile)
        
        print("Your new configfile was written to %s!" % cfgpath)
        sys.exit(0)

    else:
        try:
            config.read(cfgpath)
        except configparser.Error:
            print("Could not load config file!\n")
            sys.exit(1)
   

    con_cfg= config['CONNECTION']
    subs_cfg = config['SUBREDDITS']['subs']

    reddit = praw.Reddit(client_id = con_cfg['client_id'],
                        client_secret = con_cfg['client_secret'],
                        user_agent = con_cfg['user_agent'])

    subreddit = random.choice(subs_cfg.split(','))

    hottest = reddit.subreddit(subreddit).hot()

    with open(msgpath, 'w+') as f:
        f.write(hottest.next().title)


