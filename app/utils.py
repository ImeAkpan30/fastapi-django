from passlib.context import CryptContext   # package to hash a user's password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # algorithm to hash a password

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)