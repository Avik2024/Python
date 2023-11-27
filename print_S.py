# Python program to print alphabet pattern S or 5


#        ********
#	 *
#	 *
#	 *
#	 ********
#		*
#		*
#		*
#	 ********

def print_pattern(n):
	for row in range(n):
		for column in range(n):
			if(
			
				#FIRST ROW
				(row == 0)or
				#FIRST COLUMN
				(column == 0 and row < n // 2)or
				#MIDDLE ROW
				(row == n // 2)or
				#LAST COLUMN
				(column == n-1 and row >= n //2)or
				#LAST ROW
				(row==n-1)
			
			):
				print("*", end=" ")
			else:
				print(" ", end=" ")
		print()
			
size = int(input("Enter any size :\t"))
if size < 8:
	print("Enter a size minimum of 8")
else:
	print_pattern(size)
	
					
			
