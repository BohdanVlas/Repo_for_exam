import exam_modules as mdl

print("Вітаємо")
while True:
    sum = int(input("Введіть суму кредиту: "))
    if sum < 0:
        raise(ValueError)
    month = int(input("Термін: "))
    vids = int(input("Ставка: "))
    print(mdl.vidssum(sum, vids, month))