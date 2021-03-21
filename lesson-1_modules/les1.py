from Les1_Module import traffic_lights, traffic_lights2

print('обычный светофор - 1\nбесконечный светофор - 2')
answ = int(input())
if answ == 1:
    traffic_lights()
elif answ == 2:
    traffic_lights2()
else:
    print('Пока')
  


