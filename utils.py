import numpy as np
import plotly.graph_objects as go
from calculator import calculate_liver_volume_hwt, calculate_spleen_volume_hwt, calculate_regression_lines

# 차트 생성 함수
def create_liver_chart(sex, height, weight, age_group, measured_volumes):
    # 체중 범위 생성
    weights = np.linspace(0, 200, 200)
    
    # 각 백분위수에 대한 간 부피 계산
    p5_volumes = calculate_liver_volume_hwt(sex, height, weight, 5) 
    p50_volumes = calculate_liver_volume_hwt(sex, height, weight, 50)
    p95_volumes = calculate_liver_volume_hwt(sex, height, weight, 95)

    # regression_lines = calculate_regression_lines(sex, age_group)

    # liver_5_line = regression_lines['liver']['5th']
    # liver_50_line = regression_lines['liver']['50th']
    # liver_95_line = regression_lines['liver']['95th']
    weights = np.linspace(0, 200, 200)
    liver_5_line = calculate_liver_volume_hwt(sex, height, weights, 5)
    liver_50_line = calculate_liver_volume_hwt(sex, height, weights, 50)
    liver_95_line = calculate_liver_volume_hwt(sex, height, weights, 95)

    # Plotly 그래프 생성
    fig = go.Figure()
    
    # 간 부피 차트 - 백분위수 선 추가
    fig.add_trace(go.Scatter(x=weights, y=liver_5_line, mode='lines', name='5th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=False))
    fig.add_trace(go.Scatter(x=weights, y=liver_50_line, mode='lines', name='50th percentile', 
                            line=dict(color='rgba(255,255,255,0.7)'), showlegend=False))
    fig.add_trace(go.Scatter(x=weights, y=liver_95_line, mode='lines', name='95th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=False))
    
    
    fig.add_trace(go.Scatter(x=[weight], y=[p5_volumes], mode='markers', name='5th percentile',
                             marker=dict(size=10, color='red', symbol='circle', opacity=0.5), showlegend=False))
    fig.add_trace(go.Scatter(x=[weight], y=[p50_volumes], mode='markers', name='Estimated (50)',
                             marker=dict(size=10, color='red', symbol='circle'), showlegend=True))
    fig.add_trace(go.Scatter(x=[weight], y=[p95_volumes], mode='markers', name='95th percentile',
                             marker=dict(size=10, color='red', symbol='circle', opacity=0.5), showlegend=False))
    
    if measured_volumes is not 0:
        fig.add_trace(go.Scatter(x=[weight], y=[measured_volumes], mode='markers', name='Measured',
                             marker=dict(size=10, color='blue', symbol='circle'), showlegend=True))
    # 그래프 레이아웃 설정
    fig.update_layout(
        title="Quantile Regression Prediction",
        xaxis_title="Weight (kg)",
        yaxis_title="Liver Volume (cm³)",
        legend=dict(
            orientation="v", 
            yanchor="top", 
            y=0.99, 
            xanchor="right", 
            x=0.99,
            bgcolor="rgba(10, 25, 41, 0.7)",
            bordercolor="rgba(255, 255, 255, 0.3)",
            borderwidth=1
        ),
        margin=dict(l=20, r=20, t=40, b=20),
        height=700,
        paper_bgcolor='#0a1929',
        plot_bgcolor='#0a1929',
        font=dict(color='white'),
        showlegend=True
    )
    
    # 그리드 추가
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#1e3a5c')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#1e3a5c')

        # Set axis ranges based on age group and sex

    if age_group == "under_6":
        fig.update_xaxes(range=[5, 40])
        fig.update_yaxes(range=[100, 1100])
    elif age_group == "6_to_11":
        fig.update_xaxes(range=[5, 85])
        fig.update_yaxes(range=[400, 2100])
    else:
        fig.update_xaxes(range=[15, 105])
        fig.update_yaxes(range=[400, 2600])

    fig.update_layout(showlegend=True)
    
    return fig

def create_spleen_chart(sex, height, weight, age_group, measured_volumes):
    # 체중 범위 생성
    weights = np.linspace(0, 200, 200)
    
    # 각 백분위수에 대한 간 부피 계산
    p5_volumes = calculate_spleen_volume_hwt(sex, height, weight, 5) 
    p50_volumes = calculate_spleen_volume_hwt(sex, height, weight, 50)
    p95_volumes = calculate_spleen_volume_hwt(sex, height, weight, 95)

    # regression_lines = calculate_regression_lines(sex, age_group)

    # spleen_5_line = regression_lines['spleen']['5th']
    # spleen_50_line = regression_lines['spleen']['50th']
    # spleen_95_line = regression_lines['spleen']['95th']
    
    weights = np.linspace(0, 200, 200)
    spleen_5_line = calculate_spleen_volume_hwt(sex, height, weights, 5)
    spleen_50_line = calculate_spleen_volume_hwt(sex, height, weights, 50)
    spleen_95_line = calculate_spleen_volume_hwt(sex, height, weights, 95)

    # Plotly 그래프 생성
    fig = go.Figure()
    
    # 비장 부피 차트 - 백분위수 선 추가
    fig.add_trace(go.Scatter(x=weights, y=spleen_5_line, mode='lines', name='5th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=False))
    fig.add_trace(go.Scatter(x=weights, y=spleen_50_line, mode='lines', name='50th percentile', 
                            line=dict(color='rgba(255,255,255,0.7)'), showlegend=False))
    fig.add_trace(go.Scatter(x=weights, y=spleen_95_line, mode='lines', name='95th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=False))
    
    
    fig.add_trace(go.Scatter(x=[weight], y=[p5_volumes], mode='markers', name='5th percentile',
                             marker=dict(size=10, color='red', symbol='circle', opacity=0.5), showlegend=False))
    fig.add_trace(go.Scatter(x=[weight], y=[p50_volumes], mode='markers', name='Estimated (50)',
                             marker=dict(size=10, color='red', symbol='circle'), showlegend=True))
    fig.add_trace(go.Scatter(x=[weight], y=[p95_volumes], mode='markers', name='95th percentile',
                             marker=dict(size=10, color='red', symbol='circle', opacity=0.5), showlegend=False))
    
    if measured_volumes is not 0:
        fig.add_trace(go.Scatter(x=[weight], y=[measured_volumes], mode='markers', name='Measured',
                             marker=dict(size=10, color='blue', symbol='circle'), showlegend=True))
    
    # 그래프 레이아웃 설정
    fig.update_layout(
        title="Quantile Regression Prediction",
        xaxis_title="Weight (kg)",
        yaxis_title="Spleen Volume (cm³)",
        legend=dict(
            orientation="v", 
            yanchor="top", 
            y=0.99, 
            xanchor="right", 
            x=0.99,
            bgcolor="rgba(10, 25, 41, 0.7)",
            bordercolor="rgba(255, 255, 255, 0.3)",
            borderwidth=1
        ),
        margin=dict(l=20, r=20, t=40, b=20),
        height=700,
        paper_bgcolor='#0a1929',
        plot_bgcolor='#0a1929',
        font=dict(color='white'),
        showlegend=True
    )
    
    # 그리드 추가
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#1e3a5c')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#1e3a5c')

    # Set axis ranges based on age group and sex
    if age_group == "under_6":
        fig.update_xaxes(range=[5, 40])
        fig.update_yaxes(range=[40, 210])
    elif age_group == "6_to_11":
        fig.update_xaxes(range=[5, 85])
        fig.update_yaxes(range=[40, 360])
    else:
        fig.update_xaxes(range=[15, 105])
        fig.update_yaxes(range=[50, 750])

    fig.update_layout(showlegend=True)

    return fig 