import numpy as np
import hashlib
from typing import List
from collections import defaultdict
from scipy.spatial.distance import cdist


class LSHIndex:
        
    """
    LSHIndex is a class for implementing a Locality Sensitive Hashing (LSH) index.
    The LSH index is used to find approximate nearest neighbors for a given query.
    
    Reference: 
        https://www.cs.princeton.edu/courses/archive/spr05/cos598E/bib/p253-datar.pdf
        
    Attributes:
        features (np.ndarray): A numpy array of features.
        r (float): The desired recall.
        b (int): The number of hash tables.
        rand_vectors (np.ndarray): A numpy array of random vectors.
        index (List[List[int]]): A list of lists of indices.

    """
    def __init__(self, features: np.ndarray, r: float, b: int) -> None:
        
        """ 
        The constructor for LSHIndex class.
            
            Parameters:
                features (np.ndarray): A numpy array of features.
                r (float): The desired recall.
                b (int): The number of hash tables.
                    
        Returns:
            None      

        """
        self.features = features
        self.r = r
        self.b = b
        self.rand_vectors = np.random.normal(size=(b, len(features[0])))
        self.index = self.lsh_index()


    def hash_vector(self, v: np.ndarray) -> List[int]:
        
        """
        Hashes a vector.

        Parameters:
            v (np.ndarray): A numpy array of features.

        Returns:
            hash_values (List[int]): A list of hash values.
            
        """

        projected = np.dot(self.rand_vectors, v)
        signs = np.sign(projected)
        hash_values = [hashlib.sha256(signs[i].tobytes()).hexdigest() for i in range(self.b)]
        return hash_values


    def lsh_index(self) -> List[List[int]]:

        """
        Creates an LSH index.

        Parameters:
            None

        Returns:
            index (List[List[int]]): A list of lists of indices.
            
        """
        index = defaultdict(list)
        for i, feature in enumerate(self.features):
            hash_codes = self.hash_vector(feature)
            for hash_code in hash_codes:
                index[hash_code].append(i)
        return index


    def approximate_nearest_neighbors(self, query_features: np.ndarray, k: int) -> np.ndarray:
        
        """
        Finds approximate nearest neighbors for a given query.

        Parameters:
            query_features (np.ndarray): A numpy array of query features.
            k (int): The number of nearest neighbors to find.

        Returns:
            nn_indices (np.ndarray): A numpy array of nearest neighbor indices.

        """
        n_candidates = int(self.r * self.features.shape[0])
        candidate_indices = set()
        for i, query_feature in enumerate(query_features):
            hash_codes = self.hash_vector(query_feature)
            for hash_code in hash_codes:
                candidate_indices.update(self.index[hash_code])
            if len(candidate_indices) > n_candidates:
                break
        candidate_features = self.features[list(candidate_indices)]
        distances = cdist(query_features, candidate_features)
        nn_indices = np.argsort(distances, axis=1)[:, :k]
        return np.array(list(candidate_indices))[nn_indices]


    @staticmethod
    def exact_nearest_neighbors(features: np.ndarray, query_features: np.ndarray, k: int) -> np.ndarray:

        """
        Finds exact nearest neighbors for a given query using brute force.
        
        Parameters:
            features (np.ndarray): A numpy array of features.
            query_features (np.ndarray): A numpy array of query features.
            k (int): The number of nearest neighbors to find.

        Returns:
            nn_indices (np.ndarray): A numpy array of nearest neighbor indices.
            
        """ 
        distances = cdist(query_features, features)
        nn_indices = np.argsort(distances, axis=1)[:, :k]
        return nn_indices
   


    @staticmethod
    def precision(exact_nn: np.ndarray, approx_nn: np.ndarray, k: int) -> float:

        """
        Calculates the precision of the approximate nearest neighbors.

        Parameters:
            exact_nn (np.ndarray): A numpy array of exact nearest neighbor indices.
            approx_nn (np.ndarray): A numpy array of approximate nearest neighbor indices.
            k (int): The number of nearest neighbors to find.

        Returns:
            precision (float): The precision of the approximate nearest neighbors.

        """
        precision = np.mean([len(set(exact_nn[i]) & set(approx_nn[i])) / k for i in range(len(exact_nn))])
        return precision

