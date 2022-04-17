RESTful API сервис , позволяющий формировать ленту статей для пользователей. API предоставляет ресурсы для:
1. вывода публичных статей для неавторизованных пользователей;
2. авторизации пользователей с помощью Basic Auth. В качестве логина использовать email;
3. регистрации новых пользователей с ролью "подписчик"
  a) обязательные поля - email, пароль;
  b) должна быть валидация email на соответствие маски email и на уникальность;
  c) пароль должен быть не короче 8 символов и содержать хотя бы одну цифру и букву любого регистра);
4. чтения статей закрытых статей (только для подписчиков) пользователями с ролью "подписчик";
5. создания новых статей ролью "автор". Пользователям с ролью "подписчик" запрещено создание статей;
6. редактирования и удаления статей. Автор может удалять или редактировать только те статьи, которые он написал.
