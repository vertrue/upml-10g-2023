def calc(n: int, a: list) -> int:
	summa = 0
	for i in range(n):
		if a[i] % 2:
			summa += a[i]
	return summa
