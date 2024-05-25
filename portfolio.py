import streamlit as st
import plotly.express as px
import pandas as pd

# Определение CSS для светлой и темной тем
light_theme = """
<style>
.main {
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background: linear-gradient(to right, #ffffff, #C5A78B);
}
.stApp {
    background: linear-gradient(to right, #ffffff, #35332Cb);
    padding: 10px;
}
.stButton>button {
    color: black;
    background-color: transparent;
    border: none;
    font-size: 24px;
}

.stHeader, .stSubheader, .stText {
    color: #1f77b4;
}

a {
    color: #a88f77; /* Цвет ссылок (например, томатный) */
}

a:hover {
    color: #a47a61; /* Цвет ссылок при наведении (например, оранжево-красный) */
}
</style>
"""

dark_theme = """
<style>
.main {
    background-color: #0e1117;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background: linear-gradient(to right, #000000, #050520);
}
.stApp {
    background_gradient: linear-gradient(to right, #000000, #050520);
    padding: 10px;
}
.stButton>button {
    color: white;
    background-color: transparent;
    border: none;
    font-size: 24px;
}
.stHeader, .stSubheader, .stText {
    color: #0e1117;
}

a:hover {
    color: #1f212e; /* Цвет ссылок при наведении (например, оранжево-красный) */
}
</style>
"""

if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

def switch_theme():
    if st.session_state.theme == 'light':
        st.session_state.theme = 'dark'
    else:
        st.session_state.theme = 'light'

if st.session_state.theme == 'light':
    st.button('☀️', on_click=switch_theme)
else:
    st.button('🌙', on_click=switch_theme)

if st.session_state.theme == 'light':
    st.markdown(light_theme, unsafe_allow_html=True)
    photo_path = "path_to_light_theme_photo.jpg"
else:
    st.markdown(dark_theme, unsafe_allow_html=True)
    photo_path = "path_to_dark_theme_photo.jpg"

st.title("Привет! Познакомимся?")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(photo_path, width=200)  
with col2:

    st.write("""
 Меня зовут Галкина Юлия и я студентка НГТУ им. Р.Е. Алексеева. Обучаюсь на направлении "Информатика и вычислительная техника" профиля "Программное обеспечение средств вычислительной техники и автоматизированных систем". 
""")
    
st.write("""
**Моя специализация:**
- ML-разработка и Data Science
- Изучение методов Data Mining и Text Mining
- Работа с различными видами нейронных сетей: RNN, CNN
- Решение задач распознавания лиц, классификации изображений, кластеризации объектов, регрессии и предсказания данных
- Опыт работы с библиотеками: Pandas, NumPy, Matplotlib, Seaborn, Scikit Learn, TensorFlow, Keras

**Дополнительная деятельность:**
- Активист студенческого совета института
- Руководитель SMM-сектора студенческого совета
- Имеется опыт организатора
- Знаниt немецкого языка на уровне B1
- Есть научная публикация: "Лабораторный практикум по курсу «Сети и телекоммуникации»"
""")

st.markdown("<hr>", unsafe_allow_html=True)

st.header("Проекты")
st.write("Хочу поделиться некоторыми из моих проектов:")
project_options = {
    "Распознавание лиц с помощью библиотеки deepface": {
        "Описание": "Проверка сходства на фотографиях известных людей, а также их характеристика (эмоции, возраст, гендерная принадлежность)",
        "Технологии": "Python, deepface, OpenCV",
        "Ссылка": "https://github.com/cranberriess/face-recognition-deepface"
    },
    "Анализ датафрейма алмазов и их предсказание цены": {
        "Описание": "Проект, включающий в себя: анализ данных с описанием алмазов, предобработка фрейма, обучение нейронной сети, изменение архитектуры и предсказание цены на алмазы",
        "Технологии": "Python, NumPy, Plotly, TensorFlow, Keras",
        "Ссылка": "https://github.com/cranberriess/diamonds-data-mining"
    },
    "Генерация текста на GRU": {
        "Описание": "Построение языковой модели с использованием рекуррентных нейронных сетей с элементами GRU (Gated Recurrent Unit)",
        "Технологии": "Python, numpy, tensorflow",
        "Ссылка": "https://github.com/cranberriess/text-generation-GRU"
    },
    "Тематическое моделирование": {
        "Описание": "Латентное Размещение Дирихле для тематического моделирования нескольких статей",
        "Технологии": "Python, Pandas, pymorphy2, nltk, genism, matplotlib, pyLDAvis",
        "Ссылка": "https://github.com/cranberriess/thematic-modeling"
    },
    "Метод главных компонент библиотеки sklearn": {
        "Описание": "Реализован метод главных компонент с помощью PCA библиотеки sklearn на заданном датасете размерностью 3х10 (возраст, размер обуви, вес) и вручную.",
        "Технологии": "Python, Pandas, NumPy, PSA",
        "Ссылка": "https://github.com/cranberriess/PCA-test"
    },

    "Портфолио с помощью Streamlit": {
        "Описание": "Этот сайт-портфолио в открытом доступе",
        "Технологии": "Python, Streamlit",
        "Ссылка": "https://github.com/cranberriess/streamlit-portfolio"
    }
}

selected_project = st.selectbox("Выберите проект", list(project_options.keys()))

project_info = project_options[selected_project]
st.subheader(selected_project)
st.write(f"**Описание:**\n{project_info['Описание']}")
st.write(f"**Технологии:**\n{project_info['Технологии']}")
st.write(f"**Ссылка:**\n[{project_info['Ссылка']}]({project_info['Ссылка']})")

st.markdown("<hr>", unsafe_allow_html=True)

st.header("Коммуникативные навыки")
skills = {
    "Способность адаптироваться": 80,
    "Командная работа": 75,
    "Коммуникабельность": 85,
    "Критическое мышление": 70,
    "Эмоциональный интеллект": 80,
    "Лидерские навыки": 85,
    "Организованность": 90
}

for skill, proficiency in skills.items():
    st.write(f"{skill}: {'★' * (proficiency // 10)}{'☆' * (10 - proficiency // 10)}")
    
st.markdown("<hr>", unsafe_allow_html=True)

st.header("Профессиональные навыки")
prof = {
    "Графический дизайн": 80,
    "Машинное обучение": 80,
    "Анализ данных": 85,
    "Визуализация данных": 90,
    "Базы данных": 75,
    "Работа с пакетом MS Office": 95,
    "Разработка WEB-приложений": 70,
    "Телекоммуникации и локальные вычислительные сети": 65
}

prof_df = pd.DataFrame(list(prof.items()), columns=['Навык', 'Уровень'])

fig = px.scatter(prof_df, x='Уровень', y='Навык', orientation='h', labels={'Уровень': 'Процент'})
if st.session_state.theme == 'light':
    fig.update_layout(
     plot_bgcolor='#ffffff',  
     paper_bgcolor='#ffffff'  
    )
    fig.update_traces(marker=dict(color='#a47a61'))
else: 
    fig.update_layout(
        plot_bgcolor='#050520',  
        paper_bgcolor='#050520' 
    )

st.plotly_chart(fig)

st.markdown("<hr>", unsafe_allow_html=True)

st.header("Контакты")
st.write("""
Если появились вопросы или предложения, буду ждать сообщения:

📧 Электронная почта: [julija_galkina613348@mail.ru](mailto:julija_galkina613348@mail.ru)

💬 Telegram: [https://t.me/rar_rosenrot](https://t.me/rar_rosenrot)

🐙 GitHub: [https://github.com/cranberriess](https://github.com/cranberriess)
""")