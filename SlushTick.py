#!/usr/bin/python

import json,time,urllib,requests

while True:
	ticker = urllib.urlopen("https://beta.mining.bitcoin.cz/accounts/profile/json/121971-3978f22d8d96377e5f25b972190ac5f8")
	
	data = json.load(ticker)
	#print data
	c1 = data['username']
	c2 = data['unconfirmed_reward']
	c4 = data['confirmed_reward']
	c5 = data['estimated_reward']
	c3 = data['workers']
	d1 = c3['cjbaccus.pornapster2']
	d2 = d1['hashrate']
	d3 = d1['score']

	print "User: ",c1
	print "Unconfirmed:",c2
	print "Confirmed: ",c4
	print "Estimated Reward: ",c5
	print "Hashrate: ",d2
	print "Total Score: ",d3
	print "#########",(time.strftime("%H:%M:%S")),"#########"
	print " "
 
	time.sleep(300)

