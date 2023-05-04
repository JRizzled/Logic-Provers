

class foo:
	def __init__(self, fList = []) -> None:
		self.fooList = fList
	def __getitem__(self, index):
		return self.fooList[index]
	def __setitem__(self, index, shit):
		self.fooList[index] = shit
	def __len__(self):
		return len(self.fooList)


def main():
	bitch = foo([1,2,3,4])
	for i in bitch:
		print(i)
	print(len(bitch))



if __name__ == '__main__':
	main()