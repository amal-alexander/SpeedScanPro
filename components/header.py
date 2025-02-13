import streamlit as st

def render_header():
    """Render the application header"""
    st.title("🔍 SEO Audit Tool")
    
    st.markdown("""
    Get comprehensive insights about your website's performance, accessibility, 
    and SEO metrics for both desktop and mobile devices.
    
    ### Features:
    - Page Speed Analysis
    - Mobile & Desktop Performance
    - On-page SEO Analysis
    - Downloadable Reports
    """)
    
    st.markdown("---")
