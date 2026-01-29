


import numpy as np



def euler_angles_from_SAXIS(sx,sy,sz):
    alpha = np.atan2(sy, sx)
    beta = np.atan2(np.sqrt((sx**2)+(sy**2)), sz)
    return alpha, beta

def rotation_matrix(alpha, beta):
    R_alpha_z = np.array([[np.cos(alpha), -np.sin(alpha), 0],[np.sin(alpha), np.cos(alpha), 0],[0, 0, 1]])
    R_beta_y = np.array([[np.cos(beta), 0, np.sin(beta)],[0, 1, 0],[-np.sin(beta), 0, np.cos(beta)]])
    return R_alpha_z, R_beta_y

def from_cartesian_to_spinor(R_alpha_z, R_beta_y):
    inv_R_alpha_z = np.linalg.inv(R_alpha_z)
    inv_R_beta_y =  np.linalg.inv(R_beta_y)
    T = inv_R_beta_y @  inv_R_alpha_z
    return T

def from_spinor_to_cartesian(R_alpha_z, R_beta_y):
    T = R_alpha_z @ R_beta_y
    return T


# Choice 1
# choose some SAXIS below.
sx, sy, sz = 1, 2, 1
alpha, beta = euler_angles_from_SAXIS(sx,sy,sz)
print(f"alpha {alpha:.6f} radian and beta {beta:.6f} radian")

R_alpha_z, R_beta_y = rotation_matrix(alpha, beta)
print(f"Rotation Matrix: R_z {R_alpha_z}")
print(f"Rotation Matrix: R_y {R_beta_y}")

T1 = from_spinor_to_cartesian(R_alpha_z, R_beta_y)
T2 = from_cartesian_to_spinor(R_alpha_z, R_beta_y)

# print(T1)
# print(T2)

m=5
# taking a test vector(magmom) along z-axis.
spinor_test_magmom = np.array([0,0,m])

spinor_in_cartesian = T1 @ spinor_test_magmom
print(f"Verification (Transforming {spinor_in_cartesian}):")
# test vector is now rotated along 111. instead of 001.
print(spinor_in_cartesian / np.linalg.norm(spinor_in_cartesian))

#############################################
#Choice 2:
#FIX SAXIS along (0,0,m) direction (above in Choice 1)
# change MAGMOM VECTOR accordingly.
sx, sy, sz = 0, 0, 1
alpha, beta = euler_angles_from_SAXIS(sx,sy,sz)
# print(f"alpha {alpha:.6f} radian and beta {beta:.6f} radian")
R_alpha_z, R_beta_y = rotation_matrix(alpha, beta)
# print(f"Rotation Matrix: R_z {R_alpha_z}")
# print(f"Rotation Matrix: R_y {R_beta_y}")
T1 = from_spinor_to_cartesian(R_alpha_z, R_beta_y)
T2 = from_cartesian_to_spinor(R_alpha_z, R_beta_y)

# choose this vector.
spinor_in_cartesian = np.array([1,2,1])
spinor_in_cartesian = T1 @ spinor_in_cartesian
print(f"Verification (Transforming {spinor_in_cartesian}):")
print(spinor_in_cartesian / np.linalg.norm(spinor_in_cartesian))
