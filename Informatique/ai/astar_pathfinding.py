def heuristique(case, arrivee):
    return abs(case[0] - arrivee[0]) + abs(case[1] - arrivee[1])


def case_valide(grille, pos):
    x, y = pos
    nb_lignes = len(grille)
    nb_cols   = len(grille[0])

    dans_grille = (0 <= x < nb_lignes) and (0 <= y < nb_cols)
    pas_un_mur  = dans_grille and (grille[x][y] == 0)

    return pas_un_mur

def reconstruire_chemin(came_from, arrivee):
    chemin  = []
    current = arrivee

    while current in came_from:
        chemin.append(current)
        current = came_from[current]

    chemin.reverse()
    return chemin

def astar(grille, depart, arrivee):
    #...
    return None  # aucun chemin trouvé

grille = [
    [0,0,0,1,0,0,0,0,0,0],
    [0,1,0,1,0,1,1,1,0,0],
    [0,1,0,0,0,0,0,1,0,0],
    [0,1,1,1,1,1,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [1,1,1,1,0,1,0,1,1,0],
    [0,0,0,0,0,1,0,0,1,0],
    [0,1,1,1,0,0,0,0,1,0],
    [0,0,0,1,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

