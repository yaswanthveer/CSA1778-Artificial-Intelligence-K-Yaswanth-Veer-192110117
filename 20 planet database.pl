% Facts
planet(mercury, 0.39, 0, rocky).
planet(venus, 0.72, 0, rocky).
planet(earth, 1.0, 1, rocky).
planet(mars, 1.52, 2, rocky).
planet(jupiter, 5.2, 79, gas_giant).
planet(saturn, 9.58, 83, gas_giant).
planet(uranus, 19.22, 27, ice_giant).
planet(neptune, 30.05, 14, ice_giant).

% Rules
has_moons(Planet) :-
    planet(Planet, _, Moons, _),
    Moons > 0.

gas_giant(Planet) :-
    planet(Planet, _, _, gas_giant).

rocky_planet(Planet) :-
    planet(Planet, _, _, rocky).

ice_giant(Planet) :-
    planet(Planet, _, _, ice_giant).
