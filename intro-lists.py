# courses = ['History', 'Math', 'Physics']
# courses2 = ['Art', 'Education']

# courses.extend(courses2)

# print(courses)

# courses = ['History', 'Math', 'Physics']

# popped = courses.pop()

# print(popped)
# print(courses)

# courses = ['History', 'Math', 'Physics']

# nums = [1, 5, 2, 433, 4]

# nums.sort()

# courses.sort()

# print(courses)
# print(nums)

# courses = ['History', 'Math', 'Physics']


# for index, course in enumerate(courses, start = 1):
#   print(index, course)

# courses = ['History', 'Math', 'Physics']

# course_str = ' - '.join(courses)

# print(course_str)

# cs_courses = {'History', 'Math', 'Physics', 'Math'}
# art_courses = {'History', 'Art', 'Physics', 'Design'}

# print(cs_courses.union(art_courses))

student = {'name': 'John', 'age':24, 'courses':['Math', 'CompSci']}

# student['phone'] = '555-5555'

# student.update({'name': 'Bill'})

# print(student)

for key, value in student.items():
  print(key, value)