#!/usr/bin/python
import json, time, requests, urllib

while True:
    ticker = urllib.urlopen("https://alloscomp.com/bitcoin/calculator/json?hashrate=200000000000")


    data =  json.load(ticker)
    exRate = data['exchange_rate']
    Cph = data['coins_per_hour']
    Tpb = data['time_per_block']
    Cbr = data['coins_before_retarget']

    print "Exchange rate: %s" % exRate
    print "Coins per Hour: %s" % Cph
    print "Time per Block: %s" % Tpb
    print "Coins before retarget: %s" % Cbr

    time.sleep(360)