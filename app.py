import streamlit as st

st.set_page_config(page_title="Repositori Kurikulum PSEP", layout="wide")

st.title("📚 Perpustakaan Digital Kurikulum PSEP")
st.write("Pusat Dokumen Revisi Kurikulum 2025 & Policy Brief")
st.divider()

# Fungsi untuk membuat link download yang aman dari spasi dan karakter khusus
def make_github_url(file_name):
    base_url = "https://github.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/raw/main/"
    # Mengganti spasi dengan %20 agar link tidak terputus
    return base_url + file_name.replace(" ", "%20")

# --- BAGIAN 1: DRAFT KURIKULUM ---
st.header("📄 1. Draft 7 Kurikulum PSEP")
col1, col2 = st.columns(2)

with col1:
    st.info("Versi Dokumen (Word)")
    name_docx = "Draft 7 Revisi Kurikulum EP_2025_YS.docx"
    st.markdown(f'<a href="{make_github_url(name_docx)}"><button style="width:100%; border-radius:10px; background-color:#0078d4; color:white; padding:10px; cursor:pointer; font-weight:bold;">📥 Download .DOCX</button></a>', unsafe_allow_html=True)

with col2:
    st.success("Versi Cetak (PDF)")
    name_pdf = "Draft 7 Revisi Kurikulum EP_2025_YS.pdf"
    st.markdown(f'<a href="{make_github_url(name_pdf)}"><button style="width:100%; border-radius:10px; background-color:#d13438; color:white; padding:10px; cursor:pointer; font-weight:bold;">📂 Buka .PDF</button></a>', unsafe_allow_html=True)

st.divider()

# --- BAGIAN 2: POLICY BRIEF ---
st.header("📑 2. Policy Brief")
col3, col4 = st.columns(2)

with col3:
    st.info("Policy Brief (Word)")
    # SESUAI GAMBAR: Policy Brief_PSEP_2025_YS.docx
    pb_docx = "Policy Brief_PSEP_2025_YS.docx"
    st.markdown(f'<a href="{make_github_url(pb_docx)}"><button style="width:100%; border-radius:10px; background-color:#0078d4; color:white; padding:10px; cursor:pointer; font-weight:bold;">📥 Download .DOCX</button></a>', unsafe_allow_html=True)

with col4:
    st.success("Policy Brief (PDF)")
    # SESUAI GAMBAR: Policy Brief_PSEP_2025_YS.pdf
    pb_pdf = "Policy Brief_PSEP_2025_YS.pdf"
    st.markdown(f'<a href="{make_github_url(pb_pdf)}"><button style="width:100%; border-radius:10px; background-color:#d13438; color:white; padding:10px; cursor:pointer; font-weight:bold;">📂 Buka .PDF</button></a>', unsafe_allow_html=True)

st.divider()

# --- BAGIAN 3: DASHBOARD EXCEL ---
st.header("📊 3. Dashboard & Instrumen")
st.warning("Dashboard Excel (Full Version)")
# SESUAI GAMBAR: Dashboard Kurikulum PSEP_2025_YS.xlsx
excel_name = "Dashboard Kurikulum PSEP_2025_YS.xlsx"
st.markdown(f'<a href="{make_github_url(excel_name)}"><button style="width:100%; border-radius:10px; background-color:#107c10; color:white; padding:15px; font-weight:bold; cursor:pointer;">🟢 DOWNLOAD DASHBOARD EXCEL</button></a>', unsafe_allow_html=True)

st.divider()
st.caption("PSEP Unisba - Dokumen Digital Kurikulum")
