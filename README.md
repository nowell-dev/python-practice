# 💰 Loan Calculator

## 📌 Overview  
This project is a **Loan Calculator** that helps estimate your monthly payment based on:  
- Loan Amount
- Interest Rate
- Loan term

It is written in **Python** and includes a simple batch script (`.cmd`) so Windows users can run it easily without typing commands.

---

## 📂 Files  
- **`LoanCalculator.py`** — The Python script that performs the calculation  
- **`LoanCalculator.cmd`** — A batch script to quickly run the program on Windows  

---

## ✅ Prerequisites  
- **Python** (version 3.6 or newer)  
  👉 [Download here](https://www.python.org/downloads/)  

---

## ⚙️ Installation  

1. **Download the project**  
   - Click the green **Code** button on GitHub → **Download ZIP**  

2. **Unzip the file**  
   - Right-click the downloaded ZIP → choose **Extract All**  

3. **Run the program**  
   - Double-click `LoanCalculator.cmd`  
   - The calculator will open in a terminal window  

---

## 📊 Sample Output  

```text
-------------------------------------------------------

Loan Amount: 1000000
Loan Term (months): 12
Interest Rate (percentage): 6.5

-------------------------------------------------------

Monthly Amortization: 86,296.42

-------------------------------------------------------

Month            Payment         Principal          Interest             Balance
1              86,296.42         80,879.75          5,416.67          919,120.25
2              86,296.42         81,317.85          4,978.57          837,802.40
3              86,296.42         81,758.32          4,538.10          756,044.08
4              86,296.42         82,201.18          4,095.24          673,842.90
5              86,296.42         82,646.43          3,649.98          591,196.47
6              86,296.42         83,094.10          3,202.31          508,102.36
7              86,296.42         83,544.20          2,752.22          424,558.17
8              86,296.42         83,996.73          2,299.69          340,561.44
9              86,296.42         84,451.71          1,844.71          256,109.73
10             86,296.42         84,909.16          1,387.26          171,200.58
11             86,296.42         85,369.08            927.34           85,831.50
12             86,296.42         85,831.50            464.92               -0.00

           Total Payment   Total Principal      Total Interest
            1,035,557.00      1,000,000.00           35,557.00

-------------------------------------------------------

Would you like to export this to Excel (Y/N)?
