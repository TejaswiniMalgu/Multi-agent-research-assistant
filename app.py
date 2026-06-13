import streamlit as st
import sys
import os

# ── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Research Assistant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── GLOBAL CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* Reset & base */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0a0f;
    color: #e2e2e8;
}

.stApp {
    background-color: #0a0a0f;
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem 3rem; max-width: 900px; margin: 0 auto; }

/* ── HERO ── */
.hero {
    text-align: center;
    padding: 3.5rem 0 2rem 0;
    border-bottom: 1px solid #1e1e2e;
    margin-bottom: 2.5rem;
}
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    color: #6c63ff;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}
.hero-title {
    font-size: 2.4rem;
    font-weight: 600;
    letter-spacing: -0.03em;
    color: #f0f0f8;
    line-height: 1.15;
    margin-bottom: 0.6rem;
}
.hero-sub {
    font-size: 0.95rem;
    color: #6b6b80;
    font-weight: 300;
    letter-spacing: 0.01em;
}

/* ── INPUT AREA ── */
.stTextInput > div > div > input {
    background-color: #12121c !important;
    border: 1px solid #2a2a3e !important;
    border-radius: 8px !important;
    color: #e2e2e8 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.75rem 1rem !important;
    transition: border-color 0.2s ease;
}
.stTextInput > div > div > input:focus {
    border-color: #6c63ff !important;
    box-shadow: 0 0 0 2px rgba(108, 99, 255, 0.15) !important;
}
.stTextInput > label {
    color: #9090a8 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    font-weight: 500 !important;
}

/* ── BUTTON ── */
.stButton > button {
    background: linear-gradient(135deg, #6c63ff 0%, #4f46e5 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    padding: 0.65rem 2rem !important;
    cursor: pointer !important;
    transition: opacity 0.2s ease, transform 0.1s ease !important;
    letter-spacing: 0.02em !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── PIPELINE STEP CARDS ── */
.step-card {
    background: #12121c;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
    transition: border-color 0.3s ease;
}
.step-card.active {
    border-color: #6c63ff;
    box-shadow: 0 0 0 1px rgba(108,99,255,0.2);
}
.step-card.done {
    border-color: #22c55e;
}
.step-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0;
}
.step-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #6c63ff;
    letter-spacing: 0.1em;
    background: rgba(108,99,255,0.1);
    border-radius: 4px;
    padding: 0.15rem 0.45rem;
}
.step-num.done { color: #22c55e; background: rgba(34,197,94,0.1); }
.step-label {
    font-size: 0.85rem;
    font-weight: 500;
    color: #c0c0d0;
}
.step-status {
    margin-left: auto;
    font-size: 0.75rem;
    color: #6b6b80;
    font-family: 'JetBrains Mono', monospace;
}
.step-status.running { color: #f59e0b; }
.step-status.done { color: #22c55e; }

/* ── OUTPUT PANELS ── */
.output-panel {
    background: #0e0e1a;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    padding: 1.5rem;
    margin-top: 1.5rem;
}
.panel-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    color: #6c63ff;
    text-transform: uppercase;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.panel-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1e1e2e;
}
.report-text {
    font-size: 0.92rem;
    line-height: 1.75;
    color: #d0d0e0;
    white-space: pre-wrap;
}
.critic-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    line-height: 1.7;
    color: #b0b0c8;
    white-space: pre-wrap;
}

/* ── SCORE BADGE ── */
.score-badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.4rem;
    font-weight: 500;
    color: #6c63ff;
    background: rgba(108,99,255,0.1);
    border: 1px solid rgba(108,99,255,0.3);
    border-radius: 8px;
    padding: 0.4rem 1.1rem;
    margin-bottom: 1rem;
}

/* ── EXPANDERS ── */
.streamlit-expanderHeader {
    background: #12121c !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 8px !important;
    color: #9090a8 !important;
    font-size: 0.8rem !important;
    font-family: 'JetBrains Mono', monospace !important;
}
.streamlit-expanderContent {
    background: #0e0e1a !important;
    border: 1px solid #1e1e2e !important;
    border-top: none !important;
}

/* ── DIVIDER ── */
hr { border-color: #1e1e2e !important; margin: 2rem 0 !important; }

/* ── TOAST / STATUS ── */
.stAlert {
    background: #12121c !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 8px !important;
    color: #d0d0e0 !important;
}
</style>
""", unsafe_allow_html=True)


# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">Multi-Agent · Tavily · Mistral</div>
    <div class="hero-title">Research Assistant</div>
    <div class="hero-sub">Search → Read → Write → Critique — automated, end to end.</div>
</div>
""", unsafe_allow_html=True)


# ── PIPELINE STEP RENDERER ─────────────────────────────────────────────────────
def step_card(num: str, label: str, state: str = "idle"):
    num_cls = "done" if state == "done" else ""
    card_cls = "active" if state == "running" else ("done" if state == "done" else "")
    status_map = {"idle": "waiting", "running": "running…", "done": "complete"}
    status_cls = "running" if state == "running" else ("done" if state == "done" else "")
    st.markdown(f"""
    <div class="step-card {card_cls}">
        <div class="step-header">
            <span class="step-num {num_cls}">{num}</span>
            <span class="step-label">{label}</span>
            <span class="step-status {status_cls}">{status_map[state]}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── INPUT ──────────────────────────────────────────────────────────────────────
topic = st.text_input("Research Topic", placeholder="e.g. Quantum computing applications in drug discovery")
run_btn = st.button("Run Research Pipeline →")


# ── PIPELINE ───────────────────────────────────────────────────────────────────
if run_btn and topic.strip():

    # Import pipeline (same directory)
    sys.path.insert(0, os.path.dirname(__file__))
    from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

    state = {}
    st.markdown("<hr>", unsafe_allow_html=True)

    # ── STEP 1: SEARCH ──
    s1 = st.empty()
    with s1.container():
        step_card("01", "Web Search Agent", "running")

    with st.spinner(""):
        search_agent = build_search_agent()
        search_result = search_agent.invoke({
            "messages": [(
                "user",
                f"""Search for information about: {topic}
IMPORTANT: Return every source in this exact format:
Title:
URL:
Snippet:
Do not summarize. Do not omit URLs."""
            )]
        })
        state["search_result"] = str(search_result["messages"][-1].content)

    s1.empty()
    with s1.container():
        step_card("01", "Web Search Agent", "done")

    with st.expander("Search results", expanded=False):
        st.markdown(f'<div class="critic-text">{state["search_result"][:2000]}</div>', unsafe_allow_html=True)

    # ── STEP 2: SCRAPE ──
    s2 = st.empty()
    with s2.container():
        step_card("02", "Web Reader Agent", "running")

    with st.spinner(""):
        reader_agent = build_reader_agent()
        reader_result = reader_agent.invoke({
            "messages": [(
                "user",
                f"""Based on the following search results about '{topic}',
pick the most relevant URL and scrape it for deeper content.
Search Results:
{state['search_result'][:800]}"""
            )]
        })
        state["scraped_content"] = str(reader_result["messages"][-1].content)

    s2.empty()
    with s2.container():
        step_card("02", "Web Reader Agent", "done")

    with st.expander("Scraped content", expanded=False):
        st.markdown(f'<div class="critic-text">{state["scraped_content"][:1500]}</div>', unsafe_allow_html=True)

    # ── STEP 3: WRITE ──
    s3 = st.empty()
    with s3.container():
        step_card("03", "Report Writer", "running")

    with st.spinner(""):
        research_combined = (
            f"Search results:\n{state['search_result'][:2000]}\n\n"
            f"Detailed scraped content:\n{state['scraped_content'][:3000]}"
        )
        state["report"] = writer_chain.invoke({
            "topic": topic,
            "research": research_combined
        })

    s3.empty()
    with s3.container():
        step_card("03", "Report Writer", "done")

    # ── STEP 4: CRITIQUE ──
    s4 = st.empty()
    with s4.container():
        step_card("04", "Critic Review", "running")

    with st.spinner(""):
        state["feedback"] = critic_chain.invoke({"report": state["report"]})

    s4.empty()
    with s4.container():
        step_card("04", "Critic Review", "done")

    # ── OUTPUTS ────────────────────────────────────────────────────────────────
    st.markdown("<hr>", unsafe_allow_html=True)

    # Report panel
    st.markdown("""
    <div class="output-panel">
        <div class="panel-label">Research Report</div>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="report-text">{state["report"]}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Extract score from feedback if present
    score_line = ""
    for line in state["feedback"].splitlines():
        if line.strip().startswith("Score:"):
            score_line = line.strip().replace("Score:", "").strip()
            break

    st.markdown("<br>", unsafe_allow_html=True)

    # Critic panel
    st.markdown("""
    <div class="output-panel">
        <div class="panel-label">Critic Feedback</div>
    """, unsafe_allow_html=True)

    if score_line:
        st.markdown(f'<div class="score-badge">Score: {score_line}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="critic-text">{state["feedback"]}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Download
    st.markdown("<br>", unsafe_allow_html=True)
    full_output = f"# Research Report: {topic}\n\n{state['report']}\n\n---\n\n## Critic Feedback\n\n{state['feedback']}"
    st.download_button(
        label="Download report (.md)",
        data=full_output,
        file_name=f"research_{topic[:30].replace(' ','_')}.md",
        mime="text/markdown"
    )

elif run_btn and not topic.strip():
    st.warning("Please enter a research topic first.")

else:
    # Idle state — show pipeline preview
    st.markdown("<br>", unsafe_allow_html=True)
    for num, label in [("01", "Web Search Agent"), ("02", "Web Reader Agent"),
                       ("03", "Report Writer"), ("04", "Critic Review")]:
        step_card(num, label, "idle")