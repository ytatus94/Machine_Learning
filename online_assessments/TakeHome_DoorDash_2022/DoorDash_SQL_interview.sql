
Q1:

SELECT
    month, 
    high_freq_customers / total_customers * 100 AS pct_high_freq
FROM (
    SELECT
        month,
        total_customers,
        COUNT(*) AS high_freq_customers
    FROM (
        SELECT *
        FROM (
            SELECT
                customer_id,
                month,
                COUNT(*) OVER (PARTITION BY month ORDER BY month) AS number_of_orders
                COUNT(DISTINCT customer_id) OVER (PARTITION BY month ORDER BY month) AS total_customers
            FROM (
                SELECT
                    customer_id,
                    order_place_time,
                    EXTRACT(MONTH FROM order_place_time) AS month
                FROM delivery_orders
            )
        ) AS monthly_orders
        WHERE monthly_orders.number_of_orders > 30
    )
    GROUP BY month
)

Q2:

SELECT
    customers_id,
    MONTH,
    rank
FROM ( 
    SELECT
        customers_id,
        MONTH,
        RANK() OVER (PARTITION BY MONTH ORDER BY number_of_orders DESC) AS rank
    FROM (
        SELECT *
        FROM (
            SELECT
                customer_id,
                month,
                COUNT(*) OVER (PARTITION BY month ORDER BY month) AS number_of_orders
                COUNT(DISTINCT customer_id) OVER (PARTITION BY month ORDER BY month) AS total_customers
            FROM (
                SELECT
                    customer_id,
                    order_place_time,
                    EXTRACT(MONTH FROM order_place_time) AS month
                FROM delivery_orders
            )
        ) AS monthly_orders
        WHERE monthly_orders.number_of_orders <= 30
    )
) AS top_deliveries
WHERE top_deliveries.rank == 1