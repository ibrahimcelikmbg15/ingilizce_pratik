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
    },
    "5": {
        "youtube": [
            "https://www.youtube.com/watch?v=euUTFiZt4Zc",
            "https://www.youtube.com/watch?v=41cJ0mqWses",
            "https://www.youtube.com/watch?v=cMHUai_TkfE",
            "https://www.youtube.com/watch?v=krpkQhdkyKw",
            "https://www.youtube.com/watch?v=EzQ6Ag16rJk",
            "https://www.youtube.com/watch?v=Ke7j1jFLxbc"
        ],
        "wordwall": [
            "https://wordwall.net/resource/60655731?wwmethod=link",
            "https://wordwall.net/resource/975047?wwmethod=link",
            "https://wordwall.net/resource/53917804?wwmethod=link",
            "https://wordwall.net/resource/36645939?wwmethod=link",
            "https://wordwall.net/resource/120171163?wwmethod=link",
            "https://wordwall.net/resource/97905340?wwmethod=link",
            "https://wordwall.net/resource/91126186?wwmethod=link"
        ]
    }
}

# Sayfa Ayarları
st.set_page_config(page_title="İngilizce Ödev Linkleri", page_icon="📚", layout="wide")

# Havalı Başlık ve Açıklama
st.markdown("<h1 style='text-align: center; color: #4B0082;'>🌟 İngilizce Eğlence ve Çalışma Merkezi 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #333333;'>Bu program, Bahçeşehir 4. Sınıf İngilizce dersinde ödev olarak verilen oyun ve videoların linklerini derlemektedir.<br>Amacı, bu oyun ve videolara telefonunuzdan kolayca erişip yolculukta ya da bilgisayar olmadığı zamanlarda çocuklara pratik ve tekrar yaptırmaktır. Yeni konular geldikçe (en az iki haftada bir) listemiz güncellenecektir!</h4>", unsafe_allow_html=True)
st.markdown("---")

# Hafta Seçimi (5. hafta eklendi)
secim = st.selectbox("Lütfen çalışmak istediğiniz haftayı seçin:", ["1", "2", "3", "4", "5"])
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
st.markdown("<h3 style='text-align: right; font-style: italic; color: #2E86C1; text-shadow: 1px 1px 2px #aaa;'>Sistem Mimarı: Doç. Dr. İbrahim ÇELİK</h3>", unsafe_allow_html=True)
