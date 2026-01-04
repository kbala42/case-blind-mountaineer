import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.title("🧗‍♂️ Vaka 3: Karanlık Vadi (Optimizasyon)")

    # --- BAĞLANTI KONTROLÜ ---
    if 'inventory_coordinates' not in st.session_state:
        st.error("⛔ ERİŞİM ENGELLENDİ: Önce Vaka 2'deki sinyali çözüp 'Hedef Koordinatı' bulmalısın.")
        return

    target_pos = st.session_state['inventory_coordinates']
    st.success(f"✅ Hedef Kilitlendi: Vadi Tabanı {target_pos}")

    # --- HİKAYE MODU ---
    if 'math_mode_3' not in st.session_state:
        st.session_state['math_mode_3'] = False

    if not st.session_state['math_mode_3']:
        st.markdown("""
        **Görev:** Watson AI, Vaka 2'den gelen koordinata (0 noktasına) inmeli. 
        Ama etraf sisli. Adım büyüklüğünü (Learning Rate) sen ayarla.
        """)
    else:
        st.markdown("""
        ### 📐 MATEMATİKSEL YÜZLEŞME
        **Konu:** Gradient Descent (Bayır İnişi)
        $$ \\theta_{new} = \\theta_{old} - \\alpha \\cdot \\nabla J(\\theta) $$
        """)

    # --- SİMÜLASYON ---
    lr = st.slider("Öğrenme Hızı (Alpha)", 0.01, 1.1, 0.1)
    
    x = np.linspace(-10, 10, 100)
    y = x**2
    
    current_pos = 8.0 
    path = [current_pos]
    
    for _ in range(10): 
        gradient = 2 * current_pos
        current_pos = current_pos - (lr * gradient)
        path.append(current_pos)
        
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Hata Dağı (Loss Function)")
    ax.plot(path, [p**2 for p in path], 'ro-', label="Dağcının Yolu")
    ax.legend()
    st.pyplot(fig)
    
    final_error = path[-1]**2
    if final_error < 0.1:
        st.success("MÜKEMMEL İNİŞ! Model eğitildi.")
    elif final_error > 50:
        st.error("FELAKET! Adım çok büyüktü, dağcı uzaya fırladı.")
    else:
        st.warning("Yavaş iniyor... Biraz daha hızlanabilirsin.")

    st.divider()
    
    if st.button("🔴 Kırmızı Hap: Analojiyi Kır"):
        st.session_state['math_mode_3'] = not st.session_state['math_mode_3']
        st.rerun() # GÜNCELLENDİ

    with st.expander("🛠️ Kod Müdahalesi (Reality Check)"):
        st.write("**Soru:** Formüldeki Eksi ($-$) işaretini Artı ($+$) yaparsan ne olur?")
        ans = st.radio("Cevap:", ["Daha hızlı iner", "Tepeye tırmanır (Hata artar)", "Değişmez"])
        if ans == "Tepeye tırmanır (Hata artar)":
            st.success("Doğru!")
        elif ans:
            st.error("Yanlış. Eğim yukarıyı gösterir. Tersine gitmelisin.")

if __name__ == "__main__":
    run()