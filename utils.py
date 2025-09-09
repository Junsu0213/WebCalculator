import numpy as np
import plotly.graph_objects as go
from calculator import calculate_liver_volume_hwt, calculate_spleen_volume_hwt, calculate_liver_volume_wt, calculate_spleen_volume_wt

# Function to create liver chart using weight only
def create_liver_chart_wt(sex, weight, age_group, measured_volumes):
    # Generate weight range
    weights = np.linspace(0, 200, 200)
    
    # Calculate liver volumes for each percentile
    p5_volumes = calculate_liver_volume_wt(sex, weight, 5) 
    p25_volumes = calculate_liver_volume_wt(sex, weight, 25)
    p50_volumes = calculate_liver_volume_wt(sex, weight, 50)
    p75_volumes = calculate_liver_volume_wt(sex, weight, 75)
    p95_volumes = calculate_liver_volume_wt(sex, weight, 95)

    # Calculate regression lines
    liver_5_line = [calculate_liver_volume_wt(sex, w, 5) for w in weights]
    liver_25_line = [calculate_liver_volume_wt(sex, w, 25) for w in weights]
    liver_50_line = [calculate_liver_volume_wt(sex, w, 50) for w in weights]
    liver_75_line = [calculate_liver_volume_wt(sex, w, 75) for w in weights]
    liver_95_line = [calculate_liver_volume_wt(sex, w, 95) for w in weights]

    # Create Plotly graph
    fig = go.Figure()
    
    # Add percentile lines to liver volume chart with legend
    fig.add_trace(go.Scatter(x=weights, y=liver_5_line, mode='lines', name='5th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=liver_25_line, mode='lines', name='25th percentile', 
                            line=dict(color='rgba(255,255,255,0.4)', dash='dot'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=liver_50_line, mode='lines', name='50th percentile', 
                            line=dict(color='rgba(255,255,255,0.7)'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=liver_75_line, mode='lines', name='75th percentile', 
                            line=dict(color='rgba(255,255,255,0.4)', dash='dot'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=liver_95_line, mode='lines', name='95th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=True))
    
    
    fig.add_trace(go.Scatter(x=[weight], y=[p5_volumes], mode='markers', name='5th percentile point',
                             marker=dict(size=10, color='white', symbol='circle-open', line=dict(width=2)), showlegend=False))
    fig.add_trace(go.Scatter(x=[weight], y=[p50_volumes], mode='markers', name='Estimated (50th)',
                             marker=dict(size=10, color='red', symbol='circle'), showlegend=True))
    fig.add_trace(go.Scatter(x=[weight], y=[p95_volumes], mode='markers', name='95th percentile point',
                             marker=dict(size=10, color='white', symbol='circle-open', line=dict(width=2)), showlegend=False))
    
    if measured_volumes != 0:
        fig.add_trace(go.Scatter(x=[weight], y=[measured_volumes], mode='markers', name='Measured',
                             marker=dict(size=10, color='orange', symbol='circle'), showlegend=True))
    # Configure graph layout
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
            borderwidth=1,
            font=dict(color="white")
        ),
        margin=dict(l=20, r=20, t=40, b=20),
        height=700,
        paper_bgcolor='#0a1929',
        plot_bgcolor='#0a1929',
        font=dict(color='white'),
        showlegend=True
    )
    
    # Add grid
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

def create_spleen_chart_wt(sex, weight, age_group, measured_volumes):
    # Generate weight range
    weights = np.linspace(0, 200, 200)
    
    # Calculate spleen volumes for each percentile
    p5_volumes = calculate_spleen_volume_wt(sex, weight, 5) 
    p25_volumes = calculate_spleen_volume_wt(sex, weight, 25)
    p50_volumes = calculate_spleen_volume_wt(sex, weight, 50)
    p75_volumes = calculate_spleen_volume_wt(sex, weight, 75)
    p95_volumes = calculate_spleen_volume_wt(sex, weight, 95)

    # Calculate regression lines
    spleen_5_line = [calculate_spleen_volume_wt(sex, w, 5) for w in weights]
    spleen_25_line = [calculate_spleen_volume_wt(sex, w, 25) for w in weights]
    spleen_50_line = [calculate_spleen_volume_wt(sex, w, 50) for w in weights]
    spleen_75_line = [calculate_spleen_volume_wt(sex, w, 75) for w in weights]
    spleen_95_line = [calculate_spleen_volume_wt(sex, w, 95) for w in weights]

    # Create Plotly graph
    fig = go.Figure()
    
    # Add percentile lines to spleen volume chart with legend
    fig.add_trace(go.Scatter(x=weights, y=spleen_5_line, mode='lines', name='5th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=spleen_25_line, mode='lines', name='25th percentile', 
                            line=dict(color='rgba(255,255,255,0.4)', dash='dot'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=spleen_50_line, mode='lines', name='50th percentile', 
                            line=dict(color='rgba(255,255,255,0.7)'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=spleen_75_line, mode='lines', name='75th percentile', 
                            line=dict(color='rgba(255,255,255,0.4)', dash='dot'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=spleen_95_line, mode='lines', name='95th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=True))
    
    
    fig.add_trace(go.Scatter(x=[weight], y=[p5_volumes], mode='markers', name='5th percentile point',
                             marker=dict(size=10, color='white', symbol='circle-open', line=dict(width=2)), showlegend=False))
    fig.add_trace(go.Scatter(x=[weight], y=[p50_volumes], mode='markers', name='Estimated (50th)',
                             marker=dict(size=10, color='red', symbol='circle'), showlegend=True))
    fig.add_trace(go.Scatter(x=[weight], y=[p95_volumes], mode='markers', name='95th percentile point',
                             marker=dict(size=10, color='white', symbol='circle-open', line=dict(width=2)), showlegend=False))
    
    if measured_volumes != 0:
        fig.add_trace(go.Scatter(x=[weight], y=[measured_volumes], mode='markers', name='Measured',
                             marker=dict(size=10, color='orange', symbol='circle'), showlegend=True))
    
    # Configure graph layout
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
            borderwidth=1,
            font=dict(color="white")
        ),
        margin=dict(l=20, r=20, t=40, b=20),
        height=700,
        paper_bgcolor='#0a1929',
        plot_bgcolor='#0a1929',
        font=dict(color='white'),
        showlegend=True
    )
    
    # Add grid
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

# Function to create liver chart using height and weight
def create_liver_chart_hwt(sex, height, weight, age_group, measured_volumes):
    # Generate weight range
    weights = np.linspace(0, 200, 200)
    
    # Calculate liver volumes for each percentile
    p5_volumes = calculate_liver_volume_hwt(sex, height, weight, 5) 
    p25_volumes = calculate_liver_volume_hwt(sex, height, weight, 25)
    p50_volumes = calculate_liver_volume_hwt(sex, height, weight, 50)
    p75_volumes = calculate_liver_volume_hwt(sex, height, weight, 75)
    p95_volumes = calculate_liver_volume_hwt(sex, height, weight, 95)

    # Calculate regression lines
    liver_5_line = [calculate_liver_volume_hwt(sex, height, w, 5) for w in weights]
    liver_25_line = [calculate_liver_volume_hwt(sex, height, w, 25) for w in weights]
    liver_50_line = [calculate_liver_volume_hwt(sex, height, w, 50) for w in weights]
    liver_75_line = [calculate_liver_volume_hwt(sex, height, w, 75) for w in weights]
    liver_95_line = [calculate_liver_volume_hwt(sex, height, w, 95) for w in weights]

    # Create Plotly graph
    fig = go.Figure()
    
    # Add percentile lines to liver volume chart with legend
    fig.add_trace(go.Scatter(x=weights, y=liver_5_line, mode='lines', name='5th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=liver_25_line, mode='lines', name='25th percentile', 
                            line=dict(color='rgba(255,255,255,0.4)', dash='dot'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=liver_50_line, mode='lines', name='50th percentile', 
                            line=dict(color='rgba(255,255,255,0.7)'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=liver_75_line, mode='lines', name='75th percentile', 
                            line=dict(color='rgba(255,255,255,0.4)', dash='dot'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=liver_95_line, mode='lines', name='95th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=True))
    
    
    fig.add_trace(go.Scatter(x=[weight], y=[p5_volumes], mode='markers', name='5th percentile point',
                             marker=dict(size=10, color='white', symbol='circle-open', line=dict(width=2)), showlegend=False))
    fig.add_trace(go.Scatter(x=[weight], y=[p50_volumes], mode='markers', name='Estimated (50th)',
                             marker=dict(size=10, color='red', symbol='circle'), showlegend=True))
    fig.add_trace(go.Scatter(x=[weight], y=[p95_volumes], mode='markers', name='95th percentile point',
                             marker=dict(size=10, color='white', symbol='circle-open', line=dict(width=2)), showlegend=False))
    
    if measured_volumes != 0:
        fig.add_trace(go.Scatter(x=[weight], y=[measured_volumes], mode='markers', name='Measured',
                             marker=dict(size=10, color='orange', symbol='circle'), showlegend=True))
    # Configure graph layout
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
            borderwidth=1,
            font=dict(color="white")
        ),
        margin=dict(l=20, r=20, t=40, b=20),
        height=700,
        paper_bgcolor='#0a1929',
        plot_bgcolor='#0a1929',
        font=dict(color='white'),
        showlegend=True
    )
    
    # Add grid
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

def create_spleen_chart_hwt(sex, height, weight, age_group, measured_volumes):
    # Generate weight range
    weights = np.linspace(0, 200, 200)
    
    # Calculate spleen volumes for each percentile
    p5_volumes = calculate_spleen_volume_hwt(sex, height, weight, 5) 
    p25_volumes = calculate_spleen_volume_hwt(sex, height, weight, 25)
    p50_volumes = calculate_spleen_volume_hwt(sex, height, weight, 50)
    p75_volumes = calculate_spleen_volume_hwt(sex, height, weight, 75)
    p95_volumes = calculate_spleen_volume_hwt(sex, height, weight, 95)
    
    # Calculate regression lines
    spleen_5_line = [calculate_spleen_volume_hwt(sex, height, w, 5) for w in weights]
    spleen_25_line = [calculate_spleen_volume_hwt(sex, height, w, 25) for w in weights]
    spleen_50_line = [calculate_spleen_volume_hwt(sex, height, w, 50) for w in weights]
    spleen_75_line = [calculate_spleen_volume_hwt(sex, height, w, 75) for w in weights]
    spleen_95_line = [calculate_spleen_volume_hwt(sex, height, w, 95) for w in weights]

    # Create Plotly graph
    fig = go.Figure()
    
    # Add percentile lines to spleen volume chart with legend
    fig.add_trace(go.Scatter(x=weights, y=spleen_5_line, mode='lines', name='5th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=spleen_25_line, mode='lines', name='25th percentile', 
                            line=dict(color='rgba(255,255,255,0.4)', dash='dot'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=spleen_50_line, mode='lines', name='50th percentile', 
                            line=dict(color='rgba(255,255,255,0.7)'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=spleen_75_line, mode='lines', name='75th percentile', 
                            line=dict(color='rgba(255,255,255,0.4)', dash='dot'), showlegend=True))
    fig.add_trace(go.Scatter(x=weights, y=spleen_95_line, mode='lines', name='95th percentile', 
                            line=dict(color='rgba(255,255,255,0.3)', dash='dash'), showlegend=True))
    
    
    fig.add_trace(go.Scatter(x=[weight], y=[p5_volumes], mode='markers', name='5th percentile point',
                             marker=dict(size=10, color='white', symbol='circle-open', line=dict(width=2)), showlegend=False))
    fig.add_trace(go.Scatter(x=[weight], y=[p50_volumes], mode='markers', name='Estimated (50th)',
                             marker=dict(size=10, color='red', symbol='circle'), showlegend=True))
    fig.add_trace(go.Scatter(x=[weight], y=[p95_volumes], mode='markers', name='95th percentile point',
                             marker=dict(size=10, color='white', symbol='circle-open', line=dict(width=2)), showlegend=False))
    
    if measured_volumes != 0:
        fig.add_trace(go.Scatter(x=[weight], y=[measured_volumes], mode='markers', name='Measured',
                             marker=dict(size=10, color='orange', symbol='circle'), showlegend=True))
    
    # Configure graph layout
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
            borderwidth=1,
            font=dict(color="white")
        ),
        margin=dict(l=20, r=20, t=40, b=20),
        height=700,
        paper_bgcolor='#0a1929',
        plot_bgcolor='#0a1929',
        font=dict(color='white'),
        showlegend=True
    )
    
    # Add grid
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