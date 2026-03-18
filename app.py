import streamlit as st

# --- 1. CONFIG & ELITE APPLE/GEMINI UI ---
st.set_page_config(page_title="Akash | AI Product Portfolio", layout="wide", page_icon="💎")

st.markdown("""
    <style>
    /* Ultra-Clean White Theme */
    .stApp { background-color: #ffffff; color: #1d1d1f; }
    
    /* Hero Section - Apple Style */
    .hero {
        padding: 80px 20px;
        text-align: center;
        background: radial-gradient(circle at center, #f5f5f7 0%, #ffffff 100%);
        border-radius: 40px;
        margin-bottom: 50px;
    }
    
    /* Project Cards with Glassmorphism Hover */
    .project-card {
        background: #ffffff;
        padding: 35px;
        border-radius: 24px;
        border: 1px solid #e0e0e0;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .project-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 30px 60px rgba(0,0,0,0.08);
        border-color: #1a73e8;
    }
    
    .status-tag {
        font-size: 0.75em;
        background: #e8f0fe;
        color: #1a73e8;
        padding: 5px 14px;
        border-radius: 30px;
        font-weight: 700;
        letter-spacing: 0.5px;
        display: inline-block;
        margin-bottom: 15px;
    }

    h1, h2 { color: #1d1d1f; font-family: 'SF Pro Display', sans-serif; }
    p { color: #515154; line-height: 1.6; }

    /* Custom Button Styling */
    .stButton>button {
        background: #1d1d1f;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 25px;
        font-weight: 500;
        width: 100%;
        transition: background 0.3s;
    }
    .stButton>button:hover {
        background: #1a73e8;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
    <div class="hero">
        <h1 style="font-size: 3.5em; font-weight: 800; letter-spacing: -1px; margin-bottom: 15px;">Akash</h1>
        <p style="font-size: 1.3em; font-weight: 400; max-width: 800px; margin: 0 auto; color: #515154;">
            AI Product Strategist & Developer. <br>
            Engineering decision-intelligence tools that bridge high-level 
            business frameworks with advanced data architectures.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. PROJECT GRID ---
st.markdown("<h3 style='margin-bottom:30px; text-align:center;'>Deployments</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div class="project-card">
            <div>
                <span class="status-tag">Live: Fintech Analytics</span>
                <h2>Quantum AI</h2>
                <p>
                    A predictive market intelligence engine. Designed to analyze complex financial 
                    datasets and synthesize real-time investment insights through advanced 
                    mathematical modeling.
                </p>
                <p style="font-size: 0.8em; color: #8e8e93; font-weight: 600;">STACK: PYTHON • PREDICTIVE MODELING • PLOTLY</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Launch Quantum AI", "https://quantum-ai.streamlit.app/")

with col2:
    st.markdown("""
        <div class="project-card">
            <div>
                <span class="status-tag">Live: Strategic Product</span>
                <h2>Quantum Stratagem</h2>
                <p>
                    An elite prioritization engine for Product Owners. Implements dual-logic 
                    frameworks (RICE & WSJF) to transform raw venture goals into 
                    structured, economic-priority roadmaps.
                </p>
                <p style="font-size: 0.8em; color: #8e8e93; font-weight: 600;">STACK: BI LOGIC • ROADMAP SYNTHESIS • DATA EDITOR</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Launch Quantum Stratagem", "https://quantum-stratagem-ai.streamlit.app/")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

# --- 4. CONTACT & FOOTER ---
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**LinkedIn** \n[View Profile](https://linkedin.com/in/your-profile)") # Update this link
with c2:
    st.markdown("**GitHub** \n[Source Code](https://github.com/your-username)") # Update this link
with c3:
    st.markdown("**Location** \nGlobal / Remote")

st.markdown("<br>", unsafe_allow_html=True)
st.caption("© 2026 Akash | Lead Architect | Built with Python 3.11")
