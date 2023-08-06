import warnings


def deprecated_function():
    warnings.warn(
        "The package 'Keqing_Sword' is deprecated, please use the new package 'Keqing' instead.",
        DeprecationWarning,
        stacklevel=2,
    )


deprecated_function()
