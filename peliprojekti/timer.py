def timer(s):
    import time
    for aika in range(s, 0, -1):
        print(aika)
        time.sleep(1)
    print("Aika loppui!")

timer(5)