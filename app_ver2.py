import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="CRISPR-Bot Simulator", page_icon="🧬")

st.title("🧬 CRISPR-Bot: AI-Guided Gene Editing")
st.write("### Targeting Sickle Cell Disease")
st.info("The enhancer region of the **BCL11A** gene is edited by CRISPR/Cas9 technology to restore healthy hemoglobin production.")

# --- PART 1: THE SIMULATION ---
# Simplified BCL11A enhancer segment
dna_strand = "TGCCATA" 
st.subheader("1. Source DNA Sequence (BCL11A gene)")
st.code(dna_strand, language="text")

st.markdown("---")
st.subheader("2. Robotic Edit Mission")
st.write("**Goal:** Modify the **'A'** in the source DNA sequence to trigger the 'switch' for healthy hemoglobin.")

# User interaction: Selecting the replacement
replacement_base = st.selectbox("Select replacement base:", ["A", "T", "C", "G"])

if st.button("Execute CRISPR Edit"):
    with st.spinner("🤖 CRISPR-Bot performing precision edit..."):
        time.sleep(1.5) 
        
    if replacement_base == "A":
        st.success("✨ Great, you just edited your first gene!")
        st.balloons()
        
        # Visualize the result highlighting the targeted 'A'
        result_dna = dna_strand.replace("A", "A (EDITED)") 
        st.markdown(f"**Updated Sequence Result:** `{result_dna}`")
        
        # Store completion state to trigger the quiz
        st.session_state['finished_sim'] = True
    else:
        st.error(f"❌ Target mismatch. Try again, we can only edit the 'A' in the DNA sequence. You selected '{replacement_base}'.")

# --- PART 2: THE QUIZ MODE ---
if st.session_state.get('finished_sim'):
    st.divider()
    st.subheader("🧠 Knowledge Check: The Science of CRISPR")
    
    with st.form("quiz_form"):
        q1 = st.radio(
            "1. Which specific gene was targeted in our simulation to help with Sickle Cell Disease?",
            ["BCL11A", "HBB (Hemoglobin Beta)", "Cas9 Gene"]
        )
        
        q2 = st.radio(
            "2. Why is CRISPR considered a 'robotic' tool at the molecular level?",
            ["Because it is made of metal", "Because it follows a programmed RNA guide to a specific coordinate", "Because it can talk to the patient"]
        )
        
        q3 = st.radio(
            "3. Based on clinical trials, this specific CRISPR edit helps the body:",
            ["Turn off all DNA", "Restart production of fetal hemoglobin", "Change the color of blood"]
        )
        
        submitted = st.form_submit_button("Submit Answers")
        
        if submitted:
            score = 0
            if q1 == "BCL11A": score += 1
            if q2 == "Because it follows a programmed RNA guide to a specific coordinate": score += 1
            if q3 == "Restart production of fetal hemoglobin": score += 1
            
            st.metric("Your STEM Score", f"{score}/3")
            if score == 3:
                st.success("Master Scientist! You've successfully navigated the BCL11A edit.")
            else:
                st.warning("Good attempt! Check your science facts and try again.")