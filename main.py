import streamlit as st
import numpy as np 
import collections
from PIL import Image
import glob
import os

st.title("パーソナルカラークローゼット")
st.write("パーソナルカラーとあなたの好みの服装からあなたにピッタリの服装を提案します!")
image_title = Image.open("pc-woman-illust_all.jpg")
st.image(image_title)
"""
### パーソナルカラーとは
 似合う色は人それぞれ違い、生まれ持った肌・瞳・髪の色（ボディカラー）によって決まります。そんな「あなたに似合う色」がパーソナルカラーです。身に着けると、美肌に見えたり、あか抜けて見え、イメージアップします。また、ファッションやメイクの色選びの幅が広がるなど、嬉しい効果が期待できるのがパーソナルカラーです。
***
### 設問に答えてパーソナルカラーを分析しよう！
質問の当てはまる答えにチェックをいれてください。
"""


ans_list = []

genre = st.radio("Q1.あなたの目の色は？",['A','B','C','D',], horizontal=True,key="q1")
st.write('A.瞳は明るいブラウンかソフトなブラック。ガラス玉の様にキラキラしている。')
st.write('B.瞳はダークブラウンかブラック。落ち着いた印象がある')
st.write('C.瞳は赤みのブラウンかソフトなブラック。優しい印象がある')
st.write('D.瞳はブラックか赤みのダークブラウン。白目と黒目のコントラストがはっきりしている')
ans_list.append(genre)


genre = st.radio("Q2. あなたの肌の色は？",['A','B','C','D',], horizontal=True, key="q2")
st.write('A.肌の色は明るいオークル系で、皮膚が薄め。')
st.write('B.肌の色はオークル系でマットな肌')
st.write('C.明るいピンク系の肌。肌の質感はややマット')
st.write('D.ピンク系の白色肌、ダーク肌。あるいは黄みがかなり強いオークル系の肌、肌に艶がある。')
ans_list.append(genre)

genre = st.radio("Q3. 日焼けするとどうなる？",['A','B','C','D',], horizontal=True, key="q3")
st.write('A.すぐに日焼けするが、もどるのも早い')
st.write('B.日焼けしやすく、元にもどりにくい')
st.write('C.赤くなって日焼けしない')
st.write('D.やや赤くなり、その後日焼けす')
ans_list.append(genre)

genre = st.radio("Q4. 肌に馴染むアクセサリーは？",['A','B','C','D',], horizontal=True, key="q4")
st.write('A.キラキラした明るいゴールド')
st.write('B.黄みの強いゴールド、つや消しのゴールド、ブロンズ')
st.write('C.優しい光沢のプラチナ、シルバー')
st.write('D.艶のあるプラチナ、シルバー')
ans_list.append(genre)

genre = st.radio("Q5. 周りから褒められる口紅の色は？",['A','B','C','D',], horizontal=True, key="q5")
st.write('A.ピーチピンクなど明るいオレンジ系の口紅')
st.write('B.オレンジベージュなど落ち着いたオレンジ系の口紅')
st.write('C.ローズピンクなど明るいローズ系の口紅')
st.write('D.フューシャピンクなど鮮やかなローズ系の口紅')
ans_list.append(genre)

genre = st.radio("Q6. 反対に苦手だと思う口紅の色は？",['A','B','C','D',], horizontal=True, key="q6")
st.write('A.ワインレッド')
st.write('B.ローズピンク')
st.write('C.オレンジ')
st.write('D.オレンジベージュ')
ans_list.append(genre)

genre = st.radio("Q7. ベージュとグレーはどちらが得意？",['A','B','C','D',], horizontal=True, key="q7")
st.write('A.明るいベージュを着ると顔色がよく見える')
st.write('B.落ち着いたベージュやブラウンが地味にならな')
st.write('C.ライトグレーやブルーグレーを着ると肌が綺麗に見える')
st.write('D.暗めのグレーでお顔の印象がはっきりする')
ans_list.append(genre)

genre = st.radio("Q8. 周りからよく言われる第一印象は？",['A','B','C','D',], horizontal=True, key="q8")
st.write('A.明るい、キュート、かわいい、年齢より若く見える')
st.write('B.落ち着いている、大人っぽい、ゴージャス、ナチュラル')
st.write('C.ソフト、優しい、エレガント、爽やか')
st.write('D.シャープ、クール、華やか、印象的')
ans_list.append(genre)

ans_list2=collections.Counter(ans_list)
pc_ans = ans_list2.most_common()
pc = pc_ans[0]

#PCごとのカラーリスト
image = Image.open("spring_color.jpeg")
image_2 = Image.open("summer_color.jpeg")
image_3 = Image.open("autumn_color.jpeg")
image_4= Image.open("winter_color.jpeg")

#PCごとのカラーリストを表示
"""
### あなたのパーソナルカラーは
"""
if "A" in pc:
    st.image(image, caption='spring',use_column_width=True)
if "B" in pc:
    st.image(image_2, caption='summer',use_column_width=True)  
if "C" in pc:
    st.image(image_3, caption='autumn',use_column_width=True)
if "D" in pc:
    st.image(image_4, caption='winter',use_column_width=True)    
#季節を選ぶ
"""
***
## 好みの服装を分析します！
"""
import streamlit as st
option  = st.selectbox(
    '今の季節はSS（春夏）か AW（秋冬）か選択してください',
     ('SS', 'AW'))
season_1 = option
# st.write('You selected:', season_1)

# img_SS_photo = Image.open(r"C:\Users\frome\OneDrive\Desktop\streamlit\SS_photo\SS_1.jpg")
# st.image(img_SS_photo)

#以下重森さんと作成
# #SS_photo と　AW_photoのファルダ配下のファイルを読みこむ　おそらくできてない。。。
file_list_SS = glob.glob("SS_photo/*")
file_list_AW = glob.glob("AW_photo/*")
# st.write(file_list_SS)
# st.write(type(file_list_SS))
#季節の好きなテイストをえらぶ
#選ばれたシーズンごとの画像を表示　　表示された画像からえらぶようにするために関数？defにする
#３０のがぞうから7選ぶ  フォルダ読み込み
col = st.columns(6)

if season_1 == "SS" :
    selected_list = file_list_SS
    for i in range(len(file_list_SS)):
        # os.path.join("SS_photo",file_list_SS[i])
        SS_image = Image.open(file_list_SS[i])
        # SS_image = image.open(os.path.join("SS_photo",file_list_SS[i]))
        ii =  i % 6
        col[ii].write(i)
        col[ii].image(SS_image,use_column_width=True)
if season_1 == "AW" :
    selected_list = file_list_AW
    for i in range(len(file_list_AW)):
        AW_image = Image.open(file_list_AW[i])
    # st.image(AW_image,use_column_width=True)
        ii =  i % 6
        col[ii].write(i)
        col[ii].image(AW_image,use_column_width=True)
        
selected_numbers = st.multiselect('好みの服装の番号を6つ選択してください。', list(range(len(selected_list))))
# st.write(selected_numbers)
# st.write(type(selected_numbers))
# selected_pictures = selected_list[selected_numbers]
selected_pictures = [selected_list[i] for i in selected_numbers]

# (SS_width, SS_height) = (SS_image.width=, SS_image.height=)
# # 画像をリサイズする
#  SS_image.resize((SS_width, SS_height))
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing import image

model = load_model('cnn.h5')#学習済みモデルをロード

classes = ["hurugi","girly","handsome","casual","kireime"]
image_size = 200
#受け取った画像を読み込み、np形式に変換
img_data = []
for path in selected_pictures :
    
    img = image.load_img(path, target_size=(image_size,image_size))#filepathを選択した写真に
    img = image.img_to_array(img)
    img_data.append(img)
data = np.array(img_data)
predict_botan = False
if len(selected_pictures) >= 6:
    predict_botan = st.button('選択完了')
#変換したデータをモデルに渡して予測する
if predict_botan :
    result = model.predict(data)
    predicted = result.argmax(axis=1)
    u,counts = np.unique(predicted, return_counts=True)
#   st.write(counts)
    result_class= (u[counts.argmax()])

    season_dict = {"A":"spring","B":"summer","C":"autumn","D":"winter"}
    concut_path = [season_1, season_dict[pc[0]],classes[result_class]]
    result_filename = "_".join(concut_path)
    result_filepath = season_1 + "_" +  season_dict[pc[0]] + "/" + result_filename + ".jpg"
    result_picture = Image.open(result_filepath)
    st.write("今季のあなたにピッタリのコーディネートはこちらです。")
    st.image(result_picture)





# #選んだ画像から機械モデルを作成する
# #画像データをかさまし 
# #def scratch_image(img, flip=True, thr=True, blur=True, resize=True, erode=True):
#     methods = [flip, thr, blur, resize, erode]
#     img_size = img.shape
#     blurer1 = np.ones((3, 3))
#     images = [img]
#     scratch = np.array([
#         lambda x: cv2.flip(x, 1),
#         lambda x:cv2.threshold(x, 100, 255, cv2.THRESH_TOZERO)[1],
#         lambda x: cv2.GaussianBlur(x, (5, 5), 0),
#         lambda x:cv2.resize(cv2.resize(x, (x.shape[1] // 5 , x.shape[0] // 5)),( x.shape[1] , x.shape[0] )),
#         lambda x:cv2.erode(x, blurer1)
#         ])
# doubling_images = lambda f, imag: (imag + [f(i) for i in imag])
#     for func in scratch[methods]:
#         images =  doubling_images(func,images)
    
#     return images
#     scratch_cat_images = scratch_image(cat_img)

# #モデルの作成

# １モデル作成


# どの画像を選択するかのフォーム作成
# 動作流れ
# 選択画像➡モデルでふるいにかける➡ジャンルわけ