alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
sea_are_sum = black_sea_area + azov_sea_area
print('The area of the Black and Azov seas is: ' + str(sea_are_sum))


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_goods = 375291
first_and_second_warehouse = 250449
second_and_third_warehouse = 222950
first_warehouse = all_goods - second_and_third_warehouse
second_warehouse = first_and_second_warehouse - first_warehouse
third_warehouse = all_goods - first_and_second_warehouse
print('Number of goods in warehouses: \n'
      '1st warehouse - ' + str(first_warehouse), '\n'
      '2nd warehouse - ' + str(second_warehouse), '\n'
      '3rd warehouse - ' + str(third_warehouse))


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
credit_years = 1.5
monthly_payment = 1179
credit_months = int(credit_years * 12)
pc_price = credit_months * monthly_payment
print('The price of the PC is: ' + str(pc_price) + ' UAH')


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
num1 = (8019, 9907, 2789, 7248 , 7128, 19224)
num2 = (8, 9, 5, 6, 5, 9)
a = num1[0] % num2[0]
b = num1[1] % num2[1]
c = num1[2] % num2[2]
d = num1[3] % num2[3]
e = num1[4] % num2[4]
f = num1[5] % num2[5]
print('Remainder of dividing: ' +  '\n'
      'a b c d e f')
print (a, b, c, d, e, f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_count = 4
medium_pizza_count = 2
juice_count = 4
cake_count = 1
water_count = 3

big_pizza_price = 274
medium_pizza_price = 218
juice_price = 35
cake_price = 350
water_price = 21

total_price = ((big_pizza_count * big_pizza_price) + (medium_pizza_count * medium_pizza_price)
               + (juice_count * juice_price) + (cake_count * cake_price) + (water_count * water_price))
print('Total price is: ' + str(total_price) + ' UAH')


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
photos_per_page = 8
pages = all_photos // 8
print('Pages with photos: ' + str(pages))


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
fuel_consumption = 9 / 100
tank_volume = 48
distance = 1600
fuel = int(distance * fuel_consumption)
refueling = fuel // tank_volume
print('Fuel required: ' + str(fuel) + '\n'
      'Refills quantity: ' + str(refueling))
