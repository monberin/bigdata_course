// Отримувати всі відгуки за заданим product_id
SELECT review FROM products WHERE product_id = 1;

// Отримувати всі відгуки за заданим product_id та обраним star_rating
SELECT review FROM products WHERE product_id = 1 AND star_rating = 4;

// Отримувати всі відгуки за заданим customer_id
SELECT review FROM customers WHERE customer_id = 2;

// Дізнатися скільки позитивних відгуків (4 або 5 зірок) залишив вказаний користувач customer_id
SELECT COUNT(*) FROM customers WHERE customer_id = 1 AND star_rating > 3;
