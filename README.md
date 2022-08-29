# Raspberry Temperature db
Simple python script to track temperatures from different devices on a Raspberry. I use an API and the I2C Bus, but more can be added in a fork.

## Hardware

As a sensor I'm using a MCP9800. It's very precise while not using a lot of Power.

I created my own PCB, but you can buy something similar here: https://www.reichelt.de/de/de/temperatur-sensor-click-board-mcp9800-mikroe-2979-p312254.html?r=1


## Setup

1. Install all Requirements `pip install -r requirements.txt`.

2. Create your .env `cp .env.dist .env` and fill in your Keys.

3. To get started set up the SQLite DB `python setup.py`.

## Usage

Create a Cronjob which runs the following command: `python main.py`.

This command takes care of gathering all data and will write the output into the SQLite DB.

Depending on the usecase I suggest a configuration similar to this:

```
crontab -e

0 * * * * /usr/bin/python /home/username/projectdir/main.py >/dev/null 2>&1
```

This will gather new Data every full hour.
