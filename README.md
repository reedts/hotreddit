# hotreddit
A python script that will fetch the hottest submissions from any subreddit.

This is just very very simple (and not very pythonic) script I created to use for myself. Its purpose is, to download the
top post of a subreddit. I wanted it, to write the post in a file, so that I can use it as a greeter message in my terminal.

## Install
To install the script and its systemd service and timer files, just download this repository or clone it and run
```
sudo python setup.py install
```

This will install all necessary files to your system. That are the script itself, a systemd service unit to execute the script,
when the provided systemd timer unit runs out. So, you basically have to enable and start the timer in your user's systemctl:
```
systemctl --user enable hotreddit.timer
systemctl --user start hotreddit.timer
```

## Running
The first run of the script will generate a configuration file in `$HOME/.hotreddit` that will contain three keys that
are needed for a connection to the reddit API. You will have to create a reddit-App under the preferences tab of your reddit
account. Just fill in the necessary IDs in the config file!

Last but not least, you will have to specify the subreddits, you want to take into account. The key `subs` accepts a comma
seperated list of subreddits. Every time, the script is run, it will choose one of these subreddits randomly and fetch
the top post writing it to the file `$HOME/.hotreddit/msg`. That file can now be read to use the submission the way you want.

For example:
Install the package `cowsay` if available for your system and put the following in your shell configuration file:
```
cat ~/.hotreddit/msg | cowsay -f tux
```
and you will be greeted by Tux with the top post of your subreddits every time you start a terminal!
