import trafilatura
from typing import Dict, Any
import streamlit as st

class SEOAnalyzer:
    @st.cache_data(ttl=3600)
    def analyze_content(self, url: str) -> Dict[str, Any]:
        """Analyze on-page SEO elements"""
        try:
            downloaded = trafilatura.fetch_url(url)
            text_content = trafilatura.extract(downloaded)
            
            # Basic content analysis
            word_count = len(text_content.split()) if text_content else 0
            
            # Extract metadata
            metadata = trafilatura.extract_metadata(downloaded)
            
            return {
                'word_count': word_count,
                'title': metadata.title if metadata else None,
                'description': metadata.description if metadata else None,
                'language': metadata.language if metadata else None,
                'text_content': text_content
            }
        except Exception as e:
            raise Exception(f"Content analysis failed: {str(e)}")
