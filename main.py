from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

import uvicorn
from models import Gender, Role, User, UserUpdateRequest
from starlette.responses import RedirectResponse

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("3668cd69-4227-4dbd-bc29-9658dce1b0bb"),
        fisrt_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("e006bc5b-81d1-4efb-9ad4-6ba8497ee415"),
        fisrt_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
]


@app.get("/")
async def root():
    return RedirectResponse(url='/docs')


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return db
    raise HTTPException(
        status_code=404,
        detail=f"user  with id: {user_id} does not exists"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.fisrt_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return db
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exiists"
    )


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8050, reload=True)
