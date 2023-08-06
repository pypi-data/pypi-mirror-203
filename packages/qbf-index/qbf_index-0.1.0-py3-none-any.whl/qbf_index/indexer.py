from typing import Protocol
import numpy as np
import hashlib
import pickle

class Hashable(Protocol):
    def __hash__(self):
        pass


class QBFIndex:
    def __init__(self, capacity: int, error_rate: float, grid_resolution: float, levels: int = 4):
        
        if capacity <= 0 or error_rate <= 0 or error_rate >= 1 or grid_resolution <= 0 or levels <= 0:
            raise ValueError("Invalid input values.")

        self.capacity = capacity
        self.error_rate = error_rate
        self.grid_resolution = grid_resolution
        self.levels = levels
        self.num_bits = self.compute_num_bits(capacity, error_rate)
        self.num_hash_functions = self.compute_num_hash_functions(self.num_bits, capacity)
        self.bit_array = np.zeros(self.num_bits, dtype=np.uint8)


    def add(self, key: Hashable):
        if key is False:
            raise ValueError("Key cannot be None.")
        hash_values = self.hash(key)
        self.bit_array[hash_values] = np.minimum(self.bit_array[hash_values] + 1, self.levels - 1)

        
    def contains(self, key: Hashable) -> bool:
        if key is False:
            raise ValueError("Key cannot be None.")
        hash_values = self.hash(key)
        return np.all(np.take(self.bit_array, hash_values) > 0)


    def hash(self, key: Hashable) -> np.ndarray:
        if key is False:
            raise ValueError("Key cannot be None.")

        if isinstance(key, str):
            key = key.encode()

            hash_values = np.array([
                int(hashlib.sha256(key + str(i).encode()).hexdigest(), 16) % self.num_bits
                for i in range(self.num_hash_functions)
            ])
            return hash_values

    @staticmethod
    def compute_num_bits(capacity: int, error_rate: float) -> int:
        num_bits = int(-(capacity * np.log(error_rate)) / (np.log(2) ** 2))
        return int(num_bits + 7) & ~7

    @staticmethod
    def compute_num_hash_functions(num_bits: int, capacity: int) -> int:
        num_hash_functions = int((num_bits / capacity) * np.log(2))
        return num_hash_functions

    def merge(self, other: 'QBFIndex') -> 'QBFIndex':
        if type(other) != type(self):
            raise TypeError("The given object must be an instance of QBFIndex.")

        assert self.capacity == other.capacity
        assert self.error_rate == other.error_rate
        assert self.grid_resolution == other.grid_resolution
        assert self.levels == other.levels
        assert self.num_bits == other.num_bits
        assert self.num_hash_functions == other.num_hash_functions
        merged = QBFIndex(self.capacity, self.error_rate, self.grid_resolution, self.levels)
        merged.bit_array = np.minimum(self.bit_array + other.bit_array, self.levels - 1)
        return merged
    
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['bit_array']  # remove the bit_array from the state
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.bit_array = np.zeros(self.num_bits, dtype=np.uint8)  # recreate the bit_array

    def save(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(file_path):
        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
        return obj
