# Define TPO in residue_constants.py 

Essential Changes:

Add TPO to chi_angles_atoms (✓ already done)
Add TPO to chi_angles_mask (✓ already done)
Add TPO to chi_pi_periodic (✓ already done)
Add TPO to rigid_group_atom_positions (✓ already done)
Add TPO to residue_atoms (✓ already done)
Update atom_types to include P, O1P, O2P, O3P atoms (✓ already done)
```atom_types = [
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
    'S', 'T', 'W', 'Y', 'V', 'X'  # X for TPO
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

Data Files:
Updated stereo_chemical_props.txt to include TPO bond lengths and angles




# TRAIN  ( unfinished, CUDA requirements from my 4070 clashing with old packages )



#Start fresh
conda deactivate
conda env remove -n unifolds
conda create -n unifolds python=3.8.10 -y
conda activate unifolds

#Install numpy first at exact version
pip install numpy==1.19.5

#Install JAX ecosystem in order
pip install jaxlib==0.1.67+cuda111 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
pip install jax==0.2.14
pip install dm-tree==0.1.6
pip install toolz>=0.9.0
pip install chex==0.0.7
pip install dm-haiku==0.0.4
pip install jmp==0.0.2

#Install remaining dependencies
pip install tensorflow-cpu==2.5.3
pip install scipy==1.7.0
pip install biopython==1.79
pip install absl-py==0.13.0
pip install docker==5.0.0
pip install immutabledict==2.0.0
pip install ml-collections==0.1.0

#Install conda packages
conda install -y -c conda-forge openmm=7.5.1 pdbfixer cudatoolkit=11.1
conda install -y -c bioconda hmmer hhsuite==3.3.0 kalign2
conda install -y -c nvidia cudnn==8.0.4
















