student_names = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8',
                 'student9', 'student10']
marks = [45, 78, 12, 14, 48, 43, 47, 98, 35, 80]


def display_dash_board(student_names, marks):
    data_base = dict(zip(student_names,
                         marks)) 
    # sorting the dictionary data_base wrt the marks in Ascending order
    sorted_data_base = sorted(data_base.items(), key=lambda kv_pair: kv_pair[1])
    least5_students = sorted_data_base[:5]
    print("The list printed sorting by marks in descending order: ")
    # print(sorted(data_base.items(), key=lambda kv_pair: kv_pair[1], reverse=True))
    sorted_data_base1 = sorted(data_base.items(), key=lambda kv_pair: kv_pair[1], reverse=True)
    top5_students = sorted_data_base1[:5]

    for k, v in sorted_data_base:  
        percentile25 = v > 25
        percentile75 = v < 75
        if (percentile25) and (percentile75):
            print(k, v)
    print()
    for k, v in top5_students:  
        print(k, v)
    print()
    for k, v in least5_students:
        print(k, v)
    return top5_students, least5_students


top5_students, least5_students = display_dash_board(student_names, marks)
