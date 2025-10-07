import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

st.title("전쟁기념관 데이트 프로그램")
st.header("_전쟁기념관 지도_")

col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
  st.subheader("전쟁관 2층", divider='gray')
  img = Image.open('data/map1.png')
  st.image(img, width=600)

with col2:
  st.subheader("전쟁관 3층", divider='gray')
  img = Image.open('data/map2.png')
  st.image(img, width=600)

st.caption("출처: https://www.warmemo.or.kr:8443/Home/H10000/H10400/H10402/html")