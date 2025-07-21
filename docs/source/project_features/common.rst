Common Models and Schemas
=========================

You'll many components follow layered architecture, or "clean code". I'm not here to argue what patterns are best...for this project, it's what I choose and it's been working great.

Data Access
-----------

There includes an ``IRepository`` interface that all repository classes should implement. The default implementation support SQLAlchemy, but the interface is designed to be easily extended to other ORMs.

``BaseSQLAlchemyRepository`` provides common CRUD operations any ModelType can implement.

.. code-block:: python

    from src.models.user import User
    from src.repositories.sqlalchemy import BaseSQLAlchemyRepository
    from src.schemas.user import IUserCreate, IUserUpdate


    class UserRepository(BaseSQLAlchemyRepository[User, IUserCreate, IUserUpdate]):
        _model = User

        # add other frequently used methods here
        ...


Presentation
------------

All route responses can wrapped in an implementation of ``IResponseBase``.

.. code-block:: python

   @router.get(
        "/users",
        response_description="Get all users",
        response_model=IGetResponseBase[list[IUserRead]],
        tags=["users"],
    )
    def get_users(
        session: Session = Depends(get_session),
    ) -> IGetResponseBase[list[IUserRead]]:
        user_repo = UserRepository(db=session)
        users = user_repo.all()

        return IGetResponseBase[list[IUserRead]](data=users)
