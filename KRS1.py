import os

os.system('xdg-open https://www.facebook.com/profile.php?id=100078180585996')
import os, platform, time, sys

try:

    import requests

except:

    os.system('pip install requests')

os.system('git pull --quiet 2>/dev/null')

bit = platform.architecture()[0]

if bit == '64bit':

    

    import JOK4R64

    

elif bit == '32bit':

    

    import JOK4R32

