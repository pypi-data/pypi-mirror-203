from vectordb_orm import MilvusBase, EmbeddingField, VarCharField, PrimaryKeyField
from pymilvus import Milvus
from vectordb_orm.indexes import IVF_FLAT
import numpy as np

class MyObject(MilvusBase):
    __collection_name__ = 'my_collection'

    id: int = PrimaryKeyField()
    text: str = VarCharField(max_length=128)
    embedding: np.ndarray = EmbeddingField(dim=128, index=IVF_FLAT(cluster_units=128))
