""" You want to check whether a web page loads within 3 seconds
(performance test condition).

load_time = 4.2
⚠️ Page load too slow: 4.2 seconds"""

load_time = 4.2

if load_time <= 3:
    print("Page load is good")
else:
    print("Page load too slow: 4.2 seconds")