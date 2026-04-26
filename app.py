import streamlit as st

st.set_page_config(page_title="Repositori Kurikulum PSEP", layout="wide")

st.title("📚 Perpustakaan Digital Kurikulum PSEP")
st.write("Pusat Dokumen Revisi Kurikulum 2025 & Policy Brief")
st.divider()

# --- BAGIAN 1: DRAFT KURIKULUM ---
st.header("📄 1. Draft 7 Kurikulum PSEP")
col1, col2 = st.columns(2)

with col1:
    st.info("Versi Dokumen (Word)")
    # Pastikan nama file di GitHub sesuai: Draft 7 Revisi Kurikulum EP_2025_YS.docx
    url_doc = "https://github.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/raw/main/Draft%207%20Revisi%20Kurikulum%20EP_2025_YS.docx"
    st.markdown(f'<a href="{url_doc}"><button style="width:100%; border-radius:10px; background-color:#0078d4; color:white; padding:10px;">📥 Download .DOCX</button></a>', unsafe_allow_html=True)

with col2:
    st.success("Versi Cetak (PDF)")
    # Ganti 'nama_file_akang.pdf' dengan nama file PDF asli di GitHub nanti
    url_pdf = "https://github.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/raw/main/Draft_7_Kurikulum_PSEP_2025.pdf"
    st.markdown(f'<a href="{url_pdf}"><button style="width:100%; border-radius:10px; background-color:#d13438; color:white; padding:10px;">📂 Buka .PDF</button></a>', unsafe_allow_html=True)

st.divider()

# --- BAGIAN 2: POLICY BRIEF ---
st.header("📑 2. Policy Brief")
col3, col4 = st.columns(2)

with col3:
    st.info("Policy Brief (Word)")
    url_pb_doc = "https://github.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/raw/main/Policy_Brief_PSEP.docx"
    st.markdown(f'<a href="{url_pb_doc}"><button style="width:100%; border-radius:10px; background-color:#0078d4; color:white; padding:10px;">📥 Download .DOCX</button></a>', unsafe_allow_html=True)

with col4:
    st.success("Policy Brief (PDF)")
    url_pb_pdf = "https://github.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/raw/main/Policy_Brief_PSEP.pdf"
    st.markdown(f'<a href="{url_pb_pdf}"><button style="width:100%; border-radius:10px; background-color:#d13438; color:white; padding:10px;">📂 Buka .PDF</button></a>', unsafe_allow_html=True)

st.divider()

# --- BAGIAN 3: DASHBOARD EXCEL ---
st.header("📊 3. Dashboard & Instrumen")
st.warning("Dashboard Excel (Full Version)")
url_excel = "https://github.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/raw/main/Dashboard_Kurikulum_PSEP.xlsx"
st.markdown(f'<a href="{url_excel}"><button style="width:100%; border-radius:10px; background-color:#107c10; color:white; padding:15px; font-weight:bold;">🟢 DOWNLOAD DASHBOARD EXCEL</button></a>', unsafe_allow_html=True)

st.divider()
st.caption("PSEP Unisba - Dokumen ini dilindungi dan diperuntukkan bagi kalangan internal.")
