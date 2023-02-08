import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def make_confusion_matrix(cf,
                          group_names=None,
                          categories='auto',
                          count=True,
                          percent=True,
                          cbar=True,
                          xyticks=True,
                          xyplotlabels=True,
                          sum_stats=True,
                          figsize=None,
                          cmap='Blues',
                          title=None):
    """
    Cette fonction crée une matrice de confusion sous forme de heatmap à partir de données de confusion passées en paramètre.

        cf: matrice de confusion (numpy array)
        group_names: liste de noms de groupes (str)
        categories: liste de noms de catégories (str)
        count: booléen indiquant s'il faut afficher le nombre d'observations (True) ou non (False)
        percent: booléen indiquant s'il faut afficher la proportion d'observations (True) ou non (False)
        cbar: booléen indiquant s'il faut afficher la barre de couleur (True) ou non (False)
        xyticks: booléen indiquant s'il faut afficher les étiquettes sur les axes x et y (True) ou non (False)
        xyplotlabels: booléen indiquant s'il faut afficher les noms des groupes et des catégories en haut et à gauche de la matrice de confusion (True) ou non (False)
        sum_stats: booléen indiquant s'il faut afficher les statistiques de résumé en bas de la matrice de confusion (True) ou non (False)
        figsize: tuple de deux entiers indiquant la largeur et la hauteur de la figure
        cmap: nom de la palette de couleurs à utiliser (str)
        title: titre de la figure (str)
    """
    # Créer une liste de chaînes vides de même longueur que la matrice de confusion
    blanks = ['' for i in range(cf.size)]

    # Si les noms des groupes sont spécifiés et qu'ils ont la même longueur que la matrice de confusion, utiliser ces
    # noms comme étiquettes pour les groupes
    if group_names and len(group_names) == cf.size:
        group_labels = ["{}\n".format(value) for value in group_names]
    # Sinon, utiliser une liste de chaînes vides comme étiquettes pour les groupes
    else:
        group_labels = blanks

    # Si "count" est vrai, utiliser le nombre d'observations comme étiquettes pour les groupes
    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    # Sinon, utiliser une liste de chaînes vides comme étiquettes pour le nombre d'observations
    else:
        group_counts = blanks

    # Si "percent" est vrai, utiliser la proportion d'observations comme étiquettes pour les groupes
    if percent:
        group_percentages = ["{0:.2%}".format(value) for value in cf.flatten() / np.sum(cf)]
    # Sinon, utiliser une liste de chaînes vides comme étiquettes pour la proportion d'observations
    else:
        group_percentages = blanks

    # Concaténer les étiquettes de groupes, de nombre d'observations et de proportion d'observations en une seule
    # chaîne pour chaque groupe
    box_labels = [f"{v1}{v2}{v3}".strip() for v1, v2, v3 in zip(group_labels, group_counts, group_percentages)]

    # Réorganiser les étiquettes en une matrice de la même forme que la matrice de confusion
    box_labels = np.asarray(box_labels).reshape(cf.shape[0], cf.shape[1])

    # Si "sum_stats" est vrai, calculer et afficher les statistiques de résumé
    if sum_stats:
        accuracy = np.trace(cf) / float(np.sum(cf))

        # Si la matrice de confusion a deux groupes, calculer et afficher la précision, le rappel et le score F1
        if len(cf) == 2:
            precision = cf[1, 1] / sum(cf[:, 1])
            recall = cf[1, 1] / sum(cf[1, :])
            f1_score = 2 * precision * recall / (precision + recall)
            stats_text = "\n\nAccuracy={:0.3f}\nPrecision={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
                accuracy, precision, recall, f1_score)
        # Sinon, seulement afficher l'exactitude
        else:
            stats_text = "\n\nAccuracy={:0.3f}".format(accuracy)
    # Si "sum_stats" est faux, ne pas afficher les statistiques de résumé
    else:
        stats_text = ""

    # Si aucune taille de figure n'est spécifiée, utiliser la taille par défaut
    if figsize == None:
        figsize = plt.rcParams.get('figure.figsize')

    # Si les noms des catégories sont spécifiés et qu'ils ont la même longueur que la matrice de confusion, utiliser ces
    # noms comme étiquettes pour les catégories
    if xyticks == False:
        categories = False

    # Créer la figure et l'axe
    plt.figure(figsize=figsize)
    ax = sns.heatmap(cf, annot=box_labels, fmt="", cmap=cmap, cbar=cbar, xticklabels=categories, yticklabels=categories)

    # Si "xyplotlabels" est vrai, ajouter les étiquettes "True label" et "Predicted label" aux axes x et y et ajouter
    # les statistiques de résumé
    if xyplotlabels:
        ax.set_ylabel('True label')
        ax.set_xlabel('Predicted label' + stats_text)
    # Sinon, seulement ajouter les statistiques de résumé à l'axe x
    else:
        ax.set_xlabel(stats_text)

    # Si un titre est spécifié, ajouter le titre à la figure
    if title:
        ax.set_title(title)

    # Afficher la figure
    plt.show()
