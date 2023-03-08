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
token = st.slider(" 최대문장 길이를 지정하세요",1,1000,64)
temp = st.slider("강도를 지정하세요",0.0,1.0,0.7)
# temper 지정
tp = st.slider("top_p를 지정하세요",0.0,1.0,0.8)
# top_p 지정
#option 근데 이거 너무 복잡해
result = api.generate(prompt, token, temperature=temp, top_p=tp)
gen = result['generations']
finres = gen[0]['text']
li_res = list(finres)
st.write(len(li_res))
li_max = len(li_res)
i=0
for i in range(0,li_max,300):
    li_res[i]= '\n'
    print(li_res[i])

st.write(finres)
finres = ' '.join(map(str, li_res))
st.write(li_res)
st.write(finres)
#for letter in finres:
#    sleep(0.05)
#    st.write(sys.stdout.write(letter))
#    sys.stdout.flush()
#st.write("")


