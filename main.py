import streamlit as st
st.title("나의 첫 app")
st.write("hello")
if name:
  if name=="조서연":
    st.success("반갑습니다. 조서연님!")
  else:
    st.warning("누구세요?")
