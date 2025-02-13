import streamlit as st
from utils.api_client import PageSpeedInsightsAPI
from utils.seo_analyzer import SEOAnalyzer
from components.header import render_header
from components.metrics_display import display_metrics
from components.report_generator import generate_report
import asyncio
import re

# Page configuration
st.set_page_config(
    page_title="SEO Audit Tool",
    page_icon="🔍",
    layout="wide"
)

@st.cache_data(ttl=3600)
def validate_url(url):
    """Validate URL format"""
    pattern = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(pattern.match(url))

def main():
    render_header()
    
    # URL input
    url = st.text_input("Enter website URL to analyze", placeholder="https://example.com")
    
    if url:
        if not validate_url(url):
            st.error("Please enter a valid URL including http:// or https://")
            return
            
        with st.spinner("Analyzing your website..."):
            try:
                # Initialize API client and analyzer
                api_client = PageSpeedInsightsAPI()
                seo_analyzer = SEOAnalyzer()
                
                # Get desktop metrics
                desktop_results = api_client.get_metrics(url, strategy="desktop")
                
                # Get mobile metrics
                mobile_results = api_client.get_metrics(url, strategy="mobile")
                
                # Display metrics
                display_metrics(desktop_results, mobile_results)
                
                # Generate downloadable report
                report_data = generate_report(url, desktop_results, mobile_results)
                
                # Download button
                st.download_button(
                    label="Download Full Report",
                    data=report_data,
                    file_name="seo_audit_report.html",
                    mime="text/html"
                )
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
