import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="CRISPR-Bot Simulator", page_icon="🧬")

st.title("🧬 CRISPR-Bot: AI-Guided Gene Editing")

# --- 1 & 2. INTRODUCTION & IMAGES ---
st.write("### Introduction")
st.write("""
CRISPR is a machine that. If there is a typo in the code, the robot malfunctions[cite: 6]. 
CRISPR is a processor that acts as a **'pair of scissors'**. It helps to 'fix' the typo in the DNA[cite: 7, 18].
""")

# Displaying the CRISPR components image from the Lesson Plan
# Note: In a real app, you would use st.image("path_to_image.png")
st.info("🧬 **Visualizing the Components**")
st.markdown("""
> **I am the scissors** (Cas9) ✂️  
> **I am the GPS** (gRNA) 🛰️  
> **I am the landing pad** (PAM) 🏗️
""")
# 
st.markdown("---")

# --- 3 & 4. INTERACTIVE QUESTIONS ---
fix_it = st.selectbox(
    "If you could 'fix' one thing what would it be?",
    ["Select an option...", "make food never go bad", "cure diseases", "grow taller", "change the size of vegetables"]
)

possible_tasks = st.selectbox(
    "Which of these are already possible to do?",
    ["Select an option...", "make food never go bad", "cure diseases", "grow taller", "change the size of vegetables"]
)

if possible_tasks != "Select an option...":
    st.write("✨ **Answer:** **'change the size of vegetables'** and **'cure diseases'**. But only some of them! [cite: 8, 35]")

st.markdown("---")

# --- 5. VICTORIA GRAY CASE STUDY ---
st.subheader("The Story of Victoria Gray")
st.write("""
One of the recent applications of CRISPR was Victoria Gray, who made history as the first person in the U.S. 
to be treated for sickle cell disease using CRISPR gene-editing technology[cite: 33]. 

After a lifetime of severe pain and hospital visits, Victoria’s own cells were edited to produce **'super cells'** that create healthy cells[cite: 34]. Today, she is essentially symptom-free, proving that CRISPR can be a 
functional cure for inherited blood disorders[cite: 35].
""")
# 
st.markdown("---")

# --- 5b. HOW IT WORKS ---
st.write("### So how does CRISPR work?")
st.write("""
* **CRISPR Cas9 (The Molecular Scissors):** A machine that cuts the DNA at a specific location so that edits can be made[cite: 18].
* **Guide RNA (gRNA) (The 'GPS' or Search Function):** A custom-designed molecule that acts as a search function[cite: 19]. It guides the Cas9 scissors to the exact matching spot in the genome[cite: 20]. 
    * The gRNA is **20 DNA nucleotides long**. This ensures CRISPR binds to a specific site and doesn’t accidentally bind to other genes[cite: 21].
* **PAM (The Landing Pad):** A specific, short DNA sequence that Cas9 must look for to safely bind to the DNA before making a cut[cite: 22].
    * The PAM is a repeating DNA nucleotide (e.g., GATT, GG). This ensures the gRNA doesn’t randomly bind to any 20-nucleotide sequence[cite: 23, 24].
""")

# --- 6. THE SEQUENCE ---
st.markdown("---")
dna_strand = "CAGGCATCGATCGATCGATATGG"
st.write("Here is our target 23-base pair DNA sequence. Notice the specific patterns in the letters!")
st.code(dna_strand, language="text")

# --- 7. STEP A: PAM ---
st.subheader("Step A: Identify the Landing Pad")
st.write("Before CRISPR can cut, it needs a landing pad called a **PAM sequence**[cite: 22].")

pam_answer = st.selectbox(
    "What is the DNA for the landing pad (PAM) Cas9 needs to look for?",
    ["Select an option...", "GG", "AG", "GA", "GT", "AA", "TT"]
)

if pam_answer == "GG":
    st.success("✅ Correct! Cas9 looks for the 'NGG' pattern (ending in GG) to dock onto the DNA[cite: 23].")
    
    # --- 8. STEP B: GPS ---
    st.markdown("---")
    st.subheader("Step B: Program the GPS")
    st.write("Now that we have the landing pad, we need a guide RNA to act as a GPS.")
    
    grna_answer = st.selectbox(
        "How long does the GPS gRNA need to be to perfectly match the target?",
        ["Select an option...", "20", "10", "5", "1"]
    )
    
    if grna_answer == "20":
        st.success("✅ Correct! The standard gRNA is 20 base pairs long[cite: 21].")
        
        # --- 10. MOLECULAR SCISSORS ---
        st.markdown("---")
        st.write("### ✂️ The Molecular Scissors")
        st.write("""
        Once the gRNA perfectly matches the 20 base pairs, Cas9 acts like scissors and cuts the DNA 
        exactly **3 bases upstream** of the PAM landing pad. The CRISPR cut the DNA to trigger 
        the 'switch' to cure a disease.
        """)

        # --- 11-16. THE SMART GPS & AI ---
        st.markdown("---")
        st.subheader("The Smart GPS: Why we need AI")
        long_dna = "A G G C A T C G A T C G A T C G A T A T G G A G G C A T C G A T C G A T C G A T A T G G A G G C A T C G A T T G A T C G A T A T G G"
        st.code(long_dna)
        
        q_gg = st.selectbox("How many 'GG' landing pads do you find in the sequence above?", ["Select...", "1", "2", "3", "4"])
        
        if q_gg == "3":
            st.error("⚠️ **Danger!** 3 look-alikes present in the human genome. High risk of off-target cutting[cite: 39].")
            
            st.subheader("Changing the Landing Pad Rules")
            st.write("What if we tell our AI to search for a much more complex and unique PAM site like **GATT**?")
            
            q_gatt = st.selectbox("How many 'GATT' landing pads do you find in the sequence above?", ["Select...", "0", "1", "2", "3"])
            
            if q_gatt == "1":
                st.success("✨ **Unique Target Site:** Perfect match! This is a unique site.")
                st.info("**Conclusion:** AI helps us determine the reliability of gRNA, ensuring we don’t accidentally edit another gene[cite: 41, 51]. Scientists use AI to find the correct gRNA and PAM for CRISPR-based gene editing.")

                # --- 17-22. KNOWLEDGE CHECK ---
                st.divider()
                st.subheader("🧠 Knowledge Check: The Science of CRISPR")
                
                with st.form("quiz_form"):
                    q2 = st.radio(
                        "1. Why is CRISPR considered a 'robotic' tool at the molecular level?",
                        ["Because it is made of metal", "Because it is a molecular scissors.", "Because it can talk to the patient"]
                    )
                    
                    q_improve = st.radio(
                        "2. How can we improve the landing pad?",
                        ["making the PAM site longer", "making the PAM site unique", "creating a new PAM sites"]
                    )
                    
                    q_ai = st.radio(
                        "3. How can AI help in improving the landing pad?",
                        ["Creating the correct guide RNA (the GPS) for any PAM of interest", 
                         "Finding all available PAM sites in the genome", 
                         "Creating new PAM sites"]
                    )
                    
                    submitted = st.form_submit_button("Submit Answers")
                    
                    if submitted:
                        # Scoring: Q1 has one specific answer, Q2 and Q3 accept all listed per instructions
                        score = 0
                        if q2 == "Because it is a molecular scissors.": score += 1
                        if q_improve in ["making the PAM site longer", "making the PAM site unique", "creating a new PAM sites"]: score += 1
                        if q_ai in ["Creating the correct guide RNA (the GPS) for any PAM of interest", "Finding all available PAM sites in the genome", "Creating new PAM sites"]: score += 1
                        
                        st.metric("Your STEM Score", f"{score}/3")
                        st.success("Great job exploring the future of gene editing!")
