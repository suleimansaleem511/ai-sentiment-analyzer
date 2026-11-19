import streamlit as st
from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Download necessary NLTK data safely
@st.cache_resource
def setup_nltk():
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
    except LookupError:
        nltk.download('vader_lexicon', quiet=True)
    try:
        nltk.data.find('corpora/punkt.zip')
    except LookupError:
        nltk.download('punkt', quiet=True)

setup_nltk()

st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
    }
    .sentiment-badge-pos {
        color: #155724;
        background-color: #d4edda;
        padding: 6px 12px;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
    }
    .sentiment-badge-neu {
        color: #856404;
        background-color: #fff3cd;
        padding: 6px 12px;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
    }
    .sentiment-badge-neg {
        color: #721c24;
        background-color: #f8d7da;
        padding: 6px 12px;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=70)
    st.title("Sentiment AI")
    st.markdown("**Developer:** Suleiman Saleem")
    st.markdown("**Specialization:** AI & Machine Learning")
    st.markdown("**University:** Taylor's University")
    st.divider()
    
    analysis_mode = st.radio(
        "Navigation",
        ["🔍 Single Text Analysis", "📊 Batch & CSV Analysis", "ℹ️ About the Project"]
    )
    
    st.divider()
    st.caption("Built with Python, Streamlit, NLTK VADER & TextBlob.")

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    if not text.strip():
        return None
    
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    
    # TextBlob for subjectivity
    blob = TextBlob(text)
    subjectivity = blob.sentiment.subjectivity
    
    if compound >= 0.05:
        sentiment = "Positive"
        badge = "sentiment-badge-pos"
        emoji = "😊"
    elif compound <= -0.05:
        sentiment = "Negative"
        badge = "sentiment-badge-neg"
        emoji = "😞"
    else:
        sentiment = "Neutral"
        badge = "sentiment-badge-neu"
        emoji = "😐"
        
    return {
        "sentiment": sentiment,
        "emoji": emoji,
        "badge": badge,
        "compound": compound,
        "pos": scores['pos'],
        "neu": scores['neu'],
        "neg": scores['neg'],
        "subjectivity": subjectivity
    }

# TAB 1: Single Text
if analysis_mode == "🔍 Single Text Analysis":
    st.title("🧠 AI Sentiment Analysis Engine")
    st.markdown("Analyze emotional tone, polarity, and subjectivity of customer reviews, social media posts, or text data.")
    
    # Presets
    st.subheader("Try an Example:")
    col1, col2, col3 = st.columns(3)
    preset_text = ""
    if col1.button("🌟 Great Product Review"):
        preset_text = "The battery life on this laptop is incredible! Super fast performance, crisp display, and lightweight design. Absolutely worth every penny!"
    if col2.button("⚠️ Mixed / Balanced Review"):
        preset_text = "The hardware design looks sleek and modern, but the customer support was slow and the software had a few bugs during setup."
    if col3.button("❌ Frustrated Customer"):
        preset_text = "Extremely disappointed. The package arrived damaged after two weeks of delay, and the item stopped working within two days. Terrible experience."

    user_input = st.text_area(
        "Enter or paste your text here:",
        value=preset_text,
        height=140,
        placeholder="Type customer feedback, tweet, or product review..."
    )
    
    if st.button("🚀 Analyze Sentiment", type="primary") or user_input:
        if user_input.strip():
            result = analyze_sentiment(user_input)
            
            st.divider()
            
            # Results banner
            res_col1, res_col2, res_col3, res_col4 = st.columns(4)
            with res_col1:
                st.markdown(f"### Result")
                st.markdown(f"<span class='{result['badge']}'>{result['emoji']} {result['sentiment']}</span>", unsafe_allow_html=True)
            with res_col2:
                st.metric("Compound Score", f"{result['compound']:+.3f}", help="-1.0 (Most Negative) to +1.0 (Most Positive)")
            with res_col3:
                st.metric("Positivity Index", f"{int(result['pos'] * 100)}%")
            with res_col4:
                st.metric("Subjectivity", f"{int(result['subjectivity'] * 100)}%", help="0% = Objective Fact, 100% = Personal Opinion")
            
            st.markdown("---")
            
            # Charts
            chart_col1, chart_col2 = st.columns(2)
            
            with chart_col1:
                st.subheader("📊 Sentiment Composition Breakdown")
                breakdown_df = pd.DataFrame({
                    "Component": ["Positive", "Neutral", "Negative"],
                    "Score": [result['pos'], result['neu'], result['neg']],
                    "Color": ["#28a745", "#ffc107", "#dc3545"]
                })
                fig = px.bar(
                    breakdown_df,
                    x="Component",
                    y="Score",
                    color="Component",
                    color_discrete_map={"Positive": "#2ecc71", "Neutral": "#f39c12", "Negative": "#e74c3c"},
                    range_y=[0, 1]
                )
                fig.update_layout(showlegend=False, height=300, margin=dict(l=20, r=20, t=30, b=20))
                st.plotly_chart(fig, use_container_width=True)
                
            with chart_col2:
                st.subheader("🎯 Polarity Gauge")
                gauge_val = (result['compound'] + 1) / 2 * 100  # Map [-1, 1] to [0, 100]
                fig_gauge = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=result['compound'],
                    title={'text': "Polarity (-1 to +1)"},
                    gauge={
                        'axis': {'range': [-1, 1]},
                        'bar': {'color': "#34495e"},
                        'steps': [
                            {'range': [-1, -0.05], 'color': "#ffb3b3"},
                            {'range': [-0.05, 0.05], 'color': "#fff3cd"},
                            {'range': [0.05, 1], 'color': "#b3ffcc"}
                        ],
                        'threshold': {
                            'line': {'color': "black", 'width': 4},
                            'thickness': 0.75,
                            'value': result['compound']
                        }
                    }
                ))
                fig_gauge.update_layout(height=300, margin=dict(l=20, r=20, t=30, b=20))
                st.plotly_chart(fig_gauge, use_container_width=True)
        else:
            st.info("👆 Enter some text above or click one of the example buttons to analyze.")

# TAB 2: Batch Analysis
elif analysis_mode == "📊 Batch & CSV Analysis":
    st.title("📁 Batch Sentiment Analysis")
    st.markdown("Upload a CSV file containing user reviews, feedback, or social media comments to analyze at scale.")
    
    uploaded_file = st.file_uploader("Upload CSV file (must contain a text column)", type=["csv"])
    
    # Or load sample dataset
    if st.button("📥 Load Sample E-Commerce Dataset (5 Reviews)"):
        sample_data = {
            "Review_ID": [101, 102, 103, 104, 105],
            "Product": ["Wireless Headphones", "Mechanical Keyboard", "USB-C Hub", "Smart Watch", "Gaming Mouse"],
            "Customer_Review": [
                "Absolutely love the noise cancellation. Super comfortable for long flights!",
                "Keys feel nice and tactile, but the spacebar rattles a little bit.",
                "Complete waste of money. Disconnected constantly and overheated within an hour.",
                "Great battery life and clear screen. Accurate heart rate monitor.",
                "Average mouse. Nothing special, but works fine for daily office tasks."
            ]
        }
        st.session_state['batch_df'] = pd.DataFrame(sample_data)
        
    df = None
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state['batch_df'] = df
        except Exception as e:
            st.error(f"Error reading file: {e}")
            
    if 'batch_df' in st.session_state:
        df = st.session_state['batch_df']
        st.write("### Preview Data:")
        st.dataframe(df.head(), use_container_width=True)
        
        text_col = st.selectbox("Select the column containing the text to analyze:", df.columns)
        
        if st.button("⚡ Run Batch Analysis", type="primary"):
            with st.spinner("Analyzing all reviews..."):
                results = []
                for text in df[text_col].astype(str):
                    res = analyze_sentiment(text)
                    results.append({
                        "Sentiment": res["sentiment"],
                        "Compound": res["compound"],
                        "Positivity": res["pos"],
                        "Neutrality": res["neu"],
                        "Negativity": res["neg"]
                    })
                
                res_df = pd.concat([df, pd.DataFrame(results)], axis=1)
                st.session_state['analyzed_df'] = res_df
                
    if 'analyzed_df' in st.session_state:
        analyzed_df = st.session_state['analyzed_df']
        st.success("✅ Analysis Complete!")
        
        # Summary metrics
        total = len(analyzed_df)
        pos_count = (analyzed_df['Sentiment'] == 'Positive').sum()
        neu_count = (analyzed_df['Sentiment'] == 'Neutral').sum()
        neg_count = (analyzed_df['Sentiment'] == 'Negative').sum()
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Analyzed", total)
        m2.metric("Positive", f"{pos_count} ({int(pos_count/total*100)}%)")
        m3.metric("Neutral", f"{neu_count} ({int(neu_count/total*100)}%)")
        m4.metric("Negative", f"{neg_count} ({int(neg_count/total*100)}%)")
        
        c1, c2 = st.columns(2)
        with c1:
            fig_pie = px.pie(
                analyzed_df,
                names="Sentiment",
                title="Overall Sentiment Distribution",
                color="Sentiment",
                color_discrete_map={"Positive": "#2ecc71", "Neutral": "#f1c40f", "Negative": "#e74c3c"}
            )
            st.plotly_chart(fig_pie, use_container_width=True)
            
        with c2:
            fig_hist = px.histogram(
                analyzed_df,
                x="Compound",
                nbins=20,
                title="Polarity Score Distribution (-1 to +1)",
                color_discrete_sequence=["#3498db"]
            )
            st.plotly_chart(fig_hist, use_container_width=True)
            
        st.write("### Detailed Results:")
        st.dataframe(analyzed_df, use_container_width=True)
        
        csv_data = analyzed_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv_data,
            file_name="sentiment_analysis_results.csv",
            mime="text/csv"
        )

# TAB 3: About
else:
    st.title("ℹ️ About This Project")
    st.markdown("""
    ### 🎯 Overview
    This project is an **AI-powered Natural Language Processing (NLP) application** engineered to automatically extract sentiment, subjectivity, and emotional orientation from unstructured text data.

    ### 🛠️ Architecture: Lexicon-Based NLP
    - **Model:** NLTK VADER (Valence Aware Dictionary and sEntiment Reasoner)
    - **Mechanism:** Rule-based lexical analysis using 7,500+ human-annotated sentiment scores, negation detection, and degree modifiers (not a trained machine learning classifier).
    - **Subjectivity:** TextBlob polarity & subjectivity analysis
    - **Frontend:** Streamlit
    - **Visualizations:** Plotly Interactive Charts

    ### 👨‍💻 Developer Information
    - **Author:** Suleiman Saleem
    - **Degree:** Bachelor of Computer Science (Honours) — AI Specialization
    - **Institution:** Taylor's University
    """)
