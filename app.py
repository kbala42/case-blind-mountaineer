import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.title("🧗‍♂️ Vaka 3: Karanlık Vadi")

    if 'inventory_coordinates' not in st.session_state:
        st.error("⛔ Önce Vaka 2'yi tamamla."); return

    if 'math_mode_3' not in st.session_state: st.session_state['math_mode_3'] = False
    st.markdown("**Görev:** Yapay Zekayı hatasız bir şekilde vadi tabanına indir." if not st.session_state['math_mode_3'] else "### 📐 Gradient Descent")

    lr = st.slider("Öğrenme Hızı (Alpha)", 0.01, 1.1, 0.1)
    
    x = np.linspace(-10, 10, 100); y = x**2
    pos = 8.0; path = [pos]
    
    for _ in range(10): 
        pos = pos - (lr * 2 * pos)
        path.append(pos)
        
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Hata Fonksiyonu"); ax.plot(path, [p**2 for p in path], 'ro-', label="Rota")
    ax.legend(); st.pyplot(fig)
    
    final_error = path[-1]**2
    
    st.subheader("📰 Ertesi Gün Gazeteleri")
    if final_error < 0.1:
        st.success("MANŞET: 'Watson AI Nokta Atışı Yaptı!'")
    elif final_error > 50:
        st.error("MANŞET: 'SKANDAL! Aceleci Yapay Zeka Masum Derneği Terörist İlan Etti!'")
        st.write("**Mennan Usta:** Hızlı koşayım derken bostanı ezdin. Hızdan önce **doğruluk** gelir.")
    else:
        st.warning("MANŞET: 'Çalışmalar Sürüyor...' (Yetersiz İniş)")

    st.divider()
    if st.button("🔴 Kırmızı Hap"):
        st.session_state['math_mode_3'] = not st.session_state['math_mode_3']
        if hasattr(st, "rerun"): st.rerun() 
        else: st.experimental_rerun()

if __name__ == "__main__":
    run()