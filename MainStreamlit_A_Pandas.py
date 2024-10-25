import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu('Tutorial Desain Streamlit UTS ML 24/25',
                           ['Klasifikasi',
                            'Regresi', 'Catatan'],
                            default_index=0)
    
if selected == 'Klasifikasi':
    st.title('Klasifikasi')

    file = st.file_uploader("Masukkan File", type=["csv", "txt"])
    
    squaremeters = st.number_input("Masukan Squaremeters", 0)
    jmlruangan = st.number_input("Masukan Jumlah Ruangan", 0)

    yard = st.radio("Has Yard", ["Yes", "No"])
    pool = st.radio("Has Pool", ["Yes", "No"])

    lantai = st.number_input("Masukan Jumlah Lantai", 0)
    citycode = st.number_input("Masukan City Code", 0)
    citypartrange = st.number_input("Masukan City Part Range", 0)
    prevowners = st.number_input("Masukan Jumlah Pemilik Sebelumnya", 0)
    made = st.number_input("Masukan Tahun Dibuat", 0)

    isnewbuild = st.radio("Is New Build?", ["New", "Old"])
    stormprotector = st.radio("Has Storm Protector", ["Yes", "No"])

    basement = st.number_input("Basement", 0)
    attic = st.number_input("Attic", 0)
    garage = st.number_input("Garage", 0)

    storageroom = st.radio("Has Storage Room", ["Yes", "No"])

    guestroom = st.number_input("Guestroom", 0)

    jawaban = st.number_input("Masukkan Harga", min_value=0)

    # Tombol untuk prediksi harga
    harga = st.button("Prediksi Category")

    if harga:
        if jawaban > 6000000:
            st.success(f"Termasuk Kategori Luxury")
        elif jawaban < 3000000:
            st.success(f"Termasuk Kategori Middle")
        else:
            st.error(f"Termasuk Kategori Basic")

if selected == 'Regresi':
    st.title('Regresi')

    file = st.file_uploader("Masukkan File", type=["csv", "txt"])
    squaremeters = st.number_input("Masukan Squaremeters", 0)
    jmlruangan = st.number_input("Masukan Jumlah Ruangan", 0)

    yard = st.radio("Has Yard", ["Yes", "No"])
    pool = st.radio("Has Pool", ["Yes", "No"])

    lantai = st.number_input("Masukan Jumlah Lantai", 0)
    citycode = st.number_input("Masukan City Code", 0)
    citypartrange = st.number_input("Masukan City Part Range", 0)
    prevowners = st.number_input("Masukan Jumlah Pemilik Sebelumnya", 0)
    made = st.number_input("Masukan Tahun Dibuat", 0)

    isnewbuild = st.radio("Is New Build?", ["New", "Old"])
    stormprotector = st.radio("Has Storm Protector", ["Yes", "No"])

    basement = st.number_input("Basement", 0)
    attic = st.number_input("Attic", 0)
    garage = st.number_input("Garage", 0)

    storageroom = st.radio("Has Storage Room", ["Yes", "No"])

    guestroom = st.number_input("Guestroom", 0)

    category = st.selectbox("Category", ["Luxury","Middle","Basic"])

    hitung = st.button("Prediksi Harga")

    if hitung:
        if category == "Luxury":
            harga = 6000000 + jmlruangan * 100000
            st.success(f"Harga untuk kategori Luxury adalah: Rp {harga:,}")
        elif category == "Middle":
            harga = 3000000 + jmlruangan * 75000
            st.success(f"Harga untuk kategori Middle adalah: Rp {harga:,}")
        else:
            harga = 1000000 + jmlruangan * 50000
            st.success(f"Harga untuk kategori Basic adalah: Rp {harga:,}")

if selected == 'Catatan':
    st.title('Catatan')
    st.write('''1. Untuk memunculkan sidebar agar tidak error ketike di run, silahkan install library streamlit option menu
             di terminal dengan perintah "pip install streamlit-option-menu".''')
    st.write('2. Menu yang dibuat ada 2 yaitu Klasifikasi dan Regresi.')
    st.write('3. Inputan nya apa aja, seusaikan dengan arsitektur code anda pada notebook.')
    st.write('4. Referensi desain streamlit dapat di akses pada https://streamlit.io/')
    st.write('5. Link streamlit desain ini dapat di akses pada https://apputs-6qzfvr4ufiyzhj84mrfkt7.streamlit.app/')
    st.write('''6. Library pada file requirements yang dibutuhkan untuk deploy online di github ada 5 yaitu streamlit,
             scikit-learn, pandas, numpy, streamlit-option-menu.''')
