#!/usr/bin/env python3
""" project data module


"""

from dataclasses import dataclass
from typing import List


HYBRID_ENVIRONMENTS = [
    "sandbox",
    "dev",
    "integration",
    "qeint",
    "staging",
    "production",
]


@dataclass(frozen=True, kw_only=True)
class RDSSecret:
    """
        {
      "password": "some_password",
      "engine": "postgres",
      "port": 5432,
      "dbInstanceIdentifier": "cts-cts-staging",
      "host": "cts-cts-staging.cwi3fcl24jgg.us-east-1.rds.amazonaws.com",
      "username": "some_username"
    }
    """

    # required attributes
    username: str
    password: str
    dbInstanceIdentifier: str  # pylint: disable=invalid-name
    host: str

    # optional attributes. have defaults
    engine: str = "postgres"
    port: int = 5432


class HybridRDSInstance:  # pylint: disable=too-few-public-methods
    """RDS instance"""

    # instance:database lookup
    instance_database = {
        "applex": ["cloudauth", "onesign"],
        "biometric": ["biometric"],
        "cts": ["cts"],
        "idpadmin": ["idpadmin", "idpcore"],
        "kms": ["kms"],
        "provisioning": ["cps", "icpa"],
    }  # type: dict[str, List[str]]

    def __init__(
        self,
        hybrid_instance: str,
    ):
        self.hybrid_instance = hybrid_instance  #
