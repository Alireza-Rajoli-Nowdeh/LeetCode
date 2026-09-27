# this question teaches what queues are/ stack if LIFo but queues are FIFO
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count = 0
        while count != len(students):
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                popped= students.pop(0)
                students.append(popped)
                count +=1
        ans = len(students)
        return ans

        
