# Mark Analyzer (Python)

This is a simple Python program that analyzes student marks across multiple subjects.  
It calculates **Total Marks, Percentage, Result (Pass/Fail), and Grade** based on the input provided by the user.

---

## ✨ Features

- Accepts marks for any number of subjects
- Calculates:
  - Total Marks
  - Maximum Possible Marks
  - Percentage
- Determines **Pass/Fail**
- Assigns grade based on percentage
- Easy to use and works in Command Line

---

## 🧠 Logic Summary

| Check | Logic |
|------|-------|
| Fail Condition | If any subject mark < 33 |
| Percentage | `(Total Marks / Max Marks) × 100` |
| Grade Scale | See table below |

### **Grade System**
| Percentage | Grade |
|------------|--------|
| > 90 | A+ |
| > 80 | A |
| > 70 | B |
| > 60 | C |
| > 50 | D |
| > 40 | F |

---

## 🚀 Run the Program

Make sure Python is installed.


---

## 📝 Example Output

How many subject is ? : 5
Subject 1 mark is: 78
Subject 2 mark is: 85
Subject 3 mark is: 90
Subject 4 mark is: 82
Subject 5 mark is: 74

-------Result-------

Total : 409/500
Percentage : 81.8
Result : Pass
Grade : A


---

## 📂 Project Structure

Mark-Analyzer/
│
├── Mark_Analyzer.py
└── README.md


---

## 🔧 Technologies Used

- Python 3.x (Built-in `sum()` function)

---

## 💡 Future Improvements

- Store marks in a file for record tracking
- Show subject-wise remarks
- Generate printable report card (PDF)
- GUI version (with buttons & result screen)

---

## 🤝 Contributing

Pull requests are welcome.

