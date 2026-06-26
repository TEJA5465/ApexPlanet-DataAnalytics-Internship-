SELECT * FROM sales;

SELECT SUM(Sales) AS TotalSales
FROM sales;

SELECT SUM(Profit) AS TotalProfit
FROM sales;

SELECT Region,
SUM(Sales) AS RegionSales
FROM sales
GROUP BY Region;

SELECT Category,
SUM(Profit) AS CategoryProfit
FROM sales
GROUP BY Category;