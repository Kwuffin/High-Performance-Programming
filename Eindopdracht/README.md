# Toelichting:
Mijn sequentiele zeef gebruikt booleans, en is compleet anders geimplementeerd dan mijn MPI versie. Daarom vind ik dat ik dat ik de twee versies niet echt kan vergelijken, omdat ze op een compleet andere manier het probleem aanpakken. Mijn sequentiele versie is veel sneller dan mijn MP versie. De sequentiele versie doet er ruim 9 seconden over om 1 miljard waardes te checken. De MP versie, doet er nog 20 seconden over om 1 miljoen te tellen.

## How to run
Run het programma met `mpiexec -n <aantal nodes> python3 zeef.py`