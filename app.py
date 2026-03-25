import streamlit as st

# --- UI Setup ---
st.set_page_config(page_title="UGC Script Engine", page_icon="🎬")
st.title("⚡ UGC Ad Script Generator")
st.markdown("Generate high-converting scripts for TikTok, Reels, and Shorts.")

# --- User Inputs ---
with st.sidebar:
    st.header("Product Details")
    product_name = st.text_input("Product/Business Name", placeholder="e.g., Glow-Up Mirror")
    audience = st.text_input("Target Audience", placeholder="e.g., Gen Z Travelers")
    details = st.text_area("What problem does it solve?", placeholder="e.g., Bad hotel lighting...")

# --- The Logic (The Prompt Engine) ---
if st.button("Generate My Script"):
    if product_name and details:
        # This builds the master prompt using your inputs
        master_prompt = f"""
        Act as a Senior Direct-Response Copywriter specializing in UGC ads. 
        Write a script for {product_name}.
        
        Target Audience: {audience}
        Product Details: {details}
        
        Framework:
        1. 3 Visual/Verbal Hooks (0-3s).
        2. Body: PAS (Problem-Agitation-Solution).
        3. Style: Raw, human, handheld feel. No 'corporate' talk.
        4. CTA: Clear instruction.
        """
        
        st.subheader("🚀 Your Generated Script & Framework")
        st.info("Copy the text below and paste it into your AI of choice (Gemini/ChatGPT) to get the final version!")
        st.code(master_prompt, language="markdown")
    else:
        st.error("Please fill in the product name and details!")
