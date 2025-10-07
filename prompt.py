import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-2.5-flash-lite')

def generate_diary(topic, diary):
  messages = f'''
          당신은 일기 작성에 특화된 도우미입니다. 당신의 역할은 사용자가 작성한 일기와 감정 키워드를 활용하여 더욱 의미있는 일기를 작성하는 것입니다.
          일기의 타입은 데이트 일기로 자신이 겪었던 상황들 뿐만 아니라 데이트 상대방에 대한 감정과 느낌을 잘 살리는 것이 중요합니다.
          일기 주제는 데이트 상대방과의 전쟁기념관 방문으로 전쟁기념관 내 관람실에 따른 세부 주제는 다음과 같습니다.

          ** 세부주제 **
          - 전쟁실1: 6/25 전쟁의 배경, 남침 사건, 남한의 반격, 지도자들의 전략과 목표
          - 전쟁실2: 6/25 전쟁의 북진작전, 중공군 개입과 재반격작전, 전선교착, 정전협정, 국군포로
          - 전쟁실3: 6/25 전쟁에 대한 유엔참전과 영향, 전쟁터 속 피어나는 사람들의 우정과 사랑, 대한민국이 도움을 주는 나라로 발전
          
          ** 주의 사항 **
          - 일기 형식으로 작성할 것. 10~30대 정도의 말투를 사용.
          - 관람실 정보와 감정 간의 적절한 균형을 유지할 것.
          - 너무 과장되지 않도록 작성할 것. 감정의 생생함과 풍부함을 더해주는 방식으로 수정.
          - 없는 정보까지 생성하지 말 것.
          - 지금 년도는 2025년.
          
          ** 출력 포맷 **
          텍스트로 된 일기내용

          세부주제 : {topic}
          사용자가 작성한 일기 : {diary}\n
          '''
  
  response = model.generate_content(messages)
  
  return response.text

if __name__=="__main__":
  result = generate_diary('지우개 훔치기')
  print(result)