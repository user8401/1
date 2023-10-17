Task 1: Table Comparison

    Compare the final_assignments_qa table with the events captured in user_level_testing to ensure all necessary data fields are available for computing the 30-day view-binary metric.
    Look for fields such as user_id, item_id, view_date, view_count, etc., that would be crucial for this calculation.

Task 2: Query and Table Creation

    Write a SQL query to create a new table final_assignments based on final_assignments_qa, incorporating any missing fields identified in Task 1.

sql

CREATE TABLE final_assignments AS
SELECT *,
       CAST(NULL AS INT) AS placeholder -- If any field was missing, add a placeholder column
FROM final_assignments_qa;

Task 3: Calculate 30-day Order Binary

    Utilize a SQL query to calculate the order binary metric for item_test_2 within a 30-day window post-test assignment.

sql

SELECT item_id,
       SUM(CASE WHEN DATEDIFF(day, test_start_date, order_date) BETWEEN 0 AND 30 THEN 1 ELSE 0 END) AS order_binary
FROM final_assignments
WHERE item_id = 'item_test_2'
GROUP BY item_id;

Task 4: Calculate 30-day View Binary and Average Views

    Implement a SQL query to calculate the view binary and average views for item_test_2 within the same 30-day window.

sql

SELECT item_id,
       AVG(view_count) AS average_views,
       SUM(CASE WHEN view_count > 0 THEN 1 ELSE 0 END) AS view_binary
FROM final_assignments
WHERE item_id = 'item_test_2'
AND DATEDIFF(day, test_start_date, view_date) BETWEEN 0 AND 30
GROUP BY item_id;

Task 5: A/B Test Analysis

    Utilize the ABBA A/B test calculator to compute the lifts and p-values for the 30-day order binary and 30-day view binary metrics, applying a 95% confidence interval.
    Record the lift and p-value results, and interpret the significance based on p-value thresholds (e.g., p < 0.05 indicating statistical significance).

Report Building in Mode:

    Use Mode’s Report builder to compile the analysis.
    Include the title, graphs for each binary metric, lift and p-value results, and interpretations of the significance of the A/B test outcomes.
    Provide a shareable link to your Mode Analytics workbook for peer review.
