# Proste Planowanie
<p> Aplikacja webowa przeznaczona dla nauczycieli do tworzenia planu zajęć lekcyjnych dla szkół bądź uczelni.</p>
<p>Aplikacja ma służyć jako narzędzie do zarządzania nauczycielami, zajęciami lekcyjnymi, klasami uczniów i salami 
oraz na podstawie tych zasobów do układania planów zajęć.</p>
<h2>Struktura projektu</h2>
<p>Projekt został napisany w języku Python w wersji 3.7 z użyciem frameworku Django w wersji 2.1.3.</p>
<p>Do zarządzania paczkami zostało wykorzystane narzędzie pipenv. 
Więcaj na temat pipenv'a: https://github.com/pypa/pipenv</p>
<h2>Kroki niezbędne do zaczęcia pracy z projektem.</h2>
<p>Do pracy z projektem będzie potrzebny zainstalowany Python najlepiej w wersji 3.7 
oraz zainstalowane narzędzie pipenv, które możemy zainstalować poprzez wpisanie:
pip install pipenv w konsoli (posiadając już zainstalowanego Pythona).</p>
<p>Kolejnymi krokami będzie następująca sekwencja poleceń w konsoli:</p>
<ul>
<li>cd (wybrany folder na zapisanie projektu na dysku)</li>
<li>git clone https://github.com/kacperpabian/easy-planning.git</li>
<li>cd easy-planning</li>
<li>pipenv install</li>
</ul>
<p>Powyższe komendy zainstalują projekt w wybranym przez nas folderze oraz ściągną wszystkie paczki potrzebne 
do pracy w nim</p>
<p>Do uruchomienia projektu wystarczy wejść do folderu projektu, po czym wpisać:</p>
<p>pipenv run python manage.py runserver</p>
<p>Powinniśmy teraz móc wejść do aplikacji poprzez wpisanie localhost:8000 w przeglądarce.</p>

