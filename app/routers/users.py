from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from .. import schemas, database, models, utils


router = APIRouter(
    tags= ["users"],
    prefix= "/users"
)

#creating a new user 

@router.post('/')
def create_user(user: schemas.Users, db: Session = Depends(database.get_db)): 

    # hashing the user password
    hashed_password = utils.has_password(user.password)
    user.password = hashed_password

    
    # creating new user 
    new_user = models.Users(
        **user.dict()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user