<div align="center">

# 📏 Unit Converter

![Python](https://img.shields.io/badge/Python-3.x-00ff41?style=for-the-badge&logo=python&logoColor=00ff41&labelColor=0d1117)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-00ff41?style=for-the-badge&labelColor=0d1117)
![Status](https://img.shields.io/badge/Status-Complete-00ff41?style=for-the-badge&labelColor=0d1117)

> **Project #4 — Convert anything. KM, KG, Celsius. Instantly. 🖤**

</div>

---

## 💡 What It Does

```
Pick what you want to convert:
1. KM → Miles
2. KG → Pounds  
3. Celsius → Fahrenheit
Enter the value → Get result instantly!
```

---

## 🎮 Demo

```bash
WELCOME TO UNIT CONVERTER! 🔥
1. KM to Miles
2. KG to Pounds
3. Celsius to Fahrenheit
Enter your choice (1/2/3): 1
Enter KM: 10
Miles: 6.21
```

---

## ▶️ Run It

```bash
python unit_converter.py
```

---

## 🔄 Supported Conversions

| Option | From | To | Formula |
|--------|------|----|---------|
| 1 | KM | Miles | × 0.621 |
| 2 | KG | Pounds | × 2.205 |
| 3 | Celsius | Fahrenheit | (× 9/5) + 32 |

---

## 🧠 Concepts Used

| Concept | Purpose |
|---------|---------|
| `def km_to_miles()` | Machine for KM conversion |
| `def kg_to_pounds()` | Machine for KG conversion |
| `def celsius_to_fahrenheit()` | Machine for temperature conversion |
| `float(input())` | Get decimal numbers from user |
| `return` | Send result out of function |
| `if / elif / else` | Check user's choice |

---

## 💻 Source Code

```python
def km_to_miles(km):
    return km * 0.621

def kg_to_pounds(kg):
    return kg * 2.205

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("WELCOME TO UNIT CONVERTER! 🔥")
print("1. KM to Miles")
print("2. KG to Pounds")
print("3. Celsius to Fahrenheit")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    km = float(input("Enter KM: "))
    print("Miles:", km_to_miles(km))
elif choice == "2":
    kg = float(input("Enter KG: "))
    print("Pounds:", kg_to_pounds(kg))
elif choice == "3":
    celsius = float(input("Enter Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(celsius))
else:
    print("Invalid choice! 😅")
```

---

<div align="center">

[🔙 Back to Portfolio](../README.md) • [👤 My Profile](https://github.com/AYDINKHAN)

</div>
