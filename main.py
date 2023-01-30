import pymatrices as pm

M1 = pm.matrix([[1, 2, 1], [4, 5, 6], [7, 8, 9]])
M2 = pm.matrix([[-5, 2], [-9, 6]])
M3 = pm.I(3)

print("M1:\n", M1, sep="")
print("M2:\n", M2, sep="")
print("M3:\n", M3, sep="")

M1[0][0] = 2
print("После изменения значения M1:\n", M1, sep="")

print(f"Матрица в форме списка: {M1.asList()}")

print("Транспонировать M1:\n", M1.transpose, sep="")
print("Транспонировать M1 M2:\n", M2.transpose, sep="")
print("Транспонировать M1 M3:\n", M3.transpose, sep="")

print("M1+M3:\n", M1+M3, sep="")
print("M1-M3:\n", M1-M3, sep="")

print("M1*M3:\n", M1*M3, sep="")
print("M1*3:\n", M3*3, sep="")

print("\nПервичные диагональные значения M1 :", M1.primaryDiagonal)
print("Первичные диагональные значения M2 :", M2.primaryDiagonal)

print("\nВторичные диагональные значения M1 :", M1.secondaryDiagonal)
print("Вторичные диагональные значения M2 :", M2.secondaryDiagonal)

print("\nM1[1][1]:", M1.valueAt(1, 1))
print("M1[1][2]:", M1.valueAt(1, 2))

print("\nМладший из 1 в M1:\n", M1.minorOfValueAt(1, 1), sep="")
print("Младший из  2 в M1:\n", M1.minorOfValueAt(2, 2), sep="")

print("Индекс 1 в M1:", M1.position(1))
print("Индекс 8 в M1:", M1.position(8))

print("\nadj M1:\n", pm.adjoint(M1), sep="")
print("adj M2:\n", pm.adjoint(M2), sep="")

print("Матрица, созданная путем заполнения определенного значения:\n", pm.createByFilling(2, (2, 3)), sep="")

print("Пример матрицы столбцов:\n", pm.createColumnMatrix([2,3,4,5]), sep="")

print("Пример матрицы строк:\n", pm.createRowMatrix([2,3,4,5]), sep="")

print("|M1|:", pm.determinant(M1))
print("|M2|:", pm.determinant(M2))

print("\nСобственные значения M1:", pm.eigenvalues(M1))
print("\nСоответствующие собственные векторы M1:-")
for _ in pm.eigenvectors(M1):
	print(_)

print("Собственные значения M2 :", pm.eigenvalues(M2))
print("\nСоответствующие собственные векторы M2:-")
for _ in pm.eigenvectors(M2):
	print(_)

print("Инверсия of M1:\n", pm.inverse(M1), sep="")
print("Инверсия of M2:\n", pm.inverse(M2), sep="")

print("Матрица идентичности 3x3:\n", pm.I(3), sep="")
print("Нулевая матрица 3x3:\n", pm.O(3), sep="")

print("Является ли M1 диагональной матрицей?", pm.isDiagonal(M1), sep="")
print("Является ли M1 матрицей идентичности?", pm.isIdentity(M1), sep="")

print("\nЯвляется ли M1 идемпотентной матрицей? ", pm.isIdempotent(M1), sep="")
print("Является ли матрица идентичностей 3x3 идемпотентной матрицей? ", pm.isIdempotent(pm.I(3)), sep="")

print("\nЯвляется ли M1 инволютивной матрицей? ", pm.isInvolutory(M1), sep="")
print("Является ли матрица идентичности 3x3 инволютивной матрицей? ", pm.isInvolutory(pm.I(3)), sep="")

print("\nЯвляется ли M1 нильпотентной матрицей? ", pm.isNilpotent(M1), sep="")

print("\nЯвляется ли M1 нулевой матрицей? ", pm.isNull(M1), sep="")
print("Является ли нулевая матрица 3x3 нулевой матрицей ? ", pm.isNull(pm.O(3)), sep="")

print("\nЯвляется ли M1 скалярной матрицей? ", pm.isScalar(M1), sep="")
print("Является ли M1 сингулярной матрицей? ", pm.isSingular(M1), sep="")
print("Является ли M1 квадратной матрицей? ", pm.isSquare(M1), sep="")
print("Является ли M1 симметричной матрицей? ", pm.isSymmetric(M1), sep="")
print("Является ли M1 кососимметричной матрицей? ", pm.isSkewSymmetric(M1), sep="")