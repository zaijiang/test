import streamlit as st
st.title("wzx你在干嘛啊")
st.header("My Website")
st.subheader("Data Analytics")
st.text("Simple text")
st.write("Hello World!")
st.markdown('Streamlit is **_really_ cool**.')
st.latex('E=MC^2')
st.success('Success!')
st.warning('Warning!')
st.error('Error!')
st.code("""
class MyClass:
    def __init__(self):
        super(MyClass, self).__init__()
""")
st.json({
    "pagination": {
        "total": 100,
        "per_page": 20,
        "page": 1,
    },
    "items": [
        {
            "id": 1,
            "name": "admin",
            "email": "admin@test.com",
            "is_superuser": True
        }
    ]
})
