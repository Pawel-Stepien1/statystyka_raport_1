import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns
from scipy.stats import norm
from scipy.stats import gaussian_kde

#################################################################################### LATA 1970-1974 ####################################################################################

#################################################
### Pozyskanie danych o złocie lata 2016-2018 ###
#################################################

# Lista cen złota 2016-2018
lista_cen_złota_2016_do_2018 = [None] * 751

# Lista z datami cen złota 2016-2018
lista_dat_złoto_2016_do_2018 = [None] * 751

# Odczytanie danych
with open('gold_price.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    for _ in range(12141):
        next(reader)
    
    for i in range(751):
        row = next(reader)
        if row[1]:
            # Zapisanie danych.
            lista_cen_złota_2016_do_2018[i] = float(row[1])
            lista_dat_złoto_2016_do_2018[i] = row[0]
        if row[0]== '2018-12-28':
            break

##################################################
### Pozyskanie danych o srebrze lata 2016-2018 ###
##################################################

# Lista cen srebra 2016-2018
lista_cen_srebra_2016_do_2018 = [None] * 751

# Lista z datami cen srebra 2016-2018
lista_dat_srebro_2016_do_2018 = [None] * 751

# Odczytanie danych
with open('silver_price.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    for _ in range(12141):
        next(reader)
    
    for i in range(751):
        row = next(reader)
        if row[1]:
            # Zapisanie danych.
            lista_cen_srebra_2016_do_2018[i] = float(row[1])
            lista_dat_srebro_2016_do_2018[i] = row[0]
        if row[0]== '2018-12-28':
            break

# usuwanie None.
lista_cen_złota_2016_do_2018 = list(filter(lambda x: x is not None, lista_cen_złota_2016_do_2018))
lista_cen_srebra_2016_do_2018 = list(filter(lambda x: x is not None, lista_cen_srebra_2016_do_2018))
lista_dat_złoto_2016_do_2018 = list(filter(lambda x: x is not None, lista_dat_złoto_2016_do_2018))
lista_dat_srebro_2016_do_2018 = list(filter(lambda x: x is not None, lista_dat_srebro_2016_do_2018))

##################################################
###                 Wykresy                    ###
##################################################

# Pokazanie danych złota od 2016 do 2018.
plt.plot(lista_dat_złoto_2016_do_2018, lista_cen_złota_2016_do_2018)
xticks_indices_złoto_2016_do_2018 = lista_dat_złoto_2016_do_2018[:(len(lista_dat_złoto_2016_do_2018)-70):90]
xticks_indices_złoto_2016_do_2018.append(lista_dat_złoto_2016_do_2018[-1])
plt.xticks(xticks_indices_złoto_2016_do_2018, rotation=45)
#plt.xticks(range(0, len(lista_dat_złoto_1970_do_1974), 50),rotation='vertical')
plt.title('Wykres ceny (USD) złota za uncję od 04.01.2016 r. do 28.12.2018 r.')
plt.xlabel('Data')
plt.ylabel('Cena (USD) złota za uncję')
plt.grid(True)
plt.show()

# Pokazanie danych srebra od 2016 do 2018.
plt.plot(lista_dat_srebro_2016_do_2018, lista_cen_srebra_2016_do_2018)
xticks_indices_srebro_2016_do_2018 = lista_dat_srebro_2016_do_2018[:(len(lista_dat_srebro_2016_do_2018)-70):90]
xticks_indices_srebro_2016_do_2018.append(lista_dat_srebro_2016_do_2018[-1])
plt.xticks(xticks_indices_srebro_2016_do_2018, rotation=45)
#plt.xticks(range(0, len(lista_dat_złoto_1970_do_1974), 50),rotation='vertical')
plt.title('Wykres ceny (USD) srebra za uncję od 04.01.2016 r. do 28.12.2018 r.')
plt.xlabel('Data')
plt.ylabel('Cena (USD) srebra za uncję')
plt.grid(True)
plt.show()

##################################################
###                 Boxplot                    ###
##################################################
# Tworzenie boxplotu dla złota od 2016 do 2018
plt.boxplot(lista_cen_złota_2016_do_2018)
plt.title('Wykres pudełkowy cen (USD) złota za uncję \nod 04.01.2016 r. do 28.12.2018 r.')
plt.ylabel('Cena (USD) złota za uncję')
plt.xticks([1],['od 04.01.2016 r. do 28.12.2018 r.'])
plt.grid(True)
plt.show()

# Tworzenie boxplotu dla srebra od 2016 do 2018
plt.boxplot(lista_cen_srebra_2016_do_2018)
plt.title('Wykres pudełkowy cen (USD) srebra za uncję \nod 04.01.2016 r. do 28.12.2018 r.')
plt.ylabel('Cena (USD) srebra za uncję')
plt.xticks([1],['od 04.01.2016 r. do 28.12.2018 r.'])
plt.grid(True)
plt.show()

##################################################
###             Dystrybuanta empiryczna        ###
##################################################

######### Złoto 2016-2018 #########
# Estymacja parametrów rozkładu normalnego
mu_złota_2016_do_2018, sigma_złota_2016_do_2018 = np.mean(lista_cen_złota_2016_do_2018), np.std(lista_cen_złota_2016_do_2018)
# Sortowanie danych
Posortowa_lista_cen_złota_2016_do_2018 = np.sort(lista_cen_złota_2016_do_2018)

# Obliczanie dystrybuanty
długość_lista_cen_złota_2016_do_2018 = len(Posortowa_lista_cen_złota_2016_do_2018)
dystrybuanta_empiryczna_lista_cen_złota_2016_do_2018= np.arange(1, długość_lista_cen_złota_2016_do_2018 + 1) / długość_lista_cen_złota_2016_do_2018
# Generowanie teoretycznej dystrybuanty rozkładu normalnego
theoretical_cdf_lista_cen_złota_2016_do_2018 = norm.cdf(Posortowa_lista_cen_złota_2016_do_2018, mu_złota_2016_do_2018, sigma_złota_2016_do_2018)

# Wykres dystrybuanty
plt.plot(Posortowa_lista_cen_złota_2016_do_2018, dystrybuanta_empiryczna_lista_cen_złota_2016_do_2018, marker='.', linestyle='none', label = 'Empiryczna dystrybuanta cen (USD) złota za uncję \nod 04.01.2016 r. do 28.12.2018 r.')
plt.plot(Posortowa_lista_cen_złota_2016_do_2018, theoretical_cdf_lista_cen_złota_2016_do_2018, label = 'Teoretyczna dystrybuanta rozkładu normalnego')
plt.title('Porównanie empirycznej dystrybuanty cen (USD) złota za uncję \nod 04.01.2016 r. do 28.12.2018 r. \nz teoretyczną dystrybuantą rozkładu normalnego')
plt.xlabel('Cena (USD) złota za uncję')
plt.ylabel('Prawdopodobieństwo')
plt.legend(loc='best', fontsize='small')
plt.grid(True)
plt.show()

######### Srebro 2016-2018 #########
# Sortowanie danych
Posortowa_lista_cen_srebra_2016_do_2018 = np.sort(lista_cen_srebra_2016_do_2018)
# Estymacja parametrów rozkładu normalnego
mu_srebra_2016_do_2018, sigma_srebra_2016_do_2018 = np.mean(lista_cen_srebra_2016_do_2018), np.std(lista_cen_srebra_2016_do_2018)

# Obliczanie dystrybuanty
długość_lista_cen_srebra_2016_do_2018 = len(Posortowa_lista_cen_srebra_2016_do_2018)
dystrybuanta_empiryczna_lista_cen_srebra_2016_do_2018= np.arange(1, długość_lista_cen_srebra_2016_do_2018 + 1) / długość_lista_cen_srebra_2016_do_2018
# Generowanie teoretycznej dystrybuanty rozkładu normalnego
theoretical_cdf_lista_cen_srebra_2016_do_2018 = norm.cdf(Posortowa_lista_cen_srebra_2016_do_2018, mu_srebra_2016_do_2018, sigma_srebra_2016_do_2018)

# Wykres dystrybuanty
plt.plot(Posortowa_lista_cen_srebra_2016_do_2018, dystrybuanta_empiryczna_lista_cen_srebra_2016_do_2018, marker='.', linestyle='none', label = 'Empiryczna dystrybuanta cen (USD) srebra za uncję \nod 04.01.2016 r. do 28.12.2018 r.')
plt.plot(Posortowa_lista_cen_srebra_2016_do_2018, theoretical_cdf_lista_cen_srebra_2016_do_2018, label = 'Teoretyczna dystrybuanta rozkładu normalnego')
plt.title('Porównanie empirycznej dystrybuanty cen (USD) srebra za uncję \nod 04.01.2016 r. do 28.12.2018 r. \nz teoretyczną dystrybuantą rozkładu normalnego')
plt.xlabel('Cena (USD) srebra za uncję')
plt.ylabel('Prawdopodobieństwo')
plt.legend(loc='upper left', fontsize='small')
plt.grid(True)
plt.show()

##################################################
###             Gęstość empiryczna             ###
##################################################
##################################################
###                 Histogramy                 ###
##################################################

######### Złoto 2016-2018 #########

# Tworzenie histogramu
#plt.hist(lista_cen_złota_2016_do_2018, bins=30, color='skyblue', edgecolor='black', density = True)

# Obliczanie średniej i odchylenia standardowego Twoich danych
mu_złota_2016_do_2018 = np.mean(lista_cen_złota_2016_do_2018)
sigma_złota_2016_do_2018 = np.std(lista_cen_złota_2016_do_2018)

# Tworzenie histogramu
count, bins, ignored = plt.hist(lista_cen_złota_2016_do_2018, 20, density=True)

# Dodawanie krzywej dopasowania (PDF rozkładu normalnego)
plt.plot(bins, 1/(sigma_złota_2016_do_2018 * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu_złota_2016_do_2018)**2 / (2 * sigma_złota_2016_do_2018**2) ),
         linewidth=2, color='r')

# Dodawanie gęstości teoretycznej rozkładu normalnego
x = np.linspace(min(lista_cen_złota_2016_do_2018), max(lista_cen_złota_2016_do_2018), 1000)
mu, sigma = norm.fit(lista_cen_złota_2016_do_2018)
pdf_normal = norm.pdf(x, mu, sigma)
plt.plot(x, pdf_normal, linestyle='--', color='green', label='Gęstość teoretyczna (normalny)')
# Dodanie tytułu i etykiet osi
plt.title('Histogram cen złota')
plt.xlabel('Cena złota (USD)')
plt.ylabel('Liczba obserwacji')

# Wyświetlenie histogramu
plt.show()

################################################################################################################################
# Obliczanie histogramu
data = lista_cen_złota_2016_do_2018
count, bins, ignored = plt.hist(data, 10, density=True, alpha=0.5, color='blue', edgecolor='black')

# Dodawanie krzywej estymowanej gęstości
kde = gaussian_kde(data)
x = np.linspace(min(data), max(data), 1000)
plt.plot(x, kde(x), linewidth=2, color='red', label='Gęstość empiryczna')

# Dodawanie gęstości teoretycznej rozkładu normalnego
mu, sigma = norm.fit(data)
pdf_normal = norm.pdf(x, mu, sigma)
plt.plot(x, pdf_normal, linestyle='--', color='green', label='Gęstość teoretyczna (normalny)')

# Dodatkowe etykiety
plt.title('Histogram i gęstość empiryczna Twoich danych')
plt.xlabel('Wartość')
plt.ylabel('Gęstość')
plt.legend()

plt.show()

######### Srebro 2016-2018 #########

# Obliczanie średniej i odchylenia standardowego Twoich danych
mu_srebra_2016_do_2018 = np.mean(lista_cen_srebra_2016_do_2018)
sigma_srebra_2016_do_2018 = np.std(lista_cen_srebra_2016_do_2018)

# Tworzenie histogramu
count, bins, ignored = plt.hist(lista_cen_srebra_2016_do_2018, 20, density=True)

# Dodawanie krzywej dopasowania (PDF rozkładu normalnego)
plt.plot(bins, 1/(sigma_srebra_2016_do_2018 * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu_srebra_2016_do_2018)**2 / (2 * sigma_srebra_2016_do_2018**2) ),
         linewidth=2, color='r')

# Dodawanie gęstości teoretycznej rozkładu normalnego
x = np.linspace(min(lista_cen_srebra_2016_do_2018), max(lista_cen_srebra_2016_do_2018), 1000)
mu, sigma = norm.fit(lista_cen_srebra_2016_do_2018)
pdf_normal = norm.pdf(x, mu, sigma)
plt.plot(x, pdf_normal, linestyle='--', color='green', label='Gęstość teoretyczna (normalny)')
# Dodanie tytułu i etykiet osi
plt.title('Histogram cen złota')
plt.xlabel('Cena złota (USD)')
plt.ylabel('Liczba obserwacji')

# Wyświetlenie histogramu
plt.show()

# Obliczanie histogramu
data = lista_cen_srebra_2016_do_2018
count, bins, ignored = plt.hist(data, 10, density=True, alpha=0.5, color='blue', edgecolor='black')

# Dodawanie krzywej estymowanej gęstości
kde = gaussian_kde(data)
x = np.linspace(min(data), max(data), 1000)
plt.plot(x, kde(x), linewidth=2, color='red', label='Gęstość empiryczna')

# Dodawanie gęstości teoretycznej rozkładu normalnego
mu, sigma = norm.fit(data)
pdf_normal = norm.pdf(x, mu, sigma)
plt.plot(x, pdf_normal, linestyle='--', color='green', label='Gęstość teoretyczna (normalny)')

# Dodatkowe etykiety
plt.title('Histogram i gęstość empiryczna Twoich danych')
plt.xlabel('Wartość')
plt.ylabel('Gęstość')
plt.legend()

plt.show()

# Obliczanie korelacji Pearsona
correlation = np.corrcoef(lista_cen_złota_2016_do_2018, lista_cen_srebra_2016_do_2018)[0, 1]

##################################################
###         Korelacje,średnie, mediany         ###
##################################################

# Korelacja
print("Korelacja między cenami złota i srebra:", correlation)
# Średnie
średnia_cen_złota_2016_do_2018 = np.mean(lista_cen_złota_2016_do_2018)
średnia_cen_srebra_2016_do_2018 = np.mean(lista_cen_srebra_2016_do_2018)
print("średnia cena złota 2016 do 2018", średnia_cen_złota_2016_do_2018)
print("średnia cena srebra 2016 do 2018", średnia_cen_srebra_2016_do_2018)
#Mediany
mediana_cen_złota_2016_do_2018 = np.median(lista_cen_złota_2016_do_2018)
mediana_cen_srebra_2016_do_2018 = np.median(lista_cen_srebra_2016_do_2018)
print("Mediana cena złota 2016 do 2018:", mediana_cen_złota_2016_do_2018)
print("Mediana cena srebra 2016 do 2018:", mediana_cen_srebra_2016_do_2018)
# Odchylenie standardowe
# Obliczanie odchylenia standardowego
odchylenie_std_cen_złota_2016_do_2018 = np.sqrt(np.mean([(x - średnia_cen_złota_2016_do_2018)**2 for x in lista_cen_złota_2016_do_2018]))
odchylenie_std_cen_srebra_2016_do_2018 = np.sqrt(np.mean([(x - średnia_cen_srebra_2016_do_2018)**2 for x in lista_cen_srebra_2016_do_2018]))
print("Odchylenie standardowe cena złota 2016 do 2018:", odchylenie_std_cen_złota_2016_do_2018)
print("Odchylenie standardowe cena srebra 2016 do 2018:", odchylenie_std_cen_srebra_2016_do_2018)
# Kwartyle
# Obliczenie kwartyla dolnego (Q1)
kwartyl_dolny_cen_złota_2016_do_2018 = np.percentile(lista_cen_złota_2016_do_2018, 25)
kwartyl_dolny_cen_srebra_2016_do_2018 = np.percentile(lista_cen_srebra_2016_do_2018, 25)
# Obliczenie kwartyla górnego (Q3)
kwartyl_gorny_cen_złota_2016_do_2018 = np.percentile(lista_cen_złota_2016_do_2018, 75)
kwartyl_gorny_cen_srebra_2016_do_2018 = np.percentile(lista_cen_srebra_2016_do_2018, 75)

print("Kwartyl dolny cena złota 2016 do 2018 (Q1):", kwartyl_dolny_cen_złota_2016_do_2018)
print("Kwartyl górny cena złota 2016 do 2018(Q3):", kwartyl_gorny_cen_złota_2016_do_2018)

print("Kwartyl dolny cena srebra 2016 do 2018 (Q1):", kwartyl_dolny_cen_srebra_2016_do_2018)
print("Kwartyl górny cena srebra 2016 do 2018(Q3):", kwartyl_gorny_cen_srebra_2016_do_2018)
# Wąsy
# Pobieranie informacji o wykresie
result_lista_cen_złota_2016_do_2018 = plt.boxplot(lista_cen_złota_2016_do_2018, showmeans=True)
plt.show()

# Wyświetlanie kwartyli, wąsów i innych informacji
lower_whisker_cen_złota_2016_do_2018 = result_lista_cen_złota_2016_do_2018['whiskers'][0].get_ydata()[1]
upper_whisker_cen_złota_2016_do_2018 = result_lista_cen_złota_2016_do_2018['whiskers'][1].get_ydata()[1]

print("Dolny wąs cena złota 2016 do 2018:", lower_whisker_cen_złota_2016_do_2018)
print("Górny wąs cena złota 2016 do 2018:", upper_whisker_cen_złota_2016_do_2018)

# Pobieranie informacji o wykresie
result_lista_cen_srebra_2016_do_2018 = plt.boxplot(lista_cen_srebra_2016_do_2018, showmeans=True)
plt.show()
# Wyświetlanie kwartyli, wąsów i innych informacji
lower_whisker_cen_srebra_2016_do_2018 = result_lista_cen_srebra_2016_do_2018['whiskers'][0].get_ydata()[1]
upper_whisker_cen_srebra_2016_do_2018 = result_lista_cen_srebra_2016_do_2018['whiskers'][1].get_ydata()[1]

print("Dolny wąs cena srebra 2016 do 2018:", lower_whisker_cen_srebra_2016_do_2018)
print("Górny wąs cena srebra 2016 do 2018:", upper_whisker_cen_srebra_2016_do_2018)

##################################################
###                 Histogramy                 ###
##################################################
######### Srebro 2016-2018 #########

# Tworzenie histogramu
plt.hist(lista_cen_srebra_2016_do_2018, bins=25, color='skyblue', edgecolor='black', density = True)
# Dodanie tytułu i etykiet osi
sns.kdeplot(lista_cen_srebra_2016_do_2018, color='red', label='Gęstość empiryczna')
# Gęstość teoretyczna rozkładu normalnego
mu, sigma = np.mean(lista_cen_srebra_2016_do_2018), np.std(lista_cen_srebra_2016_do_2018)
x = np.linspace(min(lista_cen_srebra_2016_do_2018), max(lista_cen_srebra_2016_do_2018), 100)
gęstość_2_srebro = norm.pdf(x, mu, sigma)
plt.plot(x, gęstość_2_srebro, color='green', linestyle='--', label='Gęstość teoretyczna \nrozkładu normalnego')
plt.title('Histogram cen (USD) srebra za uncję \nod 04.01.2016 r. do 28.12.2018 r.')
plt.xlabel('Cena srebra (USD) za uncję')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.legend(loc='best')
plt.grid(True)
plt.show()

######### Złoto 2016-2018 #########

# Tworzenie histogramu
plt.hist(lista_cen_złota_2016_do_2018, bins=25, color='skyblue', edgecolor='black', density = True)
sns.kdeplot(lista_cen_złota_2016_do_2018, color='red', label='Gęstość empiryczna')
# Dodanie tytułu i etykiet osi
# Gęstość teoretyczna rozkładu normalnego
mu, sigma = np.mean(lista_cen_złota_2016_do_2018), np.std(lista_cen_złota_2016_do_2018)
x = np.linspace(min(lista_cen_złota_2016_do_2018), max(lista_cen_złota_2016_do_2018), 100)
gęstość_2_złoto = norm.pdf(x, mu, sigma)
plt.plot(x, gęstość_2_złoto, color='green', linestyle='--', label='Gęstość teoretyczna \nrozkładu normalnego')
plt.title('Histogram cen (USD) złota za uncję \nod 04.01.2016 r. do 28.12.2018 r.')
plt.xlabel('Cena złota (USD) za uncję')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.legend(loc='best')
plt.grid(True)
plt.show()

print(lista_dat_złoto_2016_do_2018[-1])
