from fastapi import FastAPI, Query, Path, Body, APIRouter
from pydantic import BaseModel

# Создаём главное приложение
app = FastAPI(title="basics")

# Настраиваем роутер с префиксом и тегом
router = APIRouter(
    prefix="/api/v1",             # общий префикс для всех путей в этом роутере
    tags=["Basics"]               # в Swagger UI группа будет помечена тегом "Basics"
)

# Pydantic-модель для входящих данных
class User(BaseModel):
    username: str
    email: str
    age: int

# Модель для ответа
class UserResponse(BaseModel):
    username: str
    email: str
    message: str

# GET /api/v1/basics/{item_id}
@router.get(  # Вместо app используем router
    "/basics/{item_id}",
    summary="Получить базовую информацию по item_id"
)
async def get_basics(
    name: str = Query("Alise", description="Имя пользователя"),
    item_id: int = Path(..., description="Идентификатор элемента")
):
    # Возвращаем приветствие и номер элемента
    return {
        "message": f"Hello, {name}!",
        "description": f"Item number {item_id}"
    }

# POST /api/v1/basics/users
@router.post(  # Вместо app используем router
    "/basics/users",
    response_model=UserResponse,
    summary="Создать нового пользователя"
)
async def create_user(
    user: User = Body(..., description="Данные нового пользователя")
) -> UserResponse:
    # Формируем ответ по схеме UserResponse
    return UserResponse(
        username=user.username,
        email=user.email,
        message="User created successfully!"
    )

# Подключаем роутер к основному приложению
app.include_router(router)
