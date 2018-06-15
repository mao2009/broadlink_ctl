# Broadlink Controller
A simple  controller for Broadlink IR device

## Installation
+ Manually connect for broadlink device to wifi
+ pip install broadlink
+ Download Broadlink Controller 
+　git clone https://github.com/mao2009/broadlink_ctl.git　　
+ Or download Zip and Unzip
   https://github.com/mao2009/broadlink_ctl/archive/v0.1.zip
  
  
 ## Using
 + Make a Device File    
      + Use -m or --make_device option, -d option is device file name
      + ex:) ./broadlink_ctl.py -m -d myroom
 + Learn a command IR data
      + Use -l or --learn option, -c option is command name
      + ex:) ./broadlink_ctl.py -l -d myroom -c light_on
      + Then send IR data to Broadlink device from your remote controller 
 + Send a coomand
      + Use -s or --send option 
      + ex:) ./broadlink_ctl.py -s -d myroom -c light_on
 
