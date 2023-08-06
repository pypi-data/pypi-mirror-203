# -*- coding: utf-8 -*-
from django.core import validators
from django.db.models.fields import GenericIPAddressField as DjangoGenericIPAddressField
from django.utils.ipv6 import clean_ipv6_address

from a3dj.structs.base.base_field import BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import GenericIPAddressMocker, BaseMocker
from .char_field import CharField


class GenericIPAddressFieldOpenApiManager(BaseFieldOpenApiManager):

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'ip'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String


class GenericIPAddressFieldMockManager(BaseFieldMockManager):

    def _preset_default_mocker(self) -> BaseMocker:
        return GenericIPAddressMocker()


class GenericIPAddressField(CharField):

    def __init__(self, protocol="both", unpack_ipv4=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.protocol = protocol
        self.unpack_ipv4 = unpack_ipv4
        self.validators.extend(validators.ip_address_validators(protocol, unpack_ipv4)[0])

    @classmethod
    def _build_from_model_field(cls, field_instance: DjangoGenericIPAddressField) -> 'GenericIPAddressField':
        return cls(
            protocol=field_instance.protocol, unpack_ipv4=field_instance.unpack_ipv4,
            max_length=field_instance.max_length, choices=field_instance.choices
        )

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return GenericIPAddressFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return GenericIPAddressFieldMockManager(self)

    def to_python(self, value) -> str:
        value = super().to_python(value).strip()
        if value and ":" in value:
            return clean_ipv6_address(value, self.unpack_ipv4)
        return value
