import requests
import streamlit as st

class PageSpeedInsightsAPI:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

    @st.cache_data(ttl=3600, show_spinner=False)
    def get_metrics(self, _self, url: str, strategy: str = "desktop"):
        """
        Fetch PageSpeed Insights metrics for the given URL
        """
        params = {
            'url': url,
            'strategy': strategy,
            'category': ['performance', 'accessibility', 'best-practices', 'seo']
        }

        try:
            response = requests.get(_self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch metrics: {str(e)}")