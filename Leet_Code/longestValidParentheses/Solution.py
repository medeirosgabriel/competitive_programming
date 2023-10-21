class Solution(object):
	def longestValidParentheses(self, s):
		if len(s) <= 1:
			return 0
		stack = [-1]
		max_ = 0
		for i in range(len(s)):
			if s[i] == '(':
				stack.append(i)
			elif s[i] == ')':
				if stack[-1] != -1 and s[stack[-1]] == '(':
					stack.pop()
					max_ = max(i - stack[-1], max_)
				else:
					stack.append(i)
		return max_
				
