from functools import reduce
from typing import List

from ..enums.actions_enum import ActionsEnum as actions
from ..enums.fields_enum import FieldsEnum as fields
from ..enums.modules_enum import ModulesEnum as modules


class Contracts:
    @staticmethod
    def get_contract_abi(address: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_ABI}"
            f"{fields.ADDRESS}"
            f"{address}"
        )
        return url

    @staticmethod
    def get_contract_source_code(address: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_SOURCE_CODE}"
            f"{fields.ADDRESS}"
            f"{address}"
        )
        return url

    @staticmethod
    def get_contract_creator_and_creation_tx_hash(addresses: List[str]) -> str:
        address_list = reduce(lambda w1, w2: str(w1) + "," + str(w2), addresses)
        url = (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_CONTRACT_CREATION}"
            f"{fields.CONTRACT_ADDRESSES}"
            f"{address_list}"
        )
        return url
