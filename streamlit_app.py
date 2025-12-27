import streamlit as st
import streamlit.components.v1 as components

# Saytni keng formatda sozlash
st.set_page_config(layout="wide", page_title="Al-Jabr Platform")

# Streamlit Secrets'dan maxfiy API kalitini o'qish
# Bu xavfsizlik uchun kerak
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    api_key = "KALIT_TOPILMADI" # Agar xatolik bo'lsa

# index.html faylini o'qish
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    # HTML ichidagi 'PLACEHOLDER_KEY'ni haqiqiy maxfiy kalit bilan almashtirish
    final_code = html_code.replace("PLACEHOLDER_KEY", api_key)

    # Saytni Streamlit oynasida ko'rsatish
    # height=900 bo'yi, scrolling=True esa aylantirish imkonini beradi
    components.html(final_code, height=900, scrolling=True)

except FileNotFoundError:
    st.error("Xatolik: 'index.html' fayli topilmadi. Iltimos, GitHub'ga yuklaganingizni tekshiring.")
