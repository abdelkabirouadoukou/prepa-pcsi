import heapq

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

    open_list = []
    heapq.heappush(open_list, (0, 0, depart))

    came_from = {}
    g_score   = {depart: 0}

    DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]

    while open_list:

        _, g, current = heapq.heappop(open_list)

        if current == arrivee:
            return reconstruire_chemin(came_from, arrivee)

        for dx, dy in DIRECTIONS:
            voisin = (current[0] + dx, current[1] + dy)

            if not case_valide(grille, voisin):
                continue

            g_nouveau = g + 1

            meilleur = g_nouveau < g_score.get(voisin, float('inf'))

            if meilleur:
                g_score[voisin]   = g_nouveau
                f                 = g_nouveau + heuristique(voisin, arrivee)
                came_from[voisin] = current
                heapq.heappush(open_list, (f, g_nouveau, voisin))

    return None

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

depart  = (0, 0)
arrivee = (9, 9)

chemin = astar(grille, depart, arrivee)

if chemin:
    print(f"Chemin trouvé ({len(chemin)} pas) :")
    print(chemin)
else:
    print("Aucun chemin possible.")