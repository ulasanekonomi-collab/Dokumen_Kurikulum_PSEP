import streamlit as st

st.set_page_config(page_title="Perpustakaan Kurikulum PSEP", layout="wide")

st.title("📚 Perpustakaan Digital Kurikulum PSEP")
st.write("Pusat Dokumen Revisi Kurikulum 2025")
st.divider()

# JALUR UTAMA: Pastikan Nama Repo "Dokumen_Kurikulum_PSEP" (Garis Bawah)
base_url = "https://raw.githubusercontent.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/main/"

def buat_tombol(file_name, label, warna):
    # Link langsung menggunakan ?raw=true agar memaksa download
    link = f"https://github.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/blob/main/{file_name}?raw=true"
    st.markdown(f"""
        <a href="{link}">
            <button style="
                width: 100%;
                background-color: {warna};
                color: white;
                padding: 12px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-weight: bold;
                margin-bottom: 10px;
            ">
                {label}
            </button>
        </a>
    """, unsafe_allow_html=True)

# --- SEKSI 1: DRAFT KURIKULUM ---
st.subheader("📄 1. Draft 7 Kurikulum PSEP")
col1, col2 = st.columns(2)
with col1:
    # Coba pastikan di GitHub namanya draft7.docx (huruf kecil semua)
    buat_tombol("draft7.docx", "📥 Download Word (.docx)", "#0078d4")
with col2:
    buat_tombol("draft7.pdf", "📂 Buka PDF (.pdf)", "#d13438")

st.divider()

# --- SEKSI 2: POLICY BRIEF ---
st.subheader("📑 2. Policy Brief")
col3, col4 = st.columns(2)
with col3:
    # Coba pastikan di GitHub namanya policy_brief.docx
    buat_tombol("policy_brief.docx", "📥 Download Word (.docx)", "#0078d4")
with col4:
    buat_tombol("policy_brief.pdf", "📂 Buka PDF (.pdf)", "#d13438")

st.divider()

# --- SEKSI 3: DASHBOARD ---
st.subheader("📊 3. Dashboard Excel")
# Sesuaikan jika di GitHub namanya dashboard.xlsx atau dashboard.XLSX
buat_tombol("dashboard.xlsx", "🟢 DOWNLOAD DASHBOARD EXCEL", "#107c10")

st.divider()
st.caption("PSEP Unisba - Dokumen Digital")
