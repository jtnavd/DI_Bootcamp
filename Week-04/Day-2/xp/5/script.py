  basket = ["Banana", "Apples", "Oranges", "Blueberries"]
    print('basket : ', basket)
    basket.remove('Banana')
    print('basket after removing "Banana" : ', basket)
    basket.remove('Blueberries')
    print('basket after removing "Blueberries" : ', basket)
    basket.append('Kiwi')
    print('basket after adding "Kiwi" : ', basket)
    basket.insert(0, 'Apples')
    print('basket after adding "Apples" at the beginning : ', basket)
    count = 0
    for item in basket:
        if item == 'Apples':
            count += 1
    print('Number of apples in basket : ', count)
    basket = []
    print('basket : ', basket)