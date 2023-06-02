class feature_moblie:
    len = 0
    hen = 0
    thin = 0
    __imei_no = 932480912384032184
    __pin = 3948239147
    __password = 93490182734093281
phone = feature_moblie()

phone.len = 20
phone.hen = 6.5
phone.thin = 5

print(phone.len)
print(phone.thin)
print(phone.hen)


class smartphone(feature_moblie):
    touchscreen = 0
    camera = 0
    memory = 0
    __imei_no = 890928049812
    __pin = 958034950238
    __password = 84873

smartphone.touchscreen = 10
smartphone.camera = 5
smartphone.memory = 8

print(smartphone.len)
print(smartphone.thin)
print(smartphone.hen)

print(smartphone.touchscreen)
print(smartphone.camera)
print(smartphone.memory)