from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        password = "1234"

        if password == "1234":
            print("Password Authentication Successful")
        else:
            print("Wrong Password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        otp = "5678"

        if otp == "5678":
            print("OTP Authentication Successful")
        else:
            print("Wrong OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        fingerprint = True

        if fingerprint:
            print("Biometric Authentication Successful")
        else:
            print("Biometric Authentication Failed")


a1 = PasswordAuthentication()
a1.authenticate()

a2 = OTPAuthentication()
a2.authenticate()

a3 = BiometricAuthentication()
a3.authenticate()