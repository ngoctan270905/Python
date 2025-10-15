# COMMENTS TRONG PYTHON
# Comment 1 dong : dung day #
# Comment nhieu dong : dung dau ''' va ket thuc bang ''' hoac """ va ket thuc bang """

# Vi du comment 1 dong
print("Day la comment 1 dong")

# Vi du comment nhieu dong
'''
Day la comment nhieu dong 
Day la comment nhieu dong
Day la comment nhieu dong
'''
print("Day la comment nhieu dong")

# DOCSTRING TRONG PYTHON
# Docstring la chuoi mo ta ham, lop hoac module
# Docstring duoc viet trong dau ''' va ket thuc bang ''' hoac """ va ket thuc bang """

def my_function():
  ''' Day la docstring mo ta cua ham my_function '''
  print("Hien thi ham my function")
help(my_function) # Ham help se in ra docstring cua ham my_function
my_function() # Hien thi ham my function

