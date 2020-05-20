class Log():
    def __init__(self,log_type,log_mensage,log_time,log_user):
        self.__type = log_type
        self.__mensage = log_mensage
        self.__time = log_time
        self.__user = log_user
    def get_log_content(self):
        """[summary]

        Returns:
        content [dic] -- A dictionary with the data.
        """
        content = {'type':self.__type,
                  'mensage':self.__mensage,
                  'time':self.__time,
                  'user':self.__user}
        return content
    