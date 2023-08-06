import xmlrpc.client
from xmlrpc.client import Error
from .fields import OdooField
from dotenv import dotenv_values
from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv


def load_env_vars(env_path):
    if not os.path.exists(env_path):
        raise FileNotFoundError(".env not found, wrong path")
    load_dotenv(env_path)


class OdooModel(object):
    DATABASE = None
    USERNAME = None
    PASSWORD = None
    URL = None
    UUID = None
    MODELS = None

    COMMON = '/xmlrpc/2/common'
    OBJECTS = '/xmlrpc/2/object'

    FIELDS = {}

    _name = None
    id = None

    def __init__(self, **kwargs):
        if kwargs:
            for name, value in kwargs.items():
                setattr(self, name, value)
                self.FIELDS[name] = value

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"

    class DoesNotExist(Exception):

        def __init__(self, obj_id):
            self.id = obj_id

        def __str__(self):
            return f'Element by id {self.id} does not exist'

    @classmethod
    def search_read(cls, query=[], **kwargs):
        records = cls.MODELS.execute_kw(
            cls.DATABASE,
            cls.UUID,
            cls.PASSWORD,
            cls._name,
            'search_read',
            [query],
            {'fields': list(cls.FIELDS.keys())}
        )
        instances = cls._instances_from_list(records)
        return instances

    @classmethod
    def search_count(cls, query=[]):
        records = cls.search_read(query=query)
        return len(records)

    @classmethod
    def search_by_id(cls, obj_id=None):
        if obj_id is None:
            raise ValueError("id is required")
        record = cls.search_read(query=[["id", '=', obj_id]])
        if len(record) == 0:
            raise cls.DoesNotExist(obj_id)
        return record[0]

    @classmethod
    def _instances_from_list(cls, records):
        return [cls._create_instance_from_dict(record) for record in records]

    @classmethod
    def _create_instance_from_dict(cls, obj):
        return cls(**obj)

    def create(self):
        return self.MODELS.execute_kw(self.DATABASE, self.UUID, self.PASSWORD, self._name, 'create', [self.FIELDS])

    def update(self):
        return self.MODELS.execute_kw(self.DATABASE, self.UUID, self.PASSWORD, self._name, 'write', [[self.id], self.FIELDS])

    def delete(self):
        return self.MODELS.execute_kw(self.DATABASE, self.UUID, self.PASSWORD, self._name, 'unlink', [[self.id]])

    def __init_subclass__(cls):
        cls._set_config_envs()
        cls._fill_fields()
        cls._set_attributes_initialized_none()
        super().__init_subclass__()

    @classmethod
    def _set_attributes_initialized_none(cls):
        cls._set_models_attribute()
        cls._set_uuid_attribute()

    @classmethod
    def _set_config_envs(cls):
        cls.DATABASE = os.getenv('DATABASE')
        cls.USERNAME = os.getenv('USERNAME')
        cls.PASSWORD = os.getenv('PASSWORD')
        cls.URL = os.getenv('URL')

    @classmethod
    def _set_uuid_attribute(cls):
        common = xmlrpc.client.ServerProxy('{}{}'.format(cls.URL, cls.COMMON))
        cls.UUID = common.authenticate(
            cls.DATABASE, cls.USERNAME, cls.PASSWORD, {})

    @classmethod
    def _set_models_attribute(cls):
        cls.MODELS = xmlrpc.client.ServerProxy(
            '{}{}'.format(cls.URL, cls.OBJECTS))

    @classmethod
    def _fill_fields(cls):
        cls.FIELDS = {}
        cls._iterate_dir_class()

    @classmethod
    def _iterate_dir_class(cls):
        for attr_name in dir(cls):
            attr = cls._is_not_abstract_method_attribute(attr_name)
            cls._add_field_if_is_odoo_field(attr, attr_name)

    @classmethod
    def _add_field_if_is_odoo_field(cls, attr, attr_name):
        if isinstance(attr, OdooField):
            cls.FIELDS[attr_name] = attr._type

    @classmethod
    def _is_not_abstract_method_attribute(cls, attr_name):
        if attr_name != '__abstractmethods__':
            return getattr(cls, attr_name)
