#Python program to print alphabet pattern Q




#      -*********-
#      *	 *
#      *	 *
#      *	 *
#      *	 *
#      -*********-
#	       *
#		 *
				
		 
def print_pattern(n):
	for row in range(n):
		for column in range(n):
			if(
			
				#First Row
				(row == 0 and column != 0 and column != n-1)or
				#First column
				(column == 0 and row != 0 and row == n // 2)or
				#End Row
				(row == n-1 and column != 0 and column != n-1)or
				#End Column
				(column == n-1 and row != 0 and row == n // 2)or
				#Q tail
				(row == column and row >= n-1)
			
			):
				print("*", end=" ")
			else:
				print(" ", end=" ")
			print()
size = int(input("Enter any size: \t"))
	
if size < 8:
	print("Enter a size minimum of 8")
else:
		print_pattern(size)				
					








































		 
