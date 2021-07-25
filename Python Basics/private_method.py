class car:
    __os = ""
    __version = 0.0
    def __init__(self):
        self.__os = "Windows"
        self.__version = "11.001"
    def drive(self):
        print("Driving")
        print(self.__os)
    """def updatesoftware(self, os, version):
        self.__os = os
        self.__version = version
        print("Updating software")
        print(self.__os)
        print(self.__version) """

blackcar = car()
blackcar.drive()
# blackcar.updatesoftware("Linux", 4.4)
blackcar.__software= "Linux"