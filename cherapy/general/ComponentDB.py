from collections import namedtuple

__all__ = ('Elements', 'Components')

Elem = namedtuple('Elem', ['symbol', 'name', 'MW'])
Comp = namedtuple('Comp', ['symbol', 'name', 'elems'])

Elements = (
    Elem('C', 'Carbon', 12),
    Elem('H', 'Hydrogen', 1),
    Elem('O', 'Oxygen', 16),
)

Components = (
    Comp('CH4', 'methane', {'C':1, 'H':4}),
    Comp('H2', 'hydrogen', {'H':2}),
    Comp('H2O', 'water', {'H':2,'O':1}),
    Comp('CO2', 'carbon dioxide', {'C':1, 'O':2}),
    Comp('CO', 'carbon monoxide', {'C':1, 'O':1}),
    Comp('O2', 'carbon monoxide', {'O':2}),
)

