import i18n
import streamlit as st

from utils.init import init_once
logo_path = "logo.jpg.png"
if __name__ == '__main__':

    # Init
    init_once()

    with st.sidebar:
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"] {
                background-color: #ed1b1a;  /* Change this to your desired color */
                
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    st.image(logo_path, width=80)
    # Show title
    st.title(i18n.t('Welcome to Youtube world!'))
    # Show github link
    st.write(f'Be The Star')
    # Show page description
    st.write(i18n.t('유튜브 크리에이터를 위한 주제 추천 LLM 기반 유튜브 주제 추천 서비스는 인공지능 기술을 활용하여 크리에이터들이 다음 동영상 주제를 선택할 때 도움을 줍니다. 이 서비스는 언어 모델을 활용하여 다양한 키워드 및 주제를 분석하고, 유사한 주제의 인기 있는 동영상을 분석하여 추천합니다. 이를 통해 크리에이터들은 더 많은 시청자들을 유치하고 동영상의 인기를 높일 수 있습니다. 또한, 개별 사용자의 취향과 관심사에 따라 맞춤형 추천도 제공하여 더욱 효과적인 유튜브 콘텐츠를 제작할 수 있습니다. 이 서비스는 효율적이고 정확한 주제 추천을 통해 유튜브 크리에이터들이 성공적인 채널을 운영할 수 있도록 지원합니다.'))


