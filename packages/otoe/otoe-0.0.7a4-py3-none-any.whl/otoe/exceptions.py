class OtoeException(Exception):
    """Base class for all Otoe exceptions."""
    pass


class OtoeFileNotFoundError(OtoeException, FileNotFoundError):
    """Raised when a file is not found."""
    pass


class OtoeDirectoryNotFoundError(OtoeException, FileNotFoundError):
    """Raised when a directory is not found."""
    pass


class OtoeMarkdownFileNotFoundError(OtoeException, FileNotFoundError):
    """Raised when a yaml file is not found."""
    pass


class OtoeEmptyDirectoryError(OtoeException, FileNotFoundError):
    """Raised when a directory is empty."""
    pass


class OtoeInvalidYamlError(OtoeException, ValueError):
    """Raised when a yaml file is invalid."""
    pass


class OtoeEmptyYamlError(OtoeException, ValueError):
    """Raised when a yaml file is empty."""
    pass


class OtoeEmptyMarkdownError(OtoeException, ValueError):
    """Raised when a markdown file is empty."""
    pass


class OtoeValueError(OtoeException, ValueError):
    """Raised when a value is invalid."""
    pass


class OtoeInvalidMarkdownError(OtoeException, ValueError):
    pass


class OtoeNoMatchesError(OtoeException, ValueError):
    pass
