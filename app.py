import streamlit as st

st.set_page_config(page_title="Perpustakaan Kurikulum PSEP", layout="centered")

st.title("📚 Perpustakaan Digital Kurikulum PSEP")
st.write("Pusat Dokumen Revisi Kurikulum 2025")

st.divider()

st.subheader("📄 Draft 7 Revisi Kurikulum EP 2025")
st.info("Catatan: Dokumen ini dalam format Word (.docx). Silakan klik tombol di bawah untuk mengunduh.")

# LINK INI SUDAH DISESUAIKAN DENGAN NAMA FILE ASLI DI GITHUB AKANG
# Nama file: Draft%207%20Revisi%20Kurikulum%20EP_2025_YS.docx
word_url = "https://github.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/raw/main/Draft%207%20Revisi%20Kurikulum%20EP_2025_YS.docx"

st.markdown(f"""
    <a href="{word_url}">
        <button style="
            width: 100%;
            background-color: #0078d4;
            color: white;
            padding: 15px;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
        ">
            📥 DOWNLOAD DRAFT 7 (WORD)
        </button>
    </a>
    """, unsafe_allow_html=True)

st.divider()
st.caption("PSEP Unisba - Sistem Integrasi Kurikulum")
