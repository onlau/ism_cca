# HII-alueiden mallinnus
Malli tuottaa etäisyys-ionisaatioaste-kuvaajan, jossa punainen viiva on Strömgrenin säde.
Alustusparametrit annettava config.json-tiedostossa cgs-yksiköissä (lämpötilat absoluuttisella asteikolla).

## **Parametrit:**
- timestep - aika-askelen pituus
- n - simulaatiossa suoritettavien aika-askelten määrä
- cell_edge - yhden solun reunan pituus
- stellar_surf_temp - tähden pintalämpötila
- stellar_radius - tähden säde
- hydrogen_density - vedyn hiukkastiheys
- grid_edge - koko ruudukon sivun pituus soluina

## **Lataus, ja asennus**
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
