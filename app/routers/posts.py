from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas, oath2


router = APIRouter(
    prefix= "/posts"
)

@router.get('/')
def get_all_posts(db: Session = Depends(get_db), user_id: int = Depends(oath2.get_current_user)): 
    all_post = db.query(models.Posts).all()

    return {
        "this post": all_post
    }

# creating a post
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_post(post:schemas.Posts, db: Session = Depends(get_db)): 

    new_post = models.Posts(
        **post.dict()
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


# getting new post by ID
@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_single_posts(id:int, db: Session = Depends(get_db)): 
    single_post = db.query(models.Posts).filter(models.Posts.id == id).first()

    if single_post is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'posts with the ID: {id} not found')
    
    return single_post

# Deleting Single post based in ID

@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_single_posts(id:int, db: Session = Depends(get_db)): 
    deleted_posts = db.query(models.Posts).filter(models.Posts.id == id).first()

    if deleted_posts is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id {id} not found')
    
    return deleted_posts

# Updating a posts based in their ID

@router.put('/{id}')
def update_posts(post: schemas.Posts, id: int, db: Session = Depends(get_db)): 

    updated_posts = db.query(models.Posts).filter(models.Posts.id == id).first()

    if updated_posts is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'posts with id of {id} not found')
    
    for key, value in post.dict().items(): 
        if value is not None: 
            setattr(updated_posts, key, value)

    db.commit()
    db.refresh(updated_posts)

    return updated_posts



    


