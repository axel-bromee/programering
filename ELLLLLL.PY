from datetime import datetime
def count_kost():
    date_format = "%d/%m/%Y"

    date1 = input("date1(day/month/year):")
    date2 = input("date2(day/month/year):")

    matarinstelning1 = int(input("meternumber1 in kwh:"))
    matarinstelning2 = int(input("meternumber2 in kwh:"))

    kostnad = int(input("kost:"))

    avgift = int(input("charge:"))

    date1 = datetime.strptime(date1, date_format)
    date2 = datetime.strptime(date2, date_format)

    moms = 1.25
    matardiff = matarinstelning2 - matarinstelning1


    diff = (date2 - date1).days



    total = ((diff * avgift) + (matardiff * kostnad)) * moms

    print ("total kost",total/100,"kr")


count_kost()