m = float(input('Digite uma distância em metros: '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'A medida de {m}m corresponde a\n{km}km\n{hm}hm\n{dam:.1f}dam\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm')
