sec = input("Enter Seconds: ")
if sec.isdigit():
        sec = int(sec)
        day = 86400
        minute = 60
        hour = 3600
        vdays = sec//day
        vhours = (sec - vdays*day)//hour
        vminutes = (sec - vdays*day - vhours*hour)//minute
        vsecond = sec - vdays*day - vhours*hour - vminutes*minute
        print("Days:", vdays, "Hours:", vhours, "Minutes:", vminutes, "Seconds:", vsecond)
        #code part 1
        result1 = ((vdays+vminutes)*vhours%42)+10
        #code part 2
        result2 = (((sec//(vminutes+vsecond+1))*(1+vdays))%50)+25
        print("The vault code is", result1, "-", result2)
else:
    print("Error")