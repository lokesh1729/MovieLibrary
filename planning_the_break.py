import webbrowser,time;
count=3;
while(count>0):
    print("The current time is"+time.ctime());
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=FRTUZZ-djxQ");
    count=count-1;
