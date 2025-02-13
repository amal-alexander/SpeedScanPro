import streamlit as st
from utils.visualization import create_score_gauge, create_comparison_chart

def display_metrics(desktop_results: dict, mobile_results: dict):
    """Display the analysis metrics with visualizations"""
    
    # Create tabs for desktop and mobile views
    tab1, tab2, tab3 = st.tabs(["Overview", "Desktop Metrics", "Mobile Metrics"])
    
    with tab1:
        st.subheader("Performance Overview")
        comparison_chart = create_comparison_chart(desktop_results, mobile_results)
        st.plotly_chart(comparison_chart, use_container_width=True)
    
    with tab2:
        st.subheader("Desktop Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            desktop_performance = desktop_results['lighthouse_result']['categories']['performance']['score']
            fig = create_score_gauge(desktop_performance, "Performance Score")
            st.plotly_chart(fig, use_container_width=True)
            
            # Display key metrics
            st.markdown("### Key Metrics")
            metrics = desktop_results['lighthouse_result']['audits']
            st.metric("First Contentful Paint", 
                     f"{metrics['first-contentful-paint']['displayValue']}")
            st.metric("Time to Interactive", 
                     f"{metrics['interactive']['displayValue']}")
    
    with tab3:
        st.subheader("Mobile Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            mobile_performance = mobile_results['lighthouse_result']['categories']['performance']['score']
            fig = create_score_gauge(mobile_performance, "Performance Score")
            st.plotly_chart(fig, use_container_width=True)
            
            # Display key metrics
            st.markdown("### Key Metrics")
            metrics = mobile_results['lighthouse_result']['audits']
            st.metric("First Contentful Paint", 
                     f"{metrics['first-contentful-paint']['displayValue']}")
            st.metric("Time to Interactive", 
                     f"{metrics['interactive']['displayValue']}")
