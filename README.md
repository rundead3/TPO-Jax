# Adding TPO

Add TPO as a New Residue Type
We need to extend the residue definitions to include TPO, which is threonine with a phosphate group on OG1.

Residue Representation (Uni-Fold-jax/unifold/common/residue_constants.py)
Atom positions and bonds in (rigid_group_atom_positions)
Chi angles (chi_angles_atoms)
Atom types (residue_atoms)

Bond lengths and angles (unifold/common/stereo_chemical_props.txt)


Feature Generation (unifold/model/tf/protein_features.py )
aatype: One-hot encoding of amino acid types (21 classes)
all_atom_positions: 3D coordinates for each atom
all_atom_mask: Binary mask for atom presence






# In residue_constants.py

##Add TPO to chi angles definition

chi_angles_atoms.update({
    'TPO': [['N', 'CA', 'CB', 'OG1'], ['CA', 'CB', 'OG1', 'P']],
})

##Add TPO atom positions

rigid_group_atom_positions.update({
    'TPO': [
        ['N', 0, (-0.517, 1.364, 0.000)],
        ['CA', 0, (0.000, 0.000, 0.000)],
        ['C', 0, (1.526, 0.000, -0.000)],
        ['CB', 0, (-0.516, -0.793, -1.215)],
        ['O', 3, (0.626, 1.062, 0.000)],
        ['CG2', 4, (0.550, -0.718, -1.228)],
        ['OG1', 4, (0.472, 1.353, 0.000)],
        ['P', 5, (0.000, 1.600, 0.000)],  # Phosphate group
        ['OP1', 5, (0.000, 0.000, 1.500)],  # Phosphate oxygens
        ['OP2', 5, (0.000, 0.000, -1.500)],
        ['OP3', 5, (1.500, 0.000, 0.000)],
    ],
})

##Add TPO to residue atoms

residue_atoms['TPO'] = ['N', 'CA', 'C', 'CB', 'CG2', 'OG1', 'P', 'OP1', 'OP2', 'OP3', 'O']

#Update Feature Generation

In protein_features.py

FEATURES.update({
    "aatype": (tf.float32, [NUM_RES, 22]),  # Increase to 22 to include TPO
    "all_atom_positions": (tf.float32, [NUM_RES, residue_constants.atom_type_num + 4, 3]),  # Add 4 new atoms for phosphate
    "all_atom_mask": (tf.int64, [NUM_RES, residue_constants.atom_type_num + 4]),
})


3.Add Chemical Properties
We need to add TPO's chemical properties to stereo_chemical_props.txt:
Bond            Residue     Mean        StdDev
CA-CB           TPO         1.529       0.026
CB-OG1          TPO         1.428       0.020
CB-CG2          TPO         1.519       0.033
OG1-P           TPO         1.576       0.015  # Phosphate bond
P-OP1           TPO         1.485       0.015
P-OP2           TPO         1.485       0.015
P-OP3           TPO         1.485       0.015
N-CA            TPO         1.459       0.020
CA-C            TPO         1.525       0.026
C-O             TPO         1.229       0.019

Angle           Residue     Mean        StdDev
N-CA-CB         TPO         110.3       1.9
CB-CA-C         TPO         111.6       2.7
CA-CB-OG1       TPO         109.0       2.1
CA-CB-CG2       TPO         112.4       1.4
OG1-CB-CG2      TPO         110.0       2.3
CB-OG1-P        TPO         120.5       2.0
OG1-P-OP1       TPO         109.5       1.0
OG1-P-OP2       TPO         109.5       1.0
OG1-P-OP3       TPO         109.5       1.0
OP1-P-OP2       TPO         109.5       1.0
OP1-P-OP3       TPO         109.5       1.0
OP2-P-OP3       TPO         109.5       1.0
N-CA-C          TPO         111.0       2.7
CA-C-O          TPO         120.1       2.1











#TRAIN  ( unfinished, CUDA requirements from my 4070 clashing with old packages )



###### Start fresh
conda deactivate
conda env remove -n unifolds
conda create -n unifolds python=3.8.10 -y
conda activate unifolds

## Install numpy first at exact version
pip install numpy==1.19.5

## Install JAX ecosystem in order
pip install jaxlib==0.1.67+cuda111 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
pip install jax==0.2.14
pip install dm-tree==0.1.6
pip install toolz>=0.9.0
pip install chex==0.0.7
pip install dm-haiku==0.0.4
pip install jmp==0.0.2

## Install remaining dependencies
pip install tensorflow-cpu==2.5.3
pip install scipy==1.7.0
pip install biopython==1.79
pip install absl-py==0.13.0
pip install docker==5.0.0
pip install immutabledict==2.0.0
pip install ml-collections==0.1.0

## Install conda packages
conda install -y -c conda-forge openmm=7.5.1 pdbfixer cudatoolkit=11.1
conda install -y -c bioconda hmmer hhsuite==3.3.0 kalign2
conda install -y -c nvidia cudnn==8.0.4
















