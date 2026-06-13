import streamlit as st

st.set_page_config(
    page_title="⚡ MBTI 포켓몬 카드",
    page_icon="⚡",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fef9c3 0%, #ffffff 100%);
}

.title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 20px;
}

.pokemon-card {
    background: linear-gradient(135deg,#ffd700,#fff3a3,#ffffff);
    border-radius: 30px;
    padding: 25px;
    border: 8px solid #ffcb05;
    box-shadow: 0px 0px 30px rgba(255,203,5,0.7);
    text-align: center;
}

.footer {
    text-align:center;
    color:gray;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">⚡ MBTI 포켓몬 카드 ⚡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">내 MBTI와 가장 닮은 포켓몬은 누구일까? 🎮</div>',
    unsafe_allow_html=True
)

pokemon_data = {
    "INTJ": {
        "name": "뮤츠",
        "emoji": "🧠",
        "image": "https://img.pokemondb.net/artwork/large/mewtwo.jpg",
        "desc": "전략적이고 독립적인 천재형. 항상 몇 수 앞을 내다보는 타입!"
    },
    "INTP": {
        "name": "이브이",
        "emoji": "🦊",
        "image": "https://img.pokemondb.net/artwork/large/eevee.jpg",
        "desc": "호기심이 많고 가능성이 무한한 탐험가."
    },
    "ENTJ": {
        "name": "리자몽",
        "emoji": "🔥",
        "image": "https://img.pokemondb.net/artwork/large/charizard.jpg",
        "desc": "강력한 카리스마와 리더십을 가진 지휘관."
    },
    "ENTP": {
        "name": "팬텀",
        "emoji": "👻",
        "image": "https://img.pokemondb.net/artwork/large/gengar.jpg",
        "desc": "창의력과 장난기가 넘치는 아이디어 뱅크."
    },
    "INFJ": {
        "name": "라프라스",
        "emoji": "🌊",
        "image": "https://img.pokemondb.net/artwork/large/lapras.jpg",
        "desc": "따뜻하고 공감 능력이 뛰어난 힐러."
    },
    "INFP": {
        "name": "뮤",
        "emoji": "✨",
        "image": "https://img.pokemondb.net/artwork/large/mew.jpg",
        "desc": "순수하고 상상력이 풍부한 몽상가."
    },
    "ENFJ": {
        "name": "피카츄",
        "emoji": "⚡",
        "image": "https://img.pokemondb.net/artwork/large/pikachu.jpg",
        "desc": "누구에게나 사랑받는 인기 만점 포켓몬."
    },
    "ENFP": {
        "name": "토게피",
        "emoji": "🌈",
        "image": "https://img.pokemondb.net/artwork/large/togepi.jpg",
        "desc": "행복과 에너지를 전파하는 분위기 메이커."
    },
    "ISTJ": {
        "name": "거북왕",
        "emoji": "🐢",
        "image": "https://img.pokemondb.net/artwork/large/blastoise.jpg",
        "desc": "든든하고 책임감 강한 수호자."
    },
    "ISFJ": {
        "name": "이상해꽃",
        "emoji": "🌿",
        "image": "https://img.pokemondb.net/artwork/large/venusaur.jpg",
        "desc": "친절하고 배려심 많은 친구."
    },
    "ESTJ": {
        "name": "괴력몬",
        "emoji": "💪",
        "image": "https://img.pokemondb.net/artwork/large/machamp.jpg",
        "desc": "실행력과 책임감이 강한 리더."
    },
    "ESFJ": {
        "name": "푸린",
        "emoji": "🎤",
        "image": "https://img.pokemondb.net/artwork/large/jigglypuff.jpg",
        "desc": "사람들과 어울리는 걸 좋아하는 인기쟁이."
    },
    "ISTP": {
        "name": "루카리오",
        "emoji": "🥋",
        "image": "https://img.pokemondb.net/artwork/large/lucario.jpg",
        "desc": "침착하고 강한 해결사."
    },
    "ISFP": {
        "name": "버터플",
        "emoji": "🦋",
        "image": "https://img.pokemondb.net/artwork/large/butterfree.jpg",
        "desc": "감성적이고 자유로운 예술가."
    },
    "ESTP": {
        "name": "라이츄",
        "emoji": "⚡",
        "image": "https://img.pokemondb.net/artwork/large/raichu.jpg",
        "desc": "모험과 도전을 사랑하는 액션파."
    },
    "ESFP": {
        "name": "꼬부기",
        "emoji": "😎",
        "image": "https://img.pokemondb.net/artwork/large/squirtle.jpg",
        "desc": "어디서든 분위기를 띄우는 인싸."
    }
}

mbti = st.selectbox(
    "🎯 MBTI를 선택하세요!",
    list(pokemon_data.keys())
)

if st.button("🎴 내 포켓몬 카드 뽑기!", use_container_width=True):

    st.balloons()

    p = pokemon_data[mbti]

    st.markdown('<div class="pokemon-card">', unsafe_allow_html=True)

    st.image(p["image"], width=300)

    st.markdown(
        f"""
        # {p["emoji"]} {p["name"]}

        ### ✨ {mbti} 타입의 대표 포켓몬

        **{p["desc"]}**

        ---
        🌟 희귀도: ★★★★★

        ⚔️ 특성: 개성 만렙

        🎮 오늘의 한마디:
        > 자신만의 매력을 믿고 모험을 떠나자!
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    '<div class="footer">⚡ Pokémon MBTI Card Generator 🎈</div>',
    unsafe_allow_html=True
)
