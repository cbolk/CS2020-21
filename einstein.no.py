


BASE = 10
FIRSTDIGIT = BASE * BASE

abc = int(raw_input())
if abc <= 0:
	print("input not strictly positive")
else:
	lsd = abc % BASE
	msd = abc / FIRSTDIGIT
	diff = lsd - msd
	if diff < 0:
		diff = -diff
	if diff <= 2:
		print("input not compliant")
	else:
		middle = (abc - msd * FIRSTDIGIT) / BASE
		reverse_abc = lsd * FIRSTDIGIT + middle * BASE + msd
		xyz = abc - reverse_abc
		if xyz < 0:
			xyz = -xyz
		lsd = xyz % BASE
		msd = xyz / FIRSTDIGIT
		middle = (xyz - msd * FIRSTDIGIT) / BASE
		reverse_xyz = lsd * FIRSTDIGIT + middle * BASE + msd
		ris = xyz + reverse_xyz
		print(str(ris))
		