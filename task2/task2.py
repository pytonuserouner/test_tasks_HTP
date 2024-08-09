import math

cr = []
pnt = []
variants = ['Точка лежит на окружности', 'Точка внутри', 'Точка снаружи']


def point_scaner(cen_rad, points):
    """
    :param cen_rad: list
    :param points: list
    :return: list
    Приведение данных к удобному для работы виду: list
    """
    with open(cen_rad, 'r') as file1:
        for a in file1.readlines():
            cr.append(a.split())
    with open(points, 'r') as file2:
        for b in file2.readlines():
            pnt.append(b.split())


point_scaner('center_radius.txt', 'coord.txt')
print(cr, pnt)


def calculator(cr, points):
    """
    :param cr: list
    :param points: list
    :return: list
    Расчет координаты точки
    """
    shape = []
    for i in range(len(points)):
        hypotenuse = math.sqrt((int(points[i][0]) - int(cr[0][0])) ** 2 + (int(points[i][1]) - int(cr[0][1])) ** 2)
        if hypotenuse < int(*cr[1]):
            shape.append(f"{points[i]} {variants[1]}\n")
        elif hypotenuse == int(*cr[1]):
            shape.append(f"{points[i]} {variants[0]}\n")
        else:
            shape.append(f"{points[i]} {variants[2]}\n")
    return shape


print(*calculator(cr, pnt))

