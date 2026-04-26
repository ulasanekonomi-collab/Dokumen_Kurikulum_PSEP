import streamlit as st

st.set_page_config(page_title="Repositori Dokumen Kurikulum PSEP", layout="wide")

st.title("📚 Perpustakaan Digital Kurikulum PSEP")
st.write("Selamat datang di pusat dokumen revisi kurikulum 2025.")

# Menu navigasi dokumen
tab1, tab2, tab3 = st.tabs(["📄 Draft Kurikulum", "📑 Policy Brief", "📊 Lampiran"])

with tab1:
    st.subheader("Draft 7 Kurikulum PSEP 2025")
    # Link asli ke file PDF Akang
    st.markdown("[👉 Klik di sini untuk membaca Draft Kurikulum](https://github.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/raw/main/Draft_7_Kurikulum_PSEP_2025.pdf)")
    st.info("Catatan: Dokumen ini telah melalui uji Stress Test dan Vertical Alignment Analysis.")

with tab2:
    st.subheader("Policy Brief Transformasi Digital")
    st.write("Dokumen Policy Brief sedang disiapkan.")

with tab3:
    st.subheader("Lampiran & Data Pendukung")
