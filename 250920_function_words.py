import streamlit as st

# クイズのデータをリスト形式で用意（Flask版と同じ）
quiz_data = [
    {
        "question": "1. I will meet you ___ the station.",
        "options": ["on", "in", "at", "for"],
        "answer": "at",
        "explanation": "「at」は特定の地点を指す前置詞です。"
    },
    {
        "question": "2. She studied hard, ___ she passed the exam easily.",
        "options": ["but", "so", "or", "because"],
        "answer": "so",
        "explanation": "「so」は「だから」という原因と結果の関係を示します。"
    },
    # ... (前回の回答と同じ残りの問題データをここに追加) ...
    {
        "question": "3. Which one is a function word in 'I have a new book.'?",
        "options": ["new", "book", "have", "a"],
        "answer": "a",
        "explanation": "冠詞「a」は文法的な役割を担う機能語です。"
    },
    {
        "question": "4. She is ___ best student in our class.",
        "options": ["a", "an", "the", "(no article)"],
        "answer": "the",
        "explanation": "「best」のような最上級の前には定冠詞「the」をつけます。"
    },
    {
        "question": "5. My sister loves reading. ___ favorite author is Jane Austen.",
        "options": ["She", "Her", "Hers", "She's"],
        "answer": "Her",
        "explanation": "「彼女の」という意味の所有格の代名詞が必要です。"
    },
    {
        "question": "6. ___ you speak English?",
        "options": ["Are", "Is", "Do", "Have"],
        "answer": "Do",
        "explanation": "一般動詞「speak」の疑問文を作るには助動詞「Do」を使います。"
    },
    {
        "question": "7. I wanted to go to the party, ___ I was too tired.",
        "options": ["and", "so", "but", "for"],
        "answer": "but",
        "explanation": "「しかし」という逆接の関係を示す接続詞です。"
    },
    {
        "question": "8. Which group consists of only function words?",
        "options": ["run, eat, think", "happy, sad, big", "of, with, from", "car, house, dog"],
        "answer": "of, with, from",
        "explanation": "これらはすべて単語間の関係を示す前置詞（機能語）です。"
    },
    {
        "question": "9. There isn't ___ milk left in the fridge.",
        "options": ["some", "any", "a lot", "many"],
        "answer": "any",
        "explanation": "「any」は否定文や疑問文で使われます。"
    },
    {
        "question": "10. The person ___ called you yesterday is my boss.",
        "options": ["which", "who", "whose", "what"],
        "answer": "who",
        "explanation": "先行詞が「人」で、主格の働きをする関係代名詞は「who」です。"
    }
]

# --- アプリのUI部分 ---

st.title("英語の機能語クイズ 📝")
st.write("各問題で最も適切な選択肢を選んでください。")

# ユーザーの回答を保存するリスト
user_answers = []

# 問題と選択肢をフォームで表示
with st.form("quiz_form"):
    for i, item in enumerate(quiz_data):
        st.subheader(item["question"])
        answer = st.radio(
            f"選択肢 {i+1}",
            options=item["options"],
            key=f"q{i}",
            label_visibility="collapsed" # "選択肢"というラベルを非表示にする
        )
        user_answers.append(answer)
    
    # フォームの送信ボタン
    submitted = st.form_submit_button("答え合わせをする")


# ボタンが押されたら答え合わせを実行
if submitted:
    score = 0
    st.header("クイズ結果")
    
    for i, item in enumerate(quiz_data):
        user_answer = user_answers[i]
        correct_answer = item["answer"]
        
        if user_answer == correct_answer:
            score += 1
            st.success(f"問題 {i+1}: 正解！◎")
        else:
            st.error(f"問題 {i+1}: 不正解 ✕")
            st.write(f"あなたの回答: {user_answer}")
            st.write(f"正解: {correct_answer}")
        
        st.info(f"解説: {item['explanation']}")
        st.markdown("---")

    # 最終スコアの表示
    st.subheader(f"あなたのスコア: {score} / {len(quiz_data)} 点")
    if score == len(quiz_data):
        st.balloons()
        st.success("素晴らしい！全問正解です！")