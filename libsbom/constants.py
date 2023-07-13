from cas_wrapper import CasWrapper
from version import __version__

ALMAOS_VENDOR = 'AlmaLinux OS Foundation'
ALMAOS_EMAIL = 'cloud-infra@almalinux.org'
ALMAOS_SBOMLICENSE = 'CC0-1.0'
ALMAOS_NAMESPACE = 'https://security.almalinux.org/spdx'

TOOLS = [
    {
        "vendor": ALMAOS_VENDOR,
        "name": "AlmaLinux Build System",
        "version": "0.1"  # Shall we start versioning ALBS?
    },
    {
        "vendor": ALMAOS_VENDOR,
        "name": "alma-sbom",
        "version": __version__
    },
    {
        "vendor": "Codenotary Inc",
        "name": "Community Attestation Service (CAS)",
        "version": CasWrapper.get_version()
    }
]
TOOLS_SPDX = [
    {
        "vendor": ALMAOS_VENDOR,
        "name": "spdx-tools",
        "version": "0.8"
    }
]
