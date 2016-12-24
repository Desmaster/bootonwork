Boot on work
------------

A simple wrapping script to boot multiple programs only when the current time matches your workweek's time frame. I use it to have my work related applications only start in my working schedule.

#### Installation

It's up to you how you want to install it. To call the program, run the file `bootonwork.sh` from any directory.

To define what programs you want to boot, create a file called `boot.sh`. For example:

```
#!/bin/bash

/home/timon/software/toggldesktop/TogglDesktop.sh %f &
/usr/bin/scudcloud &
```

In my use case I need to startup some applications like Toggl or Slack. There's an example of a desktop entry(`bootonwork.desktop.sample`), it's what I use to add a startup application to Gnome. 

#### Configuration

If the timeframe / working schedule does not fit your needs, you can tweak the script by adding a file called `settings.cfg` in the directory of the repository, for example: 

```
[start]
day=0     # First day of your workweek, 1 is Monday - 7 is Sunday
hour=8    # The hour your workday starts
minute=30 # The minute of the hour your workday starts

[end]
day=5     # Last day of your workweek, 1 is Monday - 7 is Sunday
hour=17   # The hour your workday ends
minute=0  # The minute of the hour your workday ends
```
#### Vacation

Having a vacation? Just run `touch vacation.flag` in this directory when your vacation starts and run `rm vacation.flag` in this directory when your vacation is over. The program will detect the flag and won't boot, whatever your schedule is!
