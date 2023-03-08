import streamlit as st
import sys
from time import sleep

res = sys.path
print("경로는 : ")
print(res)
res.append('c:\python\python311\lib\site-packages')
from PyKakao import KoGPT
# api 키 : 	eeca4e088bea66c5e702151a08532279
api = KoGPT(service_key = "eeca4e088bea66c5e702151a08532279")
idxS = 0
idxE = 0
max_tokens = 64
# 필수 파라미터



st.title('hello world')
prompt = st.text_input('대화를 입력하세요','여기에 입력하면 됩니다.')
if((prompt == "종료")|(prompt == "end")|(prompt == "끝")):
    st.write('대화를 종료할게요')
result = api.generate(prompt, max_tokens, temperature=0.7, top_p=0.8)
gen = result['generations']
finres = gen[0]['text']
st.write(finres)
#for letter in finres:
#    sleep(0.05)
#    st.write(sys.stdout.write(letter))
#    sys.stdout.flush()
#st.write("")


