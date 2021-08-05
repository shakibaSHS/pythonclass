
adad1 = int(input("adad1\n"))
adad2 = int(input("adad2\n"))
print('agar taghsim mikhahi vared kon: taghsim\n' )
print('agar taghsim mikhahi vared kon: zarb\n' )
amalgar = input("amalgar\n")
temp = 0
if amalgar == 'zarb':
    temp = adad1*adad2
    print(temp)
elif amalgar == 'taghsim':
    temp = adad1/adad2
    print(temp)
else:
    print('balad nistam')
