from model import Files as FilesModel
from fastapi_sqlalchemy import db  # an object to provide global access to a database session
from model import Files

async def save_upload(filename:str, filelink):
    File = FilesModel(filename=filename, filelink=filelink)
    """
    save the s3 file details to the database here
    """
    print('file succefully saved to db')

# async def get_all_files():
#     # all_files = some query here

#      """
#      input the query for getting all the files from the database here
#      """
#      return all_files

async def get_all_files():
    all_files = await db.session.query(Files).all()
    return all_files