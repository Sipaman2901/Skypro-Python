from address_data import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("123456", "Москва", "ул Ленина", "д 10", "кв 25")
from_address = Address(
    "654321", "Санкт-Петербург", "ул Пушкина", "д 5", "кв 30")

# Создаем почтовое отправление
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="RB123456789RU"
)

# Выводим информацию об отправлении
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
    )
