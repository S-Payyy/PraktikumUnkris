# Latihan konversi satuan temperatur
# Program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam celcius :'))
print("suhu adalah ",celcius,"C")

#reamur
reamur = (4/5)*celcius
print('suhu reamur adalah',reamur,"R")

#farenheit
farenheit = ((9/5)*celcius)+32
print("suhu dalam farenheit adalah",farenheit,"F")

#Kelvin
kelvin = celcius +273
print("suhu dalam kelvin adalah",kelvin,"K")


