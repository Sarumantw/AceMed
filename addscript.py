from questions.models import question
questions = [
    [
        "A 25-year-old woman presents with dysuria and increased urinary frequency. Urinalysis reveals pyuria, and culture identifies a gram-positive, coagulase-negative cocci resistant to novobiocin. What is the most likely pathogen?",
        "Staphylococcus aureus",
        "Staphylococcus epidermidis",
        "Staphylococcus saprophyticus",
        "Enterococcus faecalis",
        "C"
    ],
    [
        "A 6-year-old boy develops large, fluid-filled blisters on his skin. Gentle pressure causes the epidermis to slough off (positive Nikolsky sign). Which virulence factor is responsible?",
        "Toxic Shock Syndrome Toxin-1 (TSST-1)",
        "Panton-Valentine Leukocidin (PVL)",
        "Exfoliative toxin",
        "Enterotoxin A",
        "C"
    ],
    [
        "A 30-year-old man with a prosthetic heart valve presents with fever and a new heart murmur. Blood cultures reveal coagulase-negative staphylococci. Which pathogen is most likely responsible?",
        "Staphylococcus aureus",
        "Staphylococcus epidermidis",
        "Staphylococcus saprophyticus",
        "Streptococcus viridans",
        "B"
    ],
    [
        "A patient who recently had a pacemaker implanted develops a bloodstream infection. The isolated bacteria are gram-positive cocci that form biofilms on medical devices. What is the most likely organism?",
        "Staphylococcus aureus",
        "Staphylococcus epidermidis",
        "Staphylococcus saprophyticus",
        "Streptococcus pyogenes",
        "B"
    ],
    [
        "A 40-year-old man develops sudden-onset fever, hypotension, and a diffuse erythematous rash. He recently had nasal packing for a nosebleed. What is the most likely toxin responsible?",
        "Panton-Valentine Leukocidin",
        "Exfoliative toxin",
        "Enterotoxin A",
        "Toxic Shock Syndrome Toxin-1 (TSST-1)",
        "D"
    ],
    [
        "A young woman presents with acute cystitis. Her urine culture grows a novobiocin-resistant, coagulase-negative, gram-positive cocci. What is the first-line treatment?",
        "Vancomycin",
        "Trimethoprim-Sulfamethoxazole",
        "Daptomycin",
        "Ceftriaxone",
        "B"
    ],
    [
        "A hospitalized patient on a ventilator develops pneumonia. Cultures reveal a gram-positive, coagulase-positive cocci resistant to methicillin. What is the mechanism of resistance?",
        "Efflux pumps",
        "PBP2a production from the mecA gene",
        "Beta-lactamase production",
        "Altered ribosomal binding sites",
        "B"
    ],
    [
        "A neonate in the NICU develops sepsis. The causative organism forms biofilms on central lines and is coagulase-negative. What is the most likely pathogen?",
        "Staphylococcus aureus",
        "Staphylococcus epidermidis",
        "Staphylococcus saprophyticus",
        "Streptococcus agalactiae",
        "B"
    ],
    [
        "A 17-year-old boy presents with a large, painful, pus-filled abscess on his leg after a football injury. Gram stain shows gram-positive cocci in clusters. What is the most likely organism?",
        "Streptococcus pyogenes",
        "Staphylococcus aureus",
        "Pseudomonas aeruginosa",
        "Enterococcus faecalis",
        "B"
    ],
    [
        "A patient develops food poisoning with vomiting within hours of eating contaminated food. No bacteria are found in the stool. What is the causative agent?",
        "Clostridium botulinum",
        "Bacillus cereus",
        "Staphylococcus aureus",
        "Salmonella enterica",
        "C"
    ],
    [
        "A 45-year-old diabetic man develops osteomyelitis following a foot ulcer infection. Culture shows coagulase-positive gram-positive cocci. What is the most likely pathogen?",
        "Staphylococcus epidermidis",
        "Staphylococcus saprophyticus",
        "Staphylococcus aureus",
        "Streptococcus pyogenes",
        "C"
    ],
    [
        "A 3-year-old child presents with extensive skin peeling following a minor infection. The causative bacteria produce exfoliative toxins that cleave desmoglein-1. What is the diagnosis?",
        "Scarlet fever",
        "Staphylococcal Scalded Skin Syndrome (SSSS)",
        "Bullous impetigo",
        "Toxic Shock Syndrome",
        "B"
    ],
    [
        "A woman with a history of recurrent UTIs is diagnosed with Staphylococcus saprophyticus. What distinguishes this pathogen from other coagulase-negative staphylococci?",
        "Biofilm formation",
        "Novobiocin resistance",
        "Coagulase positivity",
        "Exotoxin production",
        "B"
    ],
    [
        "A 65-year-old man with a prosthetic knee joint develops persistent joint pain and swelling. Culture shows a biofilm-forming staphylococcal species. What is the best antibiotic choice?",
        "Amoxicillin",
        "Rifampin + Vancomycin",
        "Azithromycin",
        "Metronidazole",
        "B"
    ],
    [
        "A nurse in the ICU tests positive for MRSA colonization. What is the best decolonization strategy?",
        "IV vancomycin",
        "Linezolid",
        "Topical mupirocin and chlorhexidine washes",
        "Ciprofloxacin",
        "C"
    ],
    [
        "A 50-year-old woman presents with pneumonia following a viral illness. Culture shows gram-positive, coagulase-positive cocci. What is the most likely pathogen?",
        "Streptococcus pneumoniae",
        "Klebsiella pneumoniae",
        "Staphylococcus aureus",
        "Pseudomonas aeruginosa",
        "C"
    ],
    [
        "A patient with endocarditis caused by MRSA is started on vancomycin. After a few days, the infection worsens despite appropriate dosing. What resistance mechanism is likely involved?",
        "PBP2a production",
        "Beta-lactamase production",
        "VanA gene-mediated resistance",
        "Altered ribosomal binding sites",
        "C"
    ],
    [
        "A patient develops a wound infection after surgery. The isolated bacteria are gram-positive, coagulase-positive, and methicillin-resistant. What is the drug of choice?",
        "Vancomycin",
        "Penicillin",
        "Amoxicillin",
        "Ceftriaxone",
        "A"
    ],
    [
        "A burn patient develops a sepsis-like syndrome caused by a toxin-producing staphylococcal strain. What toxin is responsible?",
        "Exfoliative toxin",
        "Enterotoxin A",
        "Panton-Valentine Leukocidin",
        "Toxic Shock Syndrome Toxin-1",
        "D"
    ],
    [
        "A 35-year-old patient presents with high fever and purulent arthritis. Joint aspiration grows gram-positive cocci in clusters. What is the most common causative organism?",
        "Streptococcus pyogenes",
        "Neisseria gonorrhoeae",
        "Staphylococcus aureus",
        "Escherichia coli",
        "C"
    ],
    [
        "Which staphylococcal species is novobiocin-resistant?",
        "Staphylococcus aureus",
        "Staphylococcus epidermidis",
        "Staphylococcus saprophyticus",
        "Streptococcus pyogenes",
        "C"
    ],
    [
        "What is the major virulence factor of MRSA?",
        "Protein A",
        "PBP2a",
        "Exfoliative toxin",
        "Enterotoxin",
        "B"
    ],
    [
        "What enzyme differentiates Staphylococcus aureus from other staphylococci?",
        "Catalase",
        "Coagulase",
        "Urease",
        "Hemolysin",
        "B"
    ],
    [
        "What is the first-line treatment for MRSA infections?",
        "Penicillin",
        "Vancomycin",
        "Amoxicillin",
        "Ceftriaxone",
        "B"
    ]
]


i=1
for q in questions:
    
    x= question(question_text = q[0],
                option1 = q[1],
                option2 = q[2],
                option3 = q[3],
                option4 = q[4],
                answer = q[5],
                subject = 6,
                week = 5,
                topic = "Staphylococcus",
                )
    x.save()
    print(i)
    i+=1