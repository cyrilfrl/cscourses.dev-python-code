import time

current_time = time.time()
local_time = time.localtime(current_time)

readable_time = time.asctime(local_time)
print(readable_time)

formatted_time