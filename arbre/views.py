from django.db.models import QuerySet
from django.shortcuts import render, HttpResponse
from django.core.handlers.wsgi import WSGIRequest

from arbre.models import Personne


def get_ascendants(personne: Personne):
    ascendants = []

    # Fonction récursive pour récupérer les ascendants
    def recursive_get_ascendants(p):
        if p.pere is not None and p.mere is not None:
            ascendants.append(p.pere)
            ascendants.append(p.mere)
            recursive_get_ascendants(Personne.objects.get(id=p.pere))
            recursive_get_ascendants(Personne.objects.get(id=p.mere))

        if p.pere is not None:
            ascendants.append(p.pere)

        if p.mere is not None:
            ascendants.append(p.mere)

    # Appel initial de la fonction récursive
    recursive_get_ascendants(personne)

    return ascendants


def nombres_communs(liste1, liste2):
    communs = []
    for nombre in liste1:
        if nombre in liste2:
            communs.append(nombre)
    return communs


# Create your views here.

def home(req: WSGIRequest):
    if req.method == 'POST':
        print(req.GET)
        users = Personne.objects.filter(name=req.POST['sea'])
        return render(req, 'search.html', {'users': users, "e": False})

    return render(req, 'search.html')


def view(req: WSGIRequest):
    if req.method == 'POST':
        user = Personne()
        user.user_name = str(req.POST['nom']).lower() + "_" + str(req.POST['prenom']).lower()
        user.name = req.POST['nom']
        user.last_name = req.POST['prenom']
        user.sexe = req.POST['sexe']
        user.pere = int(req.POST['pere'])
        user.mere = int(req.POST['mere'])
        user.save()

        return HttpResponse("<h1><center>Ajout reussi</center></h1>")

    hommes = Personne.objects.filter(sexe='homme')
    femmes = Personne.objects.filter(sexe='femme')

    return render(req, "index.html", {"hommes": hommes, "femmes": femmes})


def match(req: WSGIRequest):
    if req.method == 'POST':
        u1 = Personne.objects.get(user_name=req.POST['p1'])
        u2 = Personne.objects.get(user_name=req.POST['p2'])

        asc1 = get_ascendants(u1)
        asc2 = get_ascendants(u2)
        c = nombres_communs(asc1, asc2)[:2]
        p1 = Personne.objects.get(id=c[0])
        p2 = Personne.objects.get(id=c[1])
        return render(req, "parents.html", {"u1": p1, "u2": p2})

    return render(req, 'match.html')


def liste(req: WSGIRequest):
    lis = Personne.objects.all()
    return render(req, 'liste.html', {"lis": lis})


def ascendant(req: WSGIRequest, un: str):
    ok = Personne.objects.get(user_name=un)
    try:
        pere = Personne.objects.get(id=ok.pere)
        mere = Personne.objects.get(id=ok.mere)
        return render(req, "parents.html", {"u1": pere, "u2": mere})
    except Personne.DoesNotExist:
        return HttpResponse(f"<h2>Les parents de {ok.name} {ok.last_name} ne sont pas encore fichies dans la BD</h2>")


def descendant(req: WSGIRequest, un: str):
    ok = Personne.objects.get(user_name=un)

    enfants: QuerySet = Personne.objects.filter(pere=ok.id)
    if len(enfants) == 0:
        enfants = Personne.objects.filter(mere=ok.id)

    return render(req, "children.html", {"users": enfants})


def parent(req: WSGIRequest, user_name: str):
    u = Personne.objects.get(user_name=user_name)
    p = Personne.objects.get(id=u.pere)
    m = Personne.objects.get(id=u.mere)
    return render(req, 'parents.html', {"u1": p, "u2": m})
