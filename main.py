import os
import pandas as pd
import youtube_api as yt
import datetime
from datetime import datetime
import csv


api_key = 'AIzaSyDYcXd7YhNVTppQqgwdhk7CYExtZ2hFq4Q'
yt_search = yt.YouTubeDataAPI(api_key)

searches = yt_search.search('jdg')

# print(searches)
# print('\n')
# print(searches[0])

def recherche_yt():
    
    print('Recherche YouTube :')
    a = input()
    
    print('Nombre de resultats (Entrez un nombre entier) :')
    c = input()
    
    print('Titre seul : tappez "titre"\nChaine : tappez "chaine"\nDate de publication : tappez "date"\nDescription : tappez "description"\nCatégorie : tappez "categorie"\nTous les éléments : tappez "Tout"')
    b = input()
    
    r = yt_search.search(str(a), max_results=int(c))
    
    if str(b) == 'titre':
        print('\n')
        print('Recherche de ' +  ': ' + str(a) + '\n')
        for i in range (len(r)):
            print('resultat n°' + str(i + 1) + ' : ')
            print('Titre de la Vidéo : ' + str(r[i]['video_title']))
            print('\n')
            
    elif str(b) == 'description':
        print('\n')
        print('Recherche de ' +  ': ' + str(a) + '\n')
        for i in range (len(r)):
            print('resultat n°' + str(i + 1) + ' : ')
            print('Titre de la Vidéo : ' + str(r[i]['video_title']))
            print('Description de la Vidéo : ' + str(r[i]['video_description']))
            print('\n')
            
    elif str(b) == 'chaine':
        print('\n')
        print('Recherche de ' +  ': ' + str(a) + '\n')
        for i in range (len(r)):
            print('resultat n°' + str(i + 1) + ' : ')
            print('Titre de la Vidéo : ' + str(r[i]['video_title']))
            print('Nom de la Chaine : ' + str(r[i]['channel_title']))
            print('\n')
            
    elif str(b) == 'categorie' :
        print('\n')
        print('Recherche de ' +  ': ' + str(a) + '\n')
        for i in range (len(r)):
            print('resultat n°' + str(i + 1) + ' : ')
            print('Titre de la Vidéo : ' + str(r[i]['video_title']))
            print('Catégorie de la Vidéo : ' + str(r[i]['video_category']))
            print('\n')
            
    elif str(b) == 'date':
        print('\n')
        print('Recherche de ' +  ': ' + str(a) + '\n')
        for i in range (len(r)):
            ts = int(r[i]['video_publish_date'])
            time = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            print('resultat n°' + str(i + 1) + ' : ')
            print('Titre de la Vidéo : ' + str(r[i]['video_title']))
            print('Date de publication de la Vidéo : ' + str(time))
            print('\n')
            
    elif str(b) == 'tout' :
        print('\n')
        print('Recherche de ' +  ': ' + str(a) + '\n')
        for i in range (len(r)):
            ts = int(r[i]['video_publish_date'])
            time = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            print('resultat n°' + str(i + 1) + ' : ')
            print('Nom de la Chaine : ' + str(r[i]['channel_title']))
            print('Titre de la Vidéo : ' + str(r[i]['video_title']))
            print('Date de publication de la Vidéo : ' + str(time))
            print('Description de la Vidéo : ' + str(r[i]['video_description']))
            print('Catégorie de la Vidéo : ' + str(r[i]['video_category']))
            print('\n')
            
    elif str(b) != 'titre' and str(b) != 'description' and str(b) != 'chaine' and str(b) != 'categorie' and str(b) !='date' and str(b) !='tout' :
        print('requête incorrecte, réessayez :\n')
        recherche_yt()
           
                
#recherche_yt()


def create_csv():
    print('Recherche YouTube de :')
    a = input()
    main=[' TITRE ; CHAINE ; DATE DE PUBLICATION ']
    with open(str(a)+'.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(main)
        
        print('Nombre de resultats (Entrez un nombre entier) :')
        b = input()
    
        r = yt_search.search(str(a), max_results=int(b))
        
        for i in range (len(r)):
            ts = int(r[i]['video_publish_date'])
            time = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([' ' + str(r[i]['video_title']) + ' ; ' + str(r[i]['channel_title']) + ' ; ' + str(time) + ' '])

create_csv()