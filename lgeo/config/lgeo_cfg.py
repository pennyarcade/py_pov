"""
Configuration for Lgeo Library parts.

@Todo: Put some information here that makes sense
"""

LG_QUALITY = 4
# compatible to L3Ps L3Quality for these values supported
# 2: normal studs
# 3: solid studs have logo
# 4: solid and hollow stud have logo

LG_TEST = 0
# For internal use
# 0: correct hollow studs
# 1: hollow studs are scaled to 1/10 in height to check for logo orientation

# LG_STUDS = 1
# compatible to L3Ps L3Studs
# 0: no studs and bottom cylinders for preview renderings
# 1: objects have studs.
#
# 20080720: Most parts do not evaluate this flag by now.

LG_STUD_LOGO = 0
# stud logo letters
# 0: display LEGO
# 1: display LGEO
