#!/bin/bash

#sudo salt 'discord-voice-prd-us-west343' cmd.run 'ls /home/deploy/rtc-worker'

#sudo salt 'discord-voice-prd-us-south*' test.ping
#sudo salt 'discord-voice-prd-us-south*' cmd.run 'ls /home/deploy/rtc-worker'
#sudo salt 'discord-voice-prd-us-south*' cmd.run 'md5sum /home/deploy/rtc-worker'

sudo salt 'discord-voice-prd-us-central*' cmd.run '/home/deploy/rtc-worker --version'
#sudo salt 'discord-voice-prd-hongkong*' cmd.run 'md5sum /home/deploy/rtc-worker'
#sudo salt 'discord-voice-prd-singapore*' cmd.run 'md5sum /home/deploy/rtc-worker'
#sudo salt 'discord-voice-prd-sydney*' cmd.run 'md5sum /home/deploy/rtc-worker'
#sudo salt -C 'G@video_test:true and discord-voice-prd-eu-central*' cmd.run 'md5sum /home/deploy/rtc-worker'

#sudo salt 'discord-voice-prd-brazil*' cmd.run 'ls /var/tmp/rtc_worker_dumps'
