class FilterClientService:
    
    @staticmethod
    def filter_by_attr(attr, value, clients):
        return list(filter(lambda client: getattr(client, attr) == value, clients))[0]
    