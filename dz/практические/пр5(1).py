nalog=0.13

d=float(input("Введите свой годовой доход:"))

summ_n=d*nalog
summ_d=d-summ_n

print(f"Общая сумма дохода:{d:.2f}")
print(f"Сумма рассчитанного налога:{summ_n:.2f}")
print(f"Сумма «на руки» после вычета налога:{summ_d:.2f}")