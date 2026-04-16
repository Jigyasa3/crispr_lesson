import streamlit as st
import time

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
if 'finished_sim' not in st.session_state:
    st.session_state['finished_sim'] = False

# --- PART 1: THE SEQUENCE ---
# 20 base pair sequence: "GG" at pos 5-6, and "GG" at pos 19-20. 
# Length: 4 + 2 + 12 + 2 = 20
dna_strand = "ATCAGGCATCGATCGATAGG" 

st.subheader("1. Sickle Cell gene")
st.write("Here is our target 20-base pair DNA sequence. Notice the specific patterns in the letters!")
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
    st.error("❌ Not quite. Hint: SpCas9 looks for two Guanines next to each other.")
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
    
    st.write("### 📍 Schematic: Where does the GPS gRNA bind?")
    st.write("The gRNA binds to the sequence directly upstream of the final 'GG' landing pad.")
    
    # Schematic visualization
    st.markdown("""
    ```text
    DNA:      A T C A G G C A T C G A T C G A T A | G G |
    gRNA GPS: U A G U C C G U A G C U A G C U A U |     |
                                                  ^ 
                                              Landing Pad
    ```
    """)
    
    st.write("**Goal:** Modify the **'A'** right before the landing pad to trigger the 'switch' for healthy hemoglobin.")

    # User interaction: Selecting the replacement
    replacement_base = st.selectbox("Select replacement base to fix the sequence:",["Select...", "A", "T", "C", "G"])

    if st.button("Execute CRISPR Edit"):
        if replacement_base == "Select...":
            st.warning("Please select a base first!")
        else:
            with st.spinner("🤖 CRISPR-Bot performing precision edit..."):
                time.sleep(1.5) 
                
            # Let's say we are targeting the 'A' right before the last GG (which is at index 17, so the 18th base)
            if replacement_base == "A":
                st.success("✨ Great, you just edited your first gene!")
                st.balloons()
                
                # Visualize the result highlighting the targeted edit
                # Changing the last 'A' (at index 17) to show it's edited
                edited_dna = dna_strand[:17] + "[EDITED-A]" + dna_strand[18:]
                st.markdown(f"**Updated Sequence Result:** `{edited_dna}`")
                
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
            "2. Why is CRISPR considered a 'robotic' tool at the molecular level?",["Because it is made of metal", "Because it follows a programmed RNA guide to a specific coordinate", "Because it can talk to the patient"]
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
