from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

# Verify the user password by hashing the plain password and comparing it with the database hashed password
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)