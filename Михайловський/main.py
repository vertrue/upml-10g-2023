from function import calc

def main():
	def safe_cast(val,type,default=None):
		try:
			val = type(val)
		except Exception:
			print("Not integer!")
			return default
		return val
	n = safe_cast(input(),int)
	if not n:
		return
	a = [0]*n
	for i in range(n): # Ввід працює лише по одному елементу
		a[i] = safe_cast(input(),int)
		if not a[i]:
			return
	print(calc(n,a))
main()
