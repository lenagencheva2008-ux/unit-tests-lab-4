def loyalty_points(amount: float, is_member: bool) -> int:
    """
    Повертає кількість балів лояльності.
    1 бал за кожні повні 20 грн. Учасник програми отримує x2.
    amount < 0 — помилка.
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")

    base_points = int(amount // 20)
    if is_member:
        return base_points * 2
    return base_points

