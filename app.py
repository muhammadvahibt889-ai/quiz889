st.set_page_config(
    page_title="QuizNova | Quiz Battle Arena",
    page_icon="🧠",
    layout="centered"
)

TIME_LIMIT = 15

# ---------------- QUESTION BANK ----------------
QUIZ = {
    "General Knowledge": [
        ("What is the capital of India?", ["Mumbai", "New Delhi", "Chennai", "Kolkata"], "New Delhi"),
        ("Which is the largest ocean?", ["Atlantic", "Indian", "Pacific", "Arctic"], "Pacific"),
        ("How many days are in a leap year?", ["365", "366", "364", "360"], "366"),
        ("Which is the national animal of India?", ["Lion", "Tiger", "Elephant", "Leopard"], "Tiger"),
        ("Which planet is closest to the Sun?", ["Venus", "Earth", "Mercury", "Mars"], "Mercury"),
        ("How many colours are in a rainbow?", ["5", "6", "7", "8"], "7"),
        ("What is the currency of Japan?", ["Yuan", "Yen", "Won", "Dollar"], "Yen"),
        ("Which is the largest continent?", ["Africa", "Europe", "Asia", "Australia"], "Asia"),
        ("Which country has the pyramids of Giza?", ["Egypt", "Greece", "Mexico", "India"], "Egypt"),
        ("How many sides does a hexagon have?", ["5", "6", "7", "8"], "6"),
    ],
    "Science": [
        ("Which planet is called the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
        ("Which gas do plants absorb during photosynthesis?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"], "Carbon dioxide"),
        ("What is the chemical formula of water?", ["CO2", "O2", "H2O", "NaCl"], "H2O"),
        ("Which organ pumps blood?", ["Lungs", "Brain", "Heart", "Kidney"], "Heart"),
        ("What is the centre of an atom called?", ["Electron", "Nucleus", "Cell", "Molecule"], "Nucleus"),
        ("Which force pulls objects towards Earth?", ["Friction", "Magnetism", "Gravity", "Pressure"], "Gravity"),
        ("At what temperature does water boil at sea level?", ["50°C", "75°C", "100°C", "150°C"], "100°C"),
        ("Which vitamin can the body produce with sunlight exposure?", ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"], "Vitamin D"),
        ("What is the hardest naturally occurring substance?", ["Iron", "Quartz", "Diamond", "Gold"], "Diamond"),
        ("Which part of a plant absorbs water?", ["Flower", "Leaf", "Root", "Fruit"], "Root"),
    ],
    "Mathematics": [
        ("What is 12 × 8?", ["86", "96", "108", "88"], "96"),
        ("What is the square root of 144?", ["10", "11", "12", "14"], "12"),
        ("What is 15 + 27?", ["32", "42", "52", "40"], "42"),
        ("What is 100 divided by 4?", ["20", "25", "40", "50"], "25"),
        ("How many degrees are in a right angle?", ["45", "90", "180", "360"], "90"),
        ("What is 9 squared?", ["18", "72", "81", "99"], "81"),
        ("What is half of 3/4?", ["3/8", "1/2", "2/3", "1/4"], "3/8"),
        ("Perimeter of a square with side 5 cm?", ["10 cm", "15 cm", "20 cm", "25 cm"], "20 cm"),
        ("What is 7 × 7?", ["42", "48", "49", "56"], "49"),
        ("What is 20% of 200?", ["20", "30", "40", "50"], "40"),
    ],
    "History": [
        ("In which year did India gain independence?", ["1945", "1947", "1950", "1952"], "1947"),
        ("Who was the first Mughal emperor?", ["Akbar", "Babur", "Humayun", "Shah Jahan"], "Babur"),
        ("Who commissioned the Taj Mahal?", ["Akbar", "Babur", "Shah Jahan", "Aurangzeb"], "Shah Jahan"),
        ("Who was known as the Iron Man of India?", ["Jawaharlal Nehru", "Sardar Patel", "Subhas Chandra Bose", "B. R. Ambedkar"], "Sardar Patel"),
        ("Which ancient civilization built the pyramids of Giza?", ["Roman", "Egyptian", "Greek", "Chinese"], "Egyptian"),
        ("Who was the first Prime Minister of India?", ["Mahatma Gandhi", "Rajendra Prasad", "Jawaharlal Nehru", "Sardar Patel"], "Jawaharlal Nehru"),
        ("The French Revolution began in which year?", ["1776", "1789", "1815", "1914"], "1789"),
        ("Who led the Salt March in 1930?", ["Bhagat Singh", "Mahatma Gandhi", "Nehru", "Tilak"], "Mahatma Gandhi"),
        ("Which city was the capital of the Vijayanagara Empire?", ["Hampi", "Delhi", "Agra", "Patna"], "Hampi"),
        ("Who was India's first woman Prime Minister?", ["Indira Gandhi", "Sarojini Naidu", "Pratibha Patil", "Sonia Gandhi"], "Indira Gandhi"),
    ],
    "Sports": [
        ("How many players from one football team are on the field?", ["9", "10", "11", "12"], "11"),
        ("Which sport uses a shuttlecock?", ["Tennis", "Badminton", "Cricket", "Hockey"], "Badminton"),
        ("How many rings are on the Olympic symbol?", ["4", "5", "6", "7"], "5"),
        ("Wimbledon is associated with which sport?", ["Football", "Tennis", "Golf", "Rugby"], "Tennis"),
        ("How many runs is a cricket boundary worth when the ball clears the boundary without bouncing?", ["2", "4", "5", "6"], "6"),
        ("Which country hosted the first modern Olympic Games in 1896?", ["France", "Greece", "Italy", "USA"], "Greece"),
        ("Which sport uses a puck?", ["Ice hockey", "Basketball", "Baseball", "Volleyball"], "Ice hockey"),
        ("How long is a standard football match, excluding added time?", ["60 minutes", "80 minutes", "90 minutes", "100 minutes"], "90 minutes"),
        ("Which chess piece moves in an L-shape?", ["Bishop", "Rook", "Knight", "Queen"], "Knight"),
        ("Taekwondo originated in which country?", ["Japan", "China", "South Korea", "Thailand"], "South Korea"),
    ],
    "Computer Science": [
        ("What does CPU stand for?", ["Central Processing Unit", "Computer Power Unit", "Central Program Utility", "Control Processing User"], "Central Processing Unit"),
        ("Which is a programming language?", ["Python", "Windows", "Chrome", "Google"], "Python"),
        ("What does RAM stand for?", ["Read Access Memory", "Random Access Memory", "Run All Memory", "Rapid Application Mode"], "Random Access Memory"),
        ("Which device is used to point and click?", ["Monitor", "Printer", "Mouse", "Speaker"], "Mouse"),
        ("What does HTML mainly define?", ["Webpage structure", "Computer hardware", "Internet speed", "Antivirus protection"], "Webpage structure"),
        ("Which number system uses only 0 and 1?", ["Decimal", "Binary", "Octal", "Roman"], "Binary"),
        ("What is commonly called the brain of a computer?", ["Keyboard", "CPU", "Mouse", "Monitor"], "CPU"),
        ("Which of these is a web browser?", ["Linux", "Firefox", "Python", "Excel"], "Firefox"),
        ("What does URL stand for?", ["Uniform Resource Locator", "Universal Record Link", "United Resource Language", "User Reference Location"], "Uniform Resource Locator"),
        ("Which shortcut copies selected text on Windows?", ["Ctrl+V", "Ctrl+X", "Ctrl+C", "Ctrl+Z"], "Ctrl+C"),
    ],
    "Islamic Studies": [
        ("How many Surahs are in the Holy Quran?", ["110", "112", "114", "116"], "114"),
        ("In which city was Prophet Muhammad ﷺ born?", ["Madinah", "Makkah", "Taif", "Jerusalem"], "Makkah"),
        ("What is the first month of the Islamic calendar?", ["Ramadan", "Muharram", "Shawwal", "Rajab"], "Muharram"),
        ("Which angel brought revelation to the prophets?", ["Mikail", "Israfil", "Jibril", "Malik"], "Jibril"),
        ("How many obligatory daily prayers are there?", ["3", "4", "5", "6"], "5"),
        ("Which holy book was revealed to Prophet Musa عليه السلام?", ["Zabur", "Tawrat", "Injil", "Quran"], "Tawrat"),
        ("Where did Prophet Muhammad ﷺ migrate from Makkah?", ["Taif", "Jerusalem", "Madinah", "Damascus"], "Madinah"),
        ("What is the name of the well near the Kaaba?", ["Zamzam", "Salsabil", "Kawthar", "Barhut"], "Zamzam"),
        ("During which month do Muslims fast?", ["Muharram", "Ramadan", "Safar", "Dhul Hijjah"], "Ramadan"),
        ("What is the direction Muslims face during prayer called?", ["Mihrab", "Qiblah", "Minbar", "Mimbar"], "Qiblah"),
    ],
}

# ---------------- SESSION STATE ----------------
defaults = {
    "started": False,
    "finished": False,
    "player": "",
    "quiz": [],
    "index": 0,
    "score": 0,
    "review": [],
    "start_time": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def start_quiz(player, category):
    if category == "All Categories":
        quiz = [
            (cat, question)
            for cat, questions in QUIZ.items()
            for question in questions
        ]
    else:
        quiz = [(category, q) for q in QUIZ[category]]

    random.shuffle(quiz)

    st.session_state.started = True
    st.session_state.finished = False
    st.session_state.player = player.strip() or "Player"
    st.session_state.quiz = quiz
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.review = []
    st.session_state.start_time = time.time()


def save_answer(selected):
    category, question_data = st.session_state.quiz[st.session_state.index]
    question, options, correct_answer = question_data

    is_correct = selected == correct_answer

    if is_correct:
        st.session_state.score += 1

    st.session_state.review.append({
        "category": category,
        "question": question,
        "your_answer": selected if selected else "No answer (time expired)",
        "correct_answer": correct_answer,
        "correct": is_correct,
    })

    st.session_state.index += 1

    if st.session_state.index >= len(st.session_state.quiz):
        st.session_state.finished = True
    else:
        st.session_state.start_time = time.time()


# ---------------- STYLING ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #17133b, #101827);
    color: #f5f7ff;
}
h1, h2, h3, p, label {
    color: #f5f7ff;
}
div.stButton > button {
    border-radius: 12px;
    min-height: 45px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🧠 QuizNova")
st.caption("CHALLENGE YOUR MIND • CONQUER THE QUIZ")
st.divider()

# ---------------- START SCREEN ----------------
if not st.session_state.started:
    st.subheader("🏆 Welcome to Quiz Battle Arena")
    st.write("Test your knowledge, beat the clock, and earn your rank!")

    player_name = st.text_input("Enter your player name", placeholder="Your name")

    category = st.selectbox(
        "Choose your category",
        ["All Categories"] + list(QUIZ.keys())
    )

    if category == "All Categories":
        total_questions = sum(len(q) for q in QUIZ.values())
    else:
        total_questions = len(QUIZ[category])

    col1, col2 = st.columns(2)
    col1.metric("Questions", total_questions)
    col2.metric("Time per question", f"{TIME_LIMIT} sec")

    st.info("Every category has 10 questions. Correct answers earn 1 point.")

    if st.button("🚀 START QUIZ", type="primary", use_container_width=True):
        start_quiz(player_name, category)
        st.rerun()

# ---------------- ACTIVE QUIZ ----------------
elif not st.session_state.finished:
    current = st.session_state.index
    total = len(st.session_state.quiz)
    category, data = st.session_state.quiz[current]
    question, original_options, correct_answer = data

    # Refresh the page every second so the countdown updates.
    st_autorefresh(interval=1000, limit=None, key="quiz_timer_refresh")

    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, TIME_LIMIT - int(elapsed))

    if remaining <= 0:
        save_answer(None)
        st.rerun()

    st.write(f"👤 Player: **{st.session_state.player}**")
    st.write(f"📚 Category: **{category}**")
    st.progress(current / total, text=f"Question {current + 1} of {total}")

    col1, col2 = st.columns(2)
    col1.metric("⭐ Score", st.session_state.score)
    col2.metric("⏳ Time remaining", f"{remaining}s")

    st.progress(remaining / TIME_LIMIT)

    st.subheader(question)

    # Keep the same option order during timer refreshes.
    option_key = f"options_{current}"
    if option_key not in st.session_state:
        shuffled = original_options.copy()
        random.shuffle(shuffled)
        st.session_state[option_key] = shuffled

    selected = st.radio(
        "Select your answer:",
        st.session_state[option_key],
        index=None,
        key=f"answer_{current}"
    )

    if st.button("Submit Answer ➜", type="primary", use_container_width=True):
        if selected is None:
            st.warning("Please select an answer first.")
        else:
            save_answer(selected)
            st.rerun()

    st.caption("The question will automatically move on when the timer reaches zero.")

# ---------------- RESULTS ----------------
else:
    total = len(st.session_state.quiz)
    score = st.session_state.score
    percentage = score / total * 100 if total else 0

    if percentage == 100:
        rank = "🏆 QUIZ CHAMPION"
    elif percentage >= 80:
        rank = "🥇 GOLD"
    elif percentage >= 60:
        rank = "🥈 SILVER"
    elif percentage >= 40:
        rank = "🥉 BRONZE"
    else:
        rank = "📘 KEEP PRACTISING"

    st.balloons()
    st.subheader("🎉 Quiz Completed!")
    st.write(f"Well done, **{st.session_state.player}**!")

    col1, col2, col3 = st.columns(3)
    col1.metric("Final Score", f"{score}/{total}")
    col2.metric("Percentage", f"{percentage:.1f}%")
    col3.metric("Correct Answers", score)

    st.success(f"Your Rank: {rank}")
    st.progress(percentage / 100)

    st.subheader("📝 Answer Review")

    for i, item in enumerate(st.session_state.review, 1):
        symbol = "✅" if item["correct"] else "❌"
        with st.expander(f"{symbol} Question {i}: {item['question']}"):
            st.write(f"**Category:** {item['category']}")
            st.write(f"**Your answer:** {item['your_answer']}")
            st.write(f"**Correct answer:** {item['correct_answer']}")

    if st.button("🔄 Play Again", type="primary", use_container_width=True):
        st.session_state.started = False
        st.session_state.finished = False
        st.session_state.quiz = []
        st.session_state.review = []
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.start_time = None
        st.rerun()

st.divider()
st.caption("QuizNova • Learn More. Think Faster. Aim Higher.")
