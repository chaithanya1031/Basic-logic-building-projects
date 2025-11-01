**💼 Employee Salary Filter**
**📘 Description**

This Python program filters out employees who earn more than ₹50,000 from a salary dictionary.
It creates a new dictionary that only contains the top-paid employees.

**🧠 Example**

Input Data:

{
  'ramesh': 50000,
  'akshay': 45000,
  'revanth': 100000,
  'sreenu': 75000,
  'venu': 80000,
  'naresh': 40000
}


Output:

high paid employee are {'revanth': 100000, 'sreenu': 75000, 'venu': 80000}

**⚙️ Working Logic**

1. A dictionary employees stores employee names and their respective salaries.
2. An empty dictionary top_paid is created to store filtered results.
3. The program loops through each employee’s record:
4. If the salary is greater than ₹50,000, that record is added to top_paid.
5. Finally, it prints all employees who qualify as high-paid.

**🚀 Features**

1. Automatically filters employees based on salary condition.
2. Uses dictionary iteration and conditional logic.
3. Clean, readable, and beginner-friendly structure.

**🧰 Use Cases**

1. Can be used in HR tools or employee management systems.
2. Demonstrates dictionary filtering techniques.
3. Good practice for learning condition-based data extraction.