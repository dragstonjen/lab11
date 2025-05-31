# Телефонна книга з розширеним функціоналом

contacts = [
    {"ім'я": "Анна", "прізвище": "Іваненко", "телефон": "0501234567", "місто": "Київ"},
    {"ім'я": "Олег", "прізвище": "Петренко", "телефон": "0679876543", "місто": "Львів"},
    {"ім'я": "Ірина", "прізвище": "Сидорова", "телефон": "0931112233", "місто": "Київ"},
    {"ім'я": "Богдан", "прізвище": "Ковальчук", "телефон": "0507654321", "місто": "Одеса"},
    {"ім'я": "Марія", "прізвище": "Шевченко", "телефон": "0732223344", "місто": "Львів"},
]

def print_contacts(contact_list):
    if not contact_list:
        print("Контактів не знайдено.")
        return
    print("{:<10}{:<15}{:<15}{:<10}".format("Ім'я", "Прізвище", "Телефон", "Місто"))
    for c in contact_list:
        print("{:<10}{:<15}{:<15}{:<10}".format(
            c["ім'я"], c["прізвище"], c["телефон"], c["місто"]
        ))

def search_contacts():
    try:
        field_map = {
            "ім'я": "ім'я",
            "прізвище": "прізвище",
            "місто": "місто"
        }
        field = input("Пошук за (ім'я/прізвище/місто): ").strip().lower()
        if field not in field_map:
            raise ValueError("Невірне поле пошуку.")
        query = input(f"Введіть значення для пошуку за полем '{field}': ").strip()
        if not query:
            raise ValueError("Порожній ввід.")
        result = [c for c in contacts if c[field_map[field]].lower() == query.lower()]
        print_contacts(result)
    except Exception as e:
        print("Помилка:", e)

def update_or_delete_contact():
    phone = input("Введіть телефон контакту для оновлення/видалення: ").strip()
    for i, c in enumerate(contacts):
        if c["телефон"] == phone:
            action = input("Що зробити: оновити / видалити? ").strip().lower()
            if action == "оновити":
                for key in ["ім'я", "прізвище", "місто"]:
                    new_val = input(f"Нове значення для {key} (залиште порожнім щоб не змінювати): ").strip()
                    if new_val:
                        c[key] = new_val
                print("Контакт оновлено.")
            elif action == "видалити":
                confirm = input("Ви впевнені, що хочете видалити контакт? (так/ні): ").strip().lower()
                if confirm == "так":
                    contacts.pop(i)
                    print("Контакт видалено.")
            return
    print("Контакт не знайдено.")

def analytics():
    if not contacts:
        print("Книга порожня.")
        return
    cities = {c["місто"] for c in contacts}
    print("Унікальні міста:", ", ".join(cities))
    counts = {city: 0 for city in cities}
    for c in contacts:
        counts[c["місто"]] += 1
    for city, count in counts.items():
        print(f"{city}: {count} контакт(и)")
    max_city = max(counts, key=counts.get)
    print("Місто з найбільшою кількістю контактів:", max_city)

# Головне меню
while True:
    print("\n1. Показати всі контакти")
    print("2. Пошук контакту")
    print("3. Оновити / Видалити контакт")
    print("4. Аналітика")
    print("5. Вийти")
    choice = input("Оберіть дію: ").strip()
    if choice == "1":
        print_contacts(contacts)
    elif choice == "2":
        search_contacts()
    elif choice == "3":
        update_or_delete_contact()
    elif choice == "4":
        analytics()
    elif choice == "5":
        print("До побачення!")
        break
    else:
        print("Невірний вибір.")
