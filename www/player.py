import os
import sys
from lib.streamer import streamer

p = streamer(sys.argv[1],sys.argv[2],sys.argv[3])
p.playMedia()



