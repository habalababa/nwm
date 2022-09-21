def s():
    import time
    time.sleep(0.00001)

a = 1000
while a > 1:
    a -= 1
    s()
    print("yo")
    if a == 999:
        import os

        print("chuj ci w dupeeeee")
        os.system("wir.py")