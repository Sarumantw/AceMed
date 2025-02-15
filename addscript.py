from questions.models import question
questions = [
    [
        "A 35-year-old male presents with difficulty in lifting his arm above 90 degrees. On examination, there is winging of the scapula. Which muscle is most likely affected?",
        "Pectoralis major",
        "Serratus anterior",
        "Latissimus dorsi",
        "Trapezius",
        "B"
    ],
    [
        "A patient complains of pain and weakness in shoulder abduction. On examination, there is a loss of sensation over the lower half of the deltoid. Which nerve is likely injured?",
        "Axillary nerve",
        "Radial nerve",
        "Median nerve",
        "Ulnar nerve",
        "A"
    ],
    [
        "A 40-year-old female presents with difficulty in adducting her arm. Which muscle is most likely involved?",
        "Pectoralis major",
        "Trapezius",
        "Supraspinatus",
        "Infraspinatus",
        "A"
    ],
    [
        "A patient has difficulty in rotating the scapula so that the glenoid cavity faces upward. Which muscle is most likely affected?",
        "Trapezius (upper fibers)",
        "Latissimus dorsi",
        "Rhomboid major",
        "Teres minor",
        "A"
    ],
    [
        "A patient presents with a flat shoulder and inability to abduct the arm from 15 degrees. Which nerve is likely damaged?",
        "Axillary nerve",
        "Radial nerve",
        "Median nerve",
        "Ulnar nerve",
        "A"
    ],
    [
        "A patient has difficulty in depressing the scapula. Which muscle is most likely affected?",
        "Pectoralis minor",
        "Trapezius (lower fibers)",
        "Rhomboid major",
        "Levator scapulae",
        "B"
    ],
    [
        "A patient presents with difficulty in medial rotation of the arm. Which muscle is most likely involved?",
        "Subscapularis",
        "Infraspinatus",
        "Teres minor",
        "Supraspinatus",
        "A"
    ],
    [
        "A patient has difficulty in retracting the scapula. Which muscle is most likely affected?",
        "Rhomboid major",
        "Pectoralis major",
        "Latissimus dorsi",
        "Serratus anterior",
        "A"
    ],
    [
        "A patient presents with difficulty in elevating the scapula. Which muscle is most likely involved?",
        "Levator scapulae",
        "Trapezius (upper fibers)",
        "Rhomboid minor",
        "Serratus anterior",
        "A"
    ],
    [
        "A patient has difficulty in extending the arm. Which muscle is most likely affected?",
        "Latissimus dorsi",
        "Pectoralis major",
        "Teres minor",
        "Supraspinatus",
        "A"
    ],
    [
        "A patient presents with difficulty in protracting the scapula. Which muscle is most likely involved?",
        "Serratus anterior",
        "Rhomboid major",
        "Trapezius",
        "Levator scapulae",
        "A"
    ],
    [
        "A patient has difficulty in lateral rotation of the arm. Which muscle is most likely affected?",
        "Infraspinatus",
        "Subscapularis",
        "Teres major",
        "Pectoralis major",
        "A"
    ],
    [
        "A patient presents with difficulty in initiating abduction of the arm from 0 to 15 degrees. Which muscle is most likely involved?",
        "Supraspinatus",
        "Infraspinatus",
        "Teres minor",
        "Subscapularis",
        "A"
    ],
    [
        "A patient has difficulty in holding the head of the humerus in the glenoid cavity during shoulder movement. Which group of muscles is most likely affected?",
        "Rotator cuff muscles",
        "Pectoralis major and minor",
        "Trapezius and latissimus dorsi",
        "Serratus anterior and rhomboids",
        "A"
    ],
    [
        "A patient presents with difficulty in forced inspiration. Which muscle is most likely involved?",
        "Serratus anterior",
        "Pectoralis major",
        "Latissimus dorsi",
        "Trapezius",
        "A"
    ],
    [
        "A patient has difficulty in depressing the clavicle. Which muscle is most likely affected?",
        "Subclavius",
        "Pectoralis minor",
        "Trapezius",
        "Levator scapulae",
        "A"
    ],
    [
        "A patient presents with difficulty in stabilizing the shoulder joint. Which muscle is most likely involved?",
        "Subscapularis",
        "Infraspinatus",
        "Teres minor",
        "Supraspinatus",
        "A"
    ],
    [
        "A patient has difficulty in upward rotation of the scapula during abduction above 90 degrees. Which muscle is most likely affected?",
        "Serratus anterior",
        "Trapezius",
        "Rhomboid major",
        "Levator scapulae",
        "A"
    ],
    [
        "A patient presents with difficulty in keeping the medial border of the scapula applied to the chest wall. Which muscle is most likely involved?",
        "Serratus anterior",
        "Rhomboid major",
        "Trapezius",
        "Levator scapulae",
        "A"
    ],
    [
        "A patient has difficulty in medial rotation and extension of the arm. Which muscle is most likely affected?",
        "Teres major",
        "Infraspinatus",
        "Supraspinatus",
        "Subscapularis",
        "A"
    ],
    [
        "Which muscle originates from the anterior surface of the medial half of the clavicle and inserts into the lateral lip of the bicipital groove of the humerus?",
        "Pectoralis major",
        "Pectoralis minor",
        "Subclavius",
        "Serratus anterior",
        "A"
    ],
    [
        "Which nerve supplies the pectoralis major muscle?",
        "Medial pectoral nerve",
        "Lateral pectoral nerve",
        "Both A and B",
        "Thoracodorsal nerve",
        "C"
    ],
    [
        "Which muscle is responsible for depression and protraction of the scapula?",
        "Pectoralis minor",
        "Pectoralis major",
        "Subclavius",
        "Serratus anterior",
        "A"
    ],
    [
        "Which muscle originates from the 3rd, 4th, and 5th ribs and inserts into the coracoid process of the scapula?",
        "Pectoralis major",
        "Pectoralis minor",
        "Subclavius",
        "Serratus anterior",
        "B"
    ],
    [
        "Which muscle is responsible for depressing the clavicle and steadying it during shoulder movements?",
        "Subclavius",
        "Pectoralis minor",
        "Pectoralis major",
        "Serratus anterior",
        "A"
    ],
    [
        "Which muscle originates from the posterior part of the iliac crest and inserts into the floor of the intertubercular groove of the humerus?",
        "Latissimus dorsi",
        "Trapezius",
        "Rhomboid major",
        "Levator scapulae",
        "A"
    ],
    [
        "Which muscle is responsible for elevation and downward retraction of the scapula?",
        "Levator scapulae",
        "Trapezius",
        "Rhomboid major",
        "Serratus anterior",
        "A"
    ],
    [
        "Which muscle originates from the subscapular fossa and inserts into the lesser tuberosity of the humerus?",
        "Subscapularis",
        "Supraspinatus",
        "Infraspinatus",
        "Teres minor",
        "A"
    ],
    [
        "Which muscle is responsible for initiating the abduction of the arm from 0 to 15 degrees?",
        "Supraspinatus",
        "Infraspinatus",
        "Teres minor",
        "Subscapularis",
        "A"
    ],
    [
        "Which muscle is responsible for lateral rotation of the arm?",
        "Infraspinatus",
        "Subscapularis",
        "Teres major",
        "Pectoralis major",
        "A"
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
                week = 3,
                topic = "Shoulder and Scapula"
                )
    x.save()
    print(i)
    i+=1