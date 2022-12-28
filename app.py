"""
# Streamlit超入門
Streamlitフレームワークを使いこなせるようにするための練習用のプログラム

## 実行方法
```python
$ streamlit run main.py
```
"""

# 必要ライブラリのインポート
import streamlit as st
import time

# タイトル
st.markdown('# Streamlit テストアプリケーション')

# フラグ
if ('update' not in st.session_state):
    st.session_state['update'] = False

# 題名と説明
st.markdown('# 開始・終了ボタン')
st.markdown('開始を押すと10秒経つまで終了できませんので、ご了承ください。')

# ボタンの設置
placeholder = st.empty() # プレイスホルダーを使用

# 境界線を引く
st.markdown('***')

# 問題と説明
st.markdown('## 問題')
st.markdown('10秒以内に以下の数式の答えを述べよ。')

# 押す回数によってボタンの表示を変更する処理
with placeholder:
    if 'botton_str' not in st.session_state: # デフォルトルート
        st.session_state['botton_str'] = '開始'
    elif (st.session_state['botton_str'] == '終了') and (st.session_state['update']==True): # 値が入力されて更新された時の処理
        st.session_state['botton_str'] = '終了'
    elif st.session_state['botton_str'] == '終了': # 開始が押されて、文字入力による更新以外での処理
        st.session_state['botton_str'] = '開始'
    botton_start = st.button(st.session_state['botton_str'], key='start') # ボタンの表示
    if botton_start: # ボタンが押された時の処理
        st.session_state['botton_str'] = '終了'
        st.button(st.session_state['botton_str'], key='stop') # ボタンの表示

# ボタンの表示名によって処理内容を変化
if (st.session_state['botton_str'] == '終了') or st.session_state['update']:
    # 開始ボタンが押されるもしくは文字が入力され画面が更新された時の処理
    st.markdown('**数式 $3x + 2 = 8$ : $x$の値を答えよ**')
    st.markdown('## 回答')
    # プログレスバー（カウントダウンバー）の設定
    latest_iteration = st.empty()
    bar = st.progress(0) # 整数設定
    # テキストボックスの設置
    text = st.text_input('下記に入力して下さい。', value='0')
    if text:
        st.session_state['update'] = True
    st.session_state['text'] = text
    # 正解・不正解の判定処理
    if st.session_state['text']=='2':
        answer = '正解'
        st.success(f'あなたの回答 **{text}** は、**{answer}**です !', icon="✅")
        st.balloons()
    else:
        answer = '不正解'
        st.error(f'あなたの回答 **{text}** は、**{answer}**です !', icon="🚨")
        if text!='0':
            st.snow()
    # デフォルトルート
    if 'time' not in st.session_state:
        st.session_state['time'] = 100
    # カウントダウンの処理
    for i in range(st.session_state['time'],-1,-1):
        if answer=='正解': break
        st.session_state['time'] = i
        latest_iteration.text(f'カウントダウン ->> {i/10}s')
        bar.progress(i) # プログレスバーの表示
        time.sleep(0.1)
    # タイムオーバーの処理
    st.session_state['update'] = False
elif st.session_state['botton_str'] == '開始':
    # デフォルトルートと終了が押された場合の処理
    st.markdown('**ここに数式が表示されます。**')
    st.markdown('## 回答')
    # カウントダウンの値を初期化
    st.session_state['time'] = 100