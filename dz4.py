class Student:
    def __init__(self, free_time, name, age):
        self.free_time = free_time
        self.name = name
        self.age = age

    def speak(self):
        return "I am a student."

    def status(self):
        return (f"{self.name} is a student, "
                f"he/she is {self.age} years old. "
                f"There is not much free time, only {self.free_time} hours.")


class John(Student):
    def __init__(self, free_time, age, hobby):
        super().__init__(free_time, "John", age)
        self.hobby = hobby

    def status(self):
        return super().status() + f" Hobby: {self.hobby}."


class Alice(Student):
    def __init__(self, free_time, age, hobby):
        super().__init__(free_time, "Alice", age)
        self.hobby = hobby

    def status(self):
        return super().status() + f" Hobby: {self.hobby}."


class People:
    def __init__(self, name, age, free_time, hobby, mood):
        if mood.lower() == 'angry':
            self.person = John(free_time, age, hobby)
        elif mood.lower() == 'happy':
            self.person = Alice(free_time, age, hobby)

    def learn(self):
        return f"{self.person.name} is learning."

    def speak(self):
        return self.person.speak()

    def status(self):
        return self.person.status()


student_john = People(name="John", age=18, free_time=2, mood='angry', hobby='skiing')
print(student_john.speak())
print(student_john.status())
print(student_john.learn())

print()

student_alice = People(name="Alice", age=19, free_time=3, mood='happy', hobby='Cooking')
print(student_alice.speak())
print(student_alice.status())
print(student_alice.learn())






