class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count how many students who prefer 0 or 1
        # Check if all student doesn't 
        student0, student1 = 0, 0

        for s in students:
            if s == 0:
                student0 += 1
            else:
                student1 += 1


        while student0 > 0 and student1 > 0:
            student = students.pop(0)
            if sandwiches[0] != student:
                students.append(student)
            else:
                if student == 0:
                    student0 -= 1
                else:
                    student1 -= 1
                sandwiches.pop(0)

        if student0 == 0:
            while sandwiches and sandwiches[0] == 1 and student1 > 0:
                student1 -= 1
                sandwiches.pop(0)
            return student1
        
        if student1 == 0:
            while sandwiches and sandwiches[0] == 0 and student0 > 0:
                student0 -= 1
                sandwiches.pop(0)
            return student0

        