# HII-alueiden mallinnus
Alustusparametrit annettava config.json-tiedostossa cgs-yksiköissä (lämpötilat absoluuttisella asteikolla).

## **Parametrit:**
- n - kuvaajaa piirrettäessä suoritettavien aika-askelten määrä
- cell_edge - yhden solun reunan pituus
- stellar_surf_temp - tähden pintalämpötila
- stellar_radius - tähden säde
- hydrogen_density - vedyn hiukkastiheys

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
suorittaa simulaatiota n aika-askelen verran ja piirtää kuvat ionisaatioasteesta ja hiukkastiheydestä.

`-i` ja `-f` simuloivat isotrooppista epähomogeenista jakaumaa ja filamentin sisällä sijaitsevan tähden aikaansaamaa jakaumaa.