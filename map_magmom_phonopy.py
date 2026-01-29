from phonopy import Phonopy
from phonopy.interface.vasp import read_vasp

# -----------------------------
# INPUT
# -----------------------------

primitive_poscar = "POSCAR"
supercell_matrix = [[3,0,0],[0,3,0],[0,0,3]]

# if spin-polarized calculations without SOC (Collinear). #For each atomic species: only mz exists in collinear calculations.
primitive_magmoms = [0.348, 0.348, 0.348, -0.009, -0.018, 0.010, 0.010]

# to generate the S-vectors you need another script. Just pasting below for simplicity.
# 0 :  1 0.0 0.0 -0.5 0.8660254 0.0 -0.5 -0.8660254 0.0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
# 30 : 0.8660254 0.0 0.5 -0.4330127 0.75 0.5 -0.4330127 -0.75 0.5  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
# 45 : 0.70710678 0.0 0.70710678 -0.35355339 0.61237244 0.70710678 -0.35355339 -0.61237244 0.70710678 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
# 60 : 0.5 0. 0.8660254 -0.25 0.4330127 0.8660254 -0.25 -0.4330127 0.8660254 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0

# if spin-polarized calculations with SOC (Non-collinear) # For each atomic species: m has three components. (it is spinor) m1, m2, m3 or mx, my, mz
# primitive_magmoms = [[1, 0.0, 0.0], [-0.5, 0.8660254, 0.0], [-0.5, -0.8660254, 0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 0 degree
# primitive_magmoms = [[0.8660254, 0.0, 0.5],[-0.4330127, 0.75, 0.5],[-0.4330127, -0.75, 0.5],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 30 degree 
# primitive_magmoms = [[0.70710678, 0.0, 0.70710678],[-0.35355339, 0.61237244, 0.70710678],[-0.35355339, -0.61237244, 0.70710678],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]  # 45 degree 
primitive_magmoms = [[0.5, 0, 0.8660254],[-0.25, 0.4330127, 0.8660254],[-0.25, -0.4330127, 0.8660254],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]  # 60 degrees


# -----------------------------
# SETUP PHONOPY
# -----------------------------

unitcell = read_vasp(primitive_poscar)
phonon = Phonopy(unitcell, supercell_matrix)
# print(phonon.primitive.scaled_positions)
# print(phonon.supercell.scaled_positions)
print(phonon.supercell.u2s_map)


primitive = phonon.primitive
supercell = phonon.supercell

# -----------------------------
# MAP CONSTRUCTION (CRITICAL)
# -----------------------------

# primitive index → unitcell index
p2p = primitive.p2p_map
print("p2p", p2p)
# unitcell index → primitive index
uc_to_prim = {uc: p for p, uc in enumerate(p2p)}
print("uc_to_prim",uc_to_prim)
# print(p2p)
# supercell → unitcell index
s2uc = primitive.s2p_map
print("s2uc",s2uc)
# -----------------------------
# FINAL MAGMOM MAPPING
# -----------------------------

supercell_magmoms = [
    primitive_magmoms[uc_to_prim[uc]]
    for uc in s2uc
]

# -----------------------------
# OUTPUT
# -----------------------------

print("MAGMOM = ", end="")
for m in supercell_magmoms:
    # print(f"{m:.3f}", end=" ")
    print(f"{m[0]:.3f}",f"{m[1]:.3f}",f"{m[2]:.3f}", end=" \ \n")
print()

'''
print("From here Just testing of Mapping inside supercell space: ")
import numpy as np
N = 8
num_uatom = 7
print(np.arange(7))
print(np.arange(7) * 27)
u2s_map = np.array(np.arange(num_uatom) * N, dtype="int64")
u2u_map = {j: i for i, j in enumerate(u2s_map)}
print("u2s",u2s_map)
print("u2u",u2u_map)
n_l = np.linalg.det(supercell_matrix)
print(n_l)
atom_map = np.repeat(np.arange(num_uatom), n_l)
print(atom_map)
atom_map = np.repeat(np.arange(num_uatom), n_l) * N
print(atom_map)
# _s2u_map = np.array(u2sur_map[sur2s_map] * N, dtype="int64")
'''
