import streamlit as st

st.set_page_config(page_title="Repositori Kurikulum PSEP", layout="wide")

st.title("📚 Perpustakaan Digital Kurikulum PSEP")
st.write("Pusat Dokumen Revisi Kurikulum 2025 & Policy Brief")
st.divider()

# JALUR PIPA FIX (Menggunakan domain raw asli GitHub)
base_url = "https://raw.githubusercontent.com/ulasanekonomi-collab/dokumen-kurikulum-psep/main/"

# --- SEKSI 1: DRAFT KURIKULUM ---
st.header("📄 1. Draft 7 Kurikulum PSEP")
col1, col2 = st.columns(2)

with col1:
    st.info("Versi Word")
    # Cek: apakah draft7.docx atau draft7.DOCX? Di gambar Akang tertulis kecil.
    st.markdown(f'<a href="{base_url}draft7.docx"><button style="width:100%; border-radius:10px; background-color:#0078d4; color:white; padding:15px; cursor:pointer; font-weight:bold; border:none;">📥 Download .DOCX</button></a>', unsafe_allow_html=True)

with col2:
    st.success("Versi PDF")
    st.markdown(f'<a href="{base_url}draft7.pdf"><button style="width:100%; border-radius:10px; background-color:#d13438; color:white; padding:15px; cursor:pointer; font-weight:bold; border:none;">📂 Buka .PDF</button></a>', unsafe_allow_html=True)

st.divider()

# --- SEKSI 2: POLICY BRIEF ---
st.header("📑 2. Policy Brief")
col3, col4 = st.columns(2)

with col3:
    st.info("Policy Brief (Word)")
    st.markdown(f'<a href="{base_url}policy_brief.docx"><button style="width:100%; border-radius:10px; background-color:#0078d4; color:white; padding:15px; cursor:pointer; font-weight:bold; border:none;">📥 Download .DOCX</button></a>', unsafe_allow_html=True)

with col4:
    st.success("Policy Brief (PDF)")
    st.markdown(f'<a href="{base_url}policy_brief.pdf"><button style="width:100%; border-radius:10px; background-color:#d13438; color:white; padding:15px; cursor:pointer; font-weight:bold; border:none;">📂 Buka .PDF</button></a>', unsafe_allow_html=True)

st.divider()

# --- SEKSI 3: DASHBOARD EXCEL ---
st.header("📊 3. Dashboard & Instrumen")
st.warning("Dashboard Excel (Full Version)")
# PERHATIKAN: Di gambar Akang tertulis .XLSX (HURUF BESAR)
st.markdown(f'<a href="{base_url}dashboard.XLSX"><button style="width:100%; border-radius:10px; background-color:#107c10; color:white; padding:20px; cursor:pointer; font-weight:bold; border:none;">🟢 DOWNLOAD DASHBOARD EXCEL</button></a>', unsafe_allow_html=True)

st.divider()
st.caption("PSEP Unisba - Sistem Dokumentasi Kurikulum")
