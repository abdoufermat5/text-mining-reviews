import os

import numpy as np
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px
from fermat_helpers.utils import get_data

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")


def visualization_page():
    dmImage = Image.open(os.path.join(data_path, "assets", "social-data-mining.webp"))
    # config
    st.set_page_config(
        page_title="Visualisation et Statistiques",
        page_icon=dmImage,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.sidebar.markdown("## Visualisation et Statistiques")
    st.sidebar.markdown("---")
    st.sidebar.markdown("""Dans cette section, vous pouvez voir les différentes visualisations et statistiques sur 
    les données""")
    st.header("Visualisation et Statistiques sur les autres attributs")
    # Load the data

    # display loader while loading the data
    with st.spinner("Chargement des données..."):
        data = get_data()

    reviews = data['Reviews']
    brandName = data['Brand Name'].str.upper()
    brandList = data["Brand Name"].unique().tolist()
    # unique products names
    uniqueProducts = data['Product Name'].value_counts().index.tolist()
    # total number of products
    totalProducts = len(uniqueProducts)

    # display this information in the sidebar
    st.sidebar.markdown("## Informations sur les donnees")
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"""
    > - Nombre de produits: {totalProducts}
    > - Nombre de marques: {len(brandList)}
    > - Nombre de commentaires/avis: {len(reviews)}""")
    st.markdown("""<div style="text-align: center"><img src="https://www.insee.fr/fr/statistiques/graphique/2498861/comprendre-stats.png"
            width="800" height="400" /></div>""", unsafe_allow_html=True)
    st.markdown("""
    Dans cette section, vous pouvez voir les différentes visualisations et statistiques sur les autres attributs.
    Afin d'avoir une idée sur les relations entre les différentes features nous exeplorons les données pour comprendre
     la distribution de ses derniers.""")
    st.markdown("---")

    tab1, tab2 = st.tabs(["Informations générales", "Graphiques"])

    with tab1:
        # display the brands names in a table
        st.markdown("## Liste des marques")
        st.markdown("---")
        # Collapsible table and scrollable
        with st.expander("Afficher la liste des marques"):
            # choose the number of rows to display
            nb_brand_to_show = st.slider("Nombre de lignes à afficher", 1, len(brandList), 10)
            # display the brands names in a table
            st.table(pd.DataFrame(brandList[1:], columns=['Marques']).head(nb_brand_to_show))
        # display the products names in a table
        st.markdown("## Liste des produits")
        st.markdown("---")
        # Collapsible table and scrollable
        with st.expander("Afficher la liste des produits"):
            # choose the number of rows to display
            nb_prod_to_show = st.slider("Nombre de lignes à afficher", 1, totalProducts, 10)
            # display the products names in a table
            st.table(pd.DataFrame(uniqueProducts, columns=['Produits']).head(nb_prod_to_show))

        # display the number of products per brand in a table
        st.markdown("## Nombre de produits par marques")
        st.markdown("---")
        # Collapsible table and scrollable
        with st.expander("Afficher la liste des produits par marques"):
            # choose the number of rows to display
            nb_prod_by_brand_to_show = st.slider("Nombre de lignes à afficher", 1, 100, 10)
            # display the products names in a table
            st.table(data.groupby(['Brand Name']).size().reset_index(name='Products').sort_values(
                by=['Products'], ascending=False).head(nb_prod_by_brand_to_show))

        # display the top 20 brands with reviews count according to the number of Reviews with Rating (>3)
        st.markdown("## Top 20 des marques selon le nombre d'avis avec une note supérieure à 3")
        st.markdown("---")
        # Collapsible table and scrollable
        with st.expander("Afficher la liste des marques avec le nombre d'avis"):
            st.table(data[data['Rating'] > 3].groupby(['Brand Name']).size().reset_index(name='Reviews').sort_values(
                by=['Reviews'], ascending=False).head(20))

    with tab2:
        # display the brands names in a table
        st.markdown("""<h2 align="center" style="background-color:#ffb4d8; border:1px solid green">Les 
        graphiques</h2>""", unsafe_allow_html=True)
        st.markdown("---")
        # display two diagrams in the same row
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""<h3 align="center" style="background-color:#00b4d8">Distribution des marques</h3>""",
                        unsafe_allow_html=True)
            st.markdown("---")
            st.bar_chart(brandName.value_counts())
        with col2:
            st.markdown("""<h3 align="center" style="background-color:#00b4d8">Distribution des produits</h3>""",
                        unsafe_allow_html=True)
            st.markdown("---")
            st.bar_chart(data['Product Name'].value_counts())
        with col3:
            # h3 title in light blue
            st.markdown("""<h3 align="center" style="background-color:#00b4d8">Distribution des Rating</h3>""",
                        unsafe_allow_html=True)
            st.markdown("---")
            # pie chart avec matplotlib
            fig, ax = plt.subplots()
            ax.pie(data['Rating'].value_counts(), labels=data['Rating'].value_counts().index,
                   autopct='%0.3f%%', shadow=True, startangle=90)
            ax.axis('equal')
            st.pyplot(fig)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""<h3 align="center" style="background-color:#00b4d8">Top 20 des produits les plus
                présents</h3>""", unsafe_allow_html=True)
            st.markdown("---")
            # diagramme en barre horizontal plotly en utilisant brandName.value_counts()
            fig = px.bar(brandName.value_counts().head(20),
                         x=brandName.value_counts().head(20).values,
                         y=brandName.value_counts().head(20).index,
                         color=brandName.value_counts().head(20).index,
                         orientation='h')
            # title and labels
            fig.update_layout(xaxis_title="Nombre d'occurences",
                              showlegend=False,
                              yaxis_title="Marques")
            st.plotly_chart(fig)
        with col2:
            st.markdown("""<h3 align="center" style="background-color:#00b4d8">Top 20 des marques les plus
                présentes</h3>""", unsafe_allow_html=True)
            st.markdown("---")
            # diagramme en barre vertical plotly en utilisant
            fig = px.bar(data[data['Rating'] > 3].groupby(['Brand Name']
                                                          ).size().reset_index(name='Reviews'
                                                                               ).sort_values(by=['Reviews'],
                                                                                             ascending=False).head(20),
                         y='Reviews',
                         x='Brand Name',
                         color='Brand Name',
                         color_discrete_sequence=px.colors.sequential.RdBu,
                         orientation='v')
            # title and labels
            fig.update_layout(yaxis_title="Nombre d'avis",
                              showlegend=False,
                              xaxis_title="Marques")
            st.plotly_chart(fig)

        with st.expander("Produit les plus appréciés et les moins apprécés par marque"):
            # choix de la marque parmi les 20 marques les plus présentes en fonction du
            # nombre d'avis et du nombre d'avis notés, de la moyenne et de l'écart-type
            pivot2 = pd.pivot_table(data,
                                    values=['Rating', 'Review Votes'],
                                    index=['Brand Name'],
                                    columns=[],
                                    aggfunc=[np.sum, np.mean, np.count_nonzero, np.std],
                                    margins=True, fill_value=0).sort_values(by=('count_nonzero', 'Rating'),
                                                                            ascending=False).fillna(
                '')
            top20brands = pivot2.reindex().head(n=21)
            top20 = top20brands.index.to_list()[1:]
            df_20 = data[data['Brand Name'].isin(top20)]

            # choix de la marque parmi les 20 marques
            brand = st.selectbox("Choisir une marque", top20)
            brnd_df = df_20[df_20['Brand Name'] == brand]
            p = pd.pivot_table(brnd_df, index=["Product Name"], values=["Rating", "Review Votes"], columns=[],
                               aggfunc=[np.sum, np.mean, np.count_nonzero], margins=True, fill_value=0).sort_values(
                by=("count_nonzero", "Rating"), ascending=False).fillna("")
            p2 = pd.pivot_table(brnd_df, index=["Product Name"], values=["Rating", "Review Votes"], columns=[],
                                aggfunc=[np.sum, np.mean, np.count_nonzero], margins=True, fill_value=0).sort_values(
                by=("count_nonzero", "Rating"), ascending=True).fillna("")
            top10_product = p.index.to_list()[:10]
            bottom10_product = p2.index.to_list()[:10]
            aa1 = brnd_df[brnd_df['Product Name'].isin(top10_product)]
            aa2 = brnd_df[brnd_df['Product Name'].isin(bottom10_product)]
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""<h3 align="center" style="background-color:#00b4d8">Top 10 des produits les plus 
                appréciés par {brand}</h3>""", unsafe_allow_html=True)
                st.markdown("---")

                # 10 produits les plus appréciés top10_product

                # 10 produits les moins appréciés
                # aggregate the data by product name and count the number of ratings
                fig = px.bar(
                    aa1.groupby(['Product Name']).size().reset_index(name='Reviews').sort_values(by=['Reviews'],
                                                                                                 ascending=False).head(
                        10),
                    y='Reviews',
                    x='Product Name',
                    color_discrete_sequence=px.colors.sequential.RdBu,
                    color='Product Name',
                    height=500,
                    width=500,
                    orientation='v')
                # title and labels
                fig.update_layout(yaxis_title="Nombre d'avis",
                                  xaxis_title="Produits",
                                  showlegend=False,
                                  coloraxis_showscale=False)
                fig.update_xaxes(showticklabels=False)
                st.plotly_chart(fig)

            with col2:
                st.markdown(f"""<h3 align="center" style="background-color:#00b4d8">Top 10 des produits les moins
                    appréciés par {brand}</h3>""", unsafe_allow_html=True)
                st.markdown("---")
                # plotly des 10 produits les moins appréciés top10_product
                fig = px.bar(
                    aa2.groupby(['Product Name']).size().reset_index(name='Reviews').sort_values(by=['Reviews'],
                                                                                                 ascending=True).head(
                        10),
                    y='Reviews',
                    x='Product Name',
                    # color palette
                    color_discrete_sequence=px.colors.sequential.RdBu,
                    color='Product Name',
                    height=500,
                    width=500,
                    orientation='v')
                # title and labels and color palette rotate the x axis labels
                fig.update_layout(yaxis_title="Nombre d'avis",
                                  xaxis_title="Produits",
                                  showlegend=False,
                                  )
                fig.update_xaxes(showticklabels=False)

                st.plotly_chart(fig)

        with st.expander("Les produits les plus chères et les moins chères"):
            col1, col2 = st.columns(2)
            # 10 produits les plus chères
            # aggregate the data by product name and count the number of ratings
            with col1:
                st.markdown(
                    f"""<h3 style="text-align: center;background-color:#00b4d8">Produit très bien évalués et à prix 
                    très abordable</h3>""",
                    unsafe_allow_html=True)
                low_price_df = (data[(data['Rating'] >= 3) & (data['Price'] < 300) & (data['Price'] > 50)].set_index(
                    'Product Name').groupby(level=0)['Price'].agg(
                    ['count'])).sort_values(['count'], ascending=False)[:10]
                # regroupement des données par les 10 produit les moins chères
                low_grouped = data.set_index('Product Name').loc[low_price_df.index].groupby(level=0)

                price = pd.Series(index=low_price_df.index, dtype=float)
                for i in low_price_df.index:
                    price[i] = low_grouped.get_group(i)['Price'].mean()
                low_price_df['Price'] = price
                low_price_df.reset_index(inplace=True)

                # seaborn des 10 produits les moins chères
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.barplot(x='Price',
                            y='count',
                            data=low_price_df.sort_values(by=['count'], ascending=True),
                            hue='Product Name',
                            dodge=False,
                            palette='RdBu')
                ax.set_xlabel("Prix")
                ax.set_ylabel("Nombre d'avis")
                ax.legend(loc="lower center", bbox_to_anchor=(0.5, -1.0))
                # rotate the x axis labels
                plt.setp(ax.get_xticklabels(), rotation=45)
                st.pyplot(fig)

            with col2:
                st.markdown(f"""<h3 style="text-align: center;background-color:#00b4d8">Produit très bien évalués et 
                prix entre 700€ et 1500€</h3>""",
                            unsafe_allow_html=True)
                high_price_df = (
                                    data[
                                        (data['Rating'] >= 3) & (data['Price'] > 700) & (data['Price'] < 1500)
                                        ].set_index('Product Name').groupby(level=0)['Price'].agg(
                                        ['count'])).sort_values(['count'], ascending=False)[:10]
                # regroupement des données par les 10 produit les moins chères
                high_grouped = data.set_index('Product Name').loc[high_price_df.index].groupby(level=0)

                price = pd.Series(index=high_price_df.index, dtype=float)
                for i in high_price_df.index:
                    price[i] = high_grouped.get_group(i)['Price'].mean()

                high_price_df['Price'] = price
                high_price_df.reset_index(inplace=True)

                # plotly des 10 produits les moins chères nom produit en abscisse, nombre d'avis en ordonnée
                # display seaborn barplot figure
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.barplot(x='Price',
                            y='count',
                            data=high_price_df.sort_values(by=['count'], ascending=False),
                            hue='Product Name',
                            dodge=False,
                            palette='RdBu')
                ax.set_xlabel("Prix")
                ax.set_ylabel("Nombre d'avis")
                # remove legend
                ax.legend(loc="lower center", bbox_to_anchor=(0.5, -1.0))

                # rotate the x axis labels
                plt.setp(ax.get_xticklabels(), rotation=45)
                st.pyplot(fig)

            # violin plot du prix en fonction ru rating
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.violinplot(x='Rating',
                           y='Price',
                           data=data,
                           hue='Rating',
                           dodge=False,
                           palette='RdBu')
            ax.set_xlabel("")
            ax.set_ylabel("Prix")
            # rename x labels
            ax.set_xticklabels(['Rating 1', 'Rating 2', 'Rating 3', 'Rating 4', 'Rating 5'])

            # rotate the x axis labels
            plt.setp(ax.get_xticklabels(), rotation=45)
            st.pyplot(fig)

            # in red rectangular box with light blue background write the text
            st.markdown(
                """
                <div style="background-color:#F0F8FF;padding:10px;border-radius:10px;border:1px solid red;margin:10px">
                <h3 align="center" style="color:#FF0000">Interprétation</h3>
                <p>En gros le rating n'a pas trop d'impact sur l'évaluations, la moyenne du prix est la même pour tous les niveaux d'évaluations même si on observe quelques valeurs abbérantes pour 5 et 1. Etant donnée la forme des violons au niveau de la médiane on peut en déduire que le prix n'a pas un impact énorme
                </p>
                </div>
                """,
                unsafe_allow_html=True)


if __name__ == "__main__":
    visualization_page()
