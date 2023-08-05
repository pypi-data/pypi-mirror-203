from enum import Enum


class NetZeusNetworkDriverConnectionMethodEnum(str, Enum):
    CLI_SSH = "cli_ssh"
    NETCONF = "netconf"
    RESTCONF = "restconf"


class NetZeusNetworkAuthenticatorTypeEnum(str, Enum):
    SSH_KEY_RSA = "ssh_key_rsa"
    SSH_PASSWORD = "ssh_password"
    EXTERNAL_API = "external_api"
