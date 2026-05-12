class TimeMap:

    def __init__(self):
        self.data_structure  = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        key_specific_dict = self.data_structure.get(key, {})
        key_specific_dict[timestamp] = value
        self.data_structure[key] = key_specific_dict

        
    def get(self, key: str, timestamp: int) -> str:
        key_specific_dict = self.data_structure.get(key, {})
        value = key_specific_dict.get(timestamp, None)
        if value != None:
            return value
        else:
            for i in range(timestamp, -1, -1):
                value = key_specific_dict.get(i)
                if value:
                    return value
            return ""

        
 