
"""
Script to get a platform-identifier
"""

import platform, math, sys, string

intbitlen = int(round(math.log(sys.maxint,2))+1)

print str.lower(platform.system()) + str(intbitlen)
