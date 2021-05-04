sandwich_order = ['americano','tuna','cheese','eggs']
sandwich_ready = []
while len(sandwich_order) != 0:
    sandwich = sandwich_order[0]
    print(f'{sandwich} is ready!')
    sandwich_ready.append(sandwich)
    sandwich_order.remove(sandwich)

print(sandwich_ready)
