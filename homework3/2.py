from datetime import datetime

def user_online(file_name):
    with open(file_name,'r') as file:
        for line in file:
            parts = line.strip().split(',')
            username = parts[0].strip()  
            log_on_time = parts[1].strip()  
            log_off_time = parts[2].strip() 

            fmt = '%H:%M'
            log_on = datetime.strptime(log_on_time, fmt)
            log_off = datetime.strptime(log_off_time, fmt) 


            time_online = (log_off - log_on).total_seconds() / 3600 
            
            if time_online >= 1:
                print(f"{username} was online at leats one hour")

file_name = "logfile.txt"

res = user_online(file_name)

print(res)