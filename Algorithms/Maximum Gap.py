class Solution:
	def maximumGap(self, num):
		n=len(num)
		if n<2:
		    return 0
		smalllarge=self.getMaxMin(num)
		small=smalllarge[0]
		large=smalllarge[1]
		dist=(large-small)/(float)(n-1)
		buckets=[[]for i in range(n-1)]
		for i in range(n):
			if num[i]!=large:
				index=(int)((num[i]-small)/dist)
				buckets[index].append(num[i])
		array=[]
		for i in range(n-1):
		    if len(buckets[i])>0:
				pair=self.getMaxMin(buckets[i])
				array.append(pair[0])
				array.append(pair[1])
		r=-1
		for i in range(len(array)-1):
			a=(array[i+1]-array[i])
			if r<a:
				r=a
		r=max(r,large-array[-1])
		return r

	def getMaxMin(self, num):
		n=len(num)
		if n==0:
			return None
		array=[]
		small=9223372036854775807
		large=-small-1
		for i in range(n):
			if num[i]<=small:
				small=num[i]
			if num[i]>=large:
				large=num[i]
		array.append(small)
		array.append(large)
		return array