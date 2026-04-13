import streamlit as st
from interviewer import generate_question
from evaluator import evaluate_answers

st.set_page_config(page_title="AI Mock Interviewer", layout="centered")

st.title("🎤 AI Mock Interviewer")

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.questions = []
    st.session_state.answers = []
    st.session_state.current_question = ""
    st.session_state.finished = False

# ---------------- INPUT SECTION ----------------
if st.session_state.step == 0:
    role = st.selectbox("Select Job Role", ["Frontend Developer", "Data Analyst", "ML Engineer"])
    difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

    if st.button("Start Interview"):
        st.session_state.role = role
        st.session_state.difficulty = difficulty
        st.session_state.step = 1

# ---------------- INTERVIEW FLOW ----------------
if st.session_state.step > 0 and not st.session_state.finished:

    # Generate first question
    if st.session_state.current_question == "":
        q = generate_question(
            st.session_state.role,
            st.session_state.difficulty,
            st.session_state.questions
        )
        st.session_state.current_question = q
        st.session_state.questions.append(q)

    # Progress
    st.subheader(f"Question {len(st.session_state.questions)} of 5")

    # Chat UI
    for i in range(len(st.session_state.questions)):
        st.markdown(f"🤖 **AI:** {st.session_state.questions[i]}")
        if i < len(st.session_state.answers):
            st.markdown(f"👤 **You:** {st.session_state.answers[i]}")

    # Answer input
    answer = st.text_area("Your Answer", key=f"answer_{len(st.session_state.answers)}")

    if st.button("Submit Answer"):

        # Validation
        if not answer.strip():
            st.warning("Please enter an answer.")
        elif len(answer.split()) < 5:
            st.warning("Answer too short. Write at least 5 words.")
        else:
            st.session_state.answers.append(answer)
            st.session_state.current_question = ""

            # Stop after 5 questions
            if len(st.session_state.answers) == 5:
                st.session_state.finished = True
            else:
                st.rerun()

# ---------------- FINAL EVALUATION ----------------
if st.session_state.finished:

    st.subheader("📊 Final Evaluation")

    qa_list = []
    for i in range(5):
        qa_list.append({
            "question": st.session_state.questions[i],
            "answer": st.session_state.answers[i]
        })

    result = evaluate_answers(qa_list)

    st.markdown("### 🧠 Feedback")
    st.write(result)

    # Reset button
    if st.button("🔄 Start New Interview"):
        st.session_state.clear()
        st.rerun()