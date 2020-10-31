# write 1089
# ABC		953 
# CBA		359
# XYZ = (ABC - CBA)
# ZYX
# RIS = XYZ + ZYX
# 1089

BASE = 10
FIRSTDIGIT = BASE * BASE 

abc = int(raw_input())
lsd = abc % BASE
msd = abc / FIRSTDIGIT
middle = (abc - msd * FIRSTDIGIT) / BASE
reverse_abc = lsd * FIRSTDIGIT + middle * BASE + msd
#print(str(reverse_abc))
xyz = abc - reverse_abc
#print(str(xyz))
#re-doing the same manipulation on the new computed value xyz
lsd = xyz % BASE
msd = xyz / FIRSTDIGIT
middle = (xyz - msd * FIRSTDIGIT) / BASE
reverse_xyz = lsd * FIRSTDIGIT + middle * BASE + msd
#print(str(reverse_xyz))
ris = xyz + reverse_xyz

print(str(ris))