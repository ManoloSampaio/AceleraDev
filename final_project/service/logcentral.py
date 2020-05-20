class LogCentral():
    def __init__(self,user_data_base,log_data_base):
        self.__user_data_base = user_data_base
        self.__log_data_base = log_data_base
    def login(self,user_name,user_password):
        """ 
        User login in the page.
        Arguments:
            user_name {string} -- The user name.
            user_password {string} -- The user password.
        Returns:
            If user has credetials so it has acess.
            If not using a exception handle and returns a mensage. 
        """
        pass
    def logout(self,user):
        """
        User logout of the page.
        Arguments:
            user {user} -- The user that is already login.
        Returns:
            Send the user to the login page.
        """
        pass
    def register(self,user_name,user_password):
        """
        Create the user. 
        Arguments:
            user_name {string} -- The user name.
            user_password {string} -- The user password.
        Returns:
            If the user is not already in the plataform so
            returns a fail mensage.
        """
        pass
    def post_log(self,user,log_type,log_mensage):
        """ Method to post a log. Recives the user who going to
        post the log, the log type and log mensage.
        Arguments:
            user {user} -- The user who going to post the log.
            log_type{string} -- The log type. 
            log_mensage {string} -- The mensage of the log.
        Returns:
            A confirmation mensage if the log crendentials are ok
            if not returns a error mensage.
        """
        pass
    def show_log(self,log_data_base,user):
        """[summary]

        Arguments:
            log_data_base {[type]} -- [description]
            user {[type]} -- [description]
        """
        pass
    def get_logs_data_base(self,user):
        """[summary]

        Arguments:
            user {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        pass
    def search_log_types(self,user):
        """[summary]

        Arguments:
            user {[type]} -- [description]
        """
        pass
    def organize_log_types(self,user):
        """[summary]

        Arguments:
            user {[type]} -- [description]
        """
        pass
    def remove_log(self,log,user):
        """[summary]

        Arguments:
            log {[type]} -- [description]
            user {[type]} -- [description]
        """
        pass
    def to_file_log(self,log,user):
        """[summary]

        Arguments:
            log {[type]} -- [description]
            user {[type]} -- [description]
        """
        pass