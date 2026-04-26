import streamlit as st

st.set_page_config(page_title="Repositori Kurikulum PSEP", layout="wide")

st.title("📚 Perpustakaan Digital Kurikulum PSEP")
st.write("Pusat Dokumen Revisi Kurikulum 2025 & Policy Brief")
st.divider()

# FUNGSI LINK LANGSUNG (Sudah diperbaiki ke nama repo yang benar)
def get_link(file_name):
    # Nama repo Akang ternyata pakai tanda hubung: dokumen-kurikulum-psep
    base = "https://raw.githubusercontent.com/ulasanekonomi-collab/dokumen-kurikulum-psep/main/"
    return base + file_name.replace(" ", "%20")

# --- KELOMPOK 1: DRAFT KURIKULUM ---
st.header("📄 1. Draft 7 Kurikulum PSEP")
c1, c2 = st.columns(2)
with c1:
    f1 = "Draft 7 Revisi Kurikulum EP_2025_YS.docx"
    st.markdown(f'<a href="{get_link(f1)}"><button style="width:100%; border-radius:10px; background-color:#0078d4; color:white; padding:15px; cursor:pointer; font-weight:bold;">📥 Download Word (.docx)</button></a>', unsafe_allow_html=True)
with c2:
    f2 = "Draft 7 Revisi Kurikulum EP_2025_YS.pdf"
    st.markdown(f'<a href="{get_link(f2)}"><button style="width:100%; border-radius:10px; background-color:#d13438; color:white; padding:15px; cursor:pointer; font-weight:bold;">📂 Buka PDF (.pdf)</button></a>', unsafe_allow_html=True)

st.divider()

# --- KELOMPOK 2: POLICY BRIEF ---
st.header("📑 2. Policy Brief")
c3, c4 = st.columns(2)
with c3:
    f3 = "Policy Brief_PSEP_2025_YS.docx"
    st.markdown(f'<a href="{get_link(f3)}"><button style="width:100%; border-radius:10px; background-color:#0078d4; color:white; padding:15px; cursor:pointer; font-weight:bold;">📥 Download Word (.docx)</button></a>', unsafe_allow_html=True)
with c4:
    f4 = "Policy Brief_PSEP_2025_YS.pdf"
    st.markdown(f'<a href="{get_link(f4)}"><button style="width:100%; border-radius:10px; background-color:#d13438; color:white; padding:15px; cursor:pointer; font-weight:bold;">📂 Buka PDF (.pdf)</button></a>', unsafe_allow_html=True)

st.divider()

# --- KELOMPOK 3: DASHBOARD ---
st.header("📊 3. Dashboard Excel")
f5 = "Dashboard Kurikulum PSEP_2025_YS.xlsx"
st.markdown(f'<a href="{get_link(f5)}"><button style="width:100%; border-radius:10px; background-color:#107c10; color:white; padding:20px; cursor:pointer; font-weight:bold;">🟢 DOWNLOAD DASHBOARD EXCEL</button></a>', unsafe_allow_html=True)

st.divider()
st.caption("PSEP Unisba - Dokumen Digital")
