**🔁 Invert Dictionary**
**📘 Description**

This program reverses the keys and values of a given dictionary.
If the original dictionary maps keys to values, the new dictionary maps those values back to keys.

**🧠 Example**

Input:

{'a': 1, 'b': 2, 'c': 3}


Output:

{1: 'a', 2: 'b', 3: 'c'}

**⚙️ Working Logic**

Start with a dictionary (dct1) containing key–value pairs.

Create an empty dictionary new_dct to store the inverted pairs.

Loop through each key–value pair in the original dictionary.

Swap their positions — assign the value as the new key and the key as the new value.

Print the inverted dictionary.

**🚀 Features**

Simple and easy-to-understand logic.

Converts key–value mapping direction.

Works efficiently for small and medium dictionaries.

**⚠️ Note**

If multiple keys have the same value, the last one will overwrite the others in the inverted dictionary — since dictionary keys must be unique.

**🧰 Use Cases**

Useful in data transformations.

Helpful for understanding dictionary iteration.

Can be used when you need to reverse lookup key–value mappings.