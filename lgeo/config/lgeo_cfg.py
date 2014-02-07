'''
    Configuration for Lgeo Library parts
'''

lg_quality = 2
# compatible to L3Ps L3Quality for these values supported
# 2: normal studs
# 3: solid studs have logo
# 4: solid and hollow stud have logo

lg_test = 0
# For internal use
# 0: correct hollow studs
# 1: hollow studs are scaled to 1/10 in height to check for logo orientation

lg_studs = 1
# compatible to L3Ps L3Studs
# 0: no studs and bottom cylinders for preview renderings
# 1: objects have studs.
#
# 20080720: Most parts do not evaluate this flag by now.

lg_stud_logo = 0
# stud logo letters
# 0: display LEGO
# 1: display LGEO
