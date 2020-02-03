##############################################################################
#                                                                            #
#                simpleAdmin.py - Admin Script by MisiekBest                 #
#	                    --- http://vis-clan.pl ---                           #
#                                                                            #
#    Released: 15.10.2009                                                    #
#    Script Version: 1.2                                                     #
#	 Copyright (C) 2009  Michal 'MisiekBest' Pawlikowski                     #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    any later version.                                                      #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see http://www.gnu.org/licenses/ .    #
#                                                                            #
##############################################################################


"""
################
# What it is?: #
#######################################################################
# Simple Admin Script is a Battlefield 2                              #
# python script made for few things:                                  #
# - Restart round from chat without BF2CC Daemon                      #
# - Pause game from chat, unpause from console (also no BF2CC needed) #
# - Chatting from console during pause                                #
# - Change map directly from ingame chat                              #
#######################################################################


###################
# How to install: #
##################################################################
# 1. Go to mods/bf2/python/game/ direcory located on your server #
# (ex. BF2_v1.1.2965/mods/bf2/python/game/)                      #
# 2. Paste there this file                                       #
# 3. Edit __init__.py file and add this two lines:               #
# import simpleAdmin                                             #
# simpleAdmin.init()                                             #
# 4. Restart/run your server :)                                  #
##################################################################



################
# How to use?: #
###########################################################################
# 1. RESTART ROUND                                                        #
#     Type: '!restart' in global chat.                                    #
# 2. RESTART AFTER N SECONDS                                              #
#     Type: '!restart [seconds]' (value in seconds)                       #
# 3. ABORT RESTART                                                        #
#     Type: '!restart stop'                                               #
# 4. PAUSE GAME                                                           #
#     Type: !pause in global chat.                                        #
# 5. UNPAUSE GAME                                                         #
#     Open console (press ~), type:                                       #
#     rcon unpause                                                        #
#     and press enter. Game will unpause just after pressing enter key.   #
# 6. CHAT DURING PAUSE                                                    #
#     During pause everybody can talk using in-game console.              #
#     Just open console (press ~) and type:                               #
#     rcon Your message just right here [enter]                           #
# 6. CHANGE MAP                                                           #
#     Type: '!map [map_name] [map_size]' See details below...             #
###########################################################################

####################
#   Map changing:  #
###################################################################################################
# To make it easier there are some map shortcuts availiable to use in !map command.               #
# Just say in global/team/squad chat for example:                                                 #
# !map jalalalala 16                                                                              #
# and server will change map to Road To Jalalabad for 16 players.                                 #
# Of course sizes available for all maps are only: 16,32 or 64                                    #
#                                                                                                 #
# Here is full map mapping list:                                                                  #
# Dalian Plant: dp, dalian, plant, dalian_plant                                                   #
# Daqing Oilfields: do, daqing, oilfields, daqing_oilfields, daq, oil                             #
# Dragon Valley: dv, dragon, valley, dragon_valley                                                #
# Fushe Pass: fp, fushe, pass, fushe_pass                                                         #
# Great Wall: gw, wall, great, greatwall, great_wall                                              #
# Gulf Of Oman: goo, gulf, oman, gulf_of_oman                                                     #
# Highway Tampa: ht, tampa, highway, highway_tampa, high                                          #
# Kubra Dam: kd, kubra, dam, kubra_dam                                                            #
# Mashtuur City: mc, mashtuur, city, mashtuur_city                                                #
# Midnight Sun: ms, sun, midnight, midnight_sun                                                   #
# Operation Blue Pearl: obp, pearl, blue_pearl, operation_blue_pearl                              #
# Operation Clean Sweep: ocs, clean, sweep, operation_clean_sweep                                 #
# Operation Harvest: oh, operationharvest, operation_harvest, harvest                             #
# Operation Road Rage: orr, roadrage, rage, roadrage, operationroadrage, operation_road_rage      #
# Operation Smoke Screen: oss, smoke, smokescreen, operationsmokescreen, operation_smoke_screen   #
# Road To Jalalabad: rtj, jala, jalala, jalalalala, jalalabad, road_to_jalalabad                  #
# Sharqi Peninsula: sp, sharqi, peninsula, sharqi_peninsula                                       #
# Strike At Karkand: sak, strike, karkand, strike_at_karkand                                      #
# Taraba Quarry: tq, taraba, quarry, taraba_quarry                                                #
# Songhua Stalemate: ss, songhua, stalemate, songhua_stalemate                                    #
# Zatar_Wetlands: zw, zatar, wetlands, zatar_wetlands                                             #
###################################################################################################

CHANGELOG:
1.2:
- Added !restart [custom_time_in_seconds]
- It is now possible to abort restart. Just !restart stop
- Added !map command, it is now possible to change map in game chat.
1.1:
- Removed critical bug with checking admin list. In 1.0 everybody could change map or restart the server ;) Sorry!
1.0:
- Hello world! !restart, !pause, rcon unpause and chatting during pause!

TODO
- Add python timers (not bf2 which stop after pause ;) ) to unpause after some time...
- Suggestions? Please mail to misiekbest[r3pl4cethiswith@s1gn]gmail.com or xfire: misiekbest
"""



################################################################################
################################################################################
##->                        GLOBAL CONFIGURATION                            <-##
################################################################################
################################################################################


######################
#   ADMIN SETTINGS   #
################################################################################################
# Here you can set new admin(s) for rcon administration of this script.                        #
# Just put his/her name in " " (dont forget about clan prefix!). Add comma if more then one ;] #
# example: ADMIN_LIST = "[V!S] MisiekBest[PL]", "#SOF# FrYzJeR.inf"                            #
################################################################################################
ADMIN_LIST = "[V!S] MisiekBest[PL]"


##############################
#   RESTART ROUND - CONFIG   #
###########################################################################
# Here you can specify default time to restart round in seconds.          #
# After !restart command script will countdown from this value to zero.   #
# Of course you can use for example !restart 10 to start counting from 10 #
###########################################################################
TIME_TO_RESTART = 5


################################################################################
################################################################################
##->                     END OF GLOBAL CONFIGURATION                        <-##
##->                    DONT CHANGE ANYTHING BELOW ;)                       <-##
################################################################################
################################################################################








import bf2
import host
import re
import bf2.Timer

temp_time = TIME_TO_RESTART
gstatus = 0
inCounting = False

def init():
	host.registerHandler('ChatMessage', onChatMessage, 1)
	host.registerHandler('RemoteCommand', onRemoteCommand, 1)
	host.rcon_invoke('echo "Simple Admin Script by MisiekBest: loaded"')
	
def sayAll(msg):
	host.rcon_invoke("game.sayAll \"" + str(msg) + "\"")	

def onChatMessage(playerId, text, channel, flags):
	text = text.replace( "HUD_TEXT_CHAT_TEAM", "" )
	text = text.replace( "HUD_TEXT_CHAT_SQUAD", "" )
	text = text.replace( "HUD_CHAT_DEADPREFIX", "" )
	text = text.replace( "*\xA71DEAD\xA70*", "" )
	if text[0:1] == "!":
		pattern = re.compile(r'!(\w+) ?([a-z0-9]*) ?(\d*)')
		matches = pattern.findall(text)
		command = matches[0][0]
		if matches[0][1] != "":
			parameter = matches[0][1]
		else:
			parameter = None
		if matches[0][2] != "":
			param_extra = matches[0][2]
		else:
			param_extra = None
			
		if playerId == -1:
			playerId = 255
		playerObject =  bf2.playerManager.getPlayerByIndex(playerId)
		playerName = playerObject.getName()
		global ADMIN_LIST
		if (str(playerName) in ADMIN_LIST):
			if command == "restart" and not parameter:
				global temp_time
				temp_time = TIME_TO_RESTART
				restartRound()
			elif command == "restart" and isInt(parameter):
				global temp_time
				temp_time = int(parameter)
				restartRound()
			elif command == "restart" and parameter == "stop":
				global timer
				global inCounting
				if (inCounting):
					timer.destroy()
					timer = None
					temp_time = TIME_TO_RESTART
					inCounting = False
					sayAll("Restart aborted!")
			elif command == "pause" and not parameter:
				pauseGame()
			elif command == "map" and parameter and param_extra:
				changeMap(parameter, param_extra)

def changeMap(map, size):
	###################################################################################
	# Some code below was orignally programmed by Biomass in his RconMap script.      #
	# BIG thanks to him for really good work.                                         #
	# Original RconMap script: http://bf2tech.org/index.php/Scripts:RconMap           #
	###################################################################################
	_size_allowed_ = "16","32","64"
	mapinmaplist = 0
	mapmapping = {
		'dp': 'dalian_plant',
		'dalian': 'dalian_plant',
		'plant': 'dalian_plant',
		'dalian_plant': 'dalian_plant',
		'do': 'daqing_oilfields',
		'daqing': 'daqing_oilfields',
		'oilfields': 'daqing_oilfields',
		'daqing_oilfields': 'daqing_oilfields',
		'daq': 'daqing_oilfields',
		'oil': 'daqing_oilfields',
		'dv': 'dragon_valley',
		'dragon': 'dragon_valley',
		'valley': 'dragon_valley',
		'dragon_valley': 'dragon_valley',
		'fp': 'fushe_pass',
		'fushe': 'fushe_pass',
		'pass': 'fushe_pass',
		'fushe_pass': 'fushe_pass',
		'gw': 'greatwall',
		'wall': 'greatwall',
		'great': 'greatwall',
		'greatwall': 'greatwall',
		'great_wall': 'greatwall',
		'goo': 'gulf_of_oman',
		'gulf': 'gulf_of_oman',
		'oman': 'gulf_of_oman',
		'gulf_of_oman': 'gulf_of_oman',
		'ht': 'highway_tampa',
		'tampa': 'highway_tampa',
		'highway': 'highway_tampa',
		'highway_tampa': 'highway_tampa',
		'high': 'highway_tampa',
		'kd': 'kubra_dam',
		'kubra': 'kubra_dam',
		'dam': 'kubra_dam',
		'kubra_dam': 'kubra_dam',
		'mc': 'mashtuur_city',
		'mashtuur': 'mashtuur_city',
		'city': 'mashtuur_city',
		'mashtuur_city': 'mashtuur_city',
		'ms': 'midnight_sun',
		'sun': 'midnight_sun',
		'midnight': 'midnight_sun',
		'midnight_sun': 'midnight_sun',
		'obp': 'operation_blue_pearl',
		'pearl': 'operation_blue_pearl',
		'blue_pearl': 'operation_blue_pearl',
		'operation_blue_pearl': 'operation_blue_pearl',
		'ocs': 'operation_clean_sweep',
		'clean': 'operation_clean_sweep',
		'sweep': 'operation_clean_sweep',
		'operation_clean_sweep': 'operation_clean_sweep',
		'oh': 'operationharvest',
		'operationharvest': 'operationharvest',
		'operation_harvest': 'operationharvest',
		'harvest': 'operationharvest',
		'orr': 'operationroadrage',
		'roadrage': 'operationroadrage',
		'rage': 'operationroadrage',
		'roadrage': 'operationroadrage',
		'operationroadrage': 'operationroadrage',
		'operation_road_rage': 'operationroadrage',
		'oss': 'operationsmokescreen',
		'smoke': 'operationsmokescreen',
		'smokescreen': 'operationsmokescreen',
		'operationsmokescreen': 'operationsmokescreen',
		'operation_smoke_screen': 'operationsmokescreen',
		'rtj': 'road_to_jalalabad',
		'jala': 'road_to_jalalabad',
		'jalala': 'road_to_jalalabad',
		'jalalalala': 'road_to_jalalabad',
		'jalalabad': 'road_to_jalalabad',
		'road_to_jalalabad': 'road_to_jalalabad',
		'sp': 'sharqi_peninsula',
		'sharqi': 'sharqi_peninsula',
		'peninsula': 'sharqi_peninsula',
		'sharqi_peninsula': 'sharqi_peninsula',
		'sak': 'strike_at_karkand',
		'strike': 'strike_at_karkand',
		'karkand': 'strike_at_karkand',
		'strike_at_karkand': 'strike_at_karkand',
		'tq': 'taraba_quarry',
		'taraba': 'taraba_quarry',
		'quarry': 'taraba_quarry',
		'taraba_quarry': 'taraba_quarry',
		'ss': 'songhua_stalemate',
		'songhua': 'songhua_stalemate',
		'stalemate': 'songhua_stalemate',
		'songhua_stalemate': 'songhua_stalemate',
		'zw': 'zatar_wetlands',
		'zatar': 'zatar_wetlands',
		'wetlands': 'zatar_wetlands',
		'zatar_wetlands': 'zatar_wetlands'
		}
	if mapmapping.has_key(map) and size in _size_allowed_:
		maplist = serverConfig("maplist.list")
		pattern = re.compile('^\d+:\s\"(.*?)\"\sgpm_cq\s(\d{2})$', re.MULTILINE)
		result = []
		for maplist in pattern.findall(maplist):
			result.append((maplist[0].lower(),maplist[1]))
		for mapavailable in result:
			if str(mapavailable[0]) == mapmapping[map]:
				if int(mapavailable[1]) == int(size):
					mapinmaplist = 1
		if (mapinmaplist == 1):
			host.rcon_invoke("admin.nextLevel " + str(result.index((mapmapping[map],size))))
			host.rcon_invoke("admin.runNextLevel")
		else:
			host.rcon_invoke('mapList.append ' + mapmapping[map] + ' gpm_cq ' + size)
			host.rcon_invoke("game.sayAll \"Changing map to " + mapmapping[map] + " - " + size + " players\"")
			host.rcon_invoke("admin.nextLevel " + str(len(result)))
			host.rcon_invoke("admin.runNextLevel")
	else:
		sayAll("Invalid map or illegal map size. Try again :)")
 

def restartRound():
	global timer
	global inCounting
	
	if (inCounting):
		timer.destroy()
		timer = None
		
	inCounting = True
	sayAll("Restart round in...")
	timer = bf2.Timer(onRestart, 1, 1)
	timer.setRecurring(1)

def onRestart(data):
	global TIME_TO_RESTART
	global temp_time
	global timer
	global inCounting
	
	if (temp_time>0):
		host.sgl_sendTextMessage( 0, 12, 1, "... %s "  % (temp_time), 0)
		temp_time = temp_time - 1
	else:
		timer.destroy()
		timer = None
		temp_time = TIME_TO_RESTART
		inCounting = False
		host.rcon_invoke("admin.restartMap")

def pauseGame():
	global gstatus
	if (gstatus == 0):
		host.rcon_invoke("gameLogic.togglePause")
		sayAll("Game paused!")
		sayAll("!!! You can now communicate with others. Open console and type:")
		sayAll("rcon _your_message_")
		sayAll("Admins can unpause the game by typing in console: rcon unpause")
		gstatus = 1
	else:
		host.rcon_invoke("gameLogic.togglePause")
		gstatus = 0



def onRemoteCommand(playerId, cmd):
	playerObject =  bf2.playerManager.getPlayerByIndex(playerId)
	playerName = playerObject.getName()
	global ADMIN_LIST
	global gstatus
	if (gstatus == 1):
		sayRcon(cmd,playerName)
	sc = str(cmd).split()
	if (str(playerName) in ADMIN_LIST):
		execRconCmd(cmd)
	
	
def execRconCmd(cmd):
	sc = str(cmd).split()
	if (sc[0] == "unpause"):
		pauseGame()
		
def sayRcon(cmd,pname):
	host.rcon_invoke("game.sayAll \"Player " + str(pname) + " " + str(cmd) + "\"")

def isInt(expression):
	try:
		int(expression)
		return True
	except ValueError:
		return False

def serverConfig(variableName):
 	return host.rcon_invoke(variableName).strip()
