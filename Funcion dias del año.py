def isYearLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True

    elif year % 100 == 0 and year % 400 == 0:
        return True

    else:
        return False


def daysInMonth(year, month):
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) and month == 2:
        return 29
    else:
        return meses[month - 1]


def dayOfYear(year, month, day):
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    dias = 0
    for i in range(month - 1):
        dias += meses[i]
    if isYearLeap(year) and month >= 2:
        dias += 1
    dias += day

    return dias


dia = int(input("ingrese dia: "))
mes = int(input("ingrese el mes: "))
ano = int(input("ingrese el año: "))
print(dayOfYear(ano, mes, dia))
