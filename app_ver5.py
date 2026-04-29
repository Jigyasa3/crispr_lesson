import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="CRISPR-Bot Simulator", page_icon="🧬")

st.title("🧬 CRISPR-Bot: AI-Guided Gene Editing")

# --- 1. INTRODUCTION ---
st.write("### Introduction")
st.write("""
Think of CRISPR as a highly advanced biological word processor. Just like a computer robot 
will malfunction if there is a typo in its code, our bodies can face challenges if there are 
typos in our DNA. CRISPR acts as a smart processor and a pair of 'molecular scissors' 
that can find and fix these genetic typos to keep the system running smoothly.
""")

# --- 2. FIGURE: CRISPR COMPONENTS ---
st.info("🧬 **Visualizing the Components**")
# Displaying the uploaded CRISPR illustration
st.image("Screenshot 2026-04-28 at 8.59.27 PM.png", caption="CRISPR Components: The Molecular Scissors and the GPS Guide.")

st.markdown("---")

# --- 3 & 4. INTERACTIVE QUESTIONS ---
fix_it = st.selectbox(
    "If you could 'fix' one thing, what would it be?",
    ["Select an option...", "make food never go bad", "cure diseases", "grow taller", "change the size of vegetables"]
)

possible_tasks = st.selectbox(
    "Which of these do you think are already possible to do today?",
    ["Select an option...", "make food never go bad", "cure diseases", "grow taller", "change the size of vegetables"]
)

if possible_tasks != "Select an option...":
    if possible_tasks in ["change the size of vegetables", "cure diseases"]:
        st.success("✨ Correct! Scientists are already using CRISPR to 'change the size of vegetables' and 'cure diseases'—though we are still only in the early stages!")
    else:
        st.error("❌ Sorry, wrong answer. The correct answers are 'change the size of vegetables' and 'cure diseases'!")

st.markdown("---")

# --- 5. VICTORIA GRAY CASE STUDY ---
st.subheader("The Story of Victoria Gray")
st.write("""
Victoria Gray made history as the first person in the U.S. to be treated for sickle cell disease 
using CRISPR gene-editing technology. 

After a lifetime of severe pain and hospital visits, Victoria’s own cells were edited to produce 
**'super cells'** that create healthy hemoglobin. Today, she is essentially symptom-free, 
proving that CRISPR can be a functional cure for inherited blood disorders.
""")

# Displaying the uploaded photo of Victoria Gray
st.image("Screenshot 2026-04-28 at 8.59.44 PM.png", caption="Victoria Gray: The first person in the U.S. treated for sickle cell disease using CRISPR.")

st.markdown("---")

# --- 5b. HOW IT WORKS ---
st.write("### So how does CRISPR work?")
st.write("""
* **CRISPR Cas9 (The Molecular Scissors):** A specialized protein that cuts the DNA at a specific location so edits can be made.
* **Guide RNA (gRNA) (The 'GPS'):** A custom-designed molecule that acts as a search function to guide the scissors to the exact spot in the genome.
    * The gRNA is **20 nucleotides long** to ensure it hits a unique target without accidentally editing the wrong gene.
* **PAM (The Landing Pad):** A short DNA sequence that Cas9 must find first. It acts as a safety dock to ensure the scissors only bind where they are supposed to.
    * Common PAMs include repeating patterns like **GG** or **GATT**.
""")

# --- 6. THE SEQUENCE ---
st.markdown("---")
dna_strand = "CAGGCATCGATCGATCGATATGG"
st.write("Here is our target 23-base pair DNA sequence. Notice the specific patterns at the end!")
st.code(dna_strand, language="text")

# --- 7. STEP A: PAM ---
st.subheader("Step A: Identify the Landing Pad")
pam_answer = st.selectbox(
    "What is the DNA for the landing pad (PAM) Cas9 needs to look for?",
    ["Select an option...", "GG", "AG", "GA", "GT", "AA", "TT"]
)

if pam_answer != "Select an option...":
    if pam_answer == "GG":
        st.success("✅ Correct! Cas9 looks for the 'NGG' pattern (ending in GG) to dock onto the DNA.")
        
        # --- 8. STEP B: GPS ---
        st.markdown("---")
        st.subheader("Step B: Program the GPS")
        grna_answer = st.selectbox(
            "How long does the GPS gRNA need to be to perfectly match the target?",
            ["Select an option...", "20", "10", "5", "1"]
        )
        
        if grna_answer != "Select an option...":
            if grna_answer == "20":
                st.success("✅ Correct! The standard gRNA is 20 base pairs long to maintain precision.")
                
                # --- 10. MOLECULAR SCISSORS ---
                st.markdown("---")
                st.write("### ✂️ The Molecular Scissors")
                st.write("Once the gRNA matches the 20 base pairs, Cas9 cuts the DNA exactly **3 bases upstream** of the PAM. This cut triggers the genetic 'switch' to help cure the disease.")

                # --- 11-16. THE SMART GPS & AI ---
                st.markdown("---")
                st.subheader("The Smart GPS: Why we need AI")
                long_dna = "AGGCATCGATCGATCGATATGGAGGCATCGATCGATCGATATGGAGGCATCGATTGATCGATATGG"
                st.text(f"Full DNA Sequence: {long_dna}")
                
                q_gg = st.selectbox("How many 'GG' landing pads do you find in the sequence above?", ["Select...", "1", "2", "3", "4"])
                
                if q_gg != "Select...":
                    if q_gg == "3":
                        st.error("⚠️ **Danger!** There are 3 look-alikes present. This creates a high risk of 'off-target' cutting.")
                        
                        st.subheader("Changing the Landing Pad Rules")
                        st.write("What if we use AI to find a more complex and unique landing pad, like **GATT**?")
                        
                        q_gatt = st.selectbox("How many 'GATT' landing pads do you find in that same sequence?", ["Select...", "0", "1", "2", "3"])
                        
                        if q_gatt != "Select...":
                            if q_gatt == "1":
                                st.success("✨ **Unique Target Site identified!**")
                                st.markdown("""
                                ```text
                                DNA: ... | A G G C A T C G A T C G A T C G A T A T | N G A T T | ...
                                         | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 |      ^ 
                                           (------- 20 bp perfect match -------)   Landing Pad
                                ```
                                """)
                                st.info("Conclusion: AI helps us determine the reliability of our GPS. It ensures we don't accidentally edit another gene. Scientists use AI to find the perfect gRNA and PAM for every specific edit.")

                                # --- 17-22. KNOWLEDGE CHECK ---
                                st.divider()
                                st.subheader("🧠 Knowledge Check: The Science of CRISPR")
                                
                                with st.form("quiz_form"):
                                    q2 = st.radio("1. Why is CRISPR considered a 'robotic' tool at the molecular level?", ["Because it is made of metal", "Because it is a molecular scissors.", "Because it can talk to the patient"])
                                    q_improve = st.radio("2. How can we improve the landing pad?", ["making the PAM site longer", "making the PAM site unique", "creating a new PAM sites"])
                                    q_ai = st.radio("3. How can AI help in improving the landing pad?", ["Creating the correct guide RNA (the GPS) for any PAM of interest", "Finding all available PAM sites in the genome", "Creating new PAM sites"])
                                    
                                    submitted = st.form_submit_button("Submit Answers")
                                    
                                    if submitted:
                                        score = 0
                                        if q2 == "Because it is a molecular scissors.": score += 1
                                        score += 2 # Q2 and Q3 are always correct per instructions
                                        
                                        st.metric("Your STEM Score", f"{score}/3")
                                        
                                        st.markdown("### 🔑 Answer Key:")
                                        st.write("- **Question 1:** The correct answer is **'Because it is a molecular scissors.'**")
                                        st.write("- **Question 2 & 3:** **All options are correct!** Changing the landing pad is vital for safety, and AI is incredibly versatile in designing or finding new PAM sites to make CRISPR more effective.")
                            else:
                                st.error("❌ Sorry, wrong answer. Hint: Look closely for the sequence G-A-T-T just once in the string!")
                    else:
                        st.error("❌ Sorry, wrong answer. Hint: Count every time you see 'GG' appear at the end of a segment!")
            else:
                st.error("❌ Sorry, wrong answer. Hint: The GPS needs to be long enough to be unique. Think of a common 'round' number used in genetics!")
    else:
        st.error("❌ Sorry, wrong answer. Hint: Look at the very end of the target sequence provided above!")
