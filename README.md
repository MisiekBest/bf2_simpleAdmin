Simple Admin Script is a Battlefield 2 python script made for few things: 
 - Restart round from chat without BF2CC Daemon                      
 - Pause game from chat, unpause from console (also no BF2CC needed) 
 - Chatting from console during pause                                
 - Change map directly from ingame chat                              


 How to install: 

 1. Go to mods/bf2/python/game/ direcory located on your server 
 (ex. BF2_v1.1.2965/mods/bf2/python/game/)                      
 2. Paste there this file                                       
 3. Edit __init__.py file and add this two lines:               
 import simpleAdmin                                             
 simpleAdmin.init()                                             
 4. Restart/run your server :)                                  





 How to use?: 

 1. RESTART ROUND                                                        
     Type: '!restart' in global chat.                                    
 2. RESTART AFTER N SECONDS                                              
     Type: '!restart [seconds]' (value in seconds)                       
 3. ABORT RESTART                                                        
     Type: '!restart stop'                                               
 4. PAUSE GAME                                                           
     Type: !pause in global chat.                                        
 5. UNPAUSE GAME                                                         
     Open console (press ~), type:                                       
     rcon unpause                                                        
     and press enter. Game will unpause just after pressing enter key.   
 6. CHAT DURING PAUSE                                                    
     During pause everybody can talk using in-game console.              
     Just open console (press ~) and type:                               
     rcon Your message just right here [enter]                           
 6. CHANGE MAP                                                           
     Type: '!map [map_name] [map_size]' See details below...             



   Map changing:  

 To make it easier there are some map shortcuts availiable to use in !map command.               
 Just say in global/team/squad chat for example:                                                 
 !map jalalalala 16                                                                              
 and server will change map to Road To Jalalabad for 16 players.                                 
 Of course sizes available for all maps are only: 16,32 or 64                                    
                                                                                                 
 Here is full map mapping list:                                                                  
 Dalian Plant: dp, dalian, plant, dalian_plant                                                   
 Daqing Oilfields: do, daqing, oilfields, daqing_oilfields, daq, oil                             
 Dragon Valley: dv, dragon, valley, dragon_valley                                                
 Fushe Pass: fp, fushe, pass, fushe_pass                                                         
 Great Wall: gw, wall, great, greatwall, great_wall                                              
 Gulf Of Oman: goo, gulf, oman, gulf_of_oman                                                     
 Highway Tampa: ht, tampa, highway, highway_tampa, high                                          
 Kubra Dam: kd, kubra, dam, kubra_dam                                                            
 Mashtuur City: mc, mashtuur, city, mashtuur_city                                                
 Midnight Sun: ms, sun, midnight, midnight_sun                                                   
 Operation Blue Pearl: obp, pearl, blue_pearl, operation_blue_pearl                              
 Operation Clean Sweep: ocs, clean, sweep, operation_clean_sweep                                 
 Operation Harvest: oh, operationharvest, operation_harvest, harvest                             
 Operation Road Rage: orr, roadrage, rage, roadrage, operationroadrage, operation_road_rage      
 Operation Smoke Screen: oss, smoke, smokescreen, operationsmokescreen, operation_smoke_screen   
 Road To Jalalabad: rtj, jala, jalala, jalalalala, jalalabad, road_to_jalalabad                  
 Sharqi Peninsula: sp, sharqi, peninsula, sharqi_peninsula                                       
 Strike At Karkand: sak, strike, karkand, strike_at_karkand                                      
 Taraba Quarry: tq, taraba, quarry, taraba_quarry                                                
 Songhua Stalemate: ss, songhua, stalemate, songhua_stalemate                                    
 Zatar_Wetlands: zw, zatar, wetlands, zatar_wetlands                                             


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
