# magyar


## Magyar listák gyűjteménye - Collection of Hungarian lists.

Az alábbi listákat találod :
1. vezetéknevek   =  magyar.vezeteknev
2. női keresztnevek  = magyar.keresztnev_n
3. férfi keresztnevek = magyar.keresztnev_f
4. utcanevek = magyar.utca
5. telelpülésnevek= magyar.telepules
6. vármegyék nevei = magyar.megye
7. folyók nevei = magyar.folyo
8. a hét napjai = magyar.nap
9. az év hónapjai = magyar.honap
10. gyümölcsok = magyar.gyumolcs
11. zöldségek = magyar.zoldseg
12. haszonállatok = magyar.haszonallat
13. vadallatok Magyarországon = magyar.vadallat
14. Magyarország halai = magyar.hal
15. Magyarország madarai = magyar.madar

## Szótárak  (dictionary): 
1. Királyok és uralkodásuk ideje  = magyar.kiraly
2. Vármegyék és azok székhelyei = magyar.megye_szekhely
3. Járások, székhelyük , megye = magyar.jaras

## Description
1. last names =  magyar.vezeteknev
2. female first names = magyar.keresztnev_n
3. male first names  = magyar.keresztnev_f
4. street names = magyar.utca
5. city names = magyar.telepules
6. names of counties = magyar.megye
7. names of rivers = magyar.folyo
8. he days of the week = magyar.nap
9. the months of the year = magyar.honap
10. fruits = magyar.gyumolcs
11. vegetables = magyar.zoldseg
12. domesticated animals = magyar.haszonallat
13. hungarian wildlife  = magyar.vadallat
14. Fishes of Hungary = magyar.hal
15. Birds of Hungary = magyar.madar

Dictionary:
1. Hungarian Kings and Reigns = magyar.kiraly
2. Hungarian counties and their administrative centers = magyar.megye_szekhely
3. Hungarian districts, their seats, county = magyar.jaras

## Listák használat:

 Főként véletlengenerátorok kiegészítőjeként ajánlom a listákat
 
I recommend it mainly as a supplement to random number generators. 
       
            random.sample()
            utca = random.sample(magyar.utca, k=16) 
            random.choices()
            telepulesek = random.choice(magyar.telepules)

## Szótárak:
Több adatot tartalmaznak összekapcsolva.

magyar.kiraly tartalma :   {'király neve' : (uralkodása tól, ig)}
magyar.megye_szekhely :    {'megye neve' : 'székhelye'}
magyar.jaras :             {'megye' : (székhely, megye)}




## Szerző

* Név: Nagy BÉLa
* E-mail:nagy.bela.budapest@gmail.com

## Licenc

Oktatási célra készült, szabadon használható