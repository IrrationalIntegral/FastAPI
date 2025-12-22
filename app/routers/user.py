from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash the password - user.password
    hashed_passowrd = utils.hash(user.password)
    user.password = hashed_passowrd
    new_user = models.User(**user.model_dump()) # unpack the user pydantic object into the SQLAlchemy model
    db.add(new_user)
    db.commit() # This saves the changes to the database
    db.refresh(new_user) # This will get the new user from the database
    return new_user

@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first() # type: ignore
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found")
    return user