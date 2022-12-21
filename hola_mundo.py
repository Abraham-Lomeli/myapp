hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

mints = (mins + dura) % 60
aux = (mins + dura) // 60
hours = (hour + aux) % 24

print(hours, ":", mints)