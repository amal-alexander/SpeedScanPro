import streamlit as st

def render_header():
    """Render the application header with 3D effects and credits"""
    # Custom CSS for 3D effects and dark mode
    st.markdown("""
        <style>
        @keyframes rotate {
            from { transform: rotate3d(0, 1, 0, 0deg); }
            to { transform: rotate3d(0, 1, 0, 360deg); }
        }
        
        .earth-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at center, rgba(24, 98, 204, 0.1) 0%, rgba(13, 37, 87, 0.1) 100%);
            z-index: -1;
            animation: rotate 60s linear infinite;
            pointer-events: none;
        }
        
        .title-3d {
            font-size: min(3em, 10vw);
            color: #FF4B4B;
            text-shadow: 2px 2px 0px #B83333,
                         4px 4px 0px #982B2B;
            padding: 20px 0;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(5px);
            border-radius: 15px;
            margin: 20px;
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

    # Custom CSS for header components
    st.markdown("""
    <style>
    .title-3d {
        text-align: center;
        color: white;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .credits {
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .features-box {
        background: rgba(30, 35, 41, 0.75);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
    }
    .features-box h3 {
        margin-bottom: 1rem;
        color: #FF4B4B;
    }
    .features-box ul {
        list-style-type: none;
        padding-left: 0;
    }
    .features-box li {
        padding: 0.5rem 0;
        margin-bottom: 0.5rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
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