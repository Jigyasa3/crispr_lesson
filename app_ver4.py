import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="CRISPR-Bot Simulator", page_icon="🧬")

st.title("🧬 CRISPR-Bot: AI-Guided Gene Editing")
st.write("### Targeting Sickle Cell Disease")
st.info("The enhancer region of the **BCL11A** gene is edited by CRISPR/Cas9 technology to restore healthy hemoglobin production.")

# --- INITIALIZE SESSION STATES ---
if 'pam_correct' not in st.session_state:
    st.session_state['pam_correct'] = False
if 'grna_correct' not in st.session_state:
    st.session_state['grna_correct'] = False
if 'ai_part1_done' not in st.session_state:
    st.session_state['ai_part1_done'] = False
if 'ai_part2_done' not in st.session_state:
    st.session_state['ai_part2_done'] = False
if 'finished_sim' not in st.session_state:
    st.session_state['finished_sim'] = False

# --- PART 1: THE SEQUENCE ---
# 23 base pair sequence: "GG" at pos 3-4, and "GG" at the end (pos 22-23)
dna_strand = "CAGGCATCGATCGATCGATATGG" 

st.subheader("1. Sickle Cell gene")
st.write("Here is our target 23-base pair DNA sequence. Notice the specific patterns in the letters!")
st.code(dna_strand, language="text")
st.markdown("---")

# --- STEP 2: FINDING THE LANDING PAD (PAM) ---
st.subheader("Step A: Identify the Landing Pad")
st.write("Before CRISPR can cut, it needs a landing pad called a **PAM sequence**.")

pam_answer = st.selectbox(
    "What is the DNA for the landing pad (PAM) Cas9 needs to look for?",["Select an option...", "GG", "AG", "GA", "GT", "AA", "TT"]
)

if pam_answer == "GG":
    st.success("✅ Correct! Cas9 looks for the 'NGG' pattern (ending in GG) to dock onto the DNA.")
    st.session_state['pam_correct'] = True
elif pam_answer != "Select an option...":
    st.error("❌ Not quite. Hint: SpCas9 looks for 'NGG' pattern (ending in GG) to dock onto the DNA.")
    st.session_state['pam_correct'] = False

# --- STEP 3: THE gRNA GPS ---
# Proceed only if PAM is correct
if st.session_state['pam_correct']:
    st.markdown("---")
    st.subheader("Step B: Program the GPS")
    st.write("Now that we have the landing pad, we need a guide RNA (gRNA) to act as a GPS and find the exact sequence next to it.")
    
    grna_answer = st.selectbox(
        "How long does the GPS gRNA need to be to perfectly match the target?",["Select an option...", "20", "10", "5", "1"]
    )
    
    if grna_answer == "20":
        st.success("✅ Correct! The standard gRNA is 20 base pairs long to ensure it only binds to one unique spot in the genome.")
        st.session_state['grna_correct'] = True
    elif grna_answer != "Select an option...":
        st.error("❌ Incorrect. The GPS needs to be long enough to be unique in the whole genome. Try a larger number!")
        st.session_state['grna_correct'] = False

# --- STEP 4: EDIT MISSION ---
# Proceed only if gRNA length is correct
if st.session_state['grna_correct']:
    st.markdown("---")
    st.subheader("2. Edit Mission")
    
    st.write("### 📍 Where does the GPS gRNA bind?")
    st.write("The gRNA binds to the sequence directly upstream of the final 'GG' landing pad.")
    
    # Visualization with green line matched specifically to the 20 bases before GG
    st.markdown("""
    ```text
    DNA: C | A G G C A T C G A T C G A T C G A T A T | G G |
           | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 |   ^ 
             (------- 20 bp perfect match -------)   Landing Pad
    ```
    """)
    
    st.write("### ✂️ The Molecular Scissors")
    st.write("Once the gRNA perfectly matches the 20 base pairs, Cas9 acts like scissors and cuts the DNA exactly **3 bases upstream** of the PAM landing pad.")

    # Visualization with Scissors
    st.markdown("""
    ```text
                                       ✂️ Cut site
    DNA: C | A G G C A T C G A T C G A T | C G A T A T | G G |
           | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 |   ^ 
             (------- 20 bp perfect match -------)   Landing Pad
    ```
    """)
    
    st.write("**The CRISPR cut the DNA to trigger the 'switch' for healthy hemoglobin.**")
    st.markdown("---")
    
    # --- STEP 5: THE SMART GPS (AI IN CRISPR) ---
    st.subheader("3. The Smart GPS: Why we need AI")
    st.write("Let's look at a slightly longer stretch of DNA (about 70 base pairs). Sometimes, a 20-bp target sequence can have 'look-alikes' elsewhere in the genome.")
    
    if st.button("Find all PAM sites for gRNA to bind (GG)"):
        st.session_state['ai_part1_done'] = True
        
    if st.session_state['ai_part1_done']:
        st.markdown("""
        ```text
        Target Site 1:
        DNA: ... | A G G C A T C G A T C G A T C G A T A T | G G | ...
                 | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 |   ^ 
                   (------- 20 bp perfect match -------)   Landing Pad
        
        Target Site 2 (Look-alike):
        DNA: ... | A G G C A T C G A T C G A T C G A T A T | G G | ...
                 | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 |   ^ 
                   (------- 20 bp perfect match -------)   Landing Pad
                   
        Target Site 3 (Look-alike):
        DNA: ... | A G G C A T C G A T C G A T C G A T A T | G G | ...
                 | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 |   ^ 
                   (------- 20 bp perfect match -------)   Landing Pad
        ```
        """)
        st.error("⚠️ **Danger!** 3 look-alikes present in the human genome. High risk of off-target cutting.")
        
        st.write("### Changing the Landing Pad Rules")
        st.write("What if we tell our AI to search for a much more complex and unique PAM site, like **NGATT**?")
        
        if st.button("Find all PAM sites for gRNA to bind (NGATT)"):
            st.session_state['ai_part2_done'] = True
            
    if st.session_state['ai_part2_done']:
        st.markdown("""
        ```text
        Unique Target Site:
        DNA: ... | A G G C A T C G A T C G A T C G A T A T | N G A T T | ...
                 | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 |      ^ 
                   (------- 20 bp perfect match -------)   Landing Pad
        ```
        """)
        st.success("✨ **Perfect match!** This is a unique site.")
        
        st.info("**Conclusion:** AI helps us determine the reliability of gRNA, to determine that we don’t accidentally edit another gene causing harmful effects. Scientists use AI to find the correct gRNA and PAM for CRISPR-based gene editing.")
        
        # Unlock the quiz
        st.session_state['finished_sim'] = True

# --- PART 2: THE QUIZ MODE ---
if st.session_state.get('finished_sim'):
    st.divider()
    st.subheader("🧠 Knowledge Check: The Science of CRISPR")
    
    with st.form("quiz_form"):
        q1 = st.radio(
            "1. Which specific gene was targeted in our simulation to help with Sickle Cell Disease?",["BCL11A", "HBB (Hemoglobin Beta)", "Cas9 Gene"]
        )
        
        q2 = st.radio(
            "2. Why is CRISPR considered a 'robotic' tool at the molecular level?",["Because it is made of metal", "Because it follows a programmed RNA guide to a specific coordinate", "Because it can talk to the patient"]
        )
        
        q3 = st.radio(
            "3. Based on clinical trials, this specific CRISPR edit helps the body:",["Turn off all DNA", "Restart production of hemoglobin", "Change the color of blood"]
        )
        
        submitted = st.form_submit_button("Submit Answers")
        
        if submitted:
            score = 0
            if q1 == "BCL11A": score += 1
            if q2 == "Because it follows a programmed RNA guide to a specific coordinate": score += 1
            if q3 == "Restart production of hemoglobin": score += 1
            
            st.metric("Your STEM Score", f"{score}/3")
            
            # Display correct answers clearly after submission
            st.markdown("### Answer Key:")
            st.markdown(f"- **Q1:** BCL11A ✅ *(You answered: {q1})*")
            st.markdown(f"- **Q2:** Because it follows a programmed RNA guide to a specific coordinate ✅ *(You answered: {q2})*")
            st.markdown(f"- **Q3:** Restart production of hemoglobin ✅ *(You answered: {q3})*")
            
            if score == 3:
                st.success("Master Scientist! You've successfully navigated the BCL11A edit.")
            else:
                st.warning("Good attempt! Review the correct answers above and try again.")
