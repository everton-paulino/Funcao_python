dic = {
    "musicas":[
    {"nome": "Hey Jude", "banda": "Beatles" },
    {"nome": "November Rain", "banda": "Guns N' Roses" },
    {"nome": "How Deep Is Your Love", "banda": "Bee Gees" }
    ],
    "filmes":{
    "X-men": ["wolverine", "Xavier", "Tempestade", "Vampira", "Magneto", "Ciclope", "Gambit"],
    "Avengers": ["Homem de Ferro", "Hulk", "Thanos", "Capitão América", "Thor", "Capitã Marvel", "Homem-Aranha"],
    "Star Wars": ["luke", "Leia", "C-3PO", "Darth Vader", "Obi-Wan", "Yoda", "R2-D2", "Han Solo", "Chewbacca"]
    }    
}

def func1(a,b,c,d):
    for x in a:
        if x[b] == d:
            return x[c]
        
    return"naosei"    

print("Hey Jude" in dic["nome"]["Beatles"])
