start = 9
end = 16
modifstart = 10
modifend = 15
if modifstart <= start <= end <= modifend:
    print(f'{start} から　{end} は改装期間中です')
elif start <=modifstart <= end <= modifend:
    print(f'{modifstart} から　{end} は改装期間中です')
elif start <=modifstart <= modifend <= end:
    print(f'{modifstart} から　{modifend} は改装期間中です')
elif modifstart <= start <= modifend <= end:
    print(f'{start} から　{modifend} は改装期間中です')
