import abc
from typing import List, cast

from overhave import db
from overhave.storage.converters import FeatureTypeModel


class BaseFeatureTypeStorageException(Exception):
    """Base exception for :class:`FeatureTypeStorage`."""


class FeatureTypeNotExistsError(BaseFeatureTypeStorageException):
    """Exception for situation without specified feature type."""


class IFeatureTypeStorage(abc.ABC):
    """Abstract class for feature type storage."""

    @staticmethod
    @abc.abstractmethod
    def get_default_feature_type() -> FeatureTypeModel:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_feature_type_by_name(name: str) -> FeatureTypeModel:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_all_feature_types() -> List[FeatureTypeModel]:
        pass


class FeatureTypeStorage(IFeatureTypeStorage):
    """Class for feature type storage."""

    @staticmethod
    def get_default_feature_type() -> FeatureTypeModel:
        with db.create_session() as session:
            feature_type: db.FeatureType = session.query(db.FeatureType).order_by(db.FeatureType.id.asc()).first()
            return cast(FeatureTypeModel, FeatureTypeModel.from_orm(feature_type))

    @staticmethod
    def get_feature_type_by_name(name: str) -> FeatureTypeModel:
        with db.create_session() as session:
            feature_type: db.FeatureType = (
                session.query(db.FeatureType).filter(db.FeatureType.name == name).one_or_none()
            )
            if feature_type is None:
                raise FeatureTypeNotExistsError(f"Could not find feature type with name='{name}'!")
            return cast(FeatureTypeModel, FeatureTypeModel.from_orm(feature_type))

    @staticmethod
    def get_all_feature_types() -> List[FeatureTypeModel]:
        with db.create_session() as session:
            db_feature_types = session.query(db.FeatureType).all()
            return cast(List[FeatureTypeModel], [FeatureTypeModel.from_orm(x) for x in db_feature_types])
