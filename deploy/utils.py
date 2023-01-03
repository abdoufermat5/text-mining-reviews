def load_css(file_name, st):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url, st):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name, st):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)