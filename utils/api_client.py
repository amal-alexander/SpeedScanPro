import requests
import streamlit as st

class PageSpeedInsightsAPI:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

    @staticmethod
    @st.cache_data(ttl=3600, show_spinner=False)
    def _fetch_metrics(base_url: str, url: str, strategy: str = "desktop"):
        """
        Cached function to fetch PageSpeed Insights metrics
        """
        params = {
            'url': url,
            'strategy': strategy,
            'category': ['performance', 'accessibility', 'best-practices', 'seo']
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch metrics: {str(e)}")

    def get_metrics(self, url: str, strategy: str = "desktop"):
        """
        Public method to get PageSpeed Insights metrics
        """
        return self._fetch_metrics(self.base_url, url, strategy)