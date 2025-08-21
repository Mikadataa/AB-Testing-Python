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



# 🧪 A/B Testing in Python

A hands-on project to simulate and analyze A/B test experiments using Python.  
Learn how to run statistical tests, compute confidence intervals, and visualize results with clear recommendations.

---

## 🚀 How to Run

1. **Clone this repo**

```bash
git clone https://github.com/Mikadataa/AB-Testing-Python.git
cd AB-Testing-Python
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the notebook**

```bash
jupyter notebook notebooks/ab_test_analysis.ipynb
```

---

## 📊 Demo

Here’s a sample visualization of conversion rates with confidence intervals:

![Demo Chart](demo_chart.png)

---

## 📚 What You'll Learn

- ✅ Simulate A/B test data  
- ✅ Compute conversion rates with confidence intervals  
- ✅ Run a two-proportion z-test  
- ✅ Visualize results with Matplotlib  
- ✅ Translate stats into plain-English recommendations  

---

## 🔮 Extensions (Next Steps)

- Add CTR, revenue per user, or retention as metrics  
- Use t-tests for continuous outcomes (e.g., time spent, order value)  
- Build a Streamlit dashboard for interactive analysis  
- Try Bayesian A/B testing approaches  

---

## 📈 Conclusions

- **Variant B outperformed Variant A** with a conversion rate of **12.6% vs 10.2%**.  
- The uplift of **+2.36%** was **statistically significant** (*p = 0.0087, 95% CI: 0.60% → 4.12%*).  
- Based on this experiment, the recommendation is to **roll out Variant B**, as it is highly likely to improve conversions in production.  

This demonstrates how A/B testing can guide **data-driven product decisions** instead of relying on intuition.

---


**This project demonstrated a complete A/B testing workflow in a single Jupyter Notebook:**

**Synthetic Data Generation**

- Created randomized user-level dataset with group assignment (A vs B) and binary outcome (converted).

**Exploratory Summaries**

- Computed per-group conversion rates with group_summary().

- Calculated standard errors and 95% confidence intervals for each variant.

**Visualization**

- Plotted conversion rates with error bars using Matplotlib for quick comparison.

**Hypothesis Testing**

- Performed a two-proportion z-test with propor_z_test().

- Measured uplift, p-values, and 95% confidence interval bounds.

**Plain-English Reporting**

- Interpreted statistical results into actionable recommendations (roll out B, keep A, or inconclusive).

📊 Final outputs include:

- Per-group summary table (conversion, standard error, confidence intervals)

- Conversion rate plot with 95% CI

- Z-test results with p-value, uplift, and decision recommendation

## 👩‍💻 Author

**Mikadataa**  
🔗 [LinkedIn](https://www.linkedin.com/in/smagulova/) | 🐙 [GitHub](https://github.com/Mikadataa)

---

## 📄 License

This project is licensed under the MIT License.
