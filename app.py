import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set page config
st.set_page_config(
    page_title="Sample Dashboard",
    page_icon="📊",
    layout="wide"
)

# Create sample data
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', end='2024-02-01', freq='D')
data = {
    'Date': dates,
    'Sales': np.random.normal(100, 15, len(dates)),
    'Traffic': np.random.normal(500, 50, len(dates)),
    'Conversion': np.random.uniform(0.1, 0.3, len(dates))
}
df = pd.DataFrame(data)

# Main title
st.title("📊 Sample Analytics Dashboard")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📈 Trends", "📊 Distribution", "🔍 Details"])

with tab1:
    st.header("Time Series Analysis")
    
    # Line chart
    fig_trends = px.line(df, x='Date', y=['Sales', 'Traffic'], 
                        title='Daily Sales and Traffic Trends')
    st.plotly_chart(fig_trends, use_container_width=True)
    
    # Area chart
    fig_conversion = px.area(df, x='Date', y='Conversion',
                            title='Conversion Rate Over Time')
    st.plotly_chart(fig_conversion, use_container_width=True)

with tab2:
    st.header("Statistical Distribution")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Histogram
        fig_hist = px.histogram(df, x='Sales', 
                              title='Sales Distribution',
                              nbins=20)
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Box plot
        fig_box = px.box(df, y=['Sales', 'Traffic'], 
                        title='Sales and Traffic Distribution')
        st.plotly_chart(fig_box, use_container_width=True)

with tab3:
    st.header("Detailed Data View")
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Average Sales", f"{df['Sales'].mean():.2f}")
    with col2:
        st.metric("Average Traffic", f"{df['Traffic'].mean():.2f}")
    with col3:
        st.metric("Average Conversion", f"{df['Conversion'].mean():.2%}")
    
    # Data table
    st.subheader("Raw Data")
    st.dataframe(df.style.highlight_max(axis=0), use_container_width=True) 