import streamlit as st

st.set_page_config(layout="wide")

st.title("전쟁기념관 데이트 프로그램")

st.header("_About_")

col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
  st.subheader("바로 시작하기", divider='gray')
  st.write("1. :orange[연인]과 함께 전쟁기념관을 방문해요.")
  st.page_link("pages/1_전쟁기념관 지도.py", label="전쟁기념관 지도 보기", icon="🗺️")
  st.write("2. 여기에 나와있는 순서대로 전쟁기념관을 구경해보면서 :blue[퀴즈]를 풀어보세요.")
  st.page_link("pages/2_퀴즈 풀기.py", label="퀴즈 풀기", icon="🤔")
  st.write("3. 전시관이 끝날 때, 자신의 감정을 :green[일기]로 기록해보세요.")
  st.page_link("pages/3_일기 기록하기.py", label="일기 기록하기", icon="📒")

with col2:
  st.subheader("ADDIE 모형 기반 프로그램", divider='gray')
  st.write("""
          본 프로그램은 ADDIE 모형을 기반으로 설계된 6/25 전쟁 테마 데이트 프로그램입니다. 전쟁기념관 내 '6/25 전쟁실 Ⅰ/Ⅱ/Ⅲ'을 프로그램 대상으로 선정하였습니다.
          """)
  st.page_link("https://www.warmemo.or.kr:8443/", label="전쟁기념관 사이트", icon="🌐")
  st.write("""
          이 프로그램을 통해서 사용자는 6/25 전쟁의 숨겨진 역사와 의의를 구체적으로 살펴볼 수 있어요. 또, 관람 중 자신이 느꼈던 감정들도 하나의 일기처럼 기록할 수 있어요.\n
          저희와 함께 의미있고 행복한 데이트 보내시길 바라겠습니다.
          """)