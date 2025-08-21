import streamlit as st

st.title("이상형 월드컵")

# 버튼 클릭 여부에 따라 실행
if st.button("클릭하세요"):
    st.write("버튼이 클릭되었습니다!")

# 두 개의 이미지를 가로로 나란히 배치
col1, col2 = st.columns(2)

with col1:
    st.image("dksdbwls.jpg", width=300)

with col2:
    st.image("pic2.png", width=300)
