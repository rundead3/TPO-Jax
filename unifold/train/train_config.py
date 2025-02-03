from ml_collections import ConfigDict

train_config = ConfigDict({
    'global_config':{
        'use_mpi': False,
        'model_name': 'demo',
        'verbose': 'info',
        'gpus_per_node': 1,
        'ckpt_format': 'pkl',
        'start_step': 0,
        'end_step': 200,
        'logging_freq': 10,
        'eval_freq': 50,
        'save_freq': 50,
        'save_dir': '/home/r1/TPO-Jax/out/ckpt',
        'load_dir': '/home/r1/TPO-Jax/out/ckpt',
        'precision': 'fp32',
        'max_queue_size': 4,
        'random_seed': 181129
    },
    'optimizer': {
        'name': 'adam',
        'learning_rate': 1e-3,
        'warm_up_steps': 10,
        'decay':{
            'name': 'exp',
            'decay_rate': 0.95,
            'decay_steps': 10
        },
        'clip_norm': 1e-1,
    },
    'data':{
        'train': {
            'features_dir': "/home/r1/TPO-Jax/out/training/features",
            'mmcif_dir': "/home/r1/TPO-Jax/out/training/mmcif",
            'sample_weights': None
        },
        'eval': {
            'features_dir': "/home/r1/TPO-Jax/out/validation/features",
            'mmcif_dir': "/home/r1/TPO-Jax/out/validation/mmcif",
            'sample_weights': None
        },
    }
})