import streamlit as st

def render_header():
    """Render the application header with 3D effects and credits"""
    # Custom CSS for 3D effects
    st.markdown("""
        <style>
        .title-3d {
            font-size: 3em;
            color: #FF4B4B;
            text-shadow: 2px 2px 0px #B83333,
                         4px 4px 0px #982B2B;
            padding: 20px 0;
        }
        .credits {
            font-style: italic;
            color: #666;
            margin: 10px 0;
        }
        .features-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
            transform: perspective(1000px) rotateX(5deg);
            transition: transform 0.3s ease;
        }
        .features-box:hover {
            transform: perspective(1000px) rotateX(0deg);
        }
        </style>
        """, unsafe_allow_html=True)

    # Title with 3D effect
    st.markdown('<h1 class="title-3d">🔍 SEO Audit Tool</h1>', unsafe_allow_html=True)

    # Developer credits
    st.markdown('<p class="credits">Developed with ❤️ by Amal Alexander</p>', unsafe_allow_html=True)

    # Features in 3D box
    st.markdown("""
    <div class="features-box">
    <h3>Features:</h3>
    <ul>
        <li>Page Speed Analysis</li>
        <li>Mobile & Desktop Performance</li>
        <li>On-page SEO Analysis</li>
        <li>Downloadable Reports</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")