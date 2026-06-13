import streamlit as st

st.set_page_config(
    page_title="⚡ MBTI 포켓몬 도감",
    page_icon="⚡",
    layout="centered"
)

st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:3rem;
    font-weight:bold;
    color:#ffcc00;
}

.sub{
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

.card{
    background:linear-gradient(135deg,#fff8d6,#ffffff);
    padding:25px;
    border-radius:25px;
    border:4px solid #ffcc00;
    box-shadow:0 8px 20px rgba(0,0,0,0.15);
}

.pokemon{
    font-size:2.5rem;
    font-weight:bold;
    text-align:center;
}

.desc{
    font-size:1.1rem;
    line-height:1.8;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">⚡ MBTI 포켓몬 도감 ⚡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub">나의 성격과 가장 닮은 포켓몬은 누구일까? 🤔</div>',
    unsafe_allow_html=True
)

pokemon_data = {
    "INTJ": {
        "pokemon": "🧠 뮤츠",
        "title": "전략가 포켓몬",
        "desc": "혼자 생각하는 시간을 좋아하고 계획 세우는 걸 잘해요. 목표를 정하면 끝까지 밀고 나가는 타입!"
    },
    "INTP": {
        "pokemon": "🦊 이브이",
        "title": "무한 가능성 포켓몬",
        "desc": "호기심이 많고 새로운 것을 배우는 걸 좋아해요. 성장 가능성이 무궁무진!"
    },
    "ENTJ": {
        "pokemon": "🔥 리자몽",
        "title": "카리스마 포켓몬",
        "desc": "리더십이 강하고 추진력이 뛰어나요. 목표를 향해 거침없이 돌진!"
    },
    "ENTP": {
        "pokemon": "😈 팬텀",
        "title": "장난꾸러기 천재",
        "desc": "재치 있고 창의적이에요. 늘 새로운 아이디어로 사람들을 놀라게 해요."
    },
    "INFJ": {
        "pokemon": "🌊 라프라스",
        "title": "힐러 포켓몬",
        "desc": "배려심이 깊고 공감 능력이 뛰어나요. 친구들이 고민 상담하러 자주 찾아와요."
    },
    "INFP": {
        "pokemon": "✨ 뮤",
        "title": "순수한 영혼 포켓몬",
        "desc": "상상력이 풍부하고 감성이 깊어요. 자신만의 특별한 세계가 있어요."
    },
    "ENFJ": {
        "pokemon": "⚡ 피카츄",
        "title": "인기 만점 포켓몬",
        "desc": "사람들을 잘 챙기고 분위기를 이끌어요. 어디서나 사랑받는 타입!"
    },
    "ENFP": {
        "pokemon": "🌈 토게피",
        "title": "행복 전도사",
        "desc": "밝고 긍정적이며 에너지가 넘쳐요. 주변 사람들을 웃게 만드는 재주가 있어요."
    },
    "ISTJ": {
        "pokemon": "🐢 거북왕",
        "title": "든든한 수호자",
        "desc": "책임감이 강하고 믿음직해요. 맡은 일은 반드시 끝내는 타입!"
    },
    "ISFJ": {
        "pokemon": "🌿 이상해꽃",
        "title": "따뜻한 친구",
        "desc": "친절하고 헌신적이에요. 주변 사람들을 편안하게 해줘요."
    },
    "ESTJ": {
        "pokemon": "💪 괴력몬",
        "title": "실행력 만렙",
        "desc": "결단력이 뛰어나고 행동력이 강해요. 믿고 맡길 수 있는 리더!"
    },
    "ESFJ": {
        "pokemon": "🎤 푸린",
        "title": "분위기 메이커",
        "desc": "사교성이 좋고 사람들과 함께하는 걸 좋아해요."
    },
    "ISTP": {
        "pokemon": "🥋 루카리오",
        "title": "쿨한 해결사",
        "desc": "침착하고 실전 감각이 뛰어나요. 위기 상황에서도 강한 타입!"
    },
    "ISFP": {
        "pokemon": "🦋 버터플",
        "title": "감성 아티스트",
        "desc": "자유롭고 감수성이 풍부해요. 아름다움을 사랑하는 타입!"
    },
    "ESTP": {
        "pokemon": "⚡ 라이츄",
        "title": "액션 히어로",
        "desc": "모험심이 강하고 에너지가 넘쳐요. 새로운 도전을 즐겨요!"
    },
    "ESFP": {
        "pokemon": "😎 꼬부기",
        "title": "인싸 포켓몬",
        "desc": "유쾌하고 장난기 많아요. 친구들 사이에서 늘 인기 만점!"
    }
}

mbti = st.selectbox(
    "🎮 MBTI를 선택하세요!",
    list(pokemon_data.keys())
)

if st.button("🔍 내 포켓몬 찾기!", use_container_width=True):

    st.balloons()

    result = pokemon_data[mbti]

    st.markdown(
        f"""
        <div class="card">
            <div class="pokemon">{result['pokemon']}</div>
            <h2 style="text-align:center;">{result['title']}</h2>
            <p class="desc">{result['desc']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(f"🎉 {mbti} 유형의 당신은 '{result['pokemon']}' 와(과) 가장 잘 어울려요!")

    st.markdown("### 🌟 특별 진단")
    st.info(
        f"""
        ✔️ 당신의 포켓몬 에너지 : {result['pokemon']}

        ✔️ 친구들이 보는 당신 : 개성 넘치는 사람 😆

        ✔️ 오늘의 포켓몬 한마디 :
        "자신만의 매력을 믿고 모험을 떠나자! 🚀"
        """
    )

st.markdown("---")
st.caption("⚡ Pokémon MBTI Dex | 팬이 만든 비공식 테스트 🎈")
