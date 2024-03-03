class UserMainCode(object):
	@classmethod
	def maxmarks(cls, input1, input2):
		'''
		input1 : int
		input2 : int[]
		
		Expected return type : int
		'''
		
		sum = 0
		prev_mark=[]
		highest_mark = 0
		for question_num in range(input1):
			print("iteration", question_num)
			for distinct_check in prev_mark:
				print("distinct check", distinct_check)
				if input2[question_num] == distinct_check:
					print("check highest_mark", highest_mark)
					input2[question_num] = highest_mark + 1
					print("corrected highest mark", input2[question_num])
			print(input2[question_num], "is added to sum")
			sum += input2[question_num]
			prev_mark.append(input2[question_num])
			if input2[question_num] > highest_mark:
				highest_mark = input2[question_num]
				print("changed highest mark to", highest_mark)
			
		return sum
		
usm = UserMainCode()
max_marks = usm.maxmarks(5, [1,4,5,4,5])
print(max_marks)
