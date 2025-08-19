# 🎯 A/B Testing Project (Python)

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)]()
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This project demonstrates a simple **A/B test analysis workflow** using Python.  
It includes **synthetic data generation**, **statistical testing** (z-test, confidence intervals), and **visualization of results**.  

👉 _This project is part of my portfolio to showcase practical skills in A/B testing, data analysis, and reporting._  

---

## 📊 Demo Output
Example result from the notebook:

Variant A (CTR) = 10.24%, Variant B (CTR) = 12.60%
p-value = 0.007 < 0.05 ✅ Significant
Recommendation: Roll out Variant B


📈 Demo chart:

![Demo Chart](images/demo_chart.png)

---

## 📂 Project Structure


ab-testing-project/
│
├── data/
│ └── ab_test_data.csv # synthetic dataset
│
├── notebooks/
│ └── ab_test_analysis.ipynb # Jupyter Notebook with full analysis
│
├── src/
│ ├── data_generator.py # creates synthetic A/B data
│ ├── stats.py # z-test & summary
│ └── visualization.py # plots conversion rates
│
├── results/
│ └── summary_report.md # short findings report
│
├── requirements.txt
└── README.md


---

## ⚙️ How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/Mikadataa/AB-Testing-Python.git
   cd AB-Testing-Python

2. Install dependencies:

pip install -r requirements.txt


3. Run the notebook:

jupyter notebook notebooks/ab_test_analysis.ipynb

📘 What You’ll Learn

✅ Simulate A/B test data
✅ Compute conversion rates with confidence intervals
✅ Run a two-proportion z-test
✅ Visualize results with Matplotlib
✅ Translate stats into plain-English recommendations

🔮 Extensions (Next Steps)

Add CTR, revenue per user, or retention as metrics

Use t-tests for continuous outcomes (e.g., time spent, avg order value)

Build a Streamlit dashboard for interactive analysis

Try Bayesian A/B testing approaches

👤 Author

Mikadataa
💼 LinkedIn
 • 🐙 GitHub

📜 Licensed under the MIT License

