import gzip
import pickle
from rdkit.Chem import MolToSmiles
def load_pkl_gz_smiles(filename):
    with gzip.open(filename, 'rb') as f:
        data = pickle.load(f)
    smiles = [MolToSmiles(d[1].mol) for d in data]
    return smiles
if __name__ == "__main__":
    smiles = load_pkl_gz_smiles('results/ppo/array_may_18_0/sampled_mols.pkl.gz')
    print(smiles[:5])