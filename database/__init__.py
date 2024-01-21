# from .session import SessionLocal

# async def get_db():
#     async with SessionLocal() as db:
#         yield db


from .session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
