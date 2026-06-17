#1. Convert the time entered in hh,min and sec into seconds. 

#Input hours, minutes & seconds
hh = int(input('Enter hours:'))
mm = int(input('Enter minutes:'))
ss = int(input('Enter seconds:'))

#Converting time entered in hours, minutes & seconds into seconds
seconds = (hh * 3600) + (mm * 60) + ss 

#Display result
print('Total seconds =',seconds)