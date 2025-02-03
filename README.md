# Define TPO in residue_constants.py 

Essential Changes:

Add TPO to chi_angles_atoms (✓ already done)
```
chi_angles_atoms = {
    # ... other residues ...
    'TPO': [['N', 'CA', 'CB', 'OG1'],  # Chi1 - same as THR
            ['CA', 'CB', 'OG1', 'P']],  # Chi2 - new rotation around OG1-P bond
    # ... other residues ...
}
```

Add TPO to chi_angles_mask (✓ already done)
```
chi_angles_mask = [
    # ... other residues ...
    [1.0, 1.0, 0.0, 0.0],  # TPO - has two chi angles (Chi1 and Chi2)
    # ... other residues ...
]
```

Add TPO to chi_pi_periodic (✓ already done)
```
chi_pi_periodic = [
    # ... other residues ...
    [0.0, 0.0, 0.0, 0.0],  # TPO - neither chi1 nor chi2 are pi periodic
    # ... other residues ...
]
```
Add TPO to rigid_group_atom_positions (✓ already done)
```
rigid_group_atom_positions = {
    # ... other residues ...
    'TPO': [
        ['N', 0, (-0.517, 1.364, 0.000)],
        ['CA', 0, (0.000, 0.000, 0.000)],
        ['C', 0, (1.526, 0.000, -0.000)],
        ['CB', 0, (-0.516, -0.793, -1.215)],
        ['O', 3, (0.626, 1.062, 0.000)],
        ['CG2', 4, (0.550, -0.718, -1.228)],
        ['OG1', 4, (0.472, 1.353, 0.000)],
        ['P', 5, (0.755, 1.093, 0.000)],       # New phosphate group atoms
        ['O1P', 5, (0.607, 1.095, -0.000)],    # in the 5th rigid group
        ['O2P', 5, (0.589, -1.104, -0.001)],
        ['O3P', 5, (0.634, 1.060, 0.000)],
    ],
    # ... other residues ...
}
```
Add TPO to residue_atoms (✓ already done)
```
residue_atoms = {
    # ... other residues ...
    'TPO': ['C', 'CA', 'CB', 'CG2', 'N', 'O', 'OG1', 'P', 'O1P', 'O2P', 'O3P'],
    # ... other residues ...
}
```
Update atom_types to include P, O1P, O2P, O3P atoms (✓ already done)
```
atom_types = [
    'N', 'CA', 'C', 'CB', 'O', 'CG', 'CG1', 'CG2', 'OG', 'OG1', 'SG', 'CD',
    'CD1', 'CD2', 'ND1', 'ND2', 'OD1', 'OD2', 'SD', 'CE', 'CE1', 'CE2', 'CE3',
    'NE', 'NE1', 'NE2', 'OE1', 'OE2', 'CH2', 'NH1', 'NH2', 'OH', 'CZ', 'CZ2',
    'CZ3', 'NZ', 'OXT', 'P', 'O1P', 'O2P', 'O3P'  # Added phosphate atoms
]
atom_order = {atom_type: i for i, atom_type in enumerate(atom_types)}
atom_type_num = len(atom_types)
```
Update restype mappings (✓ already done)
```
restypes = [
    'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P',
    'S', 'T', 'W', 'Y', 'V', 'J'  # J for TPO
]
restype_order = {restype: i for i, restype in enumerate(restypes)}
restype_num = len(restypes)  # := 21
unk_restype_index = restype_num  # Catch-all index for unknown restypes
```

Add TPO to restype_name_to_atom14_names (✓ already done) 
```
restype_name_to_atom14_names = {
    # ... (existing entries)
    'TPO': ['N', 'CA', 'C', 'O', 'CB', 'OG1', 'CG2', 'P', 'O1P', 'O2P', 'O3P', '', '', ''],
    # ... (rest of existing entries)
}
```
Add TPO to restype_1to3 (which by extension adds it to restype_3to1 mappings (✓ already done)
```
restype_1to3 = {
    'A': 'ALA',
    # ... (existing mappings)
    'V': 'VAL',
    'X': 'TPO',  # Map X to TPO
}

restype_3to1 = {v: k for k, v in restype_1to3.items()}
```
Add van_der_waals_radius for P atom (✓ already done)
```
van_der_waals_radius = {
    'C': 1.7,
    'N': 1.55,
    'O': 1.52,
    'S': 1.8,
    'P': 1.8,  # Phosphorus has similar vdW radius to Sulfur
}
```

# Data Files:
Updated stereo_chemical_props.txt to include TPO bond lengths and angles
```
Bond
C-O			TPO		1.229		0.019
CA-CB			TPO		1.529		0.026
CB-OG1			TPO		1.428		0.020
CB-CG2			TPO		1.519		0.033
N-CA			TPO		1.459		0.020
CA-C			TPO		1.525		0.026
C-O			TPO		1.229		0.019
OG1-P			TPO		1.428		0.020
P-O1P			TPO		1.485		0.033
P-O2P			TPO		1.485		0.020
P-O3P			TPO		1.485		0.026
```
```
Angle        Residue     Mean    StdDev
N-CA-CB      TPO         110.3   1.9
CB-CA-C      TPO         111.6   2.7
CA-CB-OG1    TPO         109.0   2.1
CA-CB-CG2    TPO         112.4   1.4
OG1-CB-CG2   TPO         110.0   2.3
N-CA-C       TPO         111.0   2.7
CA-C-O       TPO         120.1   2.1
```
```
CB-OG1-P			TPO		120.5		2.0
OG1-P-O1P			TPO		108.2		2.0
OG1-P-O2P		TPO		108.2		2.0
OG1-P-O3P		TPO		108.2		2.0
O1P-P-O2P		TPO		119.6		2.0
O2P-P-O3P		TPO		119.6		2.0
O1P-P-O3P		TPO		119.6		2.0
```


# TRAIN  ( unfinished, CUDA requirements from my 4070 clashing with old packages )



#Start fresh
```
conda deactivate
conda env remove -n unifolds
conda create -n unifolds python=3.8.10 -y
conda activate unifolds
```
#Install numpy first at exact version
```
pip install numpy==1.19.5
```
#Install JAX ecosystem in order
```
pip install jaxlib==0.1.67+cuda111 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
pip install jax==0.2.14
pip install dm-tree==0.1.6
pip install toolz>=0.9.0
pip install chex==0.0.7
pip install dm-haiku==0.0.4
pip install jmp==0.0.2
```
#Install remaining dependencies
```
pip install tensorflow-cpu==2.5.3
pip install scipy==1.7.0
pip install biopython==1.79
pip install absl-py==0.13.0
pip install docker==5.0.0
pip install immutabledict==2.0.0
pip install ml-collections==0.1.0
```
#Install conda packages
```
conda install -y -c conda-forge openmm=7.5.1 pdbfixer cudatoolkit=11.1
conda install -y -c bioconda hmmer hhsuite==3.3.0 kalign2
conda install -y -c nvidia cudnn==8.0.4
```















