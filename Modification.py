shopping = {
    'piekarnia': ['chleb', 'pączek', 'bułki', 'ciastko'],
    'warzywniak': ['marchew', 'seler', 'rukola'],
    'drogeria': ['szampon', 'krem do rąk'],
    'monopolowy': ['whisky', 'cognac', 'champagne']
}

for shopname in shopping.keys():
    new_shopname = shopname.capitalize()
    shopping[new_shopname] = shopping.pop(shopname)

for shop, prod_list in shopping.items():
    new_prod_list = [prod.capitalize() for i, prod in enumerate(prod_list)]
    shopping[shop] = new_prod_list

print('\nLista zakupów')
q = []
for shop, prod_list in shopping.items():
    print('Idę do', shop, end = ', ')
    print('kupuję tu następujące rzeczy:', prod_list, end = '.\n')
    q.append(len(prod_list))
print('W sumie kupuję', sum(q), 'produktów.\n')
