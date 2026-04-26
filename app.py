import streamlit as st

st.set_page_config(page_title="Perpustakaan Kurikulum PSEP", layout="wide")

st.title("📚 Perpustakaan Digital Kurikulum PSEP")
st.write("Pusat Dokumen Resmi Revisi Kurikulum 2025")
st.divider()

# JALUR UTAMA: Raw Github (Sudah disesuaikan dengan nama repo Dokumen_Kurikulum_PSEP)
raw_base = "https://raw.githubusercontent.com/ulasanekonomi-collab/Dokumen_Kurikulum_PSEP/main/"

def buat_tombol(file_name, label, warna):
    link = f"{raw_base}{file_name}"
    st.markdown(f"""
        <a href="{link}" target="_blank">
            <button style="
                width: 100%;
                background-color: {warna};
                color: white;
                padding: 18px;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                font-weight: bold;
                font-size: 16px;
                margin-bottom: 15px;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            ">
                {label}
            </button>
        </a>
    """, unsafe_allow_html=True)

# --- BAGIAN 1: DOKUMEN KURIKULUM ---
st.subheader("📄 Dokumen Utama & Kebijakan")
col1, col2 = st.columns(2)

with col1:
    # Dokumen Draft 7 PDF
    buat_tombol("draft7.pdf", "📂 Buka Draft 7 Kurikulum (PDF)", "#d13438")

with col2:
    # Policy Brief PDF
    buat_tombol("policy_brief.pdf", "📑 Buka Policy Brief (PDF)", "#4b4b4b")

st.divider()

# --- BAGIAN 2: DASHBOARD DATA ---
st.subheader("📊 Instrumen & Simulasi")
# Dashboard Excel (Pastikan di GitHub namanya dashboard.xlsx atau dashboard.XLSX)
# Jika di GitHub XLSX (besar), ganti di bawah jadi dashboard.XLSX
buat_tombol("dashboard.xlsx", "🟢 DOWNLOAD DASHBOARD KURIKULUM (EXCEL)", "#107c10")

st.divider()
st.info("💡 **Tips:** Gunakan PDF untuk penelaahan narasi dan Excel untuk verifikasi data capaian pembelajaran (CPL).")
st.caption("PSEP Unisba | Sistem Dokumentasi Terintegrasi 2026")
