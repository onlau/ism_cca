import argparse
import cupy as cp
from src.distributions import distributions as d
from src.automaton.automaton import automaton, update_automaton
from src.utils.plotters import plot_ion_fraction, draw_animation, update_then_draw
from src.mappings.mappings import param_map
from src.utils.setuputils import setup_params as params

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--animate", action="store_true", help="Piirrä animaatio")
    parser.add_argument("-p", "--plot", action="store_true", help="Piirrä kuvaaja")
    parser.add_argument("-d", "--draw", action="store_true", help="Piirrä kuva")
    parser.add_argument("-f", "--filament", action="store_true", help='''
    Valitse filamenttijakauma distributions.py-tiedostosta \
    Arvo hydrogen_density jätetään huomiotta jos jakauma on valittu.''')
    parser.add_argument("-i", "--isotropic", action="store_true", help='''
    Valitse isotrooppinen homogeeninen jakauma distributions.py-tiedostosta \
    Arvo hydrogen_density jätetään huomiotta jos jakauma on valittu.''')
    args = parser.parse_args()
    
    if args.filament:
        d.filament(automaton[0])
        params[[param_map["timestep"]]] = 0.09 * 31556995200e0 / cp.mean(automaton[0])
    elif args.isotropic:
        d.isotropic_from_center(automaton[0])
        params[[param_map["timestep"]]] = 0.09 * 31556995200e0 / cp.mean(automaton[0])

    if args.animate:
        draw_animation(automaton, update_automaton)
    elif args.plot:
        plot_ion_fraction(automaton, update_automaton)
    elif args.draw:
        update_then_draw(automaton, update_automaton)
    else:
        return 0


if __name__ == "__main__":
    main()

