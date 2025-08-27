import streamlit as st
import requests
names = []
url = "https://pokeapi.co/api/v2/type?limit=100&offset=0"
while url:
    res = requests.get(url)
    data = res.json()
    for item in data['results']:
        names.append(item['name'])
    url = data['next']
nome = st.selectbox('Selecione o tipo de pokemon', names)
nome = nome.strip().lower()
col1, col2, col3 = st.columns(3)
st.sidebar.title('Projeto de pokemon')
pikachu = requests.get('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/pikachu')
st.sidebar.image('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/25.gif', width=150)
def get_pokemon_by_type(tipo):
    url = f"https://pokeapi.co/api/v2/type/{tipo}/"
    resposta = requests.get(url)
    dados = resposta.json()
    return [entry['pokemon']['name'] for entry in dados['pokemon']]

pokemons = get_pokemon_by_type(nome)

tab1, = st.tabs([f"Pokémons do tipo {nome.capitalize()}"])

with tab1:
    pokenum = st.number_input(
    f"Quantos Pokémon do tipo {nome.capitalize()} você quer?",
    min_value=1,
    max_value=len(pokemons),
    value=min(5, len(pokemons)),
    step=1)
    n = int(pokenum)
    for i in range(0, n):
        with st.container():
            st.markdown(f"- ## {pokemons[i]} ")
            nome = pokemons[i]
            res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome}/')
            if res.status_code == 200:
                dados = res.json()
                pokemon_id = dados["id"]
                url_gif = (
                    f'https://raw.githubusercontent.com/PokeAPI/sprites/master/'
                    f'sprites/pokemon/other/showdown/{pokemon_id}.gif'
                )
                st.image(url_gif, caption=f"{nome.capitalize()} (ID: {pokemon_id})")