ves,rost=map(float, input("Введите вес (кг) и рост (м) через пробел: ").split())

imt=ves/(rost*rost)

print(f"Индекса Массы Тела:{imt:.1f}")
