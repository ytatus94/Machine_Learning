def main():
	Q1_quarter_transformation()
	Q2_arbitrary_shopping()
	Q3_students_and_department()
	Q4_two_circles()

def Q1_quarter_transformation():

	def calendar_map(date_string):
		calendar_list = []

		for date in date_string:
			year = date.split('-')[0]
			month = date.split('-')[1]
			calendar = year
			if int(month) in [1, 2, 3]:
				calendar += 'Q1'
			elif int(month) in [4, 5, 6]:
				calendar += 'Q2'
			elif int(month) in [7, 8, 9]:
				calendar += 'Q3'
			elif int(month) in [10, 11, 12]:
				calendar += 'Q4'
			calendar_list.append(calendar)

		return calendar_list

	print(calendar_map(['2014-03-25', '2012-08-05', '2015-05-19']))

def Q2_arbitrary_shopping():

	def getMaximumOutfits(prices, money):
		result = 0
		for i in range(len(prices)):
			count = 0
			sum = 0
			for j in range(i, len(prices)):
				sum += prices[j]
				if sum > money:
					break
				count += 1
			result = max(result, count)
		return result

	print(getMaximumOutfits([10, 10, 10], 5))
	print(getMaximumOutfits([5, 10, 10], 5))
	print(getMaximumOutfits([1, 2, 2, 3, 1, 1, 5, 2], 10))

def Q3_students_and_department():
	sql_query = '''
		SELECT D.DEPT_NAME, COUNT(DISTINCT S.STUDENT_ID)
		FROM Departments AS D
		LEFT JOIN Students AS S
		ON S.DEPT_ID = D.DEPT_ID
		GROUP BY D.DEPT_NAME
		ORDER BY 2 DESC, 1
	'''
	print(sql_query)

def Q4_two_circles():

	def two_circles_relations(infos):
		results = []
		for info in infos:
			XA, YA, RA = info[0], info[1], info[2]
			XB, YB, RB = info[3], info[4], info[5]
			if XA == 0 and XB == 0:
				results.append(relations(YA, YB, RA, RB))
			if YA == 0 and YB == 0:
				results.append(relations(XA, XB, RA, RB))
		return results

	def relations(d1, d2, r1, r2):
		if d1 == d2:
			return 'Concentric'
		elif abs(d1 - d2) > r1 + r2:
			return 'Disjoint-Outside'
		elif abs(d1 - d2) == r1 + r2:
			return 'Touching'
		elif abs(d1 - d2) + min(r1, r2) == max(r1, r2):
			return 'Touching'
		elif abs(d1 - d2) < r1 + r2:
			return 'Intersection'
		elif abs(d1 - d2) < max(r1, r2):
			return 'Disjoint-Inside'

	infos1 = [[12, 0, 21, 14, 0, 23],
	          [0, 45, 8, 0, 94, 9],
	          [35, 0, 13, 10, 0, 38],
	          [0, 26, 8, 0, 9, 25]]
	infos2 = [[0, 5, 9, 0, 9, 7],
	          [0, 15, 11, 0, 20, 16],
	          [26, 0, 10, 39, 0, 23],
	          [37, 0, 5, 30, 0, 11],
	          [41, 0, 0, 28, 0, 13]]

	print(two_circles_relations(infos1))
	print(two_circles_relations(infos2))


if __name__ == '__main__':
	main()