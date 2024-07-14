
class Solution:
	def majorityElement(self, nums: list[int]) -> int:
		reccurent = {}
		for number in nums:
			if number  not in reccurent.keys():
				reccurent[number] = 1
				continue
			reccurent[number] += 1
		return max(reccurent, key=reccurent.get)
	

if __name__ == "__main__":
	test_1 = [3,2,3]
	test_2 = [2,2,1,1,1,2,2]
	test_3 = [3,3,4]
	s = Solution()
	print('test 1 is :',s.majorityElement(test_1))
	print('test 2 is :',s.majorityElement(test_2))
	print('test 3 is :',s.majorityElement(test_3))

		