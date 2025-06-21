import streamlit as st
from PIL import Image
import base64

# Page config
st.set_page_config(
    page_title="Subhan Ahmed Chandio - Digital Resume",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS for dark theme with cool animations
st.markdown("""
<style>
    /* Dark theme background */
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #1a1a2e 75%, #0c0c0c 100%);
        background-attachment: fixed;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main header with cool gradient and animation */
    .main-header {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 2px solid rgba(255,255,255,0.1);
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Section headers with glow effect */
    .section-header {
        color: #00f5ff;
        text-shadow: 0 0 20px #00f5ff;
        border-bottom: 3px solid #00f5ff;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        font-weight: bold;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 20px #00f5ff; }
        to { text-shadow: 0 0 30px #00f5ff, 0 0 40px #00f5ff; }
    }
    
    /* Cool skill tags */
    .skill-tag {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        margin: 0.3rem;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .skill-tag:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
    }
    
    /* Contact info cards */
    .contact-info {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        transition: transform 0.3s ease;
    }
    
    .contact-info:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.4);
    }
    
    /* Experience boxes with cool styling */
    .experience-box {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .experience-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left 0.5s;
    }
    
    .experience-box:hover::before {
        left: 100%;
    }
    
    /* Project cards with neon effect */
    .project-card {
        background: linear-gradient(135deg, #0f4c75, #3282b8);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin: 1rem 0;
        border: 2px solid #00f5ff;
        position: relative;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 25px #00f5ff;
    }
    
    /* White text for all content */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown h1, 
    .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: white !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1a1a2e, #16213e);
        border-right: 2px solid #00f5ff;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    }
    
    /* Metrics styling */
    .metric-container {
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* Floating animation for elements */
    .floating {
        animation: floating 3s ease-in-out infinite;
    }
    
    @keyframes floating {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
</style>
""", unsafe_allow_html=True)

# Header with animated gradient
st.markdown("""
<div class="main-header floating">
    <h1 style="font-size: 3rem; margin-bottom: 0.5rem;">🚀 SUBHAN AHMED CHANDIO</h1>
    <h2 style="font-size: 1.8rem; margin-bottom: 1rem;">Software Engineering Student & Python Developer</h2>
    <p style="font-size: 1.2rem; font-weight: 300;">💻 Building the future, one line of code at a time ✨</p>
</div>
""", unsafe_allow_html=True)

# Contact section with hover effects
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="contact-info">
        <h3 style="color: #00f5ff; margin-bottom: 1rem;">📞 CONTACT</h3>
        <p style="font-size: 1.1rem; margin-bottom: 0.5rem;">+92 3193476353</p>
        <p style="font-size: 1rem;">📧 subhanahmed0987654@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-info">
        <h3 style="color: #00f5ff; margin-bottom: 1rem;">📍 LOCATION</h3>
        <p style="font-size: 1.1rem; margin-bottom: 0.5rem;">Qasimabad, Hyderabad</p>
        <p style="font-size: 1rem;">🇵🇰 Sindh, Pakistan</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="contact-info">
        <h3 style="color: #00f5ff; margin-bottom: 1rem;">🔗 CONNECT</h3>
        <p style="font-size: 1.1rem; margin-bottom: 0.5rem;">💼 LinkedIn Profile</p>
        <p style="font-size: 1rem;">🐙 GitHub | ✍️ Medium</p>
    </div>
    """, unsafe_allow_html=True)

# Objective with white text
st.markdown('<h2 class="section-header">🎯 OBJECTIVE</h2>', unsafe_allow_html=True)
st.markdown("""
<p style="color: white; font-size: 1.1rem; line-height: 1.6; text-align: justify;">
Motivated and detail-oriented Software Engineering undergraduate with a strong foundation in Python programming,
data structures, and problem-solving. Seeking a Python development internship to contribute to impactful projects,
enhance technical skills, and gain hands-on experience in real-world software development.
</p>
""", unsafe_allow_html=True)

# Education
st.markdown('<h2 class="section-header">🎓 EDUCATION</h2>', unsafe_allow_html=True)
st.markdown("""
<div style="color: white; font-size: 1.1rem; line-height: 1.8;">
<strong style="color: #00f5ff; font-size: 1.3rem;">Bachelor of Software Engineering</strong> | <em style="color: #feca57;">University of Sindh</em><br>
<strong>Duration:</strong> 2023 – Expected 2026<br>
<strong>Major:</strong> Software Engineering
</div>
""", unsafe_allow_html=True)

# Skills with animated tags
st.markdown('<h2 class="section-header">💻 TECHNICAL SKILLS</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<h4 style="color: #00f5ff; margin-bottom: 1rem;">🐍 Programming Languages</h4>', unsafe_allow_html=True)
    skills_prog = ["Python (Intermediate)", "Java", "SQL", "HTML", "CSS"]
    for skill in skills_prog:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown('<h4 style="color: #00f5ff; margin: 2rem 0 1rem 0;">🛠️ Libraries & Tools</h4>', unsafe_allow_html=True)
    skills_tools = ["Pandas", "NumPy", "Firebase", "Tkinter", "SQLite", "Git"]
    for skill in skills_tools:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

with col2:
    st.markdown('<h4 style="color: #00f5ff; margin-bottom: 1rem;">🧠 Core Concepts</h4>', unsafe_allow_html=True)
    skills_concepts = ["OOP", "Data Structures", "File Handling", "GUI Programming"]
    for skill in skills_concepts:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown('<h4 style="color: #00f5ff; margin: 2rem 0 1rem 0;">🤝 Soft Skills</h4>', unsafe_allow_html=True)
    skills_soft = ["Team Collaboration", "Communication", "Time Management", "Problem Solving"]
    for skill in skills_soft:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

# Experience with cool animations
st.markdown('<h2 class="section-header">💼 EXPERIENCE</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="experience-box">
    <h3 style="color: #feca57; margin-bottom: 0.5rem;">📱 Android Developer</h3>
    <p style="font-size: 1.2rem; margin-bottom: 0.5rem;"><strong>Health is Wealth Gym</strong> | Qasimabad, Hyderabad</p>
    <p style="color: #b8e6b8; margin-bottom: 1rem;"><em>Jan 2024 – Apr 2024</em></p>
    <ul style="line-height: 1.8; font-size: 1.1rem;">
        <li>🚀 Developed an all-in-one gym admin app handling member data, payments, notifications, and reporting</li>
        <li>⚡ Boosted operational efficiency by reducing manual data handling through Firebase integration and modern UI design</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Projects with neon effects
st.markdown('<h2 class="section-header">🚀 FEATURED PROJECTS</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="project-card">
    <h3 style="color: #feca57; margin-bottom: 1rem;">📦 Inventory Management System</h3>
    <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1rem;">
    Developed a command-line based inventory manager that allows product addition, sales recording, 
    stock updates, and CSV export. Implemented file I/O, dictionaries, and modular functions.
    </p>
    <p style="color: #b8e6b8; font-weight: bold;">🔧 Tech Stack: Python, File I/O, Data Structures</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="project-card">
    <h3 style="color: #feca57; margin-bottom: 1rem;">🧠 Text-Based Quiz App with Score Tracker</h3>
    <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1rem;">
    Built a CLI quiz app using classes and question banks. Tracks score, provides feedback, 
    and supports multiple quiz rounds. Great use of loops, conditionals, and OOP.
    </p>
    <p style="color: #b8e6b8; font-weight: bold;">🔧 Tech Stack: Python, OOP, Data Management</p>
</div>
""", unsafe_allow_html=True)

# Certifications
st.markdown('<h2 class="section-header">🏆 CERTIFICATIONS</h2>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="color: white; font-size: 1.1rem; line-height: 1.8;">
    <strong style="color: #feca57;">🐍 Google Crash Course on Python</strong><br>
    <em style="color: #b8e6b8;">Coursera</em> | <a href="#" style="color: #00f5ff;">Verify Certificate</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="color: white; font-size: 1.1rem; line-height: 1.8;">
    <strong style="color: #feca57;">🤖 IBM Python for Data Science and AI</strong><br>
    <em style="color: #b8e6b8;">Coursera</em> | <a href="#" style="color: #00f5ff;">Verify Certificate</a>
    </div>
    """, unsafe_allow_html=True)

# Leadership
st.markdown('<h2 class="section-header">👑 LEADERSHIP & PROGRAMS</h2>', unsafe_allow_html=True)
st.markdown("""
<div style="color: white; font-size: 1.1rem; line-height: 1.8;">
<strong style="color: #feca57; font-size: 1.3rem;">🎓 Aspire Leadership Program – Harvard University</strong><br>
<em style="color: #b8e6b8;">Cohort 1, 2025</em><br>
Selected among top university candidates across Pakistan to participate in global leadership training.
</div>
""", unsafe_allow_html=True)

# Extra-curricular
st.markdown('<h2 class="section-header">🌟 EXTRA-CURRICULAR ACTIVITIES</h2>', unsafe_allow_html=True)
activities = [
    "📸 Photography enthusiast – maintains an online gallery of street photography and local landscapes",
    "🏏 Regularly plays and manages a local cricket team in weekend tournaments", 
    "✍️ Writes blogs on tech, coding tips, and student experiences on Medium"
]

for activity in activities:
    st.markdown(f'<p style="color: white; font-size: 1.1rem; margin-bottom: 0.8rem;">• {activity}</p>', unsafe_allow_html=True)

# Cool footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 3rem; background: linear-gradient(45deg, #667eea, #764ba2); border-radius: 15px; margin-top: 2rem;">
    <h2 style="color: white; margin-bottom: 1rem;">✨ Thank you for viewing my resume! 🙏</h2>
    <p style="color: white; font-size: 1.2rem;">Ready to contribute to innovative projects and grow as a Python developer 🚀</p>
</div>
""", unsafe_allow_html=True)

# Enhanced sidebar
with st.sidebar:
    st.markdown('<h2 style="color: #00f5ff; text-align: center; margin-bottom: 2rem;">📊 QUICK STATS</h2>', unsafe_allow_html=True)
    
    # Custom metrics with styling
    st.markdown("""
    <div class="metric-container">
        <h3 style="color: #feca57;">📚 Academic Year</h3>
        <p style="color: white; font-size: 1.2rem; font-weight: bold;">3rd Year Student</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="metric-container">
        <h3 style="color: #feca57;">💻 Coding Experience</h3>
        <p style="color: white; font-size: 1.2rem; font-weight: bold;">2+ Years</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="metric-container">
        <h3 style="color: #feca57;">🚀 Projects</h3>
        <p style="color: white; font-size: 1.2rem; font-weight: bold;">10+ Completed</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="metric-container">
        <h3 style="color: #feca57;">🏆 Certifications</h3>
        <p style="color: white; font-size: 1.2rem; font-weight: bold;">2 Earned</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<h3 style="color: #00f5ff;">🔥 Currently Learning</h3>', unsafe_allow_html=True)
    learning_items = ["• Advanced Python Frameworks", "• Machine Learning", "• Web Development", "• Data Science"]
    for item in learning_items:
        st.markdown(f'<p style="color: white; margin-bottom: 0.5rem;">{item}</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<h3 style="color: #00f5ff;">💡 Fun Fact</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: white; line-height: 1.6;">I manage a cricket team and love capturing street photography in my free time! 📸🏏</p>', unsafe_allow_html=True)

# Interactive buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("📧 Get Contact Info"):
        st.balloons()
        st.success("📞 +92 3193476353 | 📧 subhanahmed0987654@gmail.com")

with col2:
    if st.button("📄 Download Resume"):
        st.snow()
        st.info("🎉 PDF download feature coming soon!")
