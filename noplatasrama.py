import streamlit as st
from data_plat import data_plat

st.set_page_config(page_title="Semakan No Plat Asrama")

st.title("🚗 Sistem Semakan No Plat Asrama Darul Aishah 2026")
st.write("Sila masukkan nombor plat kenderaan waris.")

# Input
no_plat_input = st.text_input("Masukkan No Plat:")

if st.button("Semak"):

    # Buang space dan tukar huruf besar
    no_plat = no_plat_input.replace(" ", "").upper()

    if no_plat in data_plat:
        st.success("✅ No plat dijumpai!")
        st.info(f"Nama Murid: {data_plat[no_plat]}")
    else:
        st.error("❌ No plat tidak wujud.")
        st.warning("No plat ini adalah kenderaan orang luar (bukan murid asrama).")