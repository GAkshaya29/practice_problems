hour=int(input())
minute=int(input())
hour_angle=((hour)+(minute)/60)*30
minute_angle=minute*6
diff=abs(hour_angle-minute_angle)
if(diff>180):
    print(360-diff)
print(diff)