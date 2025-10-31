**🧮 Dictionary Merge and Sum**
**📘 Description**

This program merges two dictionaries and adds the values of matching keys.
If a key appears in both dictionaries, their values are summed.
If a key appears only once, it’s directly carried into the final result.

**🧠 Example**

Input:

dict1 = {'a': 10, 'b': 20, 'c': 30}

dict2 = {'b': 5, 'c': 15, 'd': 25}

Output:
{'a': 10, 'b': 25, 'c': 45, 'd': 25}

**⚙️ Working Logic**

The program first copies all key–value pairs from the first dictionary.

Then it loops through the second dictionary:

If a key already exists in the output, it adds the values.

If not, it adds the new key–value pair as is.

The final dictionary contains all unique keys with their summed values.

**🚀 Features**

Combines data from two dictionaries efficiently.

Automatically sums values for overlapping keys.

Works with any numeric data type.

Produces a single clean, merged output.

**🧰 Use Cases**

Summing sales data from two departments.

Combining stock inventories.

Merging statistical or financial reports.