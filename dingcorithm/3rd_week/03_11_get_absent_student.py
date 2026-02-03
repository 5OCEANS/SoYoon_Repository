all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # 1. 이중 반복문
    for student in all_array:
        if student not in present_array:
            return student
    else:
        return "결석한 학생이 없습니다."

    # 2. 정렬해서 이진탐색
    def binary_search(array, target):
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return True
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    present_array.sort()
    for student in all_array:
        if not binary_search(present_array, student):
            return student
    else:
        return "결석한 학생이 없습니다."

    # 3. Dictionary, Hash table
    #    all_array들을 돌면서, hash table의 키값에 해당 학생들을 등록합니다.
    #    present_students를 돌면서 hash table의 키값을 제거한다.
    #    그리고 나서 남아있는 hash table의 키값에 해당하는 학생이 결석한 학생이다.
    student_dict = {}
    for student in all_array:
        student_dict[student] = True

    for student in present_array:
        del student_dict[student]

    for key in student_dict.keys():
        return key


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))