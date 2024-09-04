from jose import jwt, JWTError
from datetime import datetime, timedelta
from . import schemas
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

oauth_schemes = OAuth2PasswordBearer(tokenUrl='login')
# to create the access token we need 3 components 
# SECRET_KEY
# ALGORITHM
# ACESS_TOKEN_EXPIRE_MINUTES 
SECRET_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ2YWx1ZSJ9.FG-8UppwHaFp1LgRYQQeS6EDQF7_6-bMFegNucHjmWg'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# creating access token 
def create_access_token(data: dict): 
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    endcoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return endcoded_jwt

# verify the access token 

def verify_access_token(token: str, credential_exception): 
  try: 
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

    id: str = payload.get('user_id')
    if not id: 
       raise credential_exception
    token_data = schemas.TOkenData(id=str(id))
    
  except JWTError: 
     raise credential_exception
  
  return token_data

# getting the current user 

def get_current_user(token: str = Depends(oauth_schemes)): 
    exception_credential = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'user unauthorized', headers={"WWW-unathorized": "bearer"})

    return verify_access_token(token, exception_credential)





