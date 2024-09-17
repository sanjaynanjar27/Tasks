if __name__ == '__main__':
    total = 0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name,  *line = input().split()
        scores = list(map(float,  line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        total += i
    div = len(student_marks[query_name])
    print(format(total/div, '.2f'))



# Input  : 2
# Input  :sanjay 22 43 12
# Input  :karan 22 43 21
# Input  :sanjay
# Output :25.67