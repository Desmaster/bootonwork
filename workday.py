#!/usr/bin/env python

import ConfigParser;
from datetime import datetime,date,time;
import os.path;

basePath = os.path.dirname(os.path.realpath(__file__));
settingsPath = basePath + "/settings.cfg";

# Date variables
now     = datetime.now();
day     = int(now.isoweekday());
hour    = int(now.hour);
minute  = int(now.minute);

# Default start/end variables
startDay    = 0;
startHour   = 7;
startMinute = 30;
endDay      = 5;
endHour     = 17;
endMinute   = 30;

# Check if a confiugration file exists(settings.cfg) and if so, parse it
if os.path.exists(settingsPath):
    print("Using settings file " + settingsPath);
    config = ConfigParser.RawConfigParser();
    config.read(settingsPath);
    startDay    = int(config.get("start", "day"));
    startHour   = int(config.get("start", "hour"));
    startMinute = int(config.get("start", "minute"));
    endDay      = int(config.get("end", "day"));
    endHour     = int(config.get("end", "hour"));
    endMinute   = int(config.get("end", "minute"));

# Check if it's weekend
if day < startDay or day > endDay:
    print("According to my logic, it's weekend!");
    exit(1);

# Check if work day has started
if hour > endHour or hour == endHour and minute >= endMinute:
    print("According to my logic, your work day has ended!");
    exit(1);

# Check if work day has ended
if hour < startHour or hour == startHour and minute < startMinute:
    print("According to my logic, your work day hasn't started!");
    exit(1);

