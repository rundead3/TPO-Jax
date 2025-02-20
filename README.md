

# TRAIN 



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















