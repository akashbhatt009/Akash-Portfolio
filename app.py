import streamlit as st

# --- 1. CONFIG & EXECUTIVE UI ---
st.set_page_config(page_title="Akash Bhatt | Strategic Product Portfolio", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1d1d1f; }
    
    /* Executive Hero Section */
    .hero {
        padding: 90px 20px;
        text-align: center;
        background: radial-gradient(circle at center, #f8f9fa 0%, #ffffff 100%);
        border-radius: 40px;
        margin-bottom: 50px;
        border: 1px solid #f1f3f4;
    }
    
    /* High-Value Project Cards */
    .project-card {
        background: #ffffff;
        padding: 40px;
        border-radius: 28px;
        border: 1px solid #e8eaed;
        transition: all 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .project-card:hover {
        transform: translateY(-15px);
        box-shadow: 0 40px 80px rgba(0,0,0,0.06);
        border-color: #1a73e8;
    }
    
    .status-tag {
        font-size: 0.75em;
        background: #f1f3f4;
        color: #3c4043;
        padding: 6px 16px;
        border-radius: 30px;
        font-weight: 800;
        letter-spacing: 0.8px;
        display: inline-block;
        margin-bottom: 20px;
        border: 1px solid #dadce0;
    }

    h1, h2 { color: #202124; font-family: 'Inter', sans-serif; letter-spacing: -0.5px; }
    p { color: #5f6368; line-height: 1.7; font-size: 1.05em; }

    /* Action Button Styling */
    .stButton>button {
        background: #202124;
        color: white;
        border-radius: 14px;
        border: none;
        padding: 12px 30px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background: #1a73e8;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. EXECUTIVE HERO SECTION ---
st.markdown("""
    <div class="hero">
        <h1 style="font-size: 4em; font-weight: 800; margin-bottom: 20px;">Akash Bhatt</h1>
        <p style="font-size: 1.4em; font-weight: 400; max-width: 850px; margin: 0 auto; color: #3c4043;">
            <b>Strategic Product Owner & Business Analyst.</b><br>
            Architecting data-driven solutions to optimize product lifecycles, 
            streamline stakeholder alignment, and maximize ROI through 
            quantitative prioritization frameworks.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. STRATEGIC DEPLOYMENTS ---
st.markdown("<h3 style='margin-bottom:40px; text-align:center; font-weight:700;'>Executive Product Suite</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div class="project-card">
            <div>
                <span class="status-tag">FINANCIAL INTELLIGENCE</span>
                <h2>Quantum AI</h2>
                <p>
                    A decision-support engine for high-stakes financial environments. 
                    Translates complex market volatility into actionable <b>Business Intelligence</b>, 
                    enabling stakeholders to identify alpha opportunities through predictive 
                    visualization and risk-modeling.
                </p>
                <p style="font-size: 0.85em; color: #1a73e8; font-weight: 700; margin-top: 15px;">
                    DOMAIN: FINTECH • PREDICTIVE ANALYTICS • DATA ARCHITECTURE
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Review Quantum AI", "https://quantum-ai.streamlit.app/")

with col2:
    st.markdown("""
        <div class="project-card">
            <div>
                <span class="status-tag">STRATEGIC GOVERNANCE</span>
                <h2>Quantum Stratagem</h2>
                <p>
                    A digital governance tool for <b>Backlog Prioritization</b>. Implements 
                    standardized RICE and WSJF (Weighted Shortest Job First) frameworks 
                    to quantify "Value vs. Effort," ensuring delivery teams focus on 
                    highest-impact business outcomes.
                </p>
                <p style="font-size: 0.85em; color: #1a73e8; font-weight: 700; margin-top: 15px;">
                    DOMAIN: PRODUCT GOVERNANCE • SAFe • AGILE ROADMAPPING
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Review Quantum Stratagem", "https://quantum-stratagem-ai.streamlit.app/")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

# --- 4. CONTACT & GOVERNANCE ---
# --- 4. EXECUTIVE CONTACT & INQUIRY ---
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>Professional Inquiry</h3>", unsafe_allow_html=True)

# This creates a clean, centered contact box
contact_col1, contact_col2, contact_col3 = st.columns([1, 2, 1])

with contact_col2:
    st.markdown("""
        <div style="background-color: #f8f9fa; padding: 25px; border-radius: 15px; border: 1px solid #e8eaed; text-align: center;">
            <p style="margin-bottom: 10px;"><b>Akash Bhatt</b></p>
            <p style="margin-bottom: 10px; color: #5f6368;"></p>
            <hr style="margin: 15px 0;">
            <p style="font-size: 1.1em;">📧 <b>akashbhatt009@gmail.com</b></p>
            <p style="font-size: 0.9em; color: #1a73e8; margin-top: 10px;"></p>
        </div>
    """, unsafe_allow_html=True)
    
    # Optional: Keep the GitHub link but as a simple button
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("View Technical Architectures (GitHub)", "https://github.com/akashbhatt009", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Akash Bhatt | Product Owner/Business Analyst | Optimized for Executive Review")
