import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

quiz_answer = [2, 1, 3, 3, 4, 1, 3, 3, 3]

for i in range(1, 4):
  key = f"show_content_{i}"
  if key not in st.session_state:
    st.session_state[key] = False

st.title("전쟁기념관 데이트 프로그램")
st.header("_:blue[퀴즈] 풀기_")
st.write("준비됐나요? 자신있으면 도전해보세요! 👍")
st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
  if st.button("전쟁실Ⅰ 퀴즈 보기"):
    st.session_state['show_content_1'] = True
    st.session_state['show_content_2'] = False
    st.session_state['show_content_3'] = False
with col2:
  if st.button("전쟁실Ⅱ 퀴즈 보기"):
    st.session_state['show_content_2'] = True
    st.session_state['show_content_1'] = False
    st.session_state['show_content_3'] = False
with col3:
  if st.button("전쟁실Ⅲ 퀴즈 보기"):
    st.session_state['show_content_3'] = True
    st.session_state['show_content_1'] = False
    st.session_state['show_content_2'] = False
with col4:
  if st.button("모두 숨기기"):
    st.session_state['show_content_1'] = False
    st.session_state['show_content_2'] = False
    st.session_state['show_content_3'] = False

with st.form("quiz"):
  if st.session_state['show_content_1']:
    st.write("")
    img1 = Image.open('data/quiz1.png')
    st.image(img1, width=500)
    question1 = st.radio(
      "문제 1. 다음 자료를 바탕으로 옳지 않은 것은?",
      [
        "1. 이 부대는 스미스 특수임무부대이다.",
        "2. 그들은 오산 죽미령 전투에서 승리하였다.", # v
        "3. 이 부대의 활약으로 남한은 반격 시도의 시간을 벌 수 있었다.",
        "4. 이 부대는 유엔 참전 결의문 발표 이후 가장 먼저 참여한 UN군이다."
      ]
    )
    st.write("")
    img2 = Image.open('data/quiz2.png')
    st.image(img2, width=500)
    question2 = st.radio(
      "문제 2. 다음 자료를 바탕으로 옳지 않은 것은?",
      [
        "1. 본 논의는 서울 함락 직전에 이루어졌다.", # v
        "2. 이 자료의 배경 시기는 1950년 6월 29일이다.",
        "3. 자료에서 이승만 대통령, 맥아더 미극동군사령관, 무초 주한미군대사가 보인다.",
        "4. 이 논의를 통해 미 지상군 파병, 한/미 연합작전, 한국군에 대한 무기와 탄약지원이 이루어질 수 있었다."
      ]
    )
    st.write("")
    img3 = Image.open('data/quiz3.png')
    st.image(img3, width=500)
    question3 = st.radio(
      "문제 3. 다음 자료를 바탕으로 옳은 것은?",
      [
        "1. 이 명령서는 미군과 사전 협의 없이 단독으로 발령되었다.",
        "2. 이 명령서는 향후 국군의 날 제정/공포에 영향을 주었다.",
        "3. 이 명령서는 전쟁 초기 북한군의 남진을 막기 위해 작성되었다.", # v
        "4. 이 명령서는 6·25 전쟁 중 국군이 북한 지역까지 진격하도록 지시한 문서이다."
      ]
    )

  if st.session_state['show_content_2']:
    st.write("")
    img4 = Image.open('data/quiz4.png')
    st.image(img4, width=500)
    question4 = st.radio(
      "문제 1. 다음 자료를 바탕으로 옳은 것은?",
      [
        "1. 이 메달은 서울 탈환과 관련이 있다.",
        "2. 이 메달을 수여받은 부대는 국군 제7사단 제8연대이다.",
        "3. 이는 평양에 제일 먼저 진입한 공로를 인정받아 수여받은 메달이다.", # v
        "4. 이 메달을 수여받은 부대는 10월 9일 처음으로 탈환 작전에 성공하였다."
      ]
    )
    st.write("")
    img5 = Image.open('data/quiz5.png')
    st.image(img5, width=500)
    question5 = st.radio(
      "문제 2. 다음 자료를 바탕으로 옳지 않은 것은?",
      [
        "1. 이 철모는 용문산 전투에서 사용되었다.",
        "2. 용문산 전투를 통해 단독 전투로 사상 최대의 전과를 올렸다.",
        "3. 철모에는 붉은 글씨로 '결사' 표기가 적혀있어 장병들의 결연한 의지를 보여주고 있다.",
        "4. 이와 관련된 전투에서 국군은 중공군의 공세로 인해 화천발전소까지 60km정도 후퇴하였다." # v
      ]
    )
    st.write("")
    img6 = Image.open('data/quiz6.png')
    st.image(img6, width=500)
    question6 = st.radio(
      "문제 3. 다음 자료를 바탕으로 옳은 것은?",
      [
        "1. 이 탁자는 2010년 등록문화재로 지정되었다.", # v
        "2. 이는 남한이 먼저 제안한 정전과 관련된 것이다.",
        "3. 이와 관련된 협정은 서울 부근에 교착된 전선으로 인해 진행되었다.",
        "4. 정전협정으로 인해 일시적으로 전쟁은 중단되었으나 이후 다시 재개되었다."
      ]
    )

  if st.session_state['show_content_3']:
    st.write("")
    img7 = Image.open('data/quiz7.png')
    st.image(img7, width=500)
    question7 = st.radio(
      "문제 1. 다음 자료를 바탕으로 옳지 않은 것은?",
      [
        "1. 이 세 결의는 모두 한국전쟁 발발 직후 채택되었다.",
        "2. 제82호는 북한의 남침을 규탄하고 즉각 철수를 요구하였다.",
        "3. 제83호는 북한군의 공격 중단을 요구하지 않고 단순히 유엔군 파병을 승인하였다.", # v
        "4. 제84호는 유엔군 사령부를 설치하고 지휘권을 미국에 위임하였다."
      ]
    )
    st.write("")
    img8 = Image.open('data/quiz8.png')
    st.image(img8, width=500)
    question8 = st.radio(
      "문제 2. 다음 자료를 바탕으로 옳은 것은?",
      [
        "1. 초대 유엔군사령관은 일본 총리였다.",
        "2. 유엔 안전보장이사회는 유엔기 사용을 승인하지 않았다.",
        "3. 유엔기 전달은 1950년 7월 14일 도쿄의 극동군사령부에서 이루어졌다.", # v
        "4. 유엔기는 영국이 유엔군사령부의 설치를 승인하며 사용하기 시작하였다."
      ]
    )
    st.write("")
    img9 = Image.open('data/quiz9.png')
    st.image(img9, width=500)
    question9 = st.radio(
      "문제 3. 다음 자료를 바탕으로 옳은 것은?",
      [
        "1. 이 국기를 만든 나라는 미국이다.", 
        "2. 국기에는 ‘자유를 수호하자’라는 문구가 적혀 있다.",
        "3. 갈라타사라이고등학교 학생들이 직접 피로 글씨를 썼다.", # v
        "4. 이 국기는 6·25전쟁 후 평화협정 체결을 기념하기 위해 만들어졌다."
      ]
    )


  submitted = st.form_submit_button(":blue[제출]")

if submitted:
  score = 0
  total = 0
  
  if st.session_state.get('show_content_1'):
    questions = [question1, question2, question3]
    answers = [2, 1, 3]
    for i, (user_ans, correct) in enumerate(zip(questions, answers), start=1):
      total += 1
      if user_ans is not None:
        selected_num = int(user_ans.split(".")[0])
        if selected_num == correct:
          st.success(f"문제 {i}: 정답 ✅")
          score += 1
        else:
          st.error(f"문제 {i}: 오답 ❌ (정답은 {correct}번)")
      else:
        st.warning(f"문제 {i}: 답을 선택하지 않았습니다")
  
  if st.session_state.get('show_content_2'):
    questions = [question4, question5, question6]
    answers = [3, 4, 1]
    for i, (user_ans, correct) in enumerate(zip(questions, answers), start=1):
      total += 1
      if user_ans is not None:
        selected_num = int(user_ans.split(".")[0])
        if selected_num == correct:
          st.success(f"문제 {i}: 정답 ✅")
          score += 1
        else:
          st.error(f"문제 {i}: 오답 ❌ (정답은 {correct}번)")
      else:
        st.warning(f"문제 {i}: 답을 선택하지 않았습니다")
  
  if st.session_state.get('show_content_3'):
    questions = [question7, question8, question9]
    answers = [3, 3, 3]
    for i, (user_ans, correct) in enumerate(zip(questions, answers), start=1):
      total += 1
      if user_ans is not None:
        selected_num = int(user_ans.split(".")[0])
        if selected_num == correct:
          st.success(f"문제 {i}: 정답 ✅")
          score += 1
        else:
          st.error(f"문제 {i}: 오답 ❌ (정답은 {correct}번)")
      else:
        st.warning(f"문제 {i}: 답을 선택하지 않았습니다")
  
  st.markdown(f"### 🏁 최종 점수: {score} / {total}")


if st.session_state.get('show_content_1'):
  st.caption("출처: https://www.warmemo.or.kr:8443/Home/H20000/H20100/H20103/html")
if st.session_state.get('show_content_2'):
  st.caption("출처: https://www.warmemo.or.kr:8443/Home/H20000/H20100/H20104/html")
if st.session_state.get('show_content_3'):
  st.caption("출처: https://www.warmemo.or.kr:8443/Home/H20000/H20100/H20105/html")