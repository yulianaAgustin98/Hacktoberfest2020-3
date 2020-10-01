import requests
import xml.etree.ElementTree as ET
import untangle		#sudo pip install untangle
import os
from PIL import Image   #sudo pip install Pillow
import shutil
import geocoder         #sudo pip install geocoder

print("\n")
print('\x1b[6;30;42m'+"WELCOME TO MAPS-SUITE"+'\x1b[0m',"\n")
print("What would you like to do?")
print("1.Directions from A to B\n2.Geocodes of A\n3.Altitude(limited to 53S and 60N lines)\nInputs and results are limited to cities or states\nEnter choice: ")
main_num=int(input())

global autodetect
def autodetect():
	global str2
	autodet=int(input())
	if autodet==1:
		str2=input("Enter location manually:\n")
	elif autodet==2:
		autog=geocoder.ip('me')
		auto_str=autog.latlng
		str2=str(auto_str[0])+","+str(auto_str[1])

global discard	
def discard():
	if os.path.exists("data.xml"):
 		os.remove("data.xml")
	if os.path.exists("datageo.xml"):
		os.remove("datageo.xml")
	if os.path.exists("dataalt.xml"):
		os.remove("dataalt.xml")
	if os.path.exists("img.png"):
		os.remove("img.png")

global nut_geoalt
global get_geocode_api
def nut_geoalt():
	def get_geocode_api():
		global fgstr
		str6="https://www.mapquestapi.com/geocoding/v1/address?key=(YOUR KEY HERE)&inFormat=kvp&outFormat=xml&location="
		print("Enter current location\n Manual - 1\n Autodetect -2\n")
		autodetect()
		str8="&thumbMaps=false&maxResults=1"
		fgstr=str6+str2+str8
		return(fgstr)
	
	get_geocode_api()
	geocode_response=requests.get(fgstr)
	def save_response_geo():
		with open('datageo.xml', 'w') as f:
			f.write(geocode_response.text)
	save_response_geo()
	geo = untangle.parse('datageo.xml')
	global geo_lat
	global geo_lng
	geo_lat=geo.response.results.result.locations.location.displayLatLng.latLng.lat.cdata
	geo_lng=geo.response.results.result.locations.location.displayLatLng.latLng.lng.cdata

if main_num==1:
	global get_direction_api
	def get_direction_api():
		global fstr
		global str2
		global str4
		print("Select route optimization")
		print("1.Optmized for speed\n2.Optimized for shortest distance\n")
		def opts():
			global str5
			opt_select=int(input("Enter choice: "))
			if opt_select==1:
				str5="&outFormat=xml&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false"
			elif opt_select==2:
				str5="&outFormat=xml&ambiguities=ignore&routeType=shortest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false"
			else:
				print("No optimization selected")
				opts()
		opts()
		print("\n")
		str1="https://www.mapquestapi.com/directions/v2/route?key=(YOUR KEY HERE)&from="
		print("Enter current location\n Manual - 1\n Autodetect -2\n")
		autodetect()
		str3="&to="
		str4=input("Enter destination: ")
		print("\n")
		fstr=str1+str2+str3+str4+str5
		return fstr
	
	global check
	def check(x):
		if x==1:
			toll_check=obj.response.route.hasTollRoad.cdata
			if toll_check=="false":
				print("\n\nYou saved money, lets naach\n\n")
			else:
				print("\n\nEmpty your pockets right now!\n\n")
			info()
		elif x==2:
			b_check=obj.response.route.hasBridge.cdata
			if b_check=="false":
				print("\n\nAww shucks,no bridges\n\n")
			else:
				print("\n\nLets 'bridge' my friend\n\n")
			info()
		elif x==3:
			t_check=obj.response.route.hasTunnel.cdata
			if t_check=="true":
				print("\n\nSpooky tunnels ahead\n\n")
			else:
				print("\n\nNo tunnels ;_;\n\n")
			info()
		elif x==4:
			finaldist=float(obj.response.route.distance.cdata)
			print("\n\nDistance: ",round((finaldist*1.6),2), "kilometers\n\n")
			info()
		elif x==5:
			est_fuel=float(obj.response.route.fuelUsed.cdata)
			print("\n\nEstimated fuel required: ",round((est_fuel*3.78),2)," liters\n\n")
			info()
		elif x==6:
			est_time=obj.response.route.realTime.cdata
			est_time=int(est_time)
			print("\n\nETA: ",((est_time/60)//60),"hours\n\n")
			info()
		elif x==7:
			i=0
			while i<(len(obj.response.route.legs.leg.maneuvers.maneuver)):
				man_iter=obj.response.route.legs.leg.maneuvers.maneuver[i].narrative.cdata
				direction_step.append(man_iter)
				i+=1	
			for i in range(0,len(direction_step)):
				print(i+1,": ",'\x1b[6;30;42m'+direction_step[i]+'\x1b[0m',"\n")
			info()
		elif x==8:
			str_img="https://www.mapquestapi.com/staticmap/v5/map?start="				
			str_img0="&end="
			str_img1="&key=zzc4LhPVWopXqGBoHiGvCjp8Ymu9QV9I&format=png&traffic=flow&type=map"
			fstr_img=str_img+str2+str_img0+str4+str_img1
			img_response= requests.get(fstr_img, stream=True)
			with open('img.png', 'wb') as out_file:
    				shutil.copyfileobj(img_response.raw, out_file)
			with Image.open('img.png') as img:
  				img.show()
			info()
		else:
			print("\nWrong choice\n")
			info()
	def save_response():
		with open('data.xml', 'w') as f:
			f.write(response_xml.text)

	direction_step=[]
	get_direction_api()
	response_xml=requests.get(fstr)
	save_response()
	obj = untangle.parse('data.xml')
	copyright=obj.response.info.copyright.text.cdata
	print("Data from:",copyright)
	print("Script author not responsible for data inaccuracy\n")

	global info
	def info():
		print("What would you like to know\n")
		print("1.Presence of troll roads\n2.Presence of bridges\n3.Presence of tunnels\n4.Total distance\n5.Estimated fuel required\n6.Esimated Time of Arrival\n7.Directions list\n8.Route traffic flow screenshot\n-----0 to exit")
		num=int(input("Enter a choice: "))
		if num==0:
			print("\nTerminated\n")
			discard()
		else:
			check(num)
	info()
elif main_num==2:

	nut_geoalt()
	print("Geocodes are\n", geo_lat," Latitude ",geo_lng," Longitude")
	discard()
	
elif main_num==3:
	nut_geoalt()
	def altitude():
		global alt
		str9="http://open.mapquestapi.com/elevation/v1/profile?key=(YOUR KEY HERE)&outFormat=xml&latLngCollection="
		alt=str9+geo_lat+","+geo_lng
		return(alt)

	altitude()
	altitude_response=requests.get(alt)
	with open('dataalt.xml', 'w') as f:
			f.write(altitude_response.text)
	alt_parse = untangle.parse('dataalt.xml')
	alt_final=alt_parse.elevationResponse.distanceHeightCollection.distanceHeight.height.cdata
	print("Altitude=",alt_final,"Meters above sea level")
	discard()
	
else:
	print("Invalid choice\nTerminated...")
	discard()
