from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
import os

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")


def naive_bayes_description():
    st.markdown(
        """
        ### modèle de classification Naive Bayes:
        
        Le modèle de classification Naive Bayes est un modèle probabiliste simple qui utilise le théorème 
        de Bayes pour prédire la classe d'un échantillon en se basant sur des caractéristiques ou des 
        attributs de cet échantillon. 
        """
    )
    nbImage = Image.open(os.path.join(data_path, "assets", 'naive-bayes.png'))
    st.image(nbImage, caption='Naive Bayes', use_column_width=True)
    st.markdown("---")
    st.markdown(
        """
            Le modèle de Naive Bayes suppose que les différentes caractéristiques de l'échantillon sont 
            indépendantes les unes des autres, ce qui signifie que la valeur de chaque caractéristique ne dépend 
            pas des valeurs des autres caractéristiques. Cette hypothèse est connue sous le nom d'hypothèse de 
            l'indépendance conditionnelle. 
    
            Le modèle de Naive Bayes calcule la probabilité de chaque classe en utilisant la formule suivante :
    
            $$ P(C_i|X) = \\frac{P(X|C_i)P(C_i)}{P(X)} $$
    
            Où $C_i$ est la classe i, $X$ est l'échantillon et $P(C_i)$ est la probabilité a priori de la classe 
            $C_i$. Le modèle de Naive Bayes calcule également la probabilité de chaque caractéristique en 
            fonction de chaque classe, $P(X_j|C_i)$, en utilisant la même formule. 
    
            Pour prédire la classe d'un échantillon, le modèle de Naive Bayes calcule la probabilité de chaque 
            classe pour cet échantillon en utilisant les probabilités a priori et les probabilités 
            conditionnelles de chaque caractéristique. La classe avec la probabilité la plus élevée est 
            sélectionnée comme la classe prédite pour l'échantillon. 
            Le modèle de Naive Bayes est souvent utilisé pour l'analyse de sentiment, la reconnaissance de spam et la 
            reconnaissance de la parole, car il est simple à mettre en place et fonctionne bien sur de petits ensembles de 
            données. Cependant, son hypothèse d'indépendance conditionnelle peut être un frein à sa performance lorsque cette 
            hypothèse ne se vérifie pas dans les données réelles.
        """
    )


def rf_description():
    st.markdown(
        """
        # Modèle de classification Random Forest
    
        Le modèle de classification Random Forest est un modèle d'ensemble qui utilise plusieurs arbres de décision 
        pour prédire la classe d'un échantillon. 
        """)
    rfImage = Image.open(os.path.join(data_path, "assets", 'Random_forest_diagram_complete.png'))
    st.image(rfImage, caption='Random Forest', use_column_width=True)
    st.markdown("---")
    st.markdown(
        """
        Voici comment le modèle de classification Random Forest fonctionne en gros :
    
        <ol>
        <li><div style='background-color: #060c52;color:white;border-radius:5px;padding:5px'>
        Un nombre fixe d'arbres de décision est entraîné sur un sous-ensemble aléatoire des données d'entraînement.
        </div></li>
        <li><div style='background-color: #060c52;color:white;border-radius:5px;padding:5px'>Pour chaque arbre, un sous-ensemble aléatoire des caractéristiques est sélectionné comme 
        attributs à utiliser pour la séparation des ensembles de données. </div></li>
        <li><div style='background-color: #060c52;color:white;border-radius:5px;padding:5px'>Les arbres sont entraînés de manière indépendante et la prédiction de chaque arbre est 
        enregistrée.</div> </li>  
        <li><div style='background-color: #060c52;color:white;border-radius:5px;padding:5px'>La prédiction finale de l'ensemble est déterminée en utilisant la majorité des prédictions de 
        chaque arbre. </div></li>
        </ol>
    
        Le modèle de classification Random Forest est souvent utilisé pour ses performances élevées et sa robustesse 
        aux données bruyantes. Cependant, il peut être plus lent à entraîner que d'autres modèles de classification, 
        en particulier sur de grands ensembles de données.""",
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown("### Entrainement et résultats obtenus")
    st.markdown("---")


def description_section(section, chosen_model=None):
    if section == "Preprocessing":
        st.markdown("Le preprocessing est une etape importante dans le traitement des donnees textuelles. ")
        st.markdown("![preprocessing-image](https://miro.medium.com/max/580/1*VzhvZVKGVGynlsU0AZZQww.jpeg)")
    elif section == "Visualization":
        st.markdown("La visualisation des donnees est une etape importante dans le traitement des donnees textuelles. ")
        st.markdown("![visualization-image](https://miro.medium.com/max/580/1*VzhvZVKGVGynlsU0AZZQww.jpeg)")
    elif section == "Modele":
        st.markdown(
            "> <div style='background-color: black;color:white;padding:1em;border:5px solid green;border-radius:5px'><b>Dans cette etape nous allons "
            "predire le sentiment d'une critique sur les telephones "
            "portables. A partir de la description du produit, nous allons predire le sentiment de la "
            "critique.</b></div>",
            unsafe_allow_html=True)
        # description du modele choisi
        if chosen_model == "Naive Bayes":
            naive_bayes_description()
        elif chosen_model == "Random Forest":
            rf_description()
    elif section == "Explore notebooks":
        # choisir le notebook a ouvrir
        notebook = st.selectbox("Choisir le notebook", ["Pretraitement",
                                                        "Statistiques sur les autres variables",
                                                        "Modele tuning"])
        if notebook == "Pretraitement":
            # load html file
            with open(os.path.join(data_path, "assets", "preprocessing.html"), "r", encoding='utf-8') as f:
                html = f.read()
            # display html file
            components.html(html, height=500, width=1000, scrolling=True)
        elif notebook == "Statistiques sur les autres variables":
            # load html file
            with open(os.path.join(data_path, "assets", "stats_on_other_features.html"), "r", encoding='utf-8') as f:
                html = f.read()
            # display html file
            components.html(html, height=500, width=1000, scrolling=True)
        elif notebook == "Modele tuning":
            # load html file
            with open(os.path.join(data_path, "assets", "model.html"), "r", encoding='utf-8') as f:
                html = f.read()
            # display html file
            components.html(html, height=500, width=1000, scrolling=True)
