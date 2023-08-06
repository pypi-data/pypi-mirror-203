from __future__ import annotations

from vectice.utils.deprecation import deprecate


@deprecate(
    warn_at="23.1",
    fail_at="23.3",
    remove_at="23.4",
    reason="The `vectice.models.datasource.datawrapper.metadata.metadata` module "
    "is deprecated in favor the `vectice.models.resource.metadata.base` module. "
    "Importing from the deprecated module will fail in v{fail_at}, "
    "and the module will be removed in v{remove_at}.",
)
def _warn() -> None:
    pass


_warn()
