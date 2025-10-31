**🎓 Student Marks and Topper Finder**
**📘 Description**

This program uses a nested dictionary to store student names and their subject marks.
It calculates each student's average marks and identifies any student who has scored 90 or above in any subject.

**🧠 Example**

Data:

{
    'John': {'math': 80, 'science': 75},
    'Alice': {'math': 90, 'science': 82},
    'Bob': {'math': 70, 'science': 65}
}


Output:

Alice is topper has scored 90 in math
Student John has average 38.75
Student Alice has average 42.25
Student Bob has average 33.75


(Note: The averages depend on the formula logic used.)

**⚙️ Working Logic**

The program defines a nested dictionary where:

Each key is a student's name.

Each value is another dictionary of subjects and marks.

It loops through each student and then through their subjects and marks.

Calculates the average marks of each student.

Checks if any mark is greater than or equal to 90, and prints that student as a topper.

Finally, it prints the average marks of each student.

**🚀 Features**

Demonstrates how to work with nested dictionaries.

Identifies subject-wise toppers automatically.

Calculates individual student averages.

Clear and structured logic for beginners.

**🧰 Use Cases**

Useful for student management systems.

Helps understand nested loops with dictionaries.

Great example of applying logic to structured data.