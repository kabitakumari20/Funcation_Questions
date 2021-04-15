def drive_speed():
	if speed<=70:
		print("ok")
	else:
		speed1=(speed-70)//5
		if speed1>12:
			print("license suspend")
		else:
			print(speed1,"points")
speed=int(input("enter the speed="))
drive_speed()