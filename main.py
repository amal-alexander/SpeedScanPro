import streamlit as st
from utils.api_client import PageSpeedInsightsAPI
from utils.seo_analyzer import SEOAnalyzer
from components.header import render_header
from components.metrics_display import display_metrics
from components.report_generator import generate_report
import asyncio
import re
import traceback

# Page configuration
st.set_page_config(
    page_title="SEO Audit Tool",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS for button
st.markdown("""
    <style>
    .stButton > button {
        background: linear-gradient(45deg, #FF4B4B, #FF7676);
        color: white;
        padding: 0.75rem 2rem;
        font-size: 1.2em;
        border: none;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        transform: translateY(0);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.4);
    }
    .stButton > button:active {
        transform: translateY(1px);
    }
    </style>
""", unsafe_allow_html=True)

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

    # URL input with styled container
    st.markdown("""
        <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
        <h2 style='color: #333; margin-bottom: 15px;'>Enter Website URL</h2>
        </div>
    """, unsafe_allow_html=True)

    url = st.text_input("", placeholder="https://example.com")

    # Centered submit button
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        analyze_button = st.button("🚀 Analyze Website")

    if url and analyze_button:
        if not validate_url(url):
            st.error("Please enter a valid URL including http:// or https://")
            return

        with st.spinner("🔍 Analyzing your website..."):
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

                # Styled download button
                st.markdown("""
                    <div style='text-align: center; margin-top: 30px;'>
                    </div>
                """, unsafe_allow_html=True)
                st.download_button(
                    label="📊 Download Full Report",
                    data=report_data,
                    file_name="seo_audit_report.html",
                    mime="text/html"
                )

            except Exception as e:
                error_msg = str(e)
                if "API key not found" in error_msg:
                    st.error("⚠️ Configuration Error: The PageSpeed Insights API key is not properly set up. Please contact support.")
                elif "Failed to fetch metrics" in error_msg:
                    st.error("🌐 Network Error: Unable to fetch data from Google PageSpeed Insights. Please try again later.")
                elif "Invalid API response" in error_msg:
                    st.error("🚫 API Error: Received invalid response from PageSpeed Insights. Please try again later.")
                else:
                    st.error(f"❌ An unexpected error occurred: {error_msg}")

                # Log the full error for debugging
                st.write("Debug information:")
                st.code(traceback.format_exc())

if __name__ == "__main__":
    main()