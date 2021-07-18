
from datetime import date, timedelta
from calendar import SATURDAY

print("Input dates ")
#start_date = '20180728'
#end_date = '20180927'

start_date = str(input("Start date : "))
end_date = str(input("End date : "))

start_y, start_m, start_d = int(start_date[:4]), int(start_date[4:6]), int(start_date[6:])

end_y, end_m, end_d = int(end_date[:4]), int(end_date[4:6]), int(end_date[6:])

if start_y >= 1900 and end_y <= 2100:
	sdate = date(start_y, start_m, start_d)
	edate = date(end_y, end_m, end_d)
	
	delta = edate - sdate # time delta
	#print("delta : ", delta)
	#print("delta days :", delta.days)  # 61
	
	for i in range(delta.days + 1):
		#print("time delta : ", timedelta(days=i))

		current_day = sdate + timedelta(days=i)
		#print("current date : ", current_day)
		
		if current_day.weekday() == SATURDAY:
			sat_days = current_day.day
			#print("sat days:",sat_days)
			if (sat_days in range(22, 28+1)):
				if (sat_days % 5 != 0) :
					#print("------------- if -------------------")
					#print("sat_days if :", sat_days)
					if (current_day.month < 10):
						month = "0"+str(current_day.month)
						
					else:
						month = str(current_day.month)
						
					if (current_day.day < 10):
						day = "0"+str(current_day.day)
						
					else:
						day = str(current_day.day)
								
					#print("4 th sat day", current_day.day)
					print(str(current_day.year)+ month + day)
				
			elif (sat_days % 5 == 0) :
				#print("--------------------------------")
				#print("sat_days if :", sat_days)
				if (current_day.month < 10):
					month = "0"+str(current_day.month)
				else:
					month = str(current_day.month)
					
				if (current_day.day < 10):
					day = "0"+str(current_day.day)
					
				else:
					day = str(current_day.day)
							
				#print("4 th sat day", current_day.day)
				print(str(current_day.year)+ month + day)
				



