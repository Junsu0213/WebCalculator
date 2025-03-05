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
    calculate_spleen_volume_wt,
    calculate_regression_lines
)
import utils

# 페이지 설정
st.set_page_config(
    page_title="소아 간 및 비장 부피 참조 간격 계산기",
    layout="wide"
)


# 색상 설정
bg_color = "#0a1929"  # 검은색에 가까운 어두운 배경
text_color = "white"
header_bg_color = "#1e3a5c"  # 진한 남색 배경
table_odd_row_color = "#142841"  # 좀 더 어두운 배경
table_even_row_color = "#1a324c"  # 약간 밝은 배경
chart_bg_color = "#0a1929"
chart_grid_color = "#1e3a5c"
chart_line_color = "rgba(255,255,255,0.7)"
chart_line_color_light = "rgba(255,255,255,0.3)"

# 사용자 정의 CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 헤더
st.markdown("<div class='main-header'><h1>Web Calculator: reference intervals for liver and spleen volume in children</h1></div>", unsafe_allow_html=True)

# 입력 섹션
st.markdown("<div class='section-header'><h2>Input data</h2></div>", unsafe_allow_html=True)

# 성별 선택
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label>Sex <span class='required'>*</span></label>", unsafe_allow_html=True)
    sex = st.radio("", ["Boy", "Girl"], horizontal=True, label_visibility="collapsed")

# 생년월일 및 검사일
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label>Birth date <span class='required'>*</span></label>", unsafe_allow_html=True)
    birth_date = st.date_input("", value=None, min_value=datetime(1900, 1, 1), format="YYYY-MM-DD", label_visibility="collapsed", key="birth_date")

with col2:
    st.markdown("<label>Imaging date <span class='required'>*</span></label>", unsafe_allow_html=True)
    imaging_date = st.date_input("", value="today", min_value=datetime(1900, 1, 1), format="YYYY-MM-DD", label_visibility="collapsed", key="imaging_date")

# 체중 및 키
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label>Weight (kg) <span class='required'>*</span></label>", unsafe_allow_html=True)
    weight = st.number_input("", min_value=0.0, step=0.1, key="weight", format="%.1f", label_visibility="collapsed")

with col2:
    st.markdown("<label>Height (cm) <span class='required'>*</span></label>", unsafe_allow_html=True)
    height = st.number_input("", min_value=0.0, step=0.1, key="height", format="%.1f", label_visibility="collapsed")

# 측정된 간 및 비장 부피
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label>Measured liver volume (cm³)</label>", unsafe_allow_html=True)
    liver_volume = st.number_input("", min_value=0.0, step=0.1, key="liver", format="%.1f", label_visibility="collapsed")

with col2:
    st.markdown("<label>Measured spleen volume (cm³)</label>", unsafe_allow_html=True)
    spleen_volume = st.number_input("", min_value=0.0, step=0.1, key="spleen", format="%.1f", label_visibility="collapsed")

st.markdown("<p class='required'>* Required fields.</p>", unsafe_allow_html=True)

# 결과 버튼 - 필수 필드 아래로 이동
show_results = st.button("Show results", type="primary")

st.markdown("<p class='caution'>Caution: This calculator may not be suitable for children younger than 2 years old.</p>", unsafe_allow_html=True)

# 참조 간격 섹션
st.markdown("<div class='section-header'><h2>Reference interval</h2></div>", unsafe_allow_html=True)

# 계산 결과를 저장할 변수들 초기화
liver_hwt_5 = liver_hwt_50 = liver_hwt_95 = ""
spleen_hwt_5 = spleen_hwt_50 = spleen_hwt_95 = ""
ratio_hwt_5 = ratio_hwt_50 = ratio_hwt_95 = ""
liver_wt_5 = liver_wt_50 = liver_wt_95 = ""
spleen_wt_5 = spleen_wt_50 = spleen_wt_95 = ""
ratio_wt_5 = ratio_wt_50 = ratio_wt_95 = ""

# 결과 표시 조건 확인
if show_results and weight > 0:
    # 나이 계산
    age = relativedelta(imaging_date, birth_date).years
    
    # 회귀 공식을 사용한 값들 계산
    liver_hwt_5 = f"{calculate_liver_volume_hwt(sex, height, weight, 5):.1f}"
    liver_hwt_50 = f"{calculate_liver_volume_hwt(sex, height, weight, 50):.1f}"
    liver_hwt_95 = f"{calculate_liver_volume_hwt(sex, height, weight, 95):.1f}"
    
    spleen_hwt_5 = f"{calculate_spleen_volume_hwt(sex, height, weight, 5):.1f}"
    spleen_hwt_50 = f"{calculate_spleen_volume_hwt(sex, height, weight, 50):.1f}"
    spleen_hwt_95 = f"{calculate_spleen_volume_hwt(sex, height, weight, 95):.1f}"
    
    ratio_hwt_5 = "4.1"
    ratio_hwt_50 = "6.3"
    ratio_hwt_95 = "9.6"
    
    liver_wt_5 = f"{calculate_liver_volume_wt(sex, weight, 5):.1f}"
    liver_wt_50 = f"{calculate_liver_volume_wt(sex, weight, 50):.1f}"
    liver_wt_95 = f"{calculate_liver_volume_wt(sex, weight, 95):.1f}"
    
    spleen_wt_5 = f"{calculate_spleen_volume_wt(sex, weight, 5):.1f}"
    spleen_wt_50 = f"{calculate_spleen_volume_wt(sex, weight, 50):.1f}"
    spleen_wt_95 = f"{calculate_spleen_volume_wt(sex, weight, 95):.1f}"
    
    ratio_wt_5 = "4.1"
    ratio_wt_50 = "6.3"
    ratio_wt_95 = "9.6"
elif show_results and weight <= 0:
    st.error("체중을 입력해주세요.")

# 1. 성별, 키, 체중을 사용한 회귀 공식
st.markdown("<h3>1. Regression formula using sex, height, weight</h3>", unsafe_allow_html=True)

# 결과 테이블 생성
data_hwt = [
    ["Liver volume (cm³)", liver_hwt_5, liver_hwt_50, liver_hwt_95],
    ["Spleen volume (cm³)", spleen_hwt_5, spleen_hwt_50, spleen_hwt_95],
    ["Liver-to-spleen volume ratio", ratio_hwt_5, ratio_hwt_50, ratio_hwt_95]
]

# HTML 테이블 직접 생성
html_table = f"""
<table class="dataframe" style="width:100%; border-collapse: separate; border-spacing: 0; border-radius: 8px; overflow: hidden; background-color: {bg_color};">
  <thead>
    <tr>
      <th style="background-color: {header_bg_color}; color: white; padding: 12px 15px; text-align: left;">Volumetric index</th>
      <th style="background-color: {header_bg_color}; color: white; padding: 12px 15px; text-align: left;">5 percentile</th>
      <th style="background-color: {header_bg_color}; color: white; padding: 12px 15px; text-align: left;">50 percentile</th>
      <th style="background-color: {header_bg_color}; color: white; padding: 12px 15px; text-align: left;">95 percentile</th>
    </tr>
  </thead>
  <tbody>
"""

for i, row in enumerate(data_hwt):
    # 모든 행에 배경색 적용, 홀수/짝수 번갈아 다른 색상 사용
    bg_color_style = f'background-color: {table_odd_row_color}' if i % 2 == 0 else f'background-color: {table_even_row_color}'
    html_table += f'<tr style="{bg_color_style}">'
    for cell in row:
        html_table += f'<td style="padding: 10px 15px;">{cell}</td>'
    html_table += '</tr>'

html_table += """
  </tbody>
</table>
"""

st.markdown(html_table, unsafe_allow_html=True)

# 2. 성별, 체중만 사용한 회귀 공식
st.markdown("<h3>2. Regression formula using sex and weight</h3>", unsafe_allow_html=True)

# 결과 테이블 생성
data_wt = [
    ["Liver volume (cm³)", liver_wt_5, liver_wt_50, liver_wt_95],
    ["Spleen volume (cm³)", spleen_wt_5, spleen_wt_50, spleen_wt_95],
    ["Liver-to-spleen volume ratio", ratio_wt_5, ratio_wt_50, ratio_wt_95]
]

# HTML 테이블 직접 생성
html_table = f"""
<table class="dataframe" style="width:100%; border-collapse: separate; border-spacing: 0; border-radius: 8px; overflow: hidden; background-color: {bg_color};">
  <thead>
    <tr>
      <th style="background-color: {header_bg_color}; color: white; padding: 12px 15px; text-align: left;">Volumetric index</th>
      <th style="background-color: {header_bg_color}; color: white; padding: 12px 15px; text-align: left;">5 percentile</th>
      <th style="background-color: {header_bg_color}; color: white; padding: 12px 15px; text-align: left;">50 percentile</th>
      <th style="background-color: {header_bg_color}; color: white; padding: 12px 15px; text-align: left;">95 percentile</th>
    </tr>
  </thead>
  <tbody>
"""

for i, row in enumerate(data_wt):
    # 모든 행에 배경색 적용, 홀수/짝수 번갈아 다른 색상 사용
    bg_color_style = f'background-color: {table_odd_row_color}' if i % 2 == 0 else f'background-color: {table_even_row_color}'
    html_table += f'<tr style="{bg_color_style}">'
    for cell in row:
        html_table += f'<td style="padding: 10px 15px;">{cell}</td>'
    html_table += '</tr>'

html_table += """
  </tbody>
</table>
"""

st.markdown(html_table, unsafe_allow_html=True)

# 차트 섹션
st.markdown("<div class='section-header'><h2>Chart: volume vs. weight percentile graph</h2></div>", unsafe_allow_html=True)

# 두 개의 그래프를 나란히 표시
col1, col2 = st.columns(2)

# 나이대에 따른 설정
age_group = "under_6" if 'age' in locals() and age < 6 else "6_to_11" if 'age' in locals() and age <= 11 else "12_and_above" if 'age' in locals() else None

# Liver volume chart
with col1:
    st.subheader("Liver volume")
    if show_results and weight > 0 and age_group:
        fig_liver = utils.create_liver_chart(sex, height, weight, age_group, liver_volume)
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
        fig_spleen = utils.create_spleen_chart(sex, height, weight, age_group, spleen_volume)
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

# 저작권 정보 추가
st.markdown("<div class='footer'>BMC-Core</div>", unsafe_allow_html=True)
