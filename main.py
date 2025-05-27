import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dateutil.relativedelta import relativedelta
from calculator import (
    calculate_liver_volume_hwt, 
    calculate_spleen_volume_hwt,
    calculate_liver_volume_wt,
    calculate_spleen_volume_wt
)
import utils

# Page configuration
st.set_page_config(
    page_title="Pediatric Liver and Spleen Volume Reference Interval Calculator",
    layout="wide"
)

# Color settings
bg_color = "#0a1929"  # Dark background close to black
text_color = "white"
header_bg_color = "#1e3a5c"  # Dark blue background
table_odd_row_color = "#142841"  # Darker background
table_even_row_color = "#1a324c"  # Slightly lighter background
chart_bg_color = "#0a1929"
chart_grid_color = "#1e3a5c"
chart_line_color = "rgba(255,255,255,0.7)"
chart_line_color_light = "rgba(255,255,255,0.3)"

# Custom CSS
with open("styles.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown("<div class='main-header'><h1>Web Calculator: liver and spleen volume in children</h1></div>", unsafe_allow_html=True)

# Input section
st.markdown("<div class='section-header'><h2>Input data</h2></div>", unsafe_allow_html=True)

# Sex selection
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label>Sex <span class='required'>*</span></label>", unsafe_allow_html=True)
    sex = st.radio("", ["Boy", "Girl"], horizontal=True, label_visibility="collapsed")

# Birth date and examination date
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label>Birth date <span class='required'>*</span></label>", unsafe_allow_html=True)
    birth_date = st.date_input("", value=datetime(2010, 1, 1), min_value=datetime(1900, 1, 1), max_value=datetime(2035, 12, 31), format="YYYY-MM-DD", label_visibility="collapsed", key="birth_date")

with col2:
    st.markdown("<label>Imaging date <span class='required'>*</span></label>", unsafe_allow_html=True)
    imaging_date = st.date_input("", value="today", min_value=datetime(1900, 1, 1), max_value=datetime(2035, 12, 31), format="YYYY-MM-DD", label_visibility="collapsed", key="imaging_date")

# Weight and height
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label>Weight (kg) <span class='required'>*</span></label>", unsafe_allow_html=True)
    weight = st.number_input("", min_value=0.0, step=0.1, key="weight", format="%.1f", label_visibility="collapsed")

with col2:
    st.markdown("<label>Height (cm)</label>", unsafe_allow_html=True)
    height = st.number_input("", min_value=0.0, step=0.1, key="height", format="%.1f", label_visibility="collapsed")

# Measured liver and spleen volumes
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label>Measured liver volume (cm³)</label>", unsafe_allow_html=True)
    liver_volume = st.number_input("", min_value=0.0, step=0.1, key="liver", format="%.1f", label_visibility="collapsed")

with col2:
    st.markdown("<label>Measured spleen volume (cm³)</label>", unsafe_allow_html=True)
    spleen_volume = st.number_input("", min_value=0.0, step=0.1, key="spleen", format="%.1f", label_visibility="collapsed")

st.markdown("<p class='required'>* Required fields.</p>", unsafe_allow_html=True)

# Results button and measured ratio display
col1, col2 = st.columns(2)
with col1:
    show_results = st.button("Show results", type="primary")

# Display measured liver-to-spleen ratio if both values are provided
with col2:
    if liver_volume > 0 and spleen_volume > 0:
        measured_ratio = liver_volume / spleen_volume
        st.markdown(f"""
        <div style="background-color: #1a324c; padding: 10px 15px; border-radius: 8px; margin-top: 4px;">
            <span style="font-weight: 600; color: white;">Measured Liver-to-Spleen Ratio:</span>
            <span style="color: orange; margin-left: 10px; font-weight: 600;">{measured_ratio:.1f}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<p class='caution'>Caution: This calculator may not be suitable for children younger than 2 years old.</p>", unsafe_allow_html=True)

# Reference interval section
st.markdown("<div class='section-header'><h2>Reference interval</h2></div>", unsafe_allow_html=True)

# Initialize variables to store calculation results
liver_hwt_5 = liver_hwt_50 = liver_hwt_95 = ""
spleen_hwt_5 = spleen_hwt_50 = spleen_hwt_95 = ""
ratio_hwt_5 = ratio_hwt_50 = ratio_hwt_95 = ""
liver_wt_5 = liver_wt_50 = liver_wt_95 = ""
spleen_wt_5 = spleen_wt_50 = spleen_wt_95 = ""
ratio_wt_5 = ratio_wt_50 = ratio_wt_95 = ""

# Check conditions for displaying results
if show_results and weight > 0:
    # Calculate age
    age = relativedelta(imaging_date, birth_date).years
    
    # Calculate values using weight only
    liver_wt_5 = f"{calculate_liver_volume_wt(sex, weight, 5):.1f}"
    liver_wt_50 = f"{calculate_liver_volume_wt(sex, weight, 50):.1f}"
    liver_wt_95 = f"{calculate_liver_volume_wt(sex, weight, 95):.1f}"
    
    spleen_wt_5 = f"{calculate_spleen_volume_wt(sex, weight, 5):.1f}"
    spleen_wt_50 = f"{calculate_spleen_volume_wt(sex, weight, 50):.1f}"
    spleen_wt_95 = f"{calculate_spleen_volume_wt(sex, weight, 95):.1f}"
    
    ratio_wt_5 = "4.1"
    ratio_wt_50 = "6.3"
    ratio_wt_95 = "9.6"
    
    # Calculate values using height and weight if height is provided
    if height > 0:
        liver_hwt_5 = f"{calculate_liver_volume_hwt(sex, height, weight, 5):.1f}"
        liver_hwt_50 = f"{calculate_liver_volume_hwt(sex, height, weight, 50):.1f}"
        liver_hwt_95 = f"{calculate_liver_volume_hwt(sex, height, weight, 95):.1f}"
        
        spleen_hwt_5 = f"{calculate_spleen_volume_hwt(sex, height, weight, 5):.1f}"
        spleen_hwt_50 = f"{calculate_spleen_volume_hwt(sex, height, weight, 50):.1f}"
        spleen_hwt_95 = f"{calculate_spleen_volume_hwt(sex, height, weight, 95):.1f}"
        
        ratio_hwt_5 = "4.1"
        ratio_hwt_50 = "6.3"
        ratio_hwt_95 = "9.6"
elif show_results and weight <= 0:
    st.error("Please enter weight.")

# 1. Regression formula using sex and weight only
st.markdown("<h3>1. Regression formula using sex and weight</h3>", unsafe_allow_html=True)

# Create results table
data_wt = [
    ["Liver volume (cm³)", liver_wt_5, liver_wt_50, liver_wt_95],
    ["Spleen volume (cm³)", spleen_wt_5, spleen_wt_50, spleen_wt_95],
    ["Liver-to-spleen volume ratio", ratio_wt_5, ratio_wt_50, ratio_wt_95]
]

# Create HTML table directly - 개선된 스타일 (세로 줄 추가)
html_table = f"""
<table class="dataframe" style="width:100%; border-collapse: separate; border-spacing: 0; border-radius: 8px; overflow: hidden; background-color: {bg_color}; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <thead>
    <tr>
      <th style="background-color: {header_bg_color}; color: white; padding: 14px 18px; text-align: left; border-bottom: 2px solid #2a4d7a;">Volumetric index</th>
      <th style="background-color: {header_bg_color}; color: white; padding: 14px 18px; text-align: center; border-bottom: 2px solid #2a4d7a; border-left: 1px solid #2a4d7a;">5 percentile</th>
      <th style="background-color: {header_bg_color}; color: white; padding: 14px 18px; text-align: center; border-bottom: 2px solid #2a4d7a; border-left: 1px solid #2a4d7a;">50 percentile</th>
      <th style="background-color: {header_bg_color}; color: white; padding: 14px 18px; text-align: center; border-bottom: 2px solid #2a4d7a; border-left: 1px solid #2a4d7a;">95 percentile</th>
    </tr>
  </thead>
  <tbody>
"""

for i, row in enumerate(data_wt):
    # Apply background color to all rows, alternating colors for odd/even rows
    bg_color_style = f'background-color: {table_odd_row_color}' if i % 2 == 0 else f'background-color: {table_even_row_color}'
    html_table += f'<tr style="{bg_color_style}">'
    
    # 첫 번째 열은 왼쪽 정렬, 나머지 열은 가운데 정렬 (세로 줄 추가)
    html_table += f'<td style="padding: 12px 18px; border-bottom: 1px solid #2a4d7a;">{row[0]}</td>'
    html_table += f'<td style="padding: 12px 18px; text-align: center; border-bottom: 1px solid #2a4d7a; border-left: 1px solid #2a4d7a;">{row[1]}</td>'
    html_table += f'<td style="padding: 12px 18px; text-align: center; border-bottom: 1px solid #2a4d7a; border-left: 1px solid #2a4d7a;">{row[2]}</td>'
    html_table += f'<td style="padding: 12px 18px; text-align: center; border-bottom: 1px solid #2a4d7a; border-left: 1px solid #2a4d7a;">{row[3]}</td>'
    html_table += '</tr>'

html_table += """
  </tbody>
</table>
"""

st.markdown(html_table, unsafe_allow_html=True)

# 2. Regression formula using sex, height, and weight (only if height is provided)
if height > 0:
    st.markdown("<h3>2. Regression formula using sex, height, weight</h3>", unsafe_allow_html=True)
    
    # Create results table
    data_hwt = [
        ["Liver volume (cm³)", liver_hwt_5, liver_hwt_50, liver_hwt_95],
        ["Spleen volume (cm³)", spleen_hwt_5, spleen_hwt_50, spleen_hwt_95],
        ["Liver-to-spleen volume ratio", ratio_hwt_5, ratio_hwt_50, ratio_hwt_95]
    ]
    
    # Create HTML table directly - 개선된 스타일 (세로 줄 추가)
    html_table = f"""
    <table class="dataframe" style="width:100%; border-collapse: separate; border-spacing: 0; border-radius: 8px; overflow: hidden; background-color: {bg_color}; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
      <thead>
        <tr>
          <th style="background-color: {header_bg_color}; color: white; padding: 14px 18px; text-align: left; border-bottom: 2px solid #2a4d7a;">Volumetric index</th>
          <th style="background-color: {header_bg_color}; color: white; padding: 14px 18px; text-align: center; border-bottom: 2px solid #2a4d7a; border-left: 1px solid #2a4d7a;">5 percentile</th>
          <th style="background-color: {header_bg_color}; color: white; padding: 14px 18px; text-align: center; border-bottom: 2px solid #2a4d7a; border-left: 1px solid #2a4d7a;">50 percentile</th>
          <th style="background-color: {header_bg_color}; color: white; padding: 14px 18px; text-align: center; border-bottom: 2px solid #2a4d7a; border-left: 1px solid #2a4d7a;">95 percentile</th>
        </tr>
      </thead>
      <tbody>
    """

    for i, row in enumerate(data_hwt):
        # Apply background color to all rows, alternating colors for odd/even rows
        bg_color_style = f'background-color: {table_odd_row_color}' if i % 2 == 0 else f'background-color: {table_even_row_color}'
        html_table += f'<tr style="{bg_color_style}">'
        
        # 첫 번째 열은 왼쪽 정렬, 나머지 열은 가운데 정렬 (세로 줄 추가)
        html_table += f'<td style="padding: 12px 18px; border-bottom: 1px solid #2a4d7a;">{row[0]}</td>'
        html_table += f'<td style="padding: 12px 18px; text-align: center; border-bottom: 1px solid #2a4d7a; border-left: 1px solid #2a4d7a;">{row[1]}</td>'
        html_table += f'<td style="padding: 12px 18px; text-align: center; border-bottom: 1px solid #2a4d7a; border-left: 1px solid #2a4d7a;">{row[2]}</td>'
        html_table += f'<td style="padding: 12px 18px; text-align: center; border-bottom: 1px solid #2a4d7a; border-left: 1px solid #2a4d7a;">{row[3]}</td>'
        html_table += '</tr>'

    html_table += """
      </tbody>
    </table>
    """

    st.markdown(html_table, unsafe_allow_html=True)

# Chart section
st.markdown("<div class='section-header'><h2>Chart: volume vs. weight percentile graph</h2></div>", unsafe_allow_html=True)

# 1. Regression formula using sex and weight only
st.markdown("<h3>1. Regression formula using sex and weight</h3>", unsafe_allow_html=True)

# Display two graphs side by side
col1, col2 = st.columns(2)

# Determine age group for chart settings
age_group = "under_6" if 'age' in locals() and age < 6 else "6_to_11" if 'age' in locals() and age <= 11 else "12_and_above" if 'age' in locals() else None

# Liver volume chart
with col1:
    st.subheader("Liver volume")
    if show_results and weight > 0 and age_group:
        fig_liver = utils.create_liver_chart_wt(sex, weight, age_group, liver_volume)
        st.plotly_chart(fig_liver, use_container_width=True)
        # Add explanation below the chart
        st.markdown("""
        <div style="background-color: #1a324c; padding: 10px 15px; border-radius: 8px; margin-top: 10px;">
            <p style="color: white; margin: 0; font-size: 0.9rem; line-height: 1.4;">
                The oblique solid line represents the quantile regression line predicting the 50th percentile, 
                while the oblique dashed lines below and above correspond to the quantile regression lines 
                predicting the 5th and 95th percentiles, respectively.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        fig_liver = go.Figure()
        fig_liver.update_layout(
            title="Quantile Regression Prediction",
            xaxis_title="Weight (kg)",
            yaxis_title="Liver Volume (cm³)",
            height=700,
            width=700,
            paper_bgcolor=chart_bg_color,
            plot_bgcolor=chart_bg_color,
            font=dict(color=text_color)
        )
        fig_liver.update_xaxes(showgrid=True, gridwidth=1, gridcolor=chart_grid_color)
        fig_liver.update_yaxes(showgrid=True, gridwidth=1, gridcolor=chart_grid_color)
        st.plotly_chart(fig_liver, use_container_width=True)

# Spleen volume chart
with col2:
    st.subheader("Spleen volume")
    if show_results and weight > 0 and age_group:
        fig_spleen = utils.create_spleen_chart_wt(sex, weight, age_group, spleen_volume)
        st.plotly_chart(fig_spleen, use_container_width=True)
        # Add explanation below the chart
        st.markdown("""
        <div style="background-color: #1a324c; padding: 10px 15px; border-radius: 8px; margin-top: 10px;">
            <p style="color: white; margin: 0; font-size: 0.9rem; line-height: 1.4;">
                The oblique solid line represents the quantile regression line predicting the 50th percentile, 
                while the oblique dashed lines below and above correspond to the quantile regression lines 
                predicting the 5th and 95th percentiles, respectively.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        fig_spleen = go.Figure()
        fig_spleen.update_layout(
            title="Quantile Regression Prediction",
            xaxis_title="Weight (kg)",
            yaxis_title="Spleen Volume (cm³)",
            height=700,
            width=700,
            paper_bgcolor=chart_bg_color,
            plot_bgcolor=chart_bg_color,
            font=dict(color=text_color)
        )
        fig_spleen.update_xaxes(showgrid=True, gridwidth=1, gridcolor=chart_grid_color)
        fig_spleen.update_yaxes(showgrid=True, gridwidth=1, gridcolor=chart_grid_color)
        st.plotly_chart(fig_spleen, use_container_width=True)

# 2. Charts using height and weight (only if height is provided)
if height > 0:
    st.markdown("<h3>2. Regression formula using sex, height, weight</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Liver volume")
        if show_results and weight > 0 and age_group:
            fig_liver_hwt = utils.create_liver_chart_hwt(sex, height, weight, age_group, liver_volume)
            st.plotly_chart(fig_liver_hwt, use_container_width=True)
            # Add explanation below the chart
            st.markdown("""
            <div style="background-color: #1a324c; padding: 10px 15px; border-radius: 8px; margin-top: 10px;">
                <p style="color: white; margin: 0; font-size: 0.9rem; line-height: 1.4;">
                    The oblique solid line represents the quantile regression line predicting the 50th percentile, 
                    while the oblique dashed lines below and above correspond to the quantile regression lines 
                    predicting the 5th and 95th percentiles, respectively.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            fig_liver_hwt = go.Figure()
            fig_liver_hwt.update_layout(
                title="Quantile Regression Prediction",
                xaxis_title="Weight (kg)",
                yaxis_title="Liver Volume (cm³)",
                height=700,
                width=700,
                paper_bgcolor=chart_bg_color,
                plot_bgcolor=chart_bg_color,
                font=dict(color=text_color)
            )
            fig_liver_hwt.update_xaxes(showgrid=True, gridwidth=1, gridcolor=chart_grid_color)
            fig_liver_hwt.update_yaxes(showgrid=True, gridwidth=1, gridcolor=chart_grid_color)
            st.plotly_chart(fig_liver_hwt, use_container_width=True)
    
    with col2:
        st.subheader("Spleen volume")
        if show_results and weight > 0 and age_group:
            fig_spleen_hwt = utils.create_spleen_chart_hwt(sex, height, weight, age_group, spleen_volume)
            st.plotly_chart(fig_spleen_hwt, use_container_width=True)
            # Add explanation below the chart
            st.markdown("""
            <div style="background-color: #1a324c; padding: 10px 15px; border-radius: 8px; margin-top: 10px;">
                <p style="color: white; margin: 0; font-size: 0.9rem; line-height: 1.4;">
                    The oblique solid line represents the quantile regression line predicting the 50th percentile, 
                    while the oblique dashed lines below and above correspond to the quantile regression lines 
                    predicting the 5th and 95th percentiles, respectively.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            fig_spleen_hwt = go.Figure()
            fig_spleen_hwt.update_layout(
                title="Quantile Regression Prediction",
                xaxis_title="Weight (kg)",
                yaxis_title="Spleen Volume (cm³)",
                height=700,
                width=700,
                paper_bgcolor=chart_bg_color,
                plot_bgcolor=chart_bg_color,
                font=dict(color=text_color)
            )
            fig_spleen_hwt.update_xaxes(showgrid=True, gridwidth=1, gridcolor=chart_grid_color)
            fig_spleen_hwt.update_yaxes(showgrid=True, gridwidth=1, gridcolor=chart_grid_color)
            st.plotly_chart(fig_spleen_hwt, use_container_width=True)

# Copyright information
st.markdown("<div class='footer'>BMC-Core</div>", unsafe_allow_html=True)
