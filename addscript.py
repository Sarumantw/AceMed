from questions.models import question
questions = [
    [
        "A 35-year-old male presents with weakness in flexing his thumb and index finger. He also reports numbness in the lateral two-thirds of his palm. Which nerve is most likely affected?",
        "Ulnar nerve",
        "Radial nerve",
        "Median nerve",
        "Musculocutaneous nerve",
        "C"
    ],
    [
        "A patient complains of difficulty in extending their wrist and fingers after a fracture of the humerus. Which nerve is most likely injured?",
        "Median nerve",
        "Ulnar nerve",
        "Radial nerve",
        "Axillary nerve",
        "C"
    ],
    [
        "A 40-year-old female presents with tingling and numbness in the medial one-third of her palm and the medial one and a half fingers. Which nerve is likely affected?",
        "Median nerve",
        "Ulnar nerve",
        "Radial nerve",
        "Musculocutaneous nerve",
        "B"
    ],
    [
        "A patient has difficulty pronating their forearm and flexing their wrist. Which muscle group is most likely affected?",
        "Posterior compartment muscles",
        "Anterior compartment muscles",
        "Lateral compartment muscles",
        "Deep posterior compartment muscles",
        "B"
    ],
    [
        "A patient presents with a deep cut on the anterior forearm, resulting in the inability to flex the distal phalanges of the fingers. Which muscle is most likely injured?",
        "Flexor digitorum superficialis",
        "Flexor digitorum profundus",
        "Flexor carpi ulnaris",
        "Pronator teres",
        "B"
    ],
    [
        "A patient has a fracture of the radius and is unable to supinate their forearm. Which muscle is most likely affected?",
        "Pronator teres",
        "Supinator",
        "Brachioradialis",
        "Flexor carpi radialis",
        "B"
    ],
    [
        "A patient presents with a laceration on the lateral side of the forearm, resulting in the inability to extend the thumb. Which nerve is most likely injured?",
        "Median nerve",
        "Ulnar nerve",
        "Radial nerve",
        "Axillary nerve",
        "C"
    ],
    [
        "A patient has a deep cut on the medial side of the forearm, resulting in the inability to flex the wrist medially. Which muscle is most likely injured?",
        "Flexor carpi radialis",
        "Flexor carpi ulnaris",
        "Palmaris longus",
        "Pronator teres",
        "B"
    ],
    [
        "A patient presents with a fracture of the ulna and is unable to flex the distal phalanx of the thumb. Which muscle is most likely affected?",
        "Flexor pollicis longus",
        "Flexor digitorum profundus",
        "Flexor digitorum superficialis",
        "Pronator quadratus",
        "A"
    ],
    [
        "A patient has a deep laceration on the posterior forearm, resulting in the inability to extend the fingers. Which muscle group is most likely affected?",
        "Anterior compartment muscles",
        "Posterior compartment muscles",
        "Lateral compartment muscles",
        "Deep anterior compartment muscles",
        "B"
    ],
    [
        "A patient presents with a fracture of the humerus and is unable to extend their wrist. Which nerve is most likely injured?",
        "Median nerve",
        "Ulnar nerve",
        "Radial nerve",
        "Axillary nerve",
        "C"
    ],
    [
        "A patient has a deep cut on the anterior forearm, resulting in the inability to pronate the forearm. Which muscle is most likely injured?",
        "Pronator teres",
        "Pronator quadratus",
        "Supinator",
        "Brachioradialis",
        "A"
    ],
    [
        "A patient presents with a fracture of the radius and is unable to flex the wrist laterally. Which muscle is most likely affected?",
        "Flexor carpi radialis",
        "Flexor carpi ulnaris",
        "Palmaris longus",
        "Pronator teres",
        "A"
    ],
    [
        "A patient has a deep laceration on the medial side of the forearm, resulting in the inability to flex the distal phalanges of the medial two fingers. Which muscle is most likely injured?",
        "Flexor digitorum superficialis",
        "Flexor digitorum profundus",
        "Flexor carpi ulnaris",
        "Pronator teres",
        "B"
    ],
    [
        "A patient presents with a fracture of the ulna and is unable to flex the wrist medially. Which muscle is most likely affected?",
        "Flexor carpi radialis",
        "Flexor carpi ulnaris",
        "Palmaris longus",
        "Pronator teres",
        "B"
    ],
    [
        "A patient has a deep cut on the posterior forearm, resulting in the inability to extend the thumb. Which muscle is most likely injured?",
        "Extensor pollicis longus",
        "Extensor pollicis brevis",
        "Abductor pollicis longus",
        "Extensor indicis",
        "A"
    ],
    [
        "A patient presents with a fracture of the radius and is unable to supinate the forearm. Which muscle is most likely affected?",
        "Pronator teres",
        "Supinator",
        "Brachioradialis",
        "Flexor carpi radialis",
        "B"
    ],
    [
        "A patient has a deep laceration on the anterior forearm, resulting in the inability to flex the distal phalanges of the fingers. Which muscle is most likely injured?",
        "Flexor digitorum superficialis",
        "Flexor digitorum profundus",
        "Flexor carpi ulnaris",
        "Pronator teres",
        "B"
    ],
    [
        "A patient presents with a fracture of the humerus and is unable to extend their fingers. Which nerve is most likely injured?",
        "Median nerve",
        "Ulnar nerve",
        "Radial nerve",
        "Axillary nerve",
        "C"
    ],
    [
        "A patient has a deep cut on the medial side of the forearm, resulting in the inability to flex the wrist medially. Which muscle is most likely injured?",
        "Flexor carpi radialis",
        "Flexor carpi ulnaris",
        "Palmaris longus",
        "Pronator teres",
        "B"
    ],
    [
        "Which artery is the main blood supply to the anterior compartment of the forearm?",
        "Radial artery",
        "Ulnar artery",
        "Brachial artery",
        "Posterior interosseous artery",
        "B"
    ],
    [
        "Which nerve supplies the flexor carpi ulnaris muscle?",
        "Median nerve",
        "Ulnar nerve",
        "Radial nerve",
        "Musculocutaneous nerve",
        "B"
    ],
    [
        "Which muscle is responsible for pronation of the forearm?",
        "Supinator",
        "Pronator teres",
        "Brachioradialis",
        "Flexor carpi radialis",
        "B"
    ],
    [
        "Which nerve passes through the cubital fossa?",
        "Ulnar nerve",
        "Radial nerve",
        "Median nerve",
        "Axillary nerve",
        "C"
    ],
    [
        "Which muscle is innervated by the deep branch of the radial nerve?",
        "Brachioradialis",
        "Extensor carpi radialis longus",
        "Supinator",
        "Extensor carpi ulnaris",
        "C"
    ],
    [
        "Which artery anastomoses around the wrist with the radial artery?",
        "Ulnar artery",
        "Brachial artery",
        "Posterior interosseous artery",
        "Anterior interosseous artery",
        "A"
    ],
    [
        "Which nerve supplies the skin of the lateral two-thirds of the palm?",
        "Ulnar nerve",
        "Median nerve",
        "Radial nerve",
        "Musculocutaneous nerve",
        "B"
    ],
    [
        "Which muscle is part of the deep posterior compartment of the forearm?",
        "Extensor digitorum",
        "Extensor carpi ulnaris",
        "Abductor pollicis longus",
        "Extensor carpi radialis brevis",
        "C"
    ],
    [
        "Which nerve is responsible for the sensation of the medial one and a half fingers?",
        "Median nerve",
        "Ulnar nerve",
        "Radial nerve",
        "Musculocutaneous nerve",
        "B"
    ],
    [
        "Which artery is a branch of the common interosseous artery?",
        "Radial artery",
        "Ulnar artery",
        "Anterior interosseous artery",
        "Posterior interosseous artery",
        "C"
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
                subject = 1,
                week = 4,
                topic = "Forearm"
                )
    x.save()
    print(i)
    i+=1