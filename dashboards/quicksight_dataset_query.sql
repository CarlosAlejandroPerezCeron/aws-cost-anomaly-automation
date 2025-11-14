SELECT
  line_item_usage_account_id AS account_id,
  product_product_name AS service,
  SUM(line_item_unblended_cost) AS total_cost,
  DATE_TRUNC('day', line_item_usage_start_date) AS date
FROM aws_cur_dataset
GROUP BY 1, 2, 4
