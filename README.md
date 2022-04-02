<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>AlgoInvest&Trade</h1>
	<p>
		Le programme définie la meilleure stratégie d'investissement à partir d'une liste d'actions qui lui est fournit.<br>
		<h2>Deux approches de calcul pour arriver à la solution la plus optimisée.</h2><br>
		<h3>La méthode bruteforce</h3><br>
		(limitée à des données de petite taille)<br>
		Est une technique de resolution de problème dans laquelle la solution possible 
		à un probleme est decouverte en vérifiant chaque réponse une par une, en
		déterminant si le resultat satisfait ou non l'énonce d'un probleme.<br><br>
		<h3>L'approche dynamique</h3><br>
		(solution plus optimisée, couteux en taille mémoire)<br>
		La programmation dynamique est une technique algorithmique pour résoudre
		un problème d'optimisation en le décomposant en sous-problemes plus 
		simples et en utilisant le fait que la solution optimale au problème
		global dépend de la solution optimale à ses sous problèmes.
	</p>
	<h2>Installtion</h2>
	<p>
		<ul>
			<li>Clonez le repository <code>git clone</code></li>
			<li>Se déplacer dans le répertoire racine epic-events <code>cd algoinvest</code></li>
			<li>Créer un environnement virtuel <code>python -m venv env</code></li>
			<li>Activez l'environnement virtuel <code>env\Scripts\activate.bat</code></li>
			<li>Installez les dépendances du project <code>pip install -r requirements.txt</code></li>
		</ul>
	</p>
	<h2>Exécution</h2>
	<ul>
		<li>Se déplacer dans le répertoire racine AlgoInvest <code>cd AlgoInvest</code></li>
		<li>Pour lancer l'algorithme bruteforce<code>python bruteforce.py</code></li>
		<li>Pour lancer l'algorithme optimisé<code>python optimized_v1.py</code></li>
		<li>Pour changer la liste d'actions/datasets : <br>
			1.Ouvrir le fichier optimized_v1.py<br>
			2.Modifier la variable filename ligne 84 avec le bon filename<br>
		</li>
	</ul>
</body>
</html>