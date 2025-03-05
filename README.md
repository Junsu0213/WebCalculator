# Web Calculator for Reference Intervals of Liver and Spleen Volume in Children

This repository contains a web-based calculator for reference intervals of liver and spleen volume in children. This application is designed to assist medical professionals in evaluating liver and spleen volumes in pediatric patients.

## Overview

This web calculator provides the following features:
1. Calculation of reference intervals for liver and spleen volumes based on sex, height, and weight
2. Provision of 5th, 50th, and 95th percentile values
3. Visual graphs showing volume changes according to weight
4. Comparison between measured volume values and reference intervals

## How to Use

The calculator requires the following input data:
- Sex (Boy/Girl)
- Birth date
- Imaging date
- Weight (kg)
- Height (cm)
- Measured liver volume (optional)
- Measured spleen volume (optional)

After providing the input data, click the "Show results" button to display the reference intervals and graphs.

## Calculation Methods

This calculator uses two regression formulas:
1. Regression formula using sex, height, and weight
2. Regression formula using sex and weight only

Each formula calculates liver volume, spleen volume, and liver-to-spleen volume ratio for the 5th, 50th, and 95th percentiles.

## Interpreting Results

Results are displayed as follows:
- Reference intervals in tabular format (5th, 50th, 95th percentiles)
- Graphs showing volume changes according to weight
- Comparison between measured values and reference values (when measured values are entered)

## Features

- Intuitive user interface
- Dark theme design
- Responsive layout
- Interactive graphs
- Age-optimized graph scales

## Technology Stack

- Python
- Streamlit
- Plotly
- Pandas
- NumPy
- Matplotlib

## Installation

```bash
git clone https://github.com/yourusername/Web_Calculator.git
cd Web_Calculator
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run main.py
```

## Requirements

```
streamlit>=1.28.0
pandas>=1.5.3
numpy>=1.24.3
matplotlib>=3.7.1
plotly>=5.14.1
python-dateutil>=2.8.2
```

## Cautions

- This calculator may not be suitable for children younger than 2 years old.
- The calculated reference intervals do not replace clinical judgment and should be used for reference only.
- All measurements depend on the accuracy of the input data.

## Developer Information

This web calculator was developed for medical imaging data analysis and can be used as a reference tool for evaluating liver and spleen volumes in pediatric patients. 