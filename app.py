import streamlit as st

st.set_page_config(page_title="Repositori Dokumen Kurikulum PSEP", layout="wide")

st.title("📚 Perpustakaan Digital Kurikulum PSEP")
st.write("Selamat datang di pusat dokumen revisi kurikulum 2025.")

# Menu navigasi dokumen
tab1, tab2, tab3 = st.tabs(["📄 Draft Kurikulum", "📑 Policy Brief", "📊 Lampiran"])

with tab1:
    st.subheader("Draft 7 Kurikulum PSEP 2025")
    # LINK INI SUDAH DIPERBAIKI SESUAI REPO AKANG
    st.markdown("""
    <a href="https://raw.githubusercontent.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/main/Draft_7_Kurikulum_PSEP_2025.pdf" target="_blank">
        <button style="color: white; background-color: #1a4d2e; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">
            📂 Klik di sini untuk Membuka/Download Draft Kurikulum
        </button>
    </a>
    """, unsafe_allow_html=True)
    st.info("Catatan: Gunakan dokumen ini sebagai referensi utama hasil Stress Test.")

with tab2:
    st.subheader("Policy Brief Transformasi Digital")
    st.write("Sedang dalam proses penyusunan.")

with tab3:
    st.subheader("Lampiran & Data Pendukung")
    st.write("- Data Tracer Study")
    st.write("- Hasil FGD Stakeholder")
