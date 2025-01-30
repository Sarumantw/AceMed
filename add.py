from questions.models import question
mcqs = [
    # Case-based questions
    [
        "A 45-year-old woman presents with pain and flattening of the medial longitudinal arch. Which ligament is most likely compromised?",
        "Plantar calcaneo-navicular ligament", 
        "Long plantar ligament", 
        "Short plantar ligament", 
        "Plantar aponeurosis", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A runner experiences heel pain and is diagnosed with plantar fasciitis. What structure is most directly affected?",
        "Plantar aponeurosis", 
        "Achilles tendon", 
        "Calcaneonavicular ligament", 
        "Short plantar ligament", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A patient with a history of flatfoot is found to have weak muscular support for the medial arch. Which muscle is most likely underperforming?",
        "Tibialis posterior", 
        "Tibialis anterior", 
        "Fibularis longus", 
        "Flexor hallucis longus", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A 50-year-old man presents with pain and deformity in the lateral longitudinal arch. Which bones are involved in this arch?",
        "Calcaneus, cuboid, and 4th and 5th metatarsals", 
        "Calcaneus, talus, and navicular", 
        "Talus, cuboid, and 1st metatarsal", 
        "Cuneiforms and metatarsals", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "During a surgical procedure, the surgeon notes that the dorsalis pedis artery is absent. Which artery likely provides collateral circulation?",
        "Lateral tarsal artery", 
        "Posterior tibial artery", 
        "Arcuate artery", 
        "Medial plantar artery", 
        "B", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A child presents with toe-walking and tightness in the sole of the foot. Which structure is primarily responsible for maintaining the foot's arches in this condition?",
        "Plantar aponeurosis", 
        "Long plantar ligament", 
        "Short plantar ligament", 
        "Achilles tendon", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A patient with diabetes has a wound on the sole of their foot over the medial arch. What nerve provides sensation to this area?",
        "Medial plantar nerve", 
        "Lateral plantar nerve", 
        "Sural nerve", 
        "Tibial nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "An elderly man complains of difficulty pushing off while walking. Dysfunction in which structure may contribute to this symptom?",
        "Medial longitudinal arch", 
        "Lateral longitudinal arch", 
        "Transverse arch", 
        "Plantar aponeurosis", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A patient presents with pain in the medial foot and difficulty standing on tiptoes. Dysfunction in which muscle is likely?",
        "Tibialis posterior", 
        "Fibularis longus", 
        "Tibialis anterior", 
        "Flexor digitorum brevis", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A patient has a fracture of the calcaneus. Which arch of the foot is most likely to be affected?",
        "Medial longitudinal arch", 
        "Lateral longitudinal arch", 
        "Transverse arch", 
        "Both medial and lateral arches", 
        "D", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A patient develops weakness in toe abduction after surgery. Which muscles are most likely affected?",
        "Dorsal interossei", 
        "Plantar interossei", 
        "Lumbricals", 
        "Abductor hallucis", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A child is brought in with abnormal curvature of the feet and is diagnosed with congenital flatfoot. Which structure is most likely deficient?",
        "Plantar calcaneonavicular ligament", 
        "Plantar aponeurosis", 
        "Tibialis posterior", 
        "Short plantar ligament", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A basketball player has a sprain that compromises the stability of the transverse arch. Which structure primarily supports this arch?",
        "Fibularis longus", 
        "Tibialis posterior", 
        "Plantar aponeurosis", 
        "Achilles tendon", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A patient has difficulty extending the big toe. Dysfunction in which nerve is most likely responsible?",
        "Deep peroneal nerve", 
        "Tibial nerve", 
        "Superficial peroneal nerve", 
        "Medial plantar nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A woman reports heel pain with tenderness over the plantar aponeurosis. Which condition is most consistent with her symptoms?",
        "Plantar fasciitis", 
        "Achilles tendonitis", 
        "Flatfoot", 
        "Tarsal tunnel syndrome", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A patient with nerve injury shows loss of sensation in the lateral sole of the foot. Which nerve is damaged?",
        "Lateral plantar nerve", 
        "Medial plantar nerve", 
        "Tibial nerve", 
        "Sural nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A patient has reduced blood flow in the dorsalis pedis artery. Which pulse point should the clinician palpate to confirm this?",
        "Dorsum of the foot between the first and second metatarsals", 
        "Lateral malleolus", 
        "Medial malleolus", 
        "Base of the toes", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A child with congenital talipes equinovarus (clubfoot) is treated surgically. Which aspect of the foot is primarily corrected?",
        "Medial longitudinal arch", 
        "Lateral longitudinal arch", 
        "Transverse arch", 
        "All of the above", 
        "D", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A patient has pain along the first metatarsal and hallux. Examination reveals dysfunction of a tendon supporting the medial arch. Which tendon is affected?",
        "Tibialis anterior", 
        "Fibularis longus", 
        "Flexor hallucis longus", 
        "Tibialis posterior", 
        "D", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "A patient presents with pain and deformity in the lateral sole. Which ligament is likely involved?",
        "Short plantar ligament", 
        "Long plantar ligament", 
        "Plantar calcaneonavicular ligament", 
        "Plantar aponeurosis", 
        "B", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    
    # Direct questions
    [
        "Which ligament provides primary support for the medial longitudinal arch?",
        "Plantar calcaneo-navicular ligament", 
        "Long plantar ligament", 
        "Short plantar ligament", 
        "Plantar aponeurosis", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "Which muscle primarily supports the transverse arch?",
        "Fibularis longus", 
        "Tibialis posterior", 
        "Plantar aponeurosis", 
        "Tibialis anterior", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "Which artery is the continuation of the anterior tibial artery?",
        "Dorsalis pedis artery", 
        "Posterior tibial artery", 
        "Medial plantar artery", 
        "Lateral plantar artery", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "Which nerve supplies the medial two-thirds of the sole of the foot?",
        "Medial plantar nerve", 
        "Lateral plantar nerve", 
        "Tibial nerve", 
        "Sural nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "Which artery forms the plantar arterial arch with the lateral plantar artery?",
        "Dorsalis pedis artery", 
        "Posterior tibial artery", 
        "Medial plantar artery", 
        "Lateral tarsal artery", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "Which structure is a thick fibrous band supporting the foot arches?",
        "Plantar aponeurosis", 
        "Achilles tendon", 
        "Plantar calcaneo-navicular ligament", 
        "Flexor retinaculum", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "Which ligament stabilizes the lateral longitudinal arch?",
        "Long plantar ligament", 
        "Plantar calcaneo-navicular ligament", 
        "Short plantar ligament", 
        "Plantar aponeurosis", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "Which nerve supplies most of the intrinsic muscles of the sole?",
        "Lateral plantar nerve", 
        "Medial plantar nerve", 
        "Tibial nerve", 
        "Sural nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "Which muscles are responsible for toe abduction?",
        "Dorsal interossei", 
        "Plantar interossei", 
        "Lumbricals", 
        "Flexor digitorum brevis", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "Which artery is palpated on the dorsum of the foot between the first and second metatarsals?",
        "Dorsalis pedis artery", 
        "Posterior tibial artery", 
        "Arcuate artery", 
        "Plantar arch artery", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
    [
        "Which nerve provides sensation to the lateral third of the sole?",
        "Lateral plantar nerve", 
        "Medial plantar nerve", 
        "Sural nerve", 
        "Tibial nerve", 
        "A", 
        "Anatomy", 
        2, 
        "Foot"
    ],
]
for mcq in mcqs:
    x = question(question_text = mcq[0],
                 option1 = mcq[1],
        option2 = mcq[2],
        option3 = mcq[3],
        option4 = mcq[4],
        answer = mcq[5],
        subject = 1,
        week = mcq[7],
        topic = mcq[8])
    x.save()