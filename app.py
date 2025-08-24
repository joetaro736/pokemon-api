import streamlit as st
import requests
nome = st.text_input('Digite o nome do pokemon')
nome = nome.strip().lower()
col1, col2, col3 = st.columns(3)


try:
    pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome}').json()
    p_id = pokemon['id']

    with col1:
        st.image(f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/{p_id}.gif', width=300)

    with col2:
        st.title(nome.capitalize())
        st.audio(f'https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{p_id}.ogg')
        st.audio(f'https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/legacy/{p_id}.ogg')
    with col3:
        st.image(f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/back/{p_id}.gif', width=300)
except:
    st.warning('Escreva o nome do pokemon correto')



tab1, tab2, tab3, tab4 = st.tabs(['tipo',
    'locais',
    'habilidade',
    'status base'])


with tab1:
    for i in pokemon['types']:
        st.markdown(f'- ## {i['type']['name'].capitalize()}')
with tab2:
    locais = requests.get(pokemon['location_area_encounters']).json()
    for l in locais:
        st.markdown(f'- ## {l['location_area']['name']}')
with tab3:
    for i in pokemon['abilities']:
        st.markdown(f'- ## {i['ability']['name']}')
with tab4:
    with st.container():
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col3:
            st.metric('Altura', f'{pokemon['height'] / 10} M')
        with col4:
            st.metric('Peso', f'{pokemon['weight'] / 10:.0f} KG')
    with st.container():
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.metric('HP', pokemon['stats'][0]['base_stat'])
        with col2:
            st.metric('Ataque', pokemon['stats'][1]['base_stat'])
        with col3:
            st.metric('Defesa', pokemon['stats'][2]['base_stat'])
        with col4:
            st.metric('Ataque Especial', pokemon['stats'][3]['base_stat'])
        with col5:
            st.metric('Defesa Especial', pokemon['stats'][4]['base_stat'])
        with col6:
            st.metric('Velocidade', pokemon['stats'][5]['base_stat'])