def main():
    dd, mm, aa = input().split("/")
    dd = int(dd)
    mm = int(mm)
    aa = int(aa)

    soma = dd+mm+aa

    if soma % 2 == 0:
        print('par')
    else:
        print('impar')

main()
