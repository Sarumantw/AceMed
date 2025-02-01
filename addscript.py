from questions.models import question
mcqs = [
    # Case-based questions
    [
        "A 32-year-old runner complains of pain on the medial side of her lower leg. Examination reveals inflammation of the primary weight-bearing bone in the leg. Which bone is affected?",
        "Tibia", 
        "Fibula", 
        "Femur", 
        "Patella", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A hiker falls and fractures the lateral malleolus. Which bone is involved?",
        "Fibula", 
        "Tibia", 
        "Calcaneus", 
        "Talus", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A 45-year-old man presents with difficulty dorsiflexing his foot and numbness between his first and second toes. Which nerve is likely injured?",
        "Deep fibular nerve", 
        "Superficial fibular nerve", 
        "Tibial nerve", 
        "Sural nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient is diagnosed with foot drop and is unable to dorsiflex the foot. Which compartment of the leg contains the affected muscles?",
        "Anterior compartment", 
        "Lateral compartment", 
        "Posterior compartment", 
        "Deep posterior compartment", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A construction worker suffers a deep laceration to the lateral compartment of the leg. Which nerve is most likely affected?",
        "Superficial fibular nerve", 
        "Deep fibular nerve", 
        "Tibial nerve", 
        "Saphenous nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient presents with inability to evert the foot. Which muscle group is likely affected?",
        "Lateral compartment muscles", 
        "Anterior compartment muscles", 
        "Deep posterior compartment muscles", 
        "Superficial posterior compartment muscles", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A 70-year-old man complains of pain and swelling in the posterior leg. Examination reveals a ruptured calcaneal tendon. Which action is impaired?",
        "Plantarflexion of the foot", 
        "Dorsiflexion of the foot", 
        "Inversion of the foot", 
        "Eversion of the foot", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient has numbness over the medial aspect of the leg and foot. Which nerve is most likely involved?",
        "Saphenous nerve", 
        "Sural nerve", 
        "Superficial fibular nerve", 
        "Tibial nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A motorcyclist sustains a fracture to the fibular neck. Which nerve is at risk of injury?",
        "Common fibular nerve", 
        "Tibial nerve", 
        "Saphenous nerve", 
        "Sural nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient complains of pain and inability to extend the toes. Which muscle group is most likely affected?",
        "Anterior compartment muscles", 
        "Lateral compartment muscles", 
        "Superficial posterior compartment muscles", 
        "Deep posterior compartment muscles", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A runner complains of shin pain during activity. Inflammation of which structure is most likely responsible?",
        "Deep fascia of the leg", 
        "Interosseous membrane", 
        "Plantar fascia", 
        "Calcaneal tendon", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient has difficulty flexing the toes and inversion of the foot. Which compartment of the leg is affected?",
        "Deep posterior compartment", 
        "Superficial posterior compartment", 
        "Lateral compartment", 
        "Anterior compartment", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient with a fractured tibia has damage to the popliteal artery. Which area of the leg is most at risk of ischemia?",
        "Posterior compartment", 
        "Anterior compartment", 
        "Lateral compartment", 
        "Medial compartment", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient suffers from deep vein thrombosis in the posterior tibial vein. Which condition is most likely to develop?",
        "Pulmonary embolism", 
        "Peripheral neuropathy", 
        "Compartment syndrome", 
        "Varicose veins", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient presents with weakness in plantarflexion and sensory loss in the sole of the foot. Which nerve is damaged?",
        "Tibial nerve", 
        "Deep fibular nerve", 
        "Superficial fibular nerve", 
        "Sural nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient is unable to unlock the knee joint during flexion. Which muscle is affected?",
        "Popliteus", 
        "Gastrocnemius", 
        "Soleus", 
        "Plantaris", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A fracture of the tibia results in damage to the nutrient artery. Which structure is most affected?",
        "Bone marrow", 
        "Interosseous membrane", 
        "Deep fascia", 
        "Articular cartilage", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient complains of numbness in the web space between the first and second toes. Which nerve is affected?",
        "Deep fibular nerve", 
        "Superficial fibular nerve", 
        "Tibial nerve", 
        "Sural nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient presents with pain and swelling at the tibial tuberosity. What is the most likely diagnosis?",
        "Osgood-Schlatter disease", 
        "Shin splints", 
        "Compartment syndrome", 
        "Stress fracture", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "A patient has a fracture involving the interosseous membrane of the leg. Which two bones are connected by this structure?",
        "Tibia and fibula", 
        "Femur and tibia", 
        "Fibula and talus", 
        "Tibia and talus", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],

    # Direct questions
    [
        "Which bone forms the medial malleolus?",
        "Tibia", 
        "Fibula", 
        "Talus", 
        "Calcaneus", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "Which nerve innervates the muscles of the anterior compartment of the leg?",
        "Deep fibular nerve", 
        "Superficial fibular nerve", 
        "Tibial nerve", 
        "Sural nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "Which artery supplies the anterior compartment of the leg?",
        "Anterior tibial artery", 
        "Posterior tibial artery", 
        "Fibular artery", 
        "Popliteal artery", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "Which compartment of the leg contains the tibialis posterior muscle?",
        "Deep posterior compartment", 
        "Superficial posterior compartment", 
        "Lateral compartment", 
        "Anterior compartment", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "Which muscle is the strongest dorsiflexor of the foot?",
        "Tibialis anterior", 
        "Extensor digitorum longus", 
        "Extensor hallucis longus", 
        "Fibularis tertius", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "Which vein drains into the small saphenous vein?",
        "Popliteal vein", 
        "Great saphenous vein", 
        "Posterior tibial vein", 
        "Fibular vein", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "Which nerve provides sensory innervation to the lateral side of the leg and foot?",
        "Sural nerve", 
        "Saphenous nerve", 
        "Deep fibular nerve", 
        "Superficial fibular nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "Which artery divides into the posterior tibial and fibular arteries?",
        "Tibioperoneal trunk", 
        "Popliteal artery", 
        "Anterior tibial artery", 
        "Dorsalis pedis artery", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "Which muscle acts to unlock the knee joint?",
        "Popliteus", 
        "Gastrocnemius", 
        "Soleus", 
        "Plantaris", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
    [
        "Which structure connects the tibia and fibula along their length?",
        "Interosseous membrane", 
        "Deep fascia", 
        "Plantar fascia", 
        "Calcaneal tendon", 
        "A", 
        "Anatomy", 
        2, 
        "Leg"
    ],
]

for q in mcqs:
    x= question(question_text = q[0],
                option1 = q[1],
                option2 = q[2],
                option3 = q[3],
                option4 = q[4],
                answer = q[5],
                subject = 1,
                week = q[7],
                topic = q[8])
    x.save()