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
            categories = desktop_results['lighthouse_result']['categories']
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Loading Metrics")
                st.metric("First Contentful Paint (FCP)", 
                         f"{metrics['first-contentful-paint']['displayValue']}")
                st.metric("Largest Contentful Paint (LCP)", 
                         f"{metrics['largest-contentful-paint']['displayValue']}")
                st.metric("Time to First Byte (TTFB)", 
                         f"{metrics['server-response-time']['displayValue']}")
                st.metric("Time to Interactive (TTI)", 
                         f"{metrics['interactive']['displayValue']}")
                
            with col2:
                st.markdown("#### Interactivity & Visual Stability")
                st.metric("Total Blocking Time (TBT)", 
                         f"{metrics['total-blocking-time']['displayValue']}")
                st.metric("Interaction to Next Paint (INP)", 
                         f"{metrics.get('interaction-to-next-paint', {}).get('displayValue', 'N/A')}")
                st.metric("Cumulative Layout Shift (CLS)", 
                         f"{metrics['cumulative-layout-shift']['displayValue']}")
            
            st.markdown("### Scores")
            score_col1, score_col2, score_col3, score_col4 = st.columns(4)
            with score_col1:
                st.metric("Performance", 
                         f"{int(categories['performance']['score'] * 100)}%")
            with score_col2:
                st.metric("SEO", 
                         f"{int(categories['seo']['score'] * 100)}%")
            with score_col3:
                st.metric("Accessibility", 
                         f"{int(categories['accessibility']['score'] * 100)}%")
            with score_col4:
                st.metric("Best Practices", 
                         f"{int(categories['best-practices']['score'] * 100)}%")
    
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
