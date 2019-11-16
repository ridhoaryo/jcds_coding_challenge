import xlsxwriter

file = xlsxwriter.Workbook('file.xlsx')
sheet1 = file.add_worksheet('sheet 1')
sheet2 = file.add_worksheet('sheet 2')
sheet3 = file.add_worksheet('sheet 3')
sheet4 = file.add_worksheet('sheet 4')

n = 1
for r in range(3):
    for c in range(3):
        sheet1.write(r,c,n)
        n +=1

n2 = 1
for r in range(3):
    for c in range(3):
        sheet2.write(r,c,n2)
        n2 +=3
    n2 -= 8


n3 = 3
for r in range(3):
    for c in range(3):
        sheet3.write(r,c,n3)
        n3 -=1
    n3+=6

n4 = 9
for r in range(3):
    for c in range(3):
        sheet4.write(r,c,n4)
        n4 -=3
    n4+=8

file.close()


