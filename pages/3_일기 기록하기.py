import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prompt import generate_diary

st.set_page_config(layout="wide")

for i in range(1, 4):
  key = f"show_content_{i}"
  if key not in st.session_state:
    st.session_state[key] = False

st.title("전쟁기념관 데이트 프로그램")
st.header("_:green[일기] 작성_")
st.write("자신이 느꼈던 감정을 키워드로 작성해주세요! 💙")
st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
  if st.button("전쟁실Ⅰ 일기 쓰기"):
    st.session_state['show_content_1'] = True
    st.session_state['show_content_2'] = False
    st.session_state['show_content_3'] = False
with col2:
  if st.button("전쟁실Ⅱ 일기 쓰기"):
    st.session_state['show_content_2'] = True
    st.session_state['show_content_1'] = False
    st.session_state['show_content_3'] = False
with col3:
  if st.button("전쟁실Ⅲ 일기 쓰기"):
    st.session_state['show_content_3'] = True
    st.session_state['show_content_1'] = False
    st.session_state['show_content_2'] = False
with col4:
  if st.button("모두 숨기기"):
    st.session_state['show_content_1'] = False
    st.session_state['show_content_2'] = False
    st.session_state['show_content_3'] = False

with st.form("diary"):
  if st.session_state['show_content_1']:
    st.subheader("📝 전쟁실Ⅰ 일기")
    
    # 키워드 선택
    keywords_1 = ["슬픔", "감동", "존경", "숙연함", "안타까움", "희생", "용기", "비극"]
    selected_keywords_1 = st.multiselect(
      "감정 키워드를 선택하세요 (여러 개 선택 가능)",
      keywords_1,
      key="keywords_1"
    )
    
    # 선택된 키워드를 텍스트로 표시
    keyword_text_1 = ", ".join(selected_keywords_1) if selected_keywords_1 else ""
    
    # 일기 작성
    diary_1 = st.text_area(
      "일기를 작성하세요",
      height=200,
      placeholder="선택한 키워드가 자동으로 입력되며, 직접 수정하거나 추가로 작성할 수 있습니다.",
      key="diary_1"
    )

  if st.session_state['show_content_2']:
    st.subheader("📝 전쟁실Ⅱ 일기")
    
    keywords_2 = ["자랑스러움", "감사", "결연함", "희망", "뿌듯함", "단결", "극복", "승리"]
    selected_keywords_2 = st.multiselect(
      "감정 키워드를 선택하세요 (여러 개 선택 가능)",
      keywords_2,
      key="keywords_2"
    )
    
    keyword_text_2 = ", ".join(selected_keywords_2) if selected_keywords_2 else ""
    
    diary_2 = st.text_area(
      "일기를 작성하세요",
      height=200,
      placeholder="선택한 키워드가 자동으로 입력되며, 직접 수정하거나 추가로 작성할 수 있습니다.",
      key="diary_2"
    )

  if st.session_state['show_content_3']:
    st.subheader("📝 전쟁실Ⅲ 일기")
    
    keywords_3 = ["평화", "연대", "감사", "우정", "협력", "희망", "국제적", "감동"]
    selected_keywords_3 = st.multiselect(
      "감정 키워드를 선택하세요 (여러 개 선택 가능)",
      keywords_3,
      key="keywords_3"
    )
    
    keyword_text_3 = ", ".join(selected_keywords_3) if selected_keywords_3 else ""
    
    diary_3 = st.text_area(
      "일기를 작성하세요",
      height=200,
      placeholder="선택한 키워드가 자동으로 입력되며, 직접 수정하거나 추가로 작성할 수 있습니다.",
      key="diary_3"
    )

  submitted = st.form_submit_button("🪄 내 일기 꾸미기")

if submitted:
  saved = False

  if st.session_state.get('show_content_1') and (diary_1 or keyword_text_1):
    st.success("✅ 전쟁실Ⅰ 일기가 저장되었습니다. AI가 더 풍부하고 생생하게 감정을 담아 일기를 작성해주고 있어요!")
    if diary_1 and keyword_text_1:
      output_diary1 = generate_diary('전쟁실1', diary_1+' '+keyword_text_1)
    elif keyword_text_1:
      output_diary1 = generate_diary('전쟁실1', keyword_text_1)
    else:
      output_diary1 = generate_diary('전쟁실1', diary_1)
    st.session_state['output_diary1'] = output_diary1

  if st.session_state.get('show_content_2') and (diary_2 or keyword_text_2):
    st.success("✅ 전쟁실Ⅱ 일기가 저장되었습니다!")
    if diary_2 and keyword_text_2:
      output_diary2 = generate_diary('전쟁실1', diary_2+' '+keyword_text_2)
    elif keyword_text_2:
      output_diary2 = generate_diary('전쟁실1', keyword_text_2)
    else:
      output_diary2 = generate_diary('전쟁실1', diary_2)
    st.session_state['output_diary2'] = output_diary2

  if st.session_state.get('show_content_3') and (diary_3 or keyword_text_3):
    st.success("✅ 전쟁실Ⅲ 일기가 저장되었습니다!")
    if diary_3 and keyword_text_3:
      output_diary3 = generate_diary('전쟁실1', diary_3+' '+keyword_text_3)
    elif keyword_text_3:
      output_diary3 = generate_diary('전쟁실1', keyword_text_3)
    else:
      output_diary3 = generate_diary('전쟁실1', diary_3)
    st.session_state['output_diary3'] = output_diary3

if 'output_diary1' in st.session_state and st.session_state.get('show_content_1'):
  with st.form("save1"):  # 다른 이름!
    result1 = st.text_area(
      "마지막으로 다듬어서 저장해보세요!",
      value=st.session_state['output_diary1'],
      height=400
    )
    saved1 = st.form_submit_button("💾 저장하기")
  
  if saved1:  # 여기서 바로 처리
    st.session_state['final_diary1'] = result1
    with st.expander("저장된 일기 보기"):
      st.write(result1)
      st.success("성공적으로 저장되었습니다! 당신의 아름다운 기억을 소중히 간직해둘게요.")
      
if 'output_diary2' in st.session_state and st.session_state.get('show_content_2'):
  with st.form("save2"):  # 다른 이름!
    result2 = st.text_area(
      "마지막으로 다듬어서 저장해보세요!",
      value=st.session_state['output_diary2'],
      height=400
    )
    saved2 = st.form_submit_button("💾 저장하기")
  
  if saved2:
    st.session_state['final_diary2'] = result2
    with st.expander("저장된 일기 보기"):
      st.write(result2)
      st.success("성공적으로 저장되었습니다! 당신의 아름다운 기억을 소중히 간직해둘게요.")
  
if 'output_diary3' in st.session_state and st.session_state.get('show_content_3'):
  with st.form("save3"):  # 다른 이름!
    result3 = st.text_area(
      "마지막으로 다듬어서 저장해보세요!",
      value=st.session_state['output_diary3'],
      height=400
    )
    saved3 = st.form_submit_button("💾 저장하기")
  
  if saved3:
    st.session_state['final_diary3'] = result3
    with st.expander("저장된 일기 보기"):
      st.write(result3)
      st.success("성공적으로 저장되었습니다! 당신의 아름다운 기억을 소중히 간직해둘게요.")