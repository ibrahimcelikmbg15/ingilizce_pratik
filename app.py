import streamlit as st

haftalik_linkler = {
    "1": {
        "youtube": [
            "https://www.youtube.com/watch?v=99muGoXuYHI&list=RD99muGoXuYHI&start_radio=1",
            "https://www.youtube.com/watch?v=jveL3H4lrbU",
            "https://www.youtube.com/watch?v=AnwrkiSfsqU"
        ],
        "wordwall": [
            "https://wordwall.net/resource/53926394?wwmethod=link",
            "https://wordwall.net/resource/610804?wwmethod=link",
            "https://wordwall.net/resource/90748066?wwmethod=link"
        ]
    },
    "2": {
        "youtube": [
            "https://www.youtube.com/watch?v=TyOSlpt7jUQ"
        ],
        "wordwall": [
            "https://wordwall.net/resource/95409474?wwmethod=link",
            "https://wordwall.net/resource/753754?wwmethod=link"
        ]
    },
    "3": {
        "youtube": [
            "https://www.youtube.com/watch?v=lw6nJHmYcaI&t=105s",
            "https://www.youtube.com/watch?v=uu3LIgYY_lI",
            "https://www.youtube.com/watch?v=rVAV8hekpCs",
            "https://www.youtube.com/watch?v=2fFc_hdmy0o",
            "https://www.youtube.com/watch?v=eV36_j6UEUA"
        ],
        "wordwall": [
            "https://wordwall.net/resource/53660123?wwmethod=link",
            "https://wordwall.net/resource/8931053?wwmethod=link",
            "https://wordwall.net/resource/37190044/plurals?searchQuery=plurals"
        ]
    },
    "4": {
        "youtube": [
            "https://www.youtube.com/watch?v=rVAV8hekpCs",
            "https://www.youtube.com/watch?v=0b4rsDuzThE"
        ],
        "wordwall": [
            "https://wordwall.net/resource/62954332?wwmethod=link",
            "https://wordwall.net/resource/61665886?wwmethod=link",
            "https://wordwall.net/resource/10551041?wwmethod=link"
        ]
    }
}

# Sayfa Ayarları
st.set_page_config(page_title="İngilizce Ödev Linkleri", page_icon="📚", layout="wide")

# Havalı Başlık ve Açıklama
st.markdown("<h1 style='text-align: center; color: #4B0082;'>🌟 İngilizce Eğlence ve Çalışma Merkezi 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #333333;'>Hoş geldiniz! Burası, 4. Sınıf İngilizce yolculuğumuzun haftalık durağı. İstediğiniz haftayı seçin ve pratik yapmaya hemen başlayın!</h4>", unsafe_allow_html=True)
st.markdown("---")

# Hafta Seçimi
secim = st.selectbox("Lütfen çalışmak istediğiniz haftayı seçin:", ["1", "2", "3", "4"])
st.markdown("---")

# Videolar ve Oyunları 2 Sütuna Ayırma
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📺 {secim}. Hafta Videoları")
    for i, link in enumerate(haftalik_linkler[secim]["youtube"], 1):
        # Buton gibi görünen tıklanabilir linkler
        st.markdown(f"**{i}.** [▶️ Videoyu İzle]({link})")

with col2:
    st.subheader(f"🎮 {secim}. Hafta Oyunları (Wordwall)")
    for i, link in enumerate(haftalik_linkler[secim]["wordwall"], 1):
        # Buton gibi görünen tıklanabilir linkler
        st.markdown(f"**{i}.** [🎲 Oyunu Oyna]({link})")

st.markdown("---")

# Sistem Mimarı İmzası
st.markdown("<p style='text-align: right; font-style: italic; color: gray; font-size: 14px;'>Sistem Mimarı: Doç. Dr. İbrahim ÇELİK</p>", unsafe_allow_html=True)