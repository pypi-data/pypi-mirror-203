from data_watch.common.base import Base


class SearchRequest(Base):
    """
    Model for search requests
    """

    query: str
