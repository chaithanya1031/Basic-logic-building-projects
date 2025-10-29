**🔍 Key Existence Checker in Dictionary**
**📘 Description**

This Python program checks whether a specific key exists in a dictionary.
It helps verify the presence of a key before performing operations like updates or lookups.

**🧠 Example**

Input:

check whether key is existed or not: age


Output:

key existed


If you enter a non-existing key, for example:

check whether key is existed or not: city


Output:

key not existed

**⚙️ Working Logic**

A dictionary (dct) stores predefined key–value pairs.

The program asks the user to enter a key.

It checks if the entered key is present in the dictionary using:

if rand_key in dct.keys():


If the key exists, it prints “key existed”, otherwise “key not existed.”

**🚀 Features**

Checks key existence safely without raising errors.

Works with any data type of dictionary keys.

Simple and efficient for quick dictionary lookups.

**🧰 Use Cases**

Validating input keys before accessing dictionary values.

Preventing KeyError during runtime.

Useful in data validation and dictionary-based configurations.