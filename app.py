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
st.set_page_config(page_title="Bahçeşehir 4. Sınıf İngilizce", page_icon="📚", layout="wide")

# Havalı Başlık
st.markdown("<h1 style='text-align: center; color: #1E3A8A; text-shadow: 2px 2px 4px #aaa;'>🌟 Bahçeşehir 4. Sınıf İngilizce Eğlence Merkezi 🌟</h1>", unsafe_allow_html=True)

# Açıklayıcı ve Şık Bilgi Kutusu
st.markdown("""
<div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 20px; border-left: 5px solid #1E3A8A;'>
    <p style='font-size: 18px; color: #333;'>
        Bu program, <b>Bahçeşehir 4. Sınıf İngilizce</b> derslerinde ödev olarak verilen eğitici oyunları ve videoları tek bir çatı altında derlemiştir.
    </p>
    <p style='font-size: 16px; color: #555;'>
        Amacı; yolculukta, arabada ya da bilgisayarın olmadığı zamanlarda çocukların telefonunuzdan bu etkinliklere kolayca erişmesini sağlayarak, onlara her an pratik ve tekrar yapma imkanı sunmaktır.
    </p>
    <p style='font-size: 16px; color: #d32f2f; font-weight: bold;'>
        🚀 Yeni konular işlendikçe, en az iki haftada bir listeye yepyeni haftalar eklenecektir. Takipte kalın!
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Hafta Seçimi
secim = st.selectbox("🎯 Lütfen çalışmak istediğiniz haftayı seçin:", ["1", "2", "3", "4"])
st.markdown("---")

# Videolar ve Oyunları 2 Sütuna Ayırma (Düğme görünümlü linklerle)
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📺 {secim}. Hafta Videoları")
    for i, link in enumerate(haftalik_linkler[secim]["youtube"], 1):
        st.markdown(f"**{i}.** <a href='{link}' target='_blank' style='text-decoration: none; color: white; background-color: #E53935; padding: 5px 10px; border-radius: 5px;'>▶️ Videoyu İzle</a>", unsafe_allow_html=True)
        st.write("") # Görsellik için boşluk

with col2:
    st.subheader(f"🎮 {secim}. Hafta Oyunları (Wordwall)")
    for i, link in enumerate(haftalik_linkler[secim]["wordwall"], 1):
        st.markdown(f"**{i}.** <a href='{link}' target='_blank' style='text-decoration: none; color: white; background-color: #1E88E5; padding: 5px 10px; border-radius: 5px;'>🎲 Oyunu Oyna</a>", unsafe_allow_html=True)
        st.write("") # Görsellik için boşluk

# Büyük ve Gösterişli Sistem Mimarı İmzası
st.markdown("""
<div style='text-align: center; margin-top: 50px; padding: 20px; border-top: 2px dashed #bbb;'>
    <h3 style='color: #7f8c8d; font-family: "Arial", sans-serif; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 5px;'>Sistem Mimarı</h3>
    <h1 style='color: #2c3e50; font-size: 40px; text-shadow: 2px 2px 4px rgba(0,0,0,0.2); margin: 0; font-weight: 900;'>Doç. Dr. İbrahim ÇELİK</h1>
</div>
""", unsafe_allow_html=True)
