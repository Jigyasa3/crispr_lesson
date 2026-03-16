import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="CRISPR-Bot Simulator", page_icon="🧬")

st.title("🧬 CRISPR-Bot: AI-Guided Gene Editing")
st.write("Targeting Sickle Cell Disease (2025 Clinical Trial Simulation)")

# --- PART 1: THE SIMULATION ---
dna_strand = "ATCGGATTACAGCTACGATCG"
st.subheader("1. Source DNA Sequence")
st.info("The AI has identified a mutation in the sequence below.")
st.code(dna_strand)

target = st.text_input("Enter Target Sequence to 'Repair' (Hint: GATTACA)", "").upper()

if target:
    if target in dna_strand:
        if st.button("Initialize CRISPR-Bot"):
            st.success(f"Target {target} located!")
            
            # Progress bar simulates the "Robot" moving
            bar = st.progress(0)
            status = st.empty()
            for i in range(100):
                status.text(f"🤖 Robot Arm moving to position... {i+1}%")
                bar.progress(i + 1)
                time.sleep(0.01)
            
            st.write("### ✅ Edit Complete!")
            st.write("The mutated sequence has been replaced with healthy code.")
            st.balloons()
            
            # Store completion state to trigger the quiz
            st.session_state['finished_sim'] = True
    else:
        st.error("❌ Sequence match failed. AI detected an 'off-target' risk. Try again!")

# --- PART 2: THE QUIZ MODE ---
if st.session_state.get('finished_sim'):
    st.divider()
    st.subheader("🧠 Knowledge Check: The Science of 2025")
    
    with st.form("quiz_form"):
        q1 = st.radio(
            "1. In our simulation, what acted as the 'GPS' to find the DNA location?",
            ["The Cas9 Scissors", "The Guide RNA", "The Robot Arm"]
        )
        
        q2 = st.radio(
            "2. Why do scientists use AI/Machine Learning in CRISPR trials?",
            ["To make the cells grow faster", "To predict and avoid 'off-target' accidental cuts", "To change the color of the robot"]
        )
        
        q3 = st.radio(
            "3. Based on the IGI 2025 update, CRISPR is currently being used in trials for:",
            ["Creating super-powers", "Fixing computer viruses", "Curing blood disorders like Sickle Cell"]
        )
        
        submitted = st.form_submit_button("Submit Answers")
        
        if submitted:
            score = 0
            if q1 == "The Guide RNA": score += 1
            if q2 == "To predict and avoid 'off-target' accidental cuts": score += 1
            if q3 == "Curing blood disorders like Sickle Cell": score += 1
            
            st.metric("Your STEM Score", f"{score}/3")
            if score == 3:
                st.success("Master Scientist! You're ready for the lab.")
            else:
                st.warning("Almost there! Review the lesson plan and try again.")