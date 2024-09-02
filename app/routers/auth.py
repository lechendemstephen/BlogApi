from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database, utils
router = APIRouter(
    prefix= '/login',
    tags= ['Authentication']
)

@router.post('')
def login_user(logged_user: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email == logged_user.email).first()

    # verifying to see if the password is correct
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user credential invalid')
    
    # verifying to make sure the user is not entrying the wrong pasword
    if not utils.verify_password(logged_user.password, user.password): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user credential invalid')
    
    # create the access token 

    return {
        "access_token": "loggin successful"
    }


