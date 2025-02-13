import requests
import streamlit as st
import os

class PageSpeedInsightsAPI:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
        self.api_key = os.environ.get("PAGESPEED_API_KEY")
        if not self.api_key:
            raise Exception("PageSpeed API key not found. Please set the PAGESPEED_API_KEY environment variable.")

    @staticmethod
    @st.cache_data(ttl=3600, show_spinner=False)
    def _fetch_metrics(base_url: str, api_key: str, url: str, strategy: str = "desktop"):
        """
        Cached function to fetch PageSpeed Insights metrics
        """
        params = {
            'url': url,
            'strategy': strategy,
            'category': ['performance', 'accessibility', 'best-practices', 'seo'],
            'key': api_key
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()

            # Check if we have the lighthouse results
            if 'lighthouseResult' not in data:
                raise Exception("Invalid API response: No lighthouse results found")

            # Restructure the response to match our expected format
            return {
                'lighthouse_result': {
                    'categories': {
                        'performance': {
                            'score': data['lighthouseResult']['categories']['performance']['score']
                        },
                        'accessibility': {
                            'score': data['lighthouseResult']['categories']['accessibility']['score']
                        },
                        'best-practices': {
                            'score': data['lighthouseResult']['categories']['bestPractices']['score']
                        },
                        'seo': {
                            'score': data['lighthouseResult']['categories']['seo']['score']
                        }
                    },
                    'audits': {
                        'first-contentful-paint': {
                            'displayValue': data['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
                        },
                        'interactive': {
                            'displayValue': data['lighthouseResult']['audits']['interactive']['displayValue']
                        }
                    }
                }
            }
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch metrics: {str(e)}")
        except KeyError as e:
            raise Exception(f"Invalid API response format: {str(e)}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def get_metrics(self, url: str, strategy: str = "desktop"):
        """
        Public method to get PageSpeed Insights metrics
        """
        return self._fetch_metrics(self.base_url, self.api_key, url, strategy)