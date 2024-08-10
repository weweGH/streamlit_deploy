import streamlit as st 
import time

st.title("st.empty 예시")
# 빈 컨테이너를 생성합니다.
container = st.empty()

# 컨테이너에 텍스트를 출력합니다. 
container.text("Hello, Streamlit!")

# 3초 후에 컨테이너의 내용을 변경합니다. 
time.sleep(3)
container.text("Streamlit is awesome🔥") 

# 3초 후에 컨테이너의 내용을 clear합니다.
time.sleep(3) 
container.empty()
