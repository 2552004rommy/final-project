---- Time Series Forecasting Dataset
--SELECT 
--    D.Full_Date,
--    SUM(SF.Shipping_Cost) AS Total_Shipping_Cost
--FROM Sales_Fact SF
--INNER JOIN Dim_Date D ON SF.Date_Surrogate_ID = D.Date_Surrogate_ID
--GROUP BY D.Full_Date
--ORDER BY D.Full_Date;


-- Analytical Dataset for Sales Analysis
SELECT 
    D.Full_Date,
    C.Customer_Name,
    C.Gender,
    C.Membership_Status,
    P.Product_Name,
    P.Category,
    P.Brand,
    B.Branch_Name,
    E.First_Name + ' ' + E.Last_Name AS Employee_Name,
    SF.Quantity,
    SF.Unit_Price,
    SF.Total_Price,
    SF.Net_Sales,
    SF.Gross_Margin,
    SF.Shipping_Cost,
    SF.Discount,
    SF.Promotion_Surrogate_ID AS Promotion_ID,
    SF.Payment_Surrogate_ID AS Payment_ID,
    P.Weight AS Product_Weight,
    D.Year,
    D.Month,
    D.Day_of_Week,
    D.Is_Weekend
FROM Sales_Fact SF
INNER JOIN Dim_Date D ON SF.Date_Surrogate_ID = D.Date_Surrogate_ID
INNER JOIN Dim_Customers C ON SF.Customer_Surrogate_ID = C.Customer_Surrogate_ID
INNER JOIN Dim_Products P ON SF.Product_Surrogate_ID = P.Product_Surrogate_ID
INNER JOIN Dim_Employees E ON SF.Employee_Surrogate_ID = E.Employee_Surrogate_ID
INNER JOIN Dim_Branches B ON SF.Branch_Surrogate_ID = B.Branch_Surrogate_ID
ORDER BY D.Full_Date;

