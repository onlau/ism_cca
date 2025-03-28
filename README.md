# HII-alueiden mallinnus
Alustusparametrit annettava config.json-tiedostossa cgs-yksiköissä (lämpötilat absoluuttisella asteikolla).

## **Parametrit:**
- timestep - aika-askelen pituus
- n - kuvaajaa piirrettäessä suoritettavien aika-askelten määrä
- cell_edge - yhden solun reunan pituus
- stellar_surf_temp - tähden pintalämpötila
- stellar_radius - tähden säde
- hydrogen_density - vedyn hiukkastiheys
- grid_edge - koko ruudukon sivun pituus soluina

## **Lataus, ja asennus (gpu)**
Vaaditaan python 3.7 tai uudempi ja cuda-yhteensopiva grafiikkasuoritin (https://developer.nvidia.com/cuda-gpus).

Repositorion kloonaus ja riippuvuuksien asennus:
```
git clone https://github.com//onlau/ism_cca
cd ism_cca/ism_gpu
pip install -r dependencies.txt
```
Lisäksi erikseen asennettava cuda toolkit (https://developer.nvidia.com/cuda-toolkit) ja cupy (https://docs.cupy.dev/en/stable/install.html).

Suoritus:
```
python3 main.py --animate
```
piirtää animaation.
```
python3 main.py --plot
```
piirtää kuvaajan.
```
python3 main.py --draw
```
suorittaa simulaatiota n aika-askelen verran ja piirtää kuvan alueesta.

Simulaatio on hyvin herkkä aika-askelen pituudelle, sopiva pituus näyttäisi riippuvan lähinnä vedyn hiukkastiheydestä. Siksi cpu-versiossa mukana olleet timestep ja cell_edge - parametrit on poistettu config.json-tiedostosta, ne skaalataan nyt automaattisesti ohjelman sisällä. Punainen viiva kuvaajissa on Strömgrenin säde.

## **Lataus, ja asennus (cpu, VANHENTUNUT)**
Vaaditaan python 3.7 tai uudempi.

Repositorion kloonaus ja riippuvuuksien asennus:
```
git clone https://github.com//onlau/ism_cca
cd ism_cca/ism_cpu
pip install -r dependencies.txt
```
Suoritus:
```
python3 main.py
```
